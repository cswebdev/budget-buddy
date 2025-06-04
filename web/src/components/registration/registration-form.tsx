'use client'
function handleSubmit(event: React.FormEvent<HTMLFormElement>): void {
    event.preventDefault();
    const formData = new FormData(event.currentTarget);
    const username = formData.get('username');
    const password = formData.get('password');
    console.log('Registering:', { username, password });
}

export default function RegistrationForm() {
    return (
        <form onSubmit={handleSubmit} className="registration-form">
            <div className="relative mb-6">
                <input
                    type="text"
                    id="username"
                    name="username"
                    required
                    className="peer w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-primary placeholder-transparent"
                    placeholder="Username"
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
                    peer-focus:text-sm
                    peer-focus:text-primary
                    peer-focus:bg-white
                    peer-not-placeholder-shown:-top-3
                    peer-not-placeholder-shown:text-sm
                    peer-not-placeholder-shown:text-primary
                    peer-not-placeholder-shown:bg-white
                     "
                >
            Username
                </label>
            </div>
            <div className="relative mb-6">
                <input
                    type="password"
                    id="password"
                    name="password"
                    required
                    className="peer w-full px-3 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-primary placeholder-transparent"
                    placeholder="Password"
                />
                <label
                    htmlFor="password"
                    className="absolute left-3 top-2 text-gray-500 bg-white px-1 transition-all duration-200 
                    pointer-events-none
                    peer-placeholder-shown:top-2
                    peer-placeholder-shown:text-base
                    peer-placeholder-shown:text-gray-500
                    peer-focus:-top-3
                    peer-focus:text-sm
                    peer-focus:text-primary
                    peer-focus:bg-white
                    peer-not-placeholder-shown:-top-3
                    peer-not-placeholder-shown:text-sm
                    peer-not-placeholder-shown:text-primary
                    peer-not-placeholder-shown:bg-white
                     "
                >   
                    Password
                </label>
            </div>
            <button className="w-full bg-green-600 text-white py-2 rounded hover:bg-blue-600 mt-5" type="submit">
                    Sign Up
            </button>
        </form>
    );
}