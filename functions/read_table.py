import pandas as pd
from db_connection import connect_db

def read_sql():
    # Connect to the database
    db = connect_db()
    # Static query for read_sql to show all data
    query = "SELECT * FROM data_transaksi_ecommerce;"
    # Call pandas function to execute SQL query
    df = pd.read_sql_query("SELECT * FROM data_transaksi_ecommerce;", db)
    # Cut connection to the database
    db.close()
    # Output as a data frame
    print("=== DATA TRANSAKSI E-COMMERCE ===")
    print(df)
    return df

# def read_certain_data_sql():
#     # Call read_sql function to read as data frame (pandas) to show columns
#     df = read_sql()
#     show_columns = df.columns
#     # Show all columns name so that user can choose what to see
#     list_cols = [cols.lower() for cols in show_columns]
#     print('Available Column: ')
#     print(f'{list_cols}')
#     # Validation for User input columns only within available columns, no data recorded or showed if invalid
#     run = True
#     while run == True:
#         user_input = (input('Select column you want to show (separated by comma if more than 1): ')).lower()
#         selected_cols = [cols.strip() for cols in user_input.split(',')]
        
#         if selected_cols not in list_cols:
#             print('Invalid input, try again.')
#         else:
#             run = False
#     # Input limit data to be shown if needed
#     limit = True
#     while limit == True:
#         input_limit = int(input('How many rows you want to show (min 1)? '))

#         if input_limit < 1 or input_limit > len(df): # %Jangan lupa 
#             print('Invalid input, try again')
#         else:
#             limit = False
    
#     # Input filter to desired column
#     input_filter = 
#     # Sort option based on user needs

#     # Show columns based on selected_cols

def read_table():
    while True: # As long as the program didn't stopped by 4, it will continue running
        """
        ================================
                    READ TABLE
        ================================
        Program:
        1. Read raw data
        2. Read certain data
        3. Read sorted data
        4. Return to Main Menu 
        """
        user_input = int(input('Select number that you want to execute: '))
        if user_input == 1: # Call function read_table() from read_table.py
            read_sql()
        # elif user_input == 2: # Call function show_statistics() from show_statistics.py
        #     read_certain_data_sql()
        # elif user_input == 3: # Call function datavis() from datavis.py
        #     read_sorted_sql()
        # elif user_input == 4: # Call function update_data() from update_data.py
        #     return 0
        # else:
        #     print('Invalid input, try again! ')
read_table()