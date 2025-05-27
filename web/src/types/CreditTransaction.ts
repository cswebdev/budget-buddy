// Types file for credit type transactions structures
export interface CreditTransaction {
    id: number;
    transaction_name: string;
    amount: string; 
    category: string;
    transaction_date: string;
    bank_account: number;
}