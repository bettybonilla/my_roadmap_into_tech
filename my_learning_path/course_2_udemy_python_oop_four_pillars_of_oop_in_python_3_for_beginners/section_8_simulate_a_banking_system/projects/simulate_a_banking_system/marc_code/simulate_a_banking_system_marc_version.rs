use anyhow::Result;
use rand::Rng;
use std::collections::HashMap;
use thiserror::Error;

#[derive(Error, Debug)]
pub enum BankingError {
    #[error("AccountNumber {0} not found, please create an account first")]
    AccountNumberNotFound(u64),
    #[error("Account does not have enough funds. Requested {0}, have {1}")]
    NotEnoughFunds(f64, f64),
    #[error("This bank no longer has room to open new accounts")]
    NoMoreAccountAvailable,
}

pub trait IAccount {
    fn withdrawal(&mut self, account_number: u64, amount: f64) -> Result<bool, BankingError>;
    fn deposit(&mut self, account_number: u64, amount: f64) -> Result<bool, BankingError>;
    fn open_account(&mut self, first_name: String) -> Result<u64, BankingError>;
    fn display_balance(&self, account_number: u64) -> Result<(), BankingError>;
}

#[derive(Default)]
struct Account {
    records: HashMap<u64, Record>,
}

impl Account {
    pub fn new() -> Self {
        Account {
            records: Default::default(),
        }
    }

    fn generate_account_id(&self) -> u64 {
        rand::thread_rng().gen_range(10000..99999)
    }
}

impl IAccount for Account {
    fn withdrawal(&mut self, account_number: u64, amount: f64) -> Result<bool, BankingError> {
        if let Some(account) = self.records.get_mut(&account_number) {
            if amount > account.amount {
                Err(BankingError::NotEnoughFunds(amount, account.amount))?
            }
            account.amount -= amount;
            return Ok(true);
        }
        Err(BankingError::AccountNumberNotFound(account_number))?
    }

    fn deposit(&mut self, account_number: u64, amount: f64) -> Result<bool, BankingError> {
        if let Some(account) = self.records.get_mut(&account_number) {
            account.amount += amount;
            return Ok(true);
        }
        Err(BankingError::AccountNumberNotFound(account_number))?
    }

    fn open_account(&mut self, first_name: String) -> Result<u64, BankingError> {
        if self.records.len() >= 89999 {
            Err(BankingError::NoMoreAccountAvailable)?
        }

        loop {
            let account_id = self.generate_account_id();
            if self.records.get(&account_id).is_some() {
                continue;
            }
            self.records.insert(
                account_id,
                Record {
                    first_name: first_name.clone(),
                    amount: 0.0,
                },
            );
            return Ok(account_id);
        }
    }

    fn display_balance(&self, account_number: u64) -> Result<(), BankingError> {
        if let Some(account) = self.records.get(&account_number) {
            println!(
                "The balance on account: {account_number} is: {:.2}",
                account.amount
            )
        }
        Err(BankingError::AccountNumberNotFound(account_number))?
    }
}

pub struct Record {
    first_name: String,
    amount: f64,
}

pub struct Bank {
    saving_accounts: Account,
    checking_accounts: Account,
}

impl Bank {
    fn new() -> Self {
        Bank {
            saving_accounts: Account::new(),
            checking_accounts: Account::new(),
        }
    }

    pub fn open_savings_account(&mut self, first_name: String) -> Result<u64, BankingError> {
        self.saving_accounts.open_account(first_name)
    }

    pub fn withdrawal_from_savings_account(
        &mut self,
        account_number: u64,
        amount: f64,
    ) -> Result<bool, BankingError> {
        self.saving_accounts.withdrawal(account_number, amount)
    }

    pub fn deposit_into_savings_account(
        &mut self,
        account_number: u64,
        amount: f64,
    ) -> Result<bool, BankingError> {
        self.saving_accounts.deposit(account_number, amount)
    }

    pub fn display_savings_account_balance(&self, account_number: u64) -> Result<(), BankingError> {
        self.saving_accounts.display_balance(account_number)
    }

    pub fn open_checking_account(&mut self, first_name: String) -> Result<u64, BankingError> {
        self.checking_accounts.open_account(first_name)
    }

    pub fn withdrawal_from_checking_account(
        &mut self,
        account_number: u64,
        amount: f64,
    ) -> Result<bool, BankingError> {
        self.checking_accounts.withdrawal(account_number, amount)
    }

    pub fn deposit_into_checking_account(
        &mut self,
        account_number: u64,
        amount: f64,
    ) -> Result<bool, BankingError> {
        self.checking_accounts.deposit(account_number, amount)
    }

    pub fn display_checking_account_balance(
        &self,
        account_number: u64,
    ) -> Result<(), BankingError> {
        self.checking_accounts.display_balance(account_number)
    }
}
