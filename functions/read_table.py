import pandas as pd
from .db_connection import connect_db

def read_sql(show: bool = True): #Show for showing full table when True
    # Connect to the database
    db = connect_db()
    # Static query for read_sql to show all data
    query = "SELECT * FROM data_transaction_ecommerce;"
    # Call pandas function to execute SQL query
    df = pd.read_sql_query(query, db)
    # Cut connection to the database
    db.close()
    # Optionally print
    if show:
        print("\n=== DATA TRANSACTION E-COMMERCE ===")
        print(df)
    return df


def read_sql_with_date_filter(filter_type, first_year=None, first_month=None, first_day=None, 
                               second_year=None, second_month=None, second_day=None):
    db = connect_db()
    
    if filter_type == 'all':
        query = "SELECT * FROM data_transaction_ecommerce;"
    
    elif filter_type == 'year':
        query = f"""
        SELECT * FROM data_transaction_ecommerce 
        WHERE YEAR(order_date) >= {first_year} 
        AND YEAR(order_date) <= {second_year}
        """
    
    elif filter_type == 'month':
        query = f"""
        SELECT * FROM data_transaction_ecommerce 
        WHERE (YEAR(order_date) = {first_year} AND MONTH(order_date) >= {first_month})
        OR (YEAR(order_date) > {first_year} AND YEAR(order_date) < {second_year})
        OR (YEAR(order_date) = {second_year} AND MONTH(order_date) <= {second_month})
        """
    
    elif filter_type == 'day':
        query = f"""
        SELECT * FROM data_transaction_ecommerce 
        WHERE order_date >= '{first_year}-{first_month:02d}-{first_day:02d}' 
        AND order_date <= '{second_year}-{second_month:02d}-{second_day:02d}'
        """
    
    try:
        df = pd.read_sql_query(query, db)
        db.close()
        return df
    except Exception as e:
        db.close()
        print(f"Error executing query: {e}")
        return None

def read_certain_data():
    # Get full table columns to let user choose
    df_all = read_sql(show=False)
    if df_all is None or df_all.empty:
        print("No data available.")
        return

    cols = list(df_all.columns)
    print('\nAvailable columns:')
    for i, c in enumerate(cols, start=1):
        print(f" {i}. {c}")

    # Select columns
    selected_cols = None
    while selected_cols is None:
        user_in = input("Select columns to show (numbers comma-separated, or 'all'): ").strip()
        if user_in.lower() in ('all', '*'):
            selected_cols = cols
            break
        parts = [p.strip() for p in user_in.split(',') if p.strip()]
        try:
            nums = [int(p) for p in parts]
        except ValueError:
            print('Invalid input. Use numbers separated by commas, or "all".')
            continue
        if any(n < 1 or n > len(cols) for n in nums):
            print('One or more selections out of range. Try again.')
            continue
        # keep order and dedupe
        seen = set()
        selected_cols = [cols[n-1] for n in nums if not (n in seen or seen.add(n))]

    # Date filter options
    print('\nDate Range Options:')
    print(' 1. Show ALL data (no filter)')
    print(' 2. Filter by Year range')
    print(' 3. Filter by Month range (Year+Month)')
    print(' 4. Filter by Day range (Year+Month+Day)')

    filter_choice = None
    while filter_choice is None:
        try:
            v = int(input('Select date filter option (1-4): ').strip())
            if v not in (1,2,3,4):
                print('Enter a number 1-4')
                continue
            filter_choice = v
        except ValueError:
            print('Enter a valid number')

    df_filtered = None
    if filter_choice == 1:
        df_filtered = read_sql_with_date_filter('all')
    elif filter_choice == 2:
        while True:
            try:
                fy = int(input('Start year (e.g. 2023): '))
                sy = int(input('End year (e.g. 2024): '))
                if fy > sy:
                    print('Start must be <= end. Try again.')
                    continue
                df_filtered = read_sql_with_date_filter('year', first_year=fy, second_year=sy)
                break
            except ValueError:
                print('Enter numeric years')
    elif filter_choice == 3:
        while True:
            try:
                fy = int(input('Start year (e.g. 2023): '))
                fm = int(input('Start month (1-12): '))
                sy = int(input('End year (e.g. 2024): '))
                sm = int(input('End month (1-12): '))
                if fm not in range(1,13) or sm not in range(1,13):
                    print('Months must be 1-12')
                    continue
                if (fy*100+fm) > (sy*100+sm):
                    print('Start must be <= end. Try again.')
                    continue
                df_filtered = read_sql_with_date_filter('month', first_year=fy, first_month=fm, second_year=sy, second_month=sm)
                break
            except ValueError:
                print('Enter numeric year/month')
    else:
        while True:
            try:
                fy = int(input('Start year (e.g. 2023): '))
                fm = int(input('Start month (1-12): '))
                fd = int(input('Start day (1-31): '))
                sy = int(input('End year (e.g. 2024): '))
                sm = int(input('End month (1-12): '))
                sd = int(input('End day (1-31): '))
                if fm not in range(1,13) or sm not in range(1,13) or fd not in range(1,32) or sd not in range(1,32):
                    print('Invalid month/day. Try again.')
                    continue
                if (fy*10000+fm*100+fd) > (sy*10000+sm*100+sd):
                    print('Start must be <= end. Try again.')
                    continue
                df_filtered = read_sql_with_date_filter('day', first_year=fy, first_month=fm, first_day=fd, second_year=sy, second_month=sm, second_day=sd)
                break
            except ValueError:
                print('Enter numeric values')

    if df_filtered is None:
        print('No data returned or query error')
        return
    if df_filtered.empty:
        print('No rows match filters')
        return

    # Row limit
    while True:
        lim = input(f"How many rows to show? (1-{len(df_filtered)} or 'all'): ").strip().lower()
        if lim in ('all','a'):
            n = len(df_filtered)
            break
        try:
            n = int(lim)
            if n < 1 or n > len(df_filtered):
                print('Out of range')
                continue
            break
        except ValueError:
            print('Enter a number or all')

    try:
        print(df_filtered.loc[:, selected_cols].head(n).to_string(index=False))
    except Exception as e:
        print(f'Error displaying data: {e}')
    return

def read_table_menu():
    while True:
        print('\n===============================')
        print('            READ TABLE')
        print('===============================')
        print(' 1. Read full table')
        print(' 2. Read selected columns / rows')
        print(' 3. Exit')
        try:
            user_input = int(input('Select number to execute: ').strip())
        except ValueError:
            print('Enter a valid number')
            continue

        if user_input == 1:
            read_sql()
        elif user_input == 2:
            read_certain_data()
        elif user_input == 3:
            print('Returning from read_table menu')
            return
        else:
            print('Invalid choice, try again')


if __name__ == "__main__":
    # Run the interactive read_table menu when executed as a script
    read_table_menu()