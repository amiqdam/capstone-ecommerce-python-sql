import pandas as pd
from read_table import read_sql


# =================
# HELPER FUNCTIONS | Easier to call in wrapped functions
# =================

def get_average(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    avg = df[selected_cols].mean()
    return {col: (float(avg[col]) if pd.notna(avg[col]) else None) for col in selected_cols}

def get_median(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    med = df[selected_cols].median()
    return {col: (float(med[col]) if pd.notna(med[col]) else None) for col in selected_cols}

def get_stdev(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    stdev = df[selected_cols].std()
    return {col: (float(stdev[col]) if pd.notna(stdev[col]) else None) for col in selected_cols}

def get_min(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    min = df[selected_cols].min()
    return {col: min[col] for col in selected_cols}

def get_max(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    max = df[selected_cols].max()
    return {col: max[col] for col in selected_cols}

def get_unique(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    unique = {col: int(df[col].nunique(dropna=True)) for col in selected_cols}
    return unique


# ==================
# WRAPPER FUNCTIONS | modularity for easy readibility in setting up wrapped function
# ==================

# Function to describe overall data
def table_desc():
    df = read_sql(show=False)
    desc_table = df.describe()
    desc_object = df.describe(include=object)
    print(f'{desc_table}')
    print(f'{desc_object}')

# Function to show individual average
def data_average():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df = read_sql(show=False) # Don't need to print full table from SQL
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
        return {}
    
    print("Available numeric columns:")
    for i, cols in enumerate(num_cols, start=1):
        print(f"  {i}. {cols}")

    # User inputs (user friendly by enabling both string and index input)
    while True:
        user_input = input("Select column(s) to operate average (use name/number, comma-separated): ").strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        # Lowercase all of inputted columns to prevent case sensitive in user input
        lcase_num_cols = {cols.lower(): cols for cols in num_cols}

        cols_list = [cols.strip() for cols in user_input.split(",") if cols.strip()]
        valid_input = [] # True condition of user input
        invalid_input = [] # Show user their invalid input

        # Two condition of input
        for cols in cols_list:
            if cols.isdigit():
                idx = int(cols)
                if 1 <= idx <= len(num_cols):
                    valid_input.append(num_cols[idx - 1])
                else:
                    invalid_input.append(cols)
            else:
                key = cols.lower()
                if key in lcase_num_cols:
                    valid_input.append(lcase_num_cols[key])
                else:
                    invalid_input.append(cols)
                    
        # Show invalid input
        if invalid_input:
            print(f"invalid_input selection: {invalid_input}. Please try again.")
            continue

        # Prevention of duplicate input by using set
        no_duplicate_set = set()
        selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]
        break
    
    # call helper function of get_average to print results
    results = get_average(df, selected_cols)
    print("Column average(s):")
    for cols, avg in results.items():
        print(f"  {cols}: {avg}")

    return results


def data_median():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df = read_sql(show=False) # Don't need to print full table from SQL
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
        return {}
    
    print("Available numeric columns:")
    for i, cols in enumerate(num_cols, start=1):
        print(f"  {i}. {cols}")

    # User inputs (user friendly by enabling both string and index input)
    while True:
        user_input = input("Select column(s) to operate median (use name/number, comma-separated): ").strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        # Lowercase all of inputted columns to prevent case sensitive in user input
        lcase_num_cols = {cols.lower(): cols for cols in num_cols}

        cols_list = [cols.strip() for cols in user_input.split(",") if cols.strip()]
        valid_input = [] # True condition of user input
        invalid_input = [] # Show user their invalid input

        # Two condition of input
        for cols in cols_list:
            if cols.isdigit():
                idx = int(cols)
                if 1 <= idx <= len(num_cols):
                    valid_input.append(num_cols[idx - 1])
                else:
                    invalid_input.append(cols)
            else:
                key = cols.lower()
                if key in lcase_num_cols:
                    valid_input.append(lcase_num_cols[key])
                else:
                    invalid_input.append(cols)
                    
        # Show invalid input
        if invalid_input:
            print(f"invalid_input selection: {invalid_input}. Please try again.")
            continue

        # Prevention of duplicate input by using set
        no_duplicate_set = set()
        selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]
        break

# call helper function of get_median to print results
    results = get_median(df, selected_cols)
    print("Column median(s):")
    for cols, median in results.items():
        print(f"  {cols}: {median}")

    return results


def data_stdev():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df = read_sql(show=False) # Don't need to print full table from SQL
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
        return {}
    
    print("Available numeric columns:")
    for i, cols in enumerate(num_cols, start=1):
        print(f"  {i}. {cols}")

    # User inputs (user friendly by enabling both string and index input)
    while True:
        user_input = input("Select column(s) to operate standard deviation (use name/number, comma-separated): ").strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        # Lowercase all of inputted columns to prevent case sensitive in user input
        lcase_num_cols = {cols.lower(): cols for cols in num_cols}

        cols_list = [cols.strip() for cols in user_input.split(",") if cols.strip()]
        valid_input = [] # True condition of user input
        invalid_input = [] # Show user their invalid input

        # Two condition of input
        for cols in cols_list:
            if cols.isdigit():
                idx = int(cols)
                if 1 <= idx <= len(num_cols):
                    valid_input.append(num_cols[idx - 1])
                else:
                    invalid_input.append(cols)
            else:
                key = cols.lower()
                if key in lcase_num_cols:
                    valid_input.append(lcase_num_cols[key])
                else:
                    invalid_input.append(cols)
                    
        # Show invalid input
        if invalid_input:
            print(f"invalid_input selection: {invalid_input}. Please try again.")
            continue

        # Prevention of duplicate input by using set
        no_duplicate_set = set()
        selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]
        break
    
# call helper function of get_stdev to print results
    results = get_stdev(df, selected_cols)
    print("Column stdev:")
    for cols, stdev in results.items():
        print(f"  {cols}: {stdev}")

    return results


def data_min():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df = read_sql(show=False) # Don't need to print full table from SQL
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
        return {}
    
    print("Available numeric columns:")
    for i, cols in enumerate(num_cols, start=1):
        print(f"  {i}. {cols}")

    # User inputs (user friendly by enabling both string or index input [only 1 at a time])
    while True:
        user_input = input("Select column(s) to operate minimum (use name/number, comma-separated): ").strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        # Lowercase all of inputted columns to prevent case sensitive in user input
        lcase_num_cols = {cols.lower(): cols for cols in num_cols}

        cols_list = [cols.strip() for cols in user_input.split(",") if cols.strip()]
        valid_input = [] # True condition of user input
        invalid_input = [] # Show user their invalid input

        # Two condition of input
        for cols in cols_list:
            if cols.isdigit():
                idx = int(cols)
                if 1 <= idx <= len(num_cols):
                    valid_input.append(num_cols[idx - 1])
                else:
                    invalid_input.append(cols)
            else:
                key = cols.lower()
                if key in lcase_num_cols:
                    valid_input.append(lcase_num_cols[key])
                else:
                    invalid_input.append(cols)
                    
        # Show invalid input
        if invalid_input:
            print(f"invalid_input selection: {invalid_input}. Please try again.")
            continue

        # Prevention of duplicate input by using set
        no_duplicate_set = set()
        selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]
        break
    
# call helper function of get_min to print results
    results = get_min(df, selected_cols)
    print("Column minimums:")
    for cols, min in results.items():
        count = (df[cols] == min).sum()
        print(f"  {cols}: {min} (quantity: {count})")

    return results


def data_max():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df = read_sql(show=False) # Don't need to print full table from SQL
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
        return {}
    
    print("Available numeric columns:")
    for i, cols in enumerate(num_cols, start=1):
        print(f"  {i}. {cols}")

    # User inputs (user friendly by enabling both string and index input)
    while True:
        user_input = input("Select column(s) to operate maximum (use name/number, comma-separated): ").strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        # Lowercase all of inputted columns to prevent case sensitive in user input
        lcase_num_cols = {cols.lower(): cols for cols in num_cols}

        cols_list = [cols.strip() for cols in user_input.split(",") if cols.strip()]
        valid_input = [] # True condition of user input
        invalid_input = [] # Show user their invalid input

        # Two condition of input
        for cols in cols_list:
            if cols.isdigit():
                idx = int(cols)
                if 1 <= idx <= len(num_cols):
                    valid_input.append(num_cols[idx - 1])
                else:
                    invalid_input.append(cols)
            else:
                key = cols.lower()
                if key in lcase_num_cols:
                    valid_input.append(lcase_num_cols[key])
                else:
                    invalid_input.append(cols)
                    
        # Show invalid input
        if invalid_input:
            print(f"invalid_input selection: {invalid_input}. Please try again.")
            continue

        # Prevention of duplicate input by using set
        no_duplicate_set = set()
        selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]
        break
    
# call helper function of get_median to print results
    results = get_max(df, selected_cols)
    print("Column maximums:")
    for cols, max in results.items():
        count = (df[cols] == max).sum()
        print(f"  {cols}: {max} (quantity: {count})")

    return results


def data_unique():
    # Collect all columns 
    df = read_sql(show=False)
    cols = list(df.columns)

    print("Available columns:")
    for i, col in enumerate(cols, start=1):
        print(f"  {i}. {col}")

    # User inputs (user friendly by enabling both string and index input)
    user_input = input("Select column(s) to count unique values (names or numbers, comma-separated): ").strip()
    cols_list = [col.strip() for col in user_input.split(",") if col.strip()]
    
    valid_input = []
    invalid_input = []

    # Lowercase all of inputted columns to prevent case sensitive in user input
    lcase_cols = {col.lower(): col for col in cols}
    # Two condition of input
    for p in cols_list:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(cols):
                valid_input.append(cols[idx - 1])
            else:
                invalid_input.append(p)
        else:
            key = p.lower()
            if key in lcase_cols:
                valid_input.append(lcase_cols[key])
            else:
                invalid_input.append(p)

    if invalid_input:
        print(f"Invalid selection: {invalid_input}. Please try again.")
        return {}

    # Prevent duplicates while preserving order
    no_duplicate_set = set()
    selected_cols = [x for x in valid_input if not (x in no_duplicate_set or no_duplicate_set.add(x))]

    results = get_unique(df, selected_cols)
    print("Unique counts:")
    for col, n_unique in results.items():
        print(f"  {col}: {n_unique}")

    return results


# ==========
# MAIN MENU | Called in main.py for modularity simplicity
# ==========

def show_statistics_menu():
    actions = {
        1: ("Describe table", table_desc),
        2: ("Average (mean)", data_average),
        3: ("Median", data_median),
        4: ("Standard deviation", data_stdev),
        5: ("Minimum value", data_min),
        6: ("Maximum value", data_max),
        7: ("Count unique values", data_unique),
        8: ("Exit", None),
    }

    while True:
        print("""
===========================
|  SHOW STATISTICS MENU   |
===========================
""")
        for key in sorted(actions.keys()):
            label = actions[key][0]
            print(f"  {key}. {label}")

        choice = input("Select an option (number): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        key = int(choice)
        if key not in actions:
            print("Choice out of range, try again.")
            continue

        label, stat_func = actions[key]
        if stat_func is None:
            print("Exiting show_statistics.")
            break

        # Call the chosen stat_function and catch exceptions so the menu stays alive.
        try:
            stat_func()
        except Exception as e:
            print(f"Error while executing '{label}': {e}")


if __name__ == "__main__":
    show_statistics_menu()
