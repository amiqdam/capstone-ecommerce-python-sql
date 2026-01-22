import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from .read_table import read_sql, read_sql_with_date_filter

# =================
# HELPER FUNCTIONS | Easier to call in wrapped functions
# =================

# New column separating the year-month-date
def new_df(show: bool = True):
    df = read_sql(show=False)
    # add derived columns of year, month, date for convenience in grouping analysis
    parts_df = pd.DataFrame({
    'year': pd.to_datetime(df['order_date']).dt.year,
    'month': pd.to_datetime(df['order_date']).dt.month,
    'day': pd.to_datetime(df['order_date']).dt.day
    }, index=df.index)

    # place parts_df after column position pos
    pos = 2
    cols = [c for c in df.columns if c not in parts_df.columns]
    new_order = cols[:pos] + list(parts_df.columns) + cols[pos:]
    df = pd.concat([df[cols[:pos]], parts_df, df[cols[pos:]]], axis=1)
    df_new = df.reindex(columns=new_order)  # ensures order exactly as desired
    if show:
        print(df.head())
    return df_new


def _select_column(columns: list, title: str) -> str:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)
    print("\nAvailable Columns to visualize:")
    for idx, col in enumerate(columns, start=1):
        print(f" {idx}. {col}")

    while True:
        try:
            col_choice = int(input("\nSelect a column to visualize (enter number): "))
            if col_choice not in range(1, len(columns) + 1):
                print(f"Please enter a number between 1 and {len(columns)}.")
                continue
            return columns[col_choice - 1]
        except ValueError:
            print("Please enter a valid number.")


def _select_date_filter() -> str:
    print("\nDate Range Options:")
    print(" 1. Show ALL data (no filter)")
    print(" 2. Filter by Year")
    print(" 3. Filter by Month (Year + Month)")
    print(" 4. Filter by Day (Year + Month + Day)")

    while True:
        try:
            filter_choice = int(input("Select date filter option (1-4): "))
            if filter_choice not in range(1, 5):
                print("Please enter a number between 1 and 4.")
                continue
            filter_types = {1: 'all', 2: 'year', 3: 'month', 4: 'day'}
            return filter_types[filter_choice]
        except ValueError:
            print("Please enter a valid number.")
    
# Helper function to get valid date inputs and execute SQL filtered query
def get_filtered_data_sql(filter_type):
    if filter_type == 'all':
        df = read_sql_with_date_filter('all')
        return df
    
    if filter_type == 'year':
        print("\n--- Year Range Filter ---")
        
        # Get valid start year
        first_year = None
        while first_year is None:
            try:
                first_year = int(input("Enter start year (2023/2024): "))
                if first_year not in [2023, 2024]:
                    print("Year must be 2023 or 2024.")
                    first_year = None
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        # Get valid end year
        second_year = None
        while second_year is None:
            try:
                second_year = int(input("Enter end year (2023/2024): "))
                if second_year not in [2023, 2024]:
                    print("Year must be 2023 or 2024.")
                    second_year = None
                elif first_year > second_year:
                    print(f"End year ({second_year}) must be >= start year ({first_year}). Please try again.")
                    second_year = None
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        df = read_sql_with_date_filter('year', first_year=first_year, second_year=second_year)
        if df is None or df.empty:
            print(f"No data found for year range {first_year}-{second_year}.")
            return None
        return df
    
    if filter_type == 'month':
        print("\n--- Month Range Filter ---")
        first_year = None
        first_month = None
        second_year = None
        second_month = None
        
        # Get valid start date
        print("Start Date:")
        while first_year is None:
            try:
                first_year = int(input("  Enter year (2023/2024): "))
                if first_year not in [2023, 2024]:
                    print("  Year must be 2023 or 2024.")
                    first_year = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while first_month is None:
            try:
                first_month = int(input("  Enter month (1-12): "))
                if first_month not in range(1, 13):
                    print("  Month must be between 1-12. Please try again.")
                    first_month = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        # Get valid end date
        print("End Date:")
        while second_year is None:
            try:
                second_year = int(input("  Enter year (2023/2024): "))
                if second_year not in [2023, 2024]:
                    print("  Year must be 2023 or 2024.")
                    second_year = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while second_month is None:
            try:
                second_month = int(input("  Enter month (1-12): "))
                if second_month not in range(1, 13):
                    print("  Month must be between 1-12. Please try again.")
                    second_month = None
                else:
                    # Validate date range
                    first_date = first_year * 100 + first_month
                    second_date = second_year * 100 + second_month
                    if first_date > second_date:
                        print(f"  End date must be >= start date ({first_year}-{first_month:02d}). Please try again.")
                        second_month = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        df = read_sql_with_date_filter('month', first_year=first_year, first_month=first_month,
                                        second_year=second_year, second_month=second_month)
        if df is None or df.empty:
            print(f"No data found for month range {first_year}-{first_month:02d} to {second_year}-{second_month:02d}.")
            return None
        return df
    
    if filter_type == 'day':
        print("\n--- Day Range Filter ---")
        first_year = None
        first_month = None
        first_day = None
        second_year = None
        second_month = None
        second_day = None
        
        # Get valid start date
        print("Start Date:")
        while first_year is None:
            try:
                first_year = int(input("  Enter year (2023/2024): "))
                if first_year not in [2023, 2024]:
                    print("  Year must be 2023 or 2024.")
                    first_year = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while first_month is None:
            try:
                first_month = int(input("  Enter month (1-12): "))
                if first_month not in range(1, 13):
                    print("  Month must be between 1-12. Please try again.")
                    first_month = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while first_day is None:
            try:
                first_day = int(input("  Enter day (1-31): "))
                if first_day not in range(1, 32):
                    print("  Day must be between 1-31. Please try again.")
                    first_day = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        # Get valid end date
        print("End Date:")
        while second_year is None:
            try:
                second_year = int(input("  Enter year (2023/2024): "))
                if second_year not in [2023, 2024]:
                    print("  Year must be 2023 or 2024.")
                    second_year = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while second_month is None:
            try:
                second_month = int(input("  Enter month (1-12): "))
                if second_month not in range(1, 13):
                    print("  Month must be between 1-12. Please try again.")
                    second_month = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        while second_day is None:
            try:
                second_day = int(input("  Enter day (1-31): "))
                if second_day not in range(1, 32):
                    print("  Day must be between 1-31. Please try again.")
                    second_day = None
                else:
                    # Validate date range
                    first_date = first_year * 10000 + first_month * 100 + first_day
                    second_date = second_year * 10000 + second_month * 100 + second_day
                    if first_date > second_date:
                        print(f"  End date must be >= start date ({first_year}-{first_month:02d}-{first_day:02d}). Please try again.")
                        second_day = None
            except ValueError:
                print("  Invalid input. Please enter a valid number.")
        
        df = read_sql_with_date_filter('day', first_year=first_year, first_month=first_month, first_day=first_day,
                                        second_year=second_year, second_month=second_month, second_day=second_day)
        if df is None or df.empty:
            print(f"No data found for day range {first_year}-{first_month:02d}-{first_day:02d} to {second_year}-{second_month:02d}-{second_day:02d}.")
            return None
        return df

# Categorical column (pie chart)
def pie_vis():
    pie_cols = ["gender", "brand", "product", "category", "payment_method", "sales_channel", "city", "province"]

    selected_col = _select_column(pie_cols, "PIE CHART VISUALIZATION")
    filter_type = _select_date_filter()
    filtered_df = get_filtered_data_sql(filter_type)
    
    if filtered_df is None or filtered_df.empty:
        print("No data to visualize.")
        return
    
    # Create pie chart
    try:
        value_counts = filtered_df[selected_col].value_counts()
        plt.figure(figsize=(10, 8))
        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(f"Pie Chart - {selected_col.title()}")
        plt.tight_layout()
        plt.show()
        print(f"\n✓ Pie chart for '{selected_col}' displayed successfully!")
    except Exception as e:
        print(f"Error creating pie chart: {e}")


# Categorical column (bar plot chart)
def barplot_vis():
    bar_cols = ["category", "brand", "product", "payment_method", "sales_channel", "city", "province"]
    selected_col = _select_column(bar_cols, "BAR PLOT VISUALIZATION")
    filter_type = _select_date_filter()
    filtered_df = get_filtered_data_sql(filter_type)
    
    if filtered_df is None or filtered_df.empty:
        print("No data to visualize.")
        return
    
    # Create bar plot
    try:
        value_counts = filtered_df[selected_col].value_counts()
        plt.figure(figsize=(12, 6))
        value_counts.plot(kind='bar', color='steelblue', edgecolor='black')
        plt.title(f"Bar Plot - {selected_col.title()}")
        plt.xlabel(selected_col.title())
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.show()
        print(f"\n✓ Bar plot for '{selected_col}' displayed successfully!")
    except Exception as e:
        print(f"Error creating bar plot: {e}")




# Numerical column (histogram chart)
def hist_vis():
    hist_cols = ["age", "quantity", "unit_price", "discount_percent", "shipping_cost", "total_amount", "customer_rating"]

    selected_col = _select_column(hist_cols, "HISTOGRAM VISUALIZATION")
    filter_type = _select_date_filter()
    filtered_df = get_filtered_data_sql(filter_type)
    
    if filtered_df is None or filtered_df.empty:
        print("No data to visualize.")
        return
    
    # Create histogram
    try:
        plt.figure(figsize=(12, 6))
        plt.hist(filtered_df[selected_col], bins=30, color='steelblue', edgecolor='black', alpha=0.7)
        plt.title(f"Histogram - {selected_col.title()}")
        plt.xlabel(selected_col.title())
        plt.ylabel("Frequency")
        plt.grid(axis='y', alpha=0.3)
        plt.tight_layout()
        plt.show()
        print(f"\n✓ Histogram for '{selected_col}' displayed successfully!")
    except Exception as e:
        print(f"Error creating histogram: {e}")


def heatmap_vis():
    df = read_sql(show=False)
    # Select only numeric columns for correlation
    df_numeric = df.select_dtypes(include=['number'])
    corr = df_numeric.corr()
    plt.figure(figsize=(15,10))
    sns.heatmap(corr, annot=True)
    plt.title('Correlation Heatmap')
    plt.show()

def datavis_menu(): 
    table_view = {
        1: ("Pie Chart", pie_vis),
        2: ("Barplot Chart", barplot_vis),
        3: ("Histogram Chart", hist_vis),
        4: ("Correlation Heatmap", heatmap_vis),
        5: ("Exit", None)
    }
    while True:
        print("""
==============================
|  SHOW VISUALIZATIONS MENU   |
==============================
""")
        for key in sorted(table_view.keys()):
            label = table_view[key][0]
            print(f"  {key}. {label}")

        choice = input("Select an option (number): ").strip()
        if not choice.isdigit():
            print("Please enter a valid number.")
            continue

        key = int(choice)
        if key not in table_view:
            print("Choice out of range, try again.")
            continue

        label, stat_func = table_view[key]
        if stat_func is None:
            print("Exiting datavis.")
            break

        # Call the chosen stat_function and catch exceptions so the menu stays alive.
        try:
            stat_func()
        except Exception as e:
            print(f"Error while executing '{label}': {e}")




if __name__ == "__main__":
    datavis_menu()
