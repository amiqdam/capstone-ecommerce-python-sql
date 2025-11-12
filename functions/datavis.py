import matplotlib.pylab as plt
import numpy as np
import pandas as pd
import seaborn as sns
from read_table import read_sql

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
    
# Categorical column (pie chart and barplot chart)
def pie_vis():
    df = new_df(show=True)
    pie_cols = ["gender", "brand", "product", "category", "payment_method", "sales_channel", "city", "province"]
    
    # print("Available Columns to show:")
    # vis_input = input("Select columns that you want to visualize with Pie Chart")
    # for idx, cols in enumerate(pie_cols, start=1):
    #     print(f" {idx}. {cols}")



# def barplot_vis:
# """
# opt:
# - all view
# - sort by date, month, year
# 1. category
# 2. brand
# 3. product
# 4. payment_method
# 5. sales_channel
# 6. city
# 7. province
# """
# # Numerical column (histogram chart)
# def hist_vis:
# def boxplot_vis:
# """
# opt:
# - all view
# - sort by date, month, year
# 1. age
# 2. quantity
# 3. unit_price
# 4. discount_percent
# 5. shipping_cost
# 6. total_amount
# 7. customer_rating
# """

# # Time-series
# def line_vis:
# """
# a. order_date (order by date, month, year)
# b>>>
# 1. count orders
# 2. sum total amount
# 3. average unit_price
# """

# # Relationships 
# def scatter_vis:
# """
# opt:
# 1. unit_price v quantity
# 2. unit_price v total_amount
# 3. discount_percent v total_amount
# """

def heatmap_vis():
    df = new_df (show=False)
    # Select only numeric columns for correlation
    df_numeric = df.select_dtypes(include=['number'])
    corr = df_numeric.corr()
    plt.figure(figsize=(15,10))
    sns.heatmap(corr, annot=True)
    plt.title('Correlation Heatmap')
    plt.show()

# def datavis_menu(): 
#     table_view = {
#         1: ("Pie Chart", pie_vis),
#         2: ("Barplot Chart", barplot_vis),
#         3: ("Histogram Chart", hist_vis),
#         4: ("Boxplot Chart", boxplot_vis),
#         5: ("Line Chart", line_vis),
#         6: ("Scatter Plot", scatter_vis),
#         7: ("Correlation Heatmap", heatmap_vis),
#         8: ("Exit", None)
#     }
#     while True:
#         print("""
# ==============================
# |  SHOW VISUALIZATIONS MENU   |
# ==============================
# """)
#         for key in sorted(table_view.keys()):
#             label = table_view[key][0]
#             print(f"  {key}. {label}")

#         choice = input("Select an option (number): ").strip()
#         if not choice.isdigit():
#             print("Please enter a valid number.")
#             continue

#         key = int(choice)
#         if key not in table_view:
#             print("Choice out of range, try again.")
#             continue

#         label, stat_func = table_view[key]
#         if stat_func is None:
#             print("Exiting datavis.")
#             break

#         # Call the chosen stat_function and catch exceptions so the menu stays alive.
#         try:
#             stat_func()
#         except Exception as e:
#             print(f"Error while executing '{label}': {e}")




if __name__ == "__main__":
    heatmap_vis()