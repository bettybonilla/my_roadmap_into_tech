use anyhow;
use anyhow::Context;
use reqwest;
use serde_derive::{Deserialize, Serialize};
use soup::prelude::*;
use std::fs::File;
use std::io::Read;

pub(crate) struct QuotesScraper {
    base_url: String,
    current_page: u32,
    client: reqwest::Client,
    pub quotes: Vec<Quote>,
}

#[derive(Debug, Serialize, Deserialize, Clone)]
#[allow(dead_code)]
pub(crate) struct Quote {
    pub content: String,
    pub author: String,
    pub tags: Vec<String>,
    pub hint: String,
}

impl QuotesScraper {
    pub fn new() -> QuotesScraper {
        QuotesScraper {
            base_url: "https://quotes.toscrape.com".to_string(),
            current_page: 1,
            client: reqwest::Client::new(),
            quotes: Vec::new(),
        }
    }

    pub async fn download_page_markup(&mut self) -> anyhow::Result<String> {
        let url = format!("{}/page/{}", self.base_url, self.current_page);
        println!("downloading quotes from {url}");
        let result = self.client.get(&url).send().await?.text().await?;

        if result.contains("No quotes found!") {
            anyhow::bail!(format!("page not found: {url}"));
        }

        self.current_page += 1;
        Ok(result)
    }

    pub async fn download_bio_markup(&self, href: &str) -> anyhow::Result<String> {
        let url = format!("{}{}", self.base_url, href);
        println!("downloading bio info from {url}");
        let result = self.client.get(url).send().await?.text().await?;
        Ok(result)
    }

    pub async fn parse_data(&mut self, markup: String) -> anyhow::Result<()> {
        for quote in Soup::new(&markup).class("quote").find_all() {
            let inner = quote.display();
            let content = self.find_content_by_class(&inner, "text", true)?;
            let author = self.find_content_by_class(&inner, "author", false)?;
            let tags = self.find_all_content_by_class(&inner, "tag");
            let bio_href = self.find_by_tag(&inner, "a")?;
            let bio_content = self.download_bio_markup(&bio_href).await?;

            let birthday = self.find_content_by_class(&bio_content, "author-born-date", false)?;
            let location =
                self.find_content_by_class(&bio_content, "author-born-location", false)?;

            self.quotes.push(Quote {
                content,
                author,
                tags,
                hint: birthday + " " + &location,
            });
        }
        Ok(())
    }

    fn find_content_by_class(
        &self,
        html: &str,
        class_name: &str,
        trim_quotes: bool,
    ) -> anyhow::Result<String> {
        let content = Soup::new(&html)
            .class(class_name)
            .find()
            .with_context(|| format!("could not find content {class_name}"))?
            .text();
        if trim_quotes {
            return Ok(content.replace("“", "").replace("”", ""));
        }
        return Ok(content);
    }

    fn find_all_content_by_class(&self, html: &str, class_name: &str) -> Vec<String> {
        return Soup::new(&html)
            .class(class_name)
            .find_all()
            .map(|x| x.text())
            .collect();
    }

    fn find_by_tag(&self, html: &str, tag: &str) -> anyhow::Result<String> {
        let tag = Soup::new(html)
            .tag(tag)
            .find()
            .with_context(|| format!("could not find content {tag}"))?;

        Ok(tag
            .attrs()
            .get("href")
            .context("could not find href")?
            .to_string())
    }
}

#[test]
fn test_parsing() -> anyhow::Result<()> {
    let path = "src/bin/scrape_quotes/test_data/test_data.html";
    let mut file = File::open(path).with_context(|| format!("unable to open file: {path}"))?;
    let mut data = String::new();
    file.read_to_string(&mut data)
        .expect("unable to read string");

    // TODO use a mock client
    //
    // let mut parser = QuotesScraper::new();
    // let res = parser.parse_data(data);
    //
    // if let Err(e) = res {
    //     println!("{e}");
    // }
    Ok(())
}
