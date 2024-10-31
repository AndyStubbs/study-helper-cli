# Study Helper Quiz Program

**Version:** 1.0  
**Author:** Andy Stubbs

## Overview

This command-line quiz program, **Study Helper 1.0**, enables users to create, edit, and take quizzes interactively through a terminal interface. The program offers an easy-to-use menu system with options to run a quiz, create a new quiz, edit existing quizzes, and quit the application.

The quiz program uses ANSI formatting for colorful and intuitive display, and it includes basic error handling for a smooth user experience.

## Features

- **Run Quiz:** Allows users to take a quiz, answering multiple-choice questions and receiving feedback.
- **Create Quiz:** Enables users to create a custom quiz by entering questions, answers, and concepts for study topics.
- **Edit Quiz:** Lets users modify existing quizzes, adding or changing questions and answers.
- **Quit:** Exits the program gracefully.

The program supports saving quizzes to a file, so users can return to previously created quizzes.

## Requirements

- Python 3.x

## Setup and Run

1. Clone or download the repository.
2. Run the program:
Windows:
```python main.py```
Linux:
```python3 main.py```

## Usage

- **Start** the program by following the steps in the "Setup and Run" section.
- **Press Ctrl+C** to exit at any time, or use the menu to quit gracefully.
- **Follow the prompts** in the menu to create, edit, or run a quiz.

## Code Overview

- **main.py:** Initializes the program, loads quizzes, and handles the main menu interaction.
- **create.py:** Provides functionality for creating new quizzes, including adding questions, answers, and concepts.
- **edit.py:** Contains functionality for editing existing quizzes.
- **run.py:** Manages the quiz-taking experience.
- **quizzes.py:** Manages the state of the quizzes to allow persistence.
- **quiz.py:** Handles saving and loading the quiz and the quiz data.
- **ansi.py:** Handles support for ANSI colors in the terminal.

## Unit Tests

Unit tests for quiz data types and saving and loading quizes.

## Unit Test Usage

Windows:
```python test.py```

Linux:
```python3 test.py```