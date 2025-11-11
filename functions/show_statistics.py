import pandas as pd
from read_table import read_sql


# ======================
# PURE HELPER FUNCTIONS | 
# ======================

def get_average(df: pd.DataFrame, selected_cols: list) -> dict:
    if not selected_cols:
        return {}
    avg = df[selected_cols].mean()
    return {col: (float(avg[col]) if pd.notna(avg[col]) else None) for col in selected_cols}

def get_median(df: pd.DataFrame, selected_cols: list) -> dict:
    med = df[selected_cols].median()
    return {col: (float(med[col]) if pd.notna(med[col]) else None) for col in selected_cols}

def get_stdev(df: pd.DataFrame, selected_cols: list) -> dict:
    stdev = df[selected_cols].std()
    return {col: (float(stdev[col]) if pd.notna(stdev[col]) else None) for col in selected_cols}

def get_mins(df: pd.DataFrame, selected_cols: list) -> dict:
    mins = df[selected_cols].min()
    return {col: mins[col] for col in selected_cols}

def get_maxs(df: pd.DataFrame, selected_cols: list) -> dict:
    maxs = df[selected_cols].max()
    return {col: maxs[col] for col in selected_cols}

def get_uniques(df: pd.DataFrame, selected_cols: list) -> dict:
    uniques = {col: int(df[col].nunique(dropna=True)) for col in selected_cols}
    return uniques


# ==============================
# INTERACTIVE WRAPPER FUNCTIONS |
# ==============================

# Function to describe overall data
def table_desc():
    df = read_sql(show=False)
    desc_table = df.describe()
    desc_object = df.describe(include=object)
    print(f'{desc_table}')
    print(f'{desc_object}')

# Function to show individual average
def data_average():
    df = read_sql(show=False)
    num_cols = list(df.select_dtypes(include="number").columns)
    if not num_cols:
        print("No numeric columns available to compute averages.")
        return {}

    lcase_num_cols = {col.lower(): col for col in num_cols}

    print("Available numeric columns:")
    for i, col in enumerate(num_cols, start=1):
        print(f"  {i}. {col}")

    while True:
        user_input = input(
            "Select column(s) to average (names or numbers, comma-separated): "
        ).strip()
        if not user_input:
            print("No input provided. Please enter at least one column name or number.")
            continue

        parts = [p.strip() for p in user_input.split(",") if p.strip()]
        selected = []
        invalid = []

        for p in parts:
            if p.isdigit():
                idx = int(p)
                if 1 <= idx <= len(num_cols):
                    selected.append(num_cols[idx - 1])
                else:
                    invalid.append(p)
            else:
                key = p.lower()
                if key in lcase_num_cols:
                    selected.append(lcase_num_cols[key])
                else:
                    invalid.append(p)

        if invalid:
            print(f"Invalid selection: {invalid}. Please try again.")
            continue

        seen = set()
        selected_cols = [x for x in selected if not (x in seen or seen.add(x))]
        break

    results = get_average(df, selected_cols)
    print("Column averages:")
    for col in selected_cols:
        print(f"  {col}: {results[col]}")

    return results


def data_median():
    """Interactively compute and display column medians."""
    df = read_sql(show=False)
    numeric_cols = list(df.select_dtypes(include="number").columns)
    if not numeric_cols:
        print("No numeric columns available to compute medians.")
        return {}

    lcase_num_cols = {col.lower(): col for col in numeric_cols}

    print("Available numeric columns:")
    for i, col in enumerate(numeric_cols, start=1):
        print(f"  {i}. {col}")

    user_input = input("Select column(s) to compute median (names or numbers, comma-separated): ").strip()
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    selected = []

    for p in parts:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(numeric_cols):
                selected.append(numeric_cols[idx - 1])
        else:
            key = p.lower()
            if key in lcase_num_cols:
                selected.append(lcase_num_cols[key])

    seen = set()
    selected_cols = [x for x in selected if not (x in seen or seen.add(x))]

    results = get_median(df, selected_cols)
    print("Column medians:")
    for k, v in results.items():
        print(f"  {k}: {v}")

    return results


def data_std():
    """Interactively compute and display column standard deviations."""
    df = read_sql(show=False)
    numeric_cols = list(df.select_dtypes(include="number").columns)
    if not numeric_cols:
        print("No numeric columns available to compute std.")
        return {}

    lcase_num_cols = {col.lower(): col for col in numeric_cols}

    print("Available numeric columns:")
    for i, col in enumerate(numeric_cols, start=1):
        print(f"  {i}. {col}")

    user_input = input("Select column(s) to compute std (names or numbers, comma-separated): ").strip()
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    selected = []

    for p in parts:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(numeric_cols):
                selected.append(numeric_cols[idx - 1])
        else:
            key = p.lower()
            if key in lcase_num_cols:
                selected.append(lcase_num_cols[key])

    seen = set()
    selected_cols = [x for x in selected if not (x in seen or seen.add(x))]

    results = get_stdev(df, selected_cols)
    print("Column stdev:")
    for k, v in results.items():
        print(f"  {k}: {v}")

    return results


def data_min():
    """Interactively compute and display column minimum values with quantity."""
    df = read_sql(show=False)
    cols = list(df.columns)

    print("Available columns:")
    for i, col in enumerate(cols, start=1):
        print(f"  {i}. {col}")

    user_input = input("Select column(s) to compute min (names or numbers, comma-separated): ").strip()
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    selected = []
    lcase_cols = {col.lower(): col for col in cols}

    for p in parts:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(cols):
                selected.append(cols[idx - 1])
        else:
            key = p.lower()
            if key in lcase_cols:
                selected.append(lcase_cols[key])

    seen = set()
    selected_cols = [x for x in selected if not (x in seen or seen.add(x))]

    results = get_mins(df, selected_cols)
    print("Column minimums:")
    for k, v in results.items():
        count = (df[k] == v).sum()
        print(f"  {k}: {v} (quantity: {count})")

    return results


def data_max():
    """Interactively compute and display column maximum values with quantity."""
    df = read_sql(show=False)
    cols = list(df.columns)

    print("Available columns:")
    for i, col in enumerate(cols, start=1):
        print(f"  {i}. {col}")

    user_input = input("Select column(s) to compute max (names or numbers, comma-separated): ").strip()
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    selected = []
    lcase_cols = {col.lower(): col for col in cols}

    for p in parts:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(cols):
                selected.append(cols[idx - 1])
        else:
            key = p.lower()
            if key in lcase_cols:
                selected.append(lcase_cols[key])

    seen = set()
    selected_cols = [x for x in selected if not (x in seen or seen.add(x))]

    results = get_maxs(df, selected_cols)
    print("Column maximums:")
    for k, v in results.items():
        count = (df[k] == v).sum()
        print(f"  {k}: {v} (quantity: {count})")

    return results


def data_unique():
    """Interactively compute and display column unique value counts."""
    df = read_sql(show=False)
    cols = list(df.columns)

    print("Available columns:")
    for i, col in enumerate(cols, start=1):
        print(f"  {i}. {col}")

    user_input = input("Select column(s) to count unique values (names or numbers, comma-separated): ").strip()
    parts = [p.strip() for p in user_input.split(",") if p.strip()]
    selected = []
    lcase_cols = {col.lower(): col for col in cols}

    for p in parts:
        if p.isdigit():
            idx = int(p)
            if 1 <= idx <= len(cols):
                selected.append(cols[idx - 1])
        else:
            key = p.lower()
            if key in lcase_cols:
                selected.append(lcase_cols[key])

    seen = set()
    selected_cols = [x for x in selected if not (x in seen or seen.add(x))]

    results = get_uniques(df, selected_cols)
    print("Unique counts:")
    for k, v in results.items():
        print(f"  {k}: {v}")

    return results


# ============================================================================
# MAIN MENU
# ============================================================================

def show_statistics_menu():
    """Interactive menu to choose which statistics function to run."""
    # Use an explicit dict mapping numbers to (label, function).
    # This removes the need for 1-based index adjustment (idx - 1).
    actions = {
        1: ("Describe table", table_desc),
        2: ("Average (mean)", data_average),
        3: ("Median", data_median),
        4: ("Standard deviation", data_std),
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
