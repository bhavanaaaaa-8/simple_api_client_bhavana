# REST API JSON Data Viewer

## Description
A Python program that retrieves JSON data from a public REST API, checks HTTP status codes, handles connection failures, and displays selected information in a clean, readable format.

The program uses the JSONPlaceholder API to retrieve user details such as names, email addresses, cities, and company names.

## Features
- Retrieves data from a public REST API using `requests`.
- Checks HTTP status codes to verify request success.
- Converts JSON responses into Python data structures.
- Displays selected user information in a formatted layout.
- Handles connection failures and request timeouts.
- Handles HTTP errors and other request-related exceptions.
- Supports secure API key handling through environment variables for APIs that require authentication.

## Requirements
- Python 3.8 or later
- `requests` library
- Internet connection

## Installation

Install the required library:

```bash
pip install requests
```

## API Used

JSONPlaceholder Users API:

https://jsonplaceholder.typicode.com/users

This is a public testing API that does not require an API key.

## How to Run

1. Save the Python program as `main.py`.
2. Open a terminal in the project folder.
3. Run the command:

```bash
python main.py
```

4. The program retrieves the user data and displays the selected fields.

## Example Output

```text
========== USER DIRECTORY ==========

Data retrieved successfully!

Name    : Leanne Graham
Email   : Sincere@april.biz
City    : Gwenborough
Company : Romaguera-Crona
```

*The displayed values are examples of the expected output format.*

## Error Handling

The program handles common errors:

- **ConnectionError:** The server cannot be reached.
- **Timeout:** The request takes too long.
- **HTTPError:** The server returns an unsuccessful HTTP status code.
- **RequestException:** Other request-related errors.

## API Key Security

The JSONPlaceholder API does not require an API key. If the program is adapted to use an authenticated API, store its key in an environment variable instead of hard-coding it.

Never publish API keys in source code or upload them to GitHub.

## Concepts Practised

- Python modules and imports
- HTTP requests and status codes
- REST APIs
- JSON parsing
- Lists and dictionaries
- Loops and formatted strings
- Exception handling
- Environment variables and basic security

## Learning Outcome

This project demonstrates how Python communicates with web APIs, processes JSON data, handles network errors, and presents selected information in a readable format.
