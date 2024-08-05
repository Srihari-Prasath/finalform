# Application Form Project

This project is a web application for collecting user data through a form, with features for managing and exporting data. Users can select their willingness to participate, choose topics of interest, and submit their details. The application stores data in an SQLite database and exports it to an Excel file.

## Features

- **Form Submission**: Collects user information including name, department, email, qualification, designation, total experience, and experience in NSCET.
- **Topic Selection**: Users can select topics from various categories including Aptitude, Verbal Ability, Soft Skills, and Technical.
- **Willingness Handling**: Differentiates between willing and not willing users and stores their data accordingly.
- **Excel Export**: Exports the data to an Excel file, organizing it into separate sheets for willing and not willing users.
- **Database Management**: Uses SQLite for storing user data with functions for inserting, updating, and querying records.

## Installation

Follow these steps to set up and run the project on your local machine:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/your-repository.git
   cd your-repository
2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies** :
    ```bash
    pip install -r requirements.txt
4. **Create and Set Up the Database** :
Run the following script to set up your SQLite database:
    ```bash
    python setup_database.py
5. **Run the Application**:
    ```bash
    python app.py
