// Types file for debit type transactions structures
export interface DebitTransaction {
    id: number;
    is_past_due: boolean;
    is_recurring_due: boolean;
    transaction_name: string;
    amount: string; 
    category: string;
    subcategory: string | null;
    is_recurring: boolean;
    next_transaction_date: string | null;
    frequency: string | null;
    description: string;
    transaction_date: string;
    bank_account: number;
}