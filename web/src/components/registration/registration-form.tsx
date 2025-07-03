'use client'
import { Eye } from "lucide-react";
import { useState } from "react";



function handleShowPassword(): void {
    const passwordInput = document.getElementById('password') as HTMLInputElement;
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}

export default function RegistrationForm() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [message, setMessage] = useState('');

    async function handleSubmit(e: React.FormEvent<HTMLFormElement>) {
        e.preventDefault();
        setMessage('');
    
        try {
            const response = await fetch('http://localhost:8000/user/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            if (response.ok) {
                setMessage('Registration successful!');
                
            } else {
                const data = await response.json();
                setMessage(`Registration failed: ${data.detail || 'Unknown error'}`);
            }
        } catch (error) {
            console.error('Error during registration:', error);
        }
    }

    return (
        <div className="gap-4">
            <form onSubmit={handleSubmit} className="registration-form">
                <div className="relative mt-4 mb-8">
                    <input
                        type="text"
                        id="username"
                        name="username"
                        required
                        className="peer w-full px-3 py-2 border rounded focus:outline-none focus:ring-1 focus:ring-sky-500 placeholder-transparent"
                        placeholder="Username"
                        onChange={(e) => setUsername(e.target.value)}
                        value={username}
                    />
                    <label
                        htmlFor="username"
                        className="
                        absolute left-3 top-2 text-gray-500 bg-white px-1 transition-all duration-200
                        pointer-events-none
                        peer-placeholder-shown:top-2
                        peer-placeholder-shown:text-base
                        peer-placeholder-shown:text-gray-500
                        peer-focus:-top-3
                        peer-focus:text-md
                        peer-focus:text-sky-500
                        peer-focus:bg-white
                        peer-not-placeholder-shown:-top-3
                        peer-not-placeholder-shown:text-md
                        peer-not-placeholder-shown:text-blue-500
                        peer-not-placeholder-shown:bg-white
                        "
                    >
                Username
                    </label>
                </div>
                <div className="relative mt-4 mb-8">
                    <input
                        type="password"
                        id="password"
                        name="password"
                        required
                        className="peer w-full px-3 py-2 border rounded focus:outline-none focus:ring-1 focus:ring-sky-500 placeholder-transparent"
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                    />
                    <label
                        htmlFor="password"
                        className="absolute left-3 top-2 text-gray-500 bg-white px-1 transition-all duration-200 
                        pointer-events-none
                        peer-placeholder-shown:top-2
                        peer-placeholder-shown:text-base
                        peer-placeholder-shown:text-gray-500
                        peer-focus:-top-3
                        peer-focus:text-md
                        peer-focus:text-sky-500
                        peer-focus:bg-white
                        peer-not-placeholder-shown:-top-3
                        peer-not-placeholder-shown:text-md
                        peer-not-placeholder-shown:text-blue-500
                        peer-not-placeholder-shown:bg-white
                        "
                    >   
                        Password
                    </label>
                    <button
                        type="button"
                        onClick={handleShowPassword}
                        className="absolute right-3 top-2 text-gray-500 hover:text-gray-700 focus:outline-none hidden peer-focus:block peer-not-placeholder-shown:block"
                    >
                        <Eye
                        className="absolute right-3 text-gray-500 cursor-pointer hover:text-gray-700"
                        
                    />
                    </button>
                
                </div>
                <button className="w-full bg-green-600 text-white py-2 rounded hover:bg-blue-600 mt-2 mb-0
                focus-bg-green-600
                active" 
                type="submit">
                        Sign Up
                </button>
                {message && <div className="mt-4 text-center text-green-600">{message}</div>}
            </form>
        </div>
    );
}