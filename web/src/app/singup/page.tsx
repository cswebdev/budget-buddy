import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"

import RegistrationForm from "@/components/registration/registration-form";
import { Separator } from "@/components/ui/separator"

export default function SignupPage(){
    return (
        <div className="flex items-center justify-center min-h-screen">
        <Card className="w-full max-w-md gap-4 mt-10">
            <CardHeader>
                <CardTitle className="text-center my-3">Sign Up</CardTitle>
                <CardDescription className="text-center text-sm text-gray-600">
                    Get in control of your finances today.
                </CardDescription>
            </CardHeader>
            <CardContent>
                <RegistrationForm />
            </CardContent>
            <CardFooter className="flex flex-col justify-center gap-0">
                {/* google one click  */}
                <button className="w-full bg-gray-200 text-gray-800 py-2 rounded hover:bg-gray-300 mb-0">
                    Sign up with Google
                </button>
                <a href="#" className="w-full text-center text-sm mt-3 text-blue-500 hover:underline">
                    Already have an account?
                </a>
            </CardFooter>
        </Card>
        </div>
    );
}