use crate::edit_distance::edit_distance;
use crate::scraper::Quote;

use rand::prelude::SliceRandom;
use rand::thread_rng;
use std::fmt::{Display, Formatter};

pub struct QuoteGame {
    quotes: Vec<Quote>,
    current_quote: Option<Quote>,
    guess_counter: usize,
    pub score: usize,
}

#[derive(Debug)]
pub struct QuoteDisplayPrompt(Quote);

impl Display for QuoteDisplayPrompt {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "Who said this?")?;
        writeln!(f, "Quote: {}", self.0.content)
    }
}

pub struct HintDisplay(String);

impl Display for HintDisplay {
    fn fmt(&self, f: &mut Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "Hint: {}", self.0)
    }
}

// new take ownership of quotes and shuffle them
pub fn new(quotes: Vec<Quote>) -> QuoteGame {
    let mut quotes = quotes;
    quotes.shuffle(&mut thread_rng());
    QuoteGame {
        quotes,
        current_quote: None,
        guess_counter: 0,
        score: 0,
    }
}

impl QuoteGame {
    const GUESS_LIMIT: usize = 4;
    pub fn get_next_prompt(&mut self) -> Option<QuoteDisplayPrompt> {
        if let Some(q) = self.quotes.pop() {
            self.current_quote = Some(q.clone());
            return Some(QuoteDisplayPrompt(q));
        }
        return None;
    }

    pub fn check_guess(&mut self, guess: &str) -> bool {
        const MAX_EDIT_DISTANCE: usize = 4;

        let cq = self
            .current_quote
            .as_ref()
            .expect("should have a current quote by the time check_guess is called");

        let str1 = &cq.author.trim().to_lowercase();
        let str2 = &guess.to_lowercase();
        let m = str1.len();
        let n = str2.len();

        if edit_distance(str1, str2, m, n) > MAX_EDIT_DISTANCE {
            self.guess_counter += 1;
            return false;
        }
        self.score += 1;
        self.guess_counter += 0;
        return true;
    }

    pub fn user_prompt(&self) -> String {
        let mut line = String::new();
        println!("Guess the author: ");
        match std::io::stdin().read_line(&mut line) {
            Ok(_) => {}
            Err(_) => {}
        }
        line.trim().to_string()
    }

    pub fn can_continue(&self) -> bool {
        if self.guess_counter < QuoteGame::GUESS_LIMIT {
            return true;
        }
        return false;
    }

    pub fn provide_hint(&self) -> String {
        const HINT_ACTIVATION: usize = 2;
        if self.guess_counter >= HINT_ACTIVATION {
            if let Some(q) = &self.current_quote {
                let hint: Vec<String> = q
                    .author
                    .split(" ")
                    .map(|p| p.chars().nth(0).unwrap_or('\0').to_string())
                    .collect();

                return "Authors Initials: ".to_string() + &hint.join(" ");
            }
            return "".to_string();
        }
        return "".to_string();
    }

    pub fn get_answer(&self) -> String {
        return self
            .current_quote
            .as_ref()
            .expect("should have a current quote by the time get_answer is called")
            .author
            .clone();
    }

    pub fn guesses_remaining(&self) -> usize {
        return QuoteGame::GUESS_LIMIT - self.guess_counter;
    }
}
