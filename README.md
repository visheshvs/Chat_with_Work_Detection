# Produciton Control - Work Detection Query Assistant

## Description

The **Production Control - Work Detection Query Assistant** is a tool designed to facilitate the conversion of CSV files into a SQLite database and enable users to interact with the data using natural language queries. This project is an extension of the research conducted by Vishesh Vikram Singh during his Ph.D. More about the Ph.D. research can be found [here](https://visheshvsingh.notion.site/Ph-D-Dissertation-12cb1218451c8003bae4d43adfb9105b). 

The repository for the code generating the data can be found at [XYZ.COM](http://xyz.com).

## Prerequisites

Ensure you have the following installed on your system:

- **Python**: Version 3.8 or higher
- **SQLite**: For managing the database

### Python Packages

The project relies on the following Python packages:

- `openai`
- `python-dotenv`
- `sqlite3` (Standard library)
- `pandas`

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/visheshvs/Chat_with_Work_Detection.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd Chat_with_Work_Detection

   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Project Structure

The project will create the following directory structure:

```

├── CSV_Data/ # Place your CSV files here
├── Database/ # Contains generated SQLite databases
└── ...
```


## Usage

### Importing CSV Files into SQLite

Place your CSV files in the `CSV_Data` directory and run:


```bash
python csv_to_sql.py
```

The script will:

- Read each CSV file from the `CSV_Data` directory.
- Convert each CSV into a corresponding table in a SQLite database.
- Store the SQLite database in the `Database` directory.
- Ensure that table names are formatted by replacing spaces with underscores and converting them to lowercase.

### 2. Querying the Database with Natural Language

Run the query assistant:

```bash
python query_with_llm.py
```

The assistant will:

- Display a list of available SQLite databases in the `Database` directory.
- Allow you to select a database to query.
- Display the schema and sample data of the selected database for context.
- Accept natural language questions from the user.
- Convert the natural language input into SQL queries using OpenAI's GPT-4 model.
- Execute the generated SQL query and display the results.

#### Example Interaction:
```
Welcome to the Work Detection Query Assistant!
Available databases:
csv_data_database.db
Select a database (enter the number): 1
Using database: csv_data_database.db
Database Schema and Sample Data:
Table: area_qto
Columns:
Location Number (TEXT)
Location Name (TEXT)
Location Type (TEXT)
Area (INTEGER)
Area Unit (TEXT)
Sample Data:
{'Location Number': '500', 'Location Name': 'FSAE Lobby', 'Location Type': 'Lobby/Corridor', 'Area': 259, 'Area Unit': 'SF'}
{'Location Number': '501', 'Location Name': 'STAIR 1 VEST.', 'Location Type': 'Room', 'Area': 81, 'Area Unit': 'SF'}
{'Location Number': '502', 'Location Name': 'STAIR 2 VEST.', 'Location Type': 'Room', 'Area': 65, 'Area Unit': 'SF'}
Type 'exit' to quit.
Enter your question: What are the activities, their location, and their trades with longest durations (top 5)?
Generated SQL Query:
SELECT "Work Detected", "Location Name", "Trade", "Duration"
FROM "merged_ml_data"
ORDER BY "Duration" DESC
LIMIT 5;
Executing SQL Query: SELECT "Work Detected", "Location Name", "Trade", "Duration"
FROM "merged_ml_data"
ORDER BY "Duration" DESC
LIMIT 5;
Query Results:
Work Detected | Location Name | Trade | Duration
----+-----+-----+----
Thermal Insulation | FSAE Lobby | Drywall - Fireproofing | 99.0
Wet-Pipe Sprinkler Systems | FSAE Lobby | Fire Protection | 99.0
Hollow Metal Doors and Frames | SERV ELEV VEST. | Doors/Frames/Hardware | 98.0
Hollow Metal Doors and Frames | SERV ELEV VEST. | Door - waterproofing | 98.0
Raceway and Boxes for Electrical Systems | STAIR 2 | Electrical | 87.0
```

### 3. Exiting the Assistant

To exit the query assistant, type `exit` or `quit` when prompted for a question.


## Credits

- **Vishesh Vikra Singh**
  - [Website](https://visheshvsingh.notion.site/)
  - [LinkedIn](https://www.linkedin.com/in/visheshvikram/)