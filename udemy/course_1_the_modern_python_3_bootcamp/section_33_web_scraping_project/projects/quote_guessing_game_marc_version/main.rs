use crate::game::QuoteGame;
use clap::Parser;
use clap_derive::Parser;
use rand::seq::SliceRandom;
use std::fs;
use std::fs::File;
use std::io::Read;
use std::process::exit;

mod edit_distance;
mod game;
mod scraper;

#[derive(Parser, Debug)]
#[command(version, about, long_about = None)]
struct Args {
    #[arg(short, long)]
    refresh_quote_db: bool,
}

const DATA_LOCATION: &str = "src/bin/scrape_quotes/downloaded_data/data.json";

#[tokio::main]
async fn main() -> anyhow::Result<()> {
    let args = Args::parse();
    if args.refresh_quote_db {
        download_quote_data().await?
    }

    if !fs::metadata(DATA_LOCATION).is_ok() {
        println!("the file doesn't exist, downloading the quote data");
        download_quote_data().await?
    }
    let file = File::open(DATA_LOCATION)?;
    let quotes: Vec<scraper::Quote> = serde_json::from_reader(file)?;

    // GAME LOOP
    let mut game: QuoteGame = game::new(quotes);
    'game: loop {
        let quote_prompt = game.get_next_prompt();
        if quote_prompt.is_none() {
            println!("There are no more quotes");
            break;
        }

        let quote_prompt = quote_prompt.unwrap();
        while game.can_continue() {
            print!("{quote_prompt}");
            println!("{}", game.provide_hint());
            let user_input = game.user_prompt();

            if user_input.contains("quit") || user_input.contains("exit") {
                break 'game;
            }

            if game.check_guess(&user_input) {
                println!("Correct! The quote was said by: {}", game.get_answer());
                break;
            } else {
                println!(
                    "Incorrect! You have {} guesses remaining",
                    game.guesses_remaining()
                );
            }

            if game.guesses_remaining() <= 0 {
                break 'game;
            }
        }
    }
    println!("You solved {} Quotes!", game.score);
    Ok(())
}

async fn download_quote_data() -> anyhow::Result<()> {
    let mut parser = scraper::QuotesScraper::new();
    // pull in data from up to 100 pages
    for _ in 0..100 {
        let markup = match parser.download_page_markup().await {
            Ok(markup) => markup,
            Err(e) => {
                eprintln!("could not download the data {e}");
                break;
            }
        };

        match parser.parse_data(markup).await {
            Ok(_) => (),
            Err(e) => {
                eprintln!("could not parse the data {e}");
                break;
            }
        };
    }
    let output = serde_json::to_string(&parser.quotes)?;
    fs::write(DATA_LOCATION, output)?;
    Ok(())
}
