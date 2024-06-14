Below is an HTML code snippet for a login form based on the user story for a streamlined and secure user login, utilizing Modus Web Components. This example assumes the Modus Web Components library is correctly integrated into your project.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Form</title>
    <!-- Ensure Modus Components CSS & JS are included -->
</head>
<body>
    <div class="login-container">
        <!-- Login Form -->
        <form id="loginForm">
            <!-- Username Input -->
            <modus-text-input
                label="Username"
                placeholder="Enter your username"
                type="text"
                required
                aria-label="Username">
            </modus-text-input>

            <!-- Password Input with Visibility Toggle -->
            <modus-text-input
                label="Password"
                placeholder="Enter your password"
                type="password"
                required
                include-password-text-toggle="true"
                aria-label="Password">
            </modus-text-input>

            <!-- Login Button -->
            <modus-button
                variant="primary"
                onclick="handleLogin()">
                Log In
            </modus-button>

            <!-- Forgot Password Link -->
            <modus-button
                variant="link"
                onclick="navigateToForgotPassword()">
                Forgot Password?
            </modus-button>

            <!-- Sign Up Link for New Users -->
            <modus-button
                variant="link"
                onclick="navigateToSignUp()">
                Sign Up
            </modus-button>
        </form>
    </div>

    <script>
        // Handle Login Submission
        function handleLogin() {
            // Implement login logic here
            console.log('Login attempt');
            // Prevent form from submitting for demonstration
            event.preventDefault();
        }

        // Navigate to Forgot Password Page
        function navigateToForgotPassword() {
            console.log('Navigate to Forgot Password');
            // Implement navigation logic here
        }

        // Navigate to Sign Up Page
        function navigateToSignUp() {
            console.log('Navigate to Sign Up');
            // Implement navigation logic here
        }
    </script>
</body>
</html>
```

Please note:
- This example provides a basic structure and needs to be integrated with your backend authentication logic for handling login attempts, navigating to forgot password, and sign-up pages.
- You need to include the Modus Components library in your project for the `modus-text-input` and `modus-button` components to work. This typically involves adding the library's CSS and JavaScript files to your HTML document's `<head>` section.
- The `onclick` attributes of the buttons are used here for demonstration purposes. In a real application, you would likely use a more robust event handling mechanism to process the login and navigate to other pages securely.