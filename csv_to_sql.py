import os
import pandas as pd
import sqlite3

def convert_dataframe_to_sqlite(csv_file_path, sqlite_db_path, table_name):
    """
    Convert a single CSV file to a SQLite table.
    
    Parameters:
        csv_file_path (str): Path to the CSV file.
        sqlite_db_path (str): Path to the SQLite database file.
        table_name (str): Name of the table to create in SQLite.
    """
    try:
        # Read CSV into DataFrame
        df = pd.read_csv(csv_file_path)
        print(f"Successfully read CSV file: {csv_file_path}")
    except Exception as e:
        print(f"Error reading CSV file '{csv_file_path}': {e}")
        return

    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect(sqlite_db_path)
        cursor = conn.cursor()
        print(f"Connected to SQLite database at: {sqlite_db_path}")
    except sqlite3.Error as e:
        print(f"Error connecting to SQLite database: {e}")
        return

    try:
        # Replace spaces with underscores in table name and make it lowercase
        formatted_table_name = table_name.replace(' ', '_').lower()
        
        # Insert DataFrame into SQLite table
        df.to_sql(formatted_table_name, conn, if_exists='replace', index=False)
        print(f"Inserted {len(df)} records into table '{formatted_table_name}' in SQLite database.")
    except Exception as e:
        print(f"Error inserting data into table '{formatted_table_name}': {e}")
    finally:
        conn.close()
        print("SQLite connection closed.\n")

def parse_csv_to_sqlite(csv_data_dir, sqlite_db_path):
    """
    Parse all CSV files in a directory and store them into a SQLite database.
    
    Parameters:
        csv_data_dir (str): Directory containing CSV files.
        sqlite_db_path (str): Path to the SQLite database file.
    """
    # Ensure the CSV data directory exists
    if not os.path.isdir(csv_data_dir):
        print(f"CSV data directory does not exist: {csv_data_dir}")
        return

    # Get all CSV files from the directory
    csv_files = [f for f in os.listdir(csv_data_dir) if f.lower().endswith('.csv')]

    if not csv_files:
        print("No CSV files found in the specified directory.")
        return

    # Process each CSV file
    for csv_file in csv_files:
        print(f"Processing {csv_file}...")
        
        # Full path to the CSV file
        csv_file_path = os.path.join(csv_data_dir, csv_file)
        
        # Table name based on CSV filename
        table_name = os.path.splitext(csv_file)[0]
        
        # Convert CSV to SQLite table
        convert_dataframe_to_sqlite(csv_file_path, sqlite_db_path, table_name)

def main():
    # Define the directory containing CSV files
    csv_data_dir = os.path.join(os.getcwd(), "CSV_Data")
    
    # Define the path for the SQLite database
    sqlite_db_path = os.path.join(os.getcwd(), "Database", "csv_data_database.db")
    
    # Ensure the database directory exists
    os.makedirs(os.path.dirname(sqlite_db_path), exist_ok=True)
    
    # Parse CSV files and store them in SQLite
    parse_csv_to_sqlite(csv_data_dir, sqlite_db_path)

if __name__ == "__main__":
    main()
