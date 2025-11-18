# Import all functions from different files so it can be used in this file
# Using package-style imports (functions is sibling package)
import sys
from pathlib import Path

# Add the project root to sys.path so functions package can be found
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from functions import read_table_menu, show_statistics_menu, datavis_menu, update_menu

# Create a function as a base of this program with main_program()
def main_program():
    while True: # As long as the program didn't stopped by 5, it will continue running
        user_input = int(input("""
================================
            MAIN MENU
================================
Program:
1. Read all data
2. Show statistics of data
3. Show visualization of data
4. Update database 
5. Exit program
Select number that you want to execute: """))

        if user_input == 1: # Call function read_table() from read_table.py
            read_table_menu()
        elif user_input == 2: # Call function show_statistics() from show_statistics.py
            show_statistics_menu()
        elif user_input == 3: # Call function datavis() from datavis.py
            datavis_menu()
        elif user_input == 4: # Call functions from update_data.py (create/delete)
            update_menu()
        elif user_input == 5: # Instruction to break the function to stop the program
            print('Thank you for using us, see you again! :D')
            break
        else:
            print('Invalid input, try again! ')
        
# Run main when executed directly
if __name__ == "__main__":
    main_program()






























