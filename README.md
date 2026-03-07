# Online Retail Sales Analysis (EDA with Python)

A mini data analytics project exploring customer purchasing behavior and product performance using the **Online Retail dataset (500,000+ transactions)**.

This project demonstrates a complete **data analytics workflow in Python** including **data quality checks, cleaning, feature engineering, exploratory data analysis (EDA), and business insight generation.**

---

## Dataset

Source: Kaggle – Online Retail Dataset  
https://www.kaggle.com/datasets/vijayuv/onlineretail

The dataset contains **~541,000 transaction records** from an online retail store.

### Key Columns

- InvoiceNo – Invoice identifier
- StockCode – Product code
- Description – Product name
- Quantity – Units purchased
- UnitPrice – Price per unit
- InvoiceDate – Transaction timestamp
- CustomerID – Customer identifier
- Country – Customer country

---

## Tools & Libraries

- **Python**
- **Pandas** – Data manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Visualization
- **Seaborn** – Statistical visualization
- **DuckDB** – SQL-style analytics on Pandas DataFrames

---

## Project Workflow

### 1️⃣ Data Loading

- Loaded dataset containing **500K+ rows**
- Handled encoding issues using **latin1**
- Inspected structure using:
  - `df.info()`
  - `df.describe()`
  - `df.shape`

---

### 2️⃣ Data Quality Checks

Initial inspection identified common real-world data issues:

- Negative quantities (returns)
- Missing `CustomerID`
- Missing product descriptions
- Duplicate transactions
- Non-optimal data types

These checks mimic the **first step of any real analytics project.**

---

### 3️⃣ Data Cleaning

Cleaning steps included:

- Filtering **United Kingdom transactions**
- Removing **cancelled invoices (`InvoiceNo` starting with "C")**
- Removing rows with:
  - Missing `CustomerID`
  - Missing `Description`
- Removing duplicates
- Filtering invalid values:
  - `Quantity > 0`
  - `UnitPrice > 0`

After cleaning, the dataset contained **~46,000 high-quality records** for analysis.

---

### 4️⃣ Feature Engineering

Created new analytical features:

- **TotalRevenue = Quantity × UnitPrice**
- **Year**
- **Month**
- **Day**
- **Hour**

These features enabled **time-based sales analysis**.

---

### 5️⃣ Exploratory Data Analysis (EDA)

Key business questions answered:

#### 🏆 Top 10 Bestselling Products
- Grouped by product description
- Ranked by **total quantity sold**

#### 💰 Top 10 Revenue Generating Products
- Ranked by **total sales revenue**

#### ⏰ Sales by Hour
- Extracted hour from `InvoiceDate`
- Identified peak shopping hours

#### 📅 Sales by Day of Week
- Compared revenue distribution across weekdays

#### 📊 Sales by Month
- Analyzed seasonality patterns

---

## Visualizations

Created multiple charts using **Matplotlib**:

- Top 10 Bestselling Products
- Top Revenue Products
- Sales by Hour
- Sales by Day of Week
- Sales by Month

These visualizations help translate raw data into **clear business insights**.

---

## Key Insight 

Peak revenue occurs during **midday shopping hours**, suggesting customers tend to purchase during working hours.

### Business Recommendation

Schedule **promotional campaigns and marketing emails between 10 AM – 12 PM** to capture peak buying activity.

---

## Skills Demonstrated

✔ Handling **large datasets (500K+ rows)**  
✔ Data cleaning and preprocessing  
✔ Exploratory Data Analysis (EDA)  
✔ Feature engineering for time-series analysis  
✔ SQL-style analysis using **DuckDB**  
✔ Data visualization with **Matplotlib**  
✔ Translating data findings into **business insights**

