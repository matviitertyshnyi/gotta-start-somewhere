# gotta-start-somewhere
Just a simple CRUD python + json script. 

# Python CLI Task Tracker

A lightweight, interactive command-line task management application built with pure Python. It provides a clean terminal interface for organizing daily tasks, tracking their progress, and saving data locally.

This project was built to practice core Python concepts, including file handling, JSON serialization, list/dictionary manipulation, and building interactive command-line loops.

## Features

- **Interactive Menu:** A clean terminal UI that automatically refreshes the screen between operations.
- **Task Management:** Add new tasks and remove unwanted ones.
- **Status Tracking:** Update tasks to specific states:
  - `Uncompleted`
  - `In progress`
  - `Completed`
- **Filtering:** Quickly filter and view tasks based on their current progress.
- **Persistent Storage:** Automatically saves tasks to a local `todolist.json` file so progress is never lost between sessions.
- **Zero External Dependencies:** Built entirely with Python's standard `json` and `os` libraries.

## Prerequisites

- Python 3.x installed on your machine.

## How to Run

1. Clone this repository to your local machine:
   ```bash
   git clone <your-repository-url-here>
   cd <your-repository-folder>

2. Run the application from your terminal:
    ```bash
    python todolist.py
