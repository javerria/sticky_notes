# Sticky Notes Project

Welcome to the Sticky Notes Project! This project allows users to create, edit, and delete notes on a virtual pinboard. It's designed to provide a simple and interactive way to manage notes.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Project Overview

The Sticky Notes Project is a web application that mimics a physical pinboard where users can add sticky notes. Each note can be customized with text, and users can edit or delete them as needed. The project leverages modern web technologies to create an intuitive user interface.

## Features

- **Add Notes**: Users can add new notes to the pinboard.
- **Edit Notes**: Users can edit the content of existing notes.
- **Delete Notes**: Users can remove notes from the pinboard.
- **View Notes**: Users can view the details of any note.
- **User-Friendly Interface**: The interface is designed to be simple and easy to use.

## Technologies Used

- **Frontend**:
  - HTML
  - CSS
  - Bootstrap 
  - Font Awesome

- **Backend**:
  - Django (Python)

- **Database**:
  - SQLite (default for Django projects)

## Installation

To get a local copy of the project up and running, follow these steps:

1. **Clone the repository:**
  ```
  git clone https://github.com/javerria/sticky-notes.git
  ```
2. **Navigate to the project directory:**
  ```
  cd .\sticky-notes
  ```
4. **Create a virtual environment:**
  ```
  python -m venv venv
  ```
5. **Activate the virtual environment:**

  On windows:
  ```
  venv\Scripts\activate
  ```
  On macOS/Linux:
  ```
  source venv/bin/activate
  ```
6. **Install the dependencies:**
  ```
  pip install -r requirements.txt
  ```
7. **Run the initial Django migrations:**
  ```
  python manage.py migrate
  ```
8. **Start the development server:**
  ```
  python manage.py runserver
  ```

## Usage
- *Adding a Note:* Click on the "New Note" button to create a new note. Fill in the details and save.
- *Editing a Note:* Click on the "Edit" button or icon on an existing note to modify its content.
- *Deleting a Note:* Click on the "Delete" button or icon on an existing note to remove it.
- *Viewing a Note:* Click on the title on the note on the pinboard to view it seperately.
  
## Contributing
Contributions to this project are welcome! If you have an idea for a new feature or have found a bug, please open an issue or submit a pull request.

