import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import LoginForm from "@/components/login/login-form";
export default function LoginPage() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <Card className="w-full max-w-md gap-4 mt-10">
        <CardHeader>
            <CardTitle className="text-center my-3">Login</CardTitle>
            <CardDescription className="text-center text-sm text-gray-600">
            Welcome back! Please log in to your account.
            </CardDescription>
        </CardHeader>
        <CardContent>
            <LoginForm />
        </CardContent>
        <CardFooter className="flex flex-col justify-center gap-0">
            {/* google one click  */}
            <button className="w-full bg-gray-200 text-gray-800 py-2
            rounded hover:bg-gray-300 mb-0">
                Sign in with Google
            </button>
            <a href="#" className="w-full text-center text-sm mt-3 text-blue-500 hover:underline">
                Don&#39;t have an account? Sign up
            </a>
        </CardFooter>
      </Card>
    </div>
  );
}