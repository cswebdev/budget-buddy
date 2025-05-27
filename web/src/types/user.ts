// Types for user-related data structures
import { BankAccount } from './BankAccount';
export interface User {
    id: number;
    username: string;
    date_joined: string; 
    linked_bank_accounts: BankAccount[];
}