// Types for bank account-related data structures
export interface BankAccount {
    id: number;
    total_credit: number;
    total_debit: number;
    number_of_credit_transactions: number;
    number_of_debit_transactions: number;
    account_type: "Checking" | "Savings" | "Credit" | "Other";
    account_number: string;
    bank_name: string;
    account_name: string;
    balance: string; 
    updated_at: string;
    payment_due_date: string | null;
    minimum_payment: string | null;
    last_payment_date: string | null;
    past_due_amount: string | null;
    is_over_limit: boolean;
}