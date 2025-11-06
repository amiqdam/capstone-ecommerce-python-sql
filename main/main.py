# Import all functions from different files so it can be used in this file
from functions import (read_table, show_statistics, datavis, update_data, db_connection)

# Create a function as a base of this program with main_program()
def main_program():
    while True: # As long as the program didn't stopped by 5, it will continue running
        """
        ================================
                    MAIN MENU
        ================================
        Program:
        1. Read all data
        2. Show statistics of data
        3. Show visualization of data
        4. Update database 
        5. Exit program
        """
        user_input = int(input('Select number that you want to execute: '))

        if user_input == 1: # Call function read_table() from read_table.py
            read_table()
        elif user_input == 2: # Call function show_statistics() from show_statistics.py
            show_statistics()
        elif user_input == 3: # Call function datavis() from datavis.py
            datavis()
        elif user_input == 4: # Call function update_data() from update_data.py
            update_data()
        elif user_input == 5: # Instruction to break the function to stop the program
            print('Thank you for using us, see you again! :D')
            break
        else:
            print('Invalid input, try again! ')
        
        # Testing to ensure the main_program function is running in main.py folder
        if __name__ == "__main__":
            main_program()       






























