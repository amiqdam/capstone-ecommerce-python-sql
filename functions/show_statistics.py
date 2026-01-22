import pandas as pd
from .read_table import read_sql


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
    min_values = df[selected_cols].min()
    return {col: min_values[col] for col in selected_cols}

def get_max(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    max_values = df[selected_cols].max()
    return {col: max_values[col] for col in selected_cols}

def get_unique(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    unique = {col: int(df[col].nunique(dropna=True)) for col in selected_cols}
    return unique


def _print_columns(columns: list) -> None:
    print("Available columns:")
    for i, col in enumerate(columns, start=1):
        print(f"  {i}. {col}")


def _select_columns(columns: list, prompt: str, invalid_prefix: str) -> list:
    if not columns:
        return []
    while True:
        user_input = input(prompt).strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        lcase_cols = {col.lower(): col for col in columns}
        cols_list = [col.strip() for col in user_input.split(",") if col.strip()]
        valid_input = []
        invalid_input = []

        for col in cols_list:
            if col.isdigit():
                idx = int(col)
                if 1 <= idx <= len(columns):
                    valid_input.append(columns[idx - 1])
                else:
                    invalid_input.append(col)
            else:
                key = col.lower()
                if key in lcase_cols:
                    valid_input.append(lcase_cols[key])
                else:
                    invalid_input.append(col)

        if invalid_input:
            print(f"{invalid_prefix} {invalid_input}. Please try again.")
            continue

        no_duplicate_set = set()
        return [col for col in valid_input if not (col in no_duplicate_set or no_duplicate_set.add(col))]


def _get_numeric_columns() -> tuple[pd.DataFrame, list]:
    df = read_sql(show=False)
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available.")
    return df, num_cols


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
    df, num_cols = _get_numeric_columns()
    if not num_cols:
        return {}

    _print_columns(num_cols)
    selected_cols = _select_columns(
        num_cols,
        "Select column(s) to operate average (use name/number, comma-separated): ",
        "invalid_input selection:",
    )
    
    # call helper function of get_average to print results
    results = get_average(df, selected_cols)
    print("Column average(s):")
    for cols, avg in results.items():
        print(f"  {cols}: {avg}")

    return results


def data_median():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df, num_cols = _get_numeric_columns()
    if not num_cols:
        return {}
    
    _print_columns(num_cols)
    selected_cols = _select_columns(
        num_cols,
        "Select column(s) to operate median (use name/number, comma-separated): ",
        "invalid_input selection:",
    )

# call helper function of get_median to print results
    results = get_median(df, selected_cols)
    print("Column median(s):")
    for cols, median in results.items():
        print(f"  {cols}: {median}")

    return results


def data_stdev():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df, num_cols = _get_numeric_columns()
    if not num_cols:
        return {}
    
    _print_columns(num_cols)
    selected_cols = _select_columns(
        num_cols,
        "Select column(s) to operate standard deviation (use name/number, comma-separated): ",
        "invalid_input selection:",
    )
    
# call helper function of get_stdev to print results
    results = get_stdev(df, selected_cols)
    print("Column stdev:")
    for cols, stdev in results.items():
        print(f"  {cols}: {stdev}")

    return results


def data_min():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df, num_cols = _get_numeric_columns()
    if not num_cols:
        return {}
    
    _print_columns(num_cols)
    selected_cols = _select_columns(
        num_cols,
        "Select column(s) to operate minimum (use name/number, comma-separated): ",
        "invalid_input selection:",
    )
    
# call helper function of get_min to print results
    results = get_min(df, selected_cols)
    print("Column minimums:")
    for cols, min_value in results.items():
        count = (df[cols] == min_value).sum()
        print(f"  {cols}: {min_value} (quantity: {count})")

    return results


def data_max():
    # Collect all possible numerical columns that can be called in function (string cannot be operated)
    df, num_cols = _get_numeric_columns()
    if not num_cols:
        return {}
    
    _print_columns(num_cols)
    selected_cols = _select_columns(
        num_cols,
        "Select column(s) to operate maximum (use name/number, comma-separated): ",
        "invalid_input selection:",
    )
    
# call helper function of get_median to print results
    results = get_max(df, selected_cols)
    print("Column maximums:")
    for cols, max_value in results.items():
        count = (df[cols] == max_value).sum()
        print(f"  {cols}: {max_value} (quantity: {count})")

    return results


def data_unique():
    # Collect all columns 
    df = read_sql(show=False)
    cols = list(df.columns)

    _print_columns(cols)
    selected_cols = _select_columns(
        cols,
        "Select column(s) to count unique values (names or numbers, comma-separated): ",
        "Invalid selection:",
    )

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
