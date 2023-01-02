# TOTP Token Generator

This code generates Time-Based One-Time Passwords (TOTPs) for multiple issuers. It also includes a GUI with a dark mode toggle.

## Dependencies
- pyotp
- PyQt6

To install these dependencies, use

```
pip install pyotp PyQt6
```

## Usage

To use the TOTP generator, replace the randomly generated issuer names and secrets with your own. Then run the code and click the "Copy" button next to the desired issuer. The TOTP token will be copied to your clipboard. You can toggle between dark and light mode using the "Toggle Dark Mode" button.

## Code Structure

The code is organized as follows:
1. Import necessary dependencies
2. Define style sheets for dark and light modes
3. Create the `TOTPWindow` class that inherits from `QtWidgets.QWidget`
4. Define the `__init__` method to initialize the GUI and create a dictionary of secrets
5. Define the `initUI` method to create the GUI elements, including a label and read-only line edit for each issuer, and a "Copy" button to copy the TOTP token to the clipboard
6. Define the `copy_token` method to copy the TOTP token to the clipboard when the "Copy" button is clicked
7. Define the `toggle_dark_mode` method to switch between dark and light modes when the "Toggle Dark Mode" button is clicked
8. Define the `update_tokens` method to update the TOTP tokens every 30 seconds
9. Create a timer to call the `update_tokens` method every 30 seconds
10. Create an instance of `TOTPWindow` and display it
