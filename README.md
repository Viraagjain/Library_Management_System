# Library Management System

## Overview

The Library Management System is a simple application that allows users to perform basic operations such as adding books, borrowing books, returning books, and viewing available books. This project follows Test-Driven Development (TDD) principles, ensuring high test coverage and clean, maintainable code.

## Features

- *Add Books*: Add new books to the library with unique identifiers, titles, authors, and publication years.
- *Borrow Books*: Borrow a book if it's available; otherwise, an error is raised.
- *Return Books*: Return a borrowed book and update its availability.
- *View Available Books*: View a list of all available books in the library.

## Technology Stack

- *Language*: Python 3.x
- *Testing Framework*: Pytest

## Project Structure

```plaintext
LibraryManagementSystem/
│
├── library.py             # Contains the main logic for the Library Management System
├── test_library.py        # Contains the test cases following TDD principles
├── README.md              # Project documentation
├── requirements.txt       # List of dependencies
└── venv/                  # Python virtual environment
