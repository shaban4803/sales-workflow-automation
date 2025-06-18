LinkedIn Contact Extractor with Apollo Sidebar (Python Automation)

This Python script automates the process of opening a LinkedIn profile in Google Chrome, interacting with the Apollo.io sidebar, and extracting contact details such as email addresses and phone numbers.

Features:
- Opens a LinkedIn profile using Chrome with a specific user profile
- Waits for and clicks Apollo buttons to reveal email and phone
- Copies the full page content
- Extracts emails and phone numbers using regular expressions
- Prints the extracted data in JSON format in the terminal

Requirements:
- Python 3
- pyautogui
- pyperclip

Usage:
1. Place the required Apollo sidebar button images (apollo_button.png, etc.) in the project folder.
2. Update the LinkedIn profile URL and Apollo sidebar click coordinates if needed.
3. Run the script.
4. View extracted contact info in the terminal.

This script is helpful for basic data extraction where manual copy-paste is not efficient.
