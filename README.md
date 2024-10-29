# Produciton Control - Work Detection Query Assistant

## Description

The **Produciton Control - Work Detection Query Assistant** is a tool designed to facilitate the conversion of CSV files into a SQLite database and enable users to interact with the data using natural language queries. It processes CSV exports from various sources, stores the data into a SQLite database, and allows users to generate and execute SQL queries through intuitive language prompts powered by OpenAI's API.

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
   git clone https://github.com/yourusername/your-repo.git
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd your-repo
   ```

3. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your OpenAI API key:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

4. **Install Dependencies**

   If you have a `requirements.txt` file, you can install all dependencies at once:

   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

The project will create the following directory structure:


The project will create the following directory structure:

```

├── CSV_Data/ # Place your CSV files here
├── Database/ # Contains generated SQLite databases
└── CSV Exports/ # Contains processed CSV files
├── export1/ # Processed exports from source1
├── export2/ # Processed exports from source2
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

#### Example

```bash
python csv_to_sql.py
```

**Output:**
Processing sales_data.csv...
Successfully read CSV file: CSV_Data/sales_data.csv
Connected to SQLite database at: Database/csv_data_database.db
Inserted 150 records into table 'sales_data' in SQLite database.
SQLite connection closed.
Processing inventory.csv...
Successfully read CSV file: CSV_Data/inventory.csv
Connected to SQLite database at: Database/csv_data_database.db
Inserted 75 records into table 'inventory' in SQLite database.
SQLite connection closed.

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
Welcome to the CSV Database Query Assistant!
Available databases:
csv_data_database.db
export1_database.db
Select a database (enter the number): 1
Using database: csv_data_database.db
Database Schema and Sample Data:
Table: sales_data
Columns:
order_id (INTEGER)
product_name (TEXT)
quantity (INTEGER)
price (REAL)
order_date (TEXT)
Sample Data:
{'order_id': 1, 'product_name': 'Widget A', 'quantity': 10, 'price': 9.99, 'order_date': '2023-01-15'}
{'order_id': 2, 'product_name': 'Widget B', 'quantity': 5, 'price': 19.99, 'order_date': '2023-01-17'}
{'order_id': 3, 'product_name': 'Widget C', 'quantity': 7, 'price': 14.99, 'order_date': '2023-01-20'}
Type 'exit' to quit.
Enter your question: What is the total revenue from all sales?
Generated SQL Query:
SELECT SUM(quantity price) AS total_revenue FROM "sales_data";
Query Results:
total_revenue
-------------
249.80
```

### 3. Exiting the Assistant

To exit the query assistant, type `exit` or `quit` when prompted for a question.

## Sample Files

- **CSV Samples:** You can use any CSV files relevant to your data. Ensure that the CSVs are properly formatted with headers.
  
  Example CSV Structure:

  **sales_data.csv**
  
  | order_id | product_name | quantity | price | order_date |
  |----------|--------------|----------|-------|------------|
  | 1        | Widget A     | 10       | 9.99  | 2023-01-15 |
  | 2        | Widget B     | 5        | 19.99 | 2023-01-17 |
  | 3        | Widget C     | 7        | 14.99 | 2023-01-20 |

## Credits

- **Vishesh Vikra Singh**
  - [Website](https://visheshvsingh.notion.site/)
  - [LinkedIn](https://www.linkedin.com/in/visheshvikram/)