Automated E-Commerce Insight & Visualization Engine
This is a CLI-based analytics tool that automates the exploration of e-commerce transaction data, providing instant statistical insights and visualizations without manual SQL scripting.

Features

Automated EDA: Generates descriptive statistics and distributions for sales data instantly.

Interactive Visualizations: Produces correlation heatmaps and sales charts based on user-selected filters.

Transaction Management: Full CRUD (Create, Read, Update, Delete) capabilities with data validation.

E-Commerce Insight Engine - Application Flow Documentation

1. Overview The Automated E-Commerce Engine is a modular Python application designed to empower business users to analyze sales performance. It bridges MySQL database management with Pandas-based analytics, allowing users to perform complex data queries and visualization through a simple Command Line Interface (CLI).

2. High-Level Architecture The application consists of three main pillars:

Interface Layer: A modular CLI menu system (main.py) handling user inputs and navigation.

Data Layer: Secure MySQL connection utilizing mysql-connector-python for transactional operations.

Analytical Layer: A suite of functions (functions/) leveraging Pandas for data manipulation and Seaborn/Matplotlib for visual output.

3. Step-by-Step Data Flow

Step 1: System Initialization & Connection

Action: App starts and connects to the database.

Module: main.py -> db_connection

Process: Loads credentials from .env, establishes a secure connection to the MySQL instance, and verifies schema integrity using seed data (*.sql).

Step 2: User Command & Data Retrieval

Action: User selects "Analyze Sales Trends" and sets a date filter (e.g., "2023").

Module: main.py -> read_data()

Process: Constructs a dynamic SQL query based on user input, fetching raw transaction records into a Pandas DataFrame.

Step 3: Data Processing & Feature Engineering

Action: Raw data is prepared for analysis.

Module: functions/analytics.py (Hypothetical module based on desc)

Process:

Calculates derived columns (e.g., total_amount validation).

Extracts temporal features (Year, Month, Day) for grouping.

Computes descriptive statistics (Mean, Median, Std Dev) for numerical columns.

Step 4: Visualization Generation

Action: User requests a visual report (e.g., "Correlation Heatmap").

Module: functions/visualization.py

Process:

Uses Seaborn to generate the requested plot (Barplot/Heatmap).

Displays the plot window to the user for immediate insight.

Step 5: CRUD Operations (Optional)

Action: User adds or updates a transaction.

Module: functions/crud.py

Process: Validates input types (dates, numbers), executes the SQL INSERT/UPDATE command, and ensures database consistency.
