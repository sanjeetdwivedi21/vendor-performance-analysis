# Vendor Performance Analysis

An end-to-end data analytics project focused on evaluating vendor sales performance, profitability, purchasing efficiency, inventory turnover, and supplier concentration.

## 📌 Project Overview

The objective of this project is to analyze vendor-level sales and purchasing data and identify:

- Top-performing vendors
- Supplier concentration and dependency
- High-margin but low-sales opportunities
- Slow-moving inventory
- Purchasing and pricing patterns
- Relationships between sales, profit, and inventory metrics

The project uses a consolidated vendor-summary analytical dataset generated from the underlying inventory database.

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SQLite
- SciPy
- Jupyter Notebook

## 🔄 Project Workflow

1. Data ingestion into SQLite
2. Data consolidation and vendor-level aggregation
3. Exploratory Data Analysis (EDA)
4. Sales and profitability analysis
5. Vendor concentration analysis
6. Purchasing and inventory analysis
7. Statistical testing
8. Business recommendations

## 📊 Key Analysis

The analysis covers:

- Vendor sales performance
- Top-selling products
- Vendor procurement contribution
- Pareto analysis
- Purchase price and bulk purchasing patterns
- Stock turnover
- Gross profit and profit margins
- Correlation analysis
- High-margin / low-sales opportunities
- Statistical validation using Welch's t-test

## 🔍 Key Findings

- The top vendors contribute a significant share of total procurement, indicating supplier concentration risk.
- A small group of products contributes a substantial portion of overall sales.
- Bulk purchasing is associated with lower average unit purchase prices.
- Several vendors show low stock turnover, indicating potential slow-moving inventory.
- High-margin, low-sales products represent potential opportunities for targeted pricing, promotion, and distribution strategies.
- Sales and gross profit show a strong positive relationship.

## 💡 Business Recommendations

- Re-evaluate pricing for low-sales, high-margin products.
- Diversify vendor partnerships to reduce supplier dependency.
- Leverage bulk purchasing where economically justified.
- Optimize slow-moving inventory through better replenishment and purchasing decisions.
- Improve marketing and distribution strategies for low-performing vendors.
- Use a balanced vendor scorecard combining sales, profit, margin, turnover, and procurement contribution.

## 📁 Project Structure

```text
vendor-performance-analysis/
│
├── Exploratory Data Analysis.ipynb
├── Vendor Performance Analysis.ipynb
├── get_vendor_summary.py
├── ingestion_db.py
├── README.md
├── 
│
├── report/
│   └─Report.pdf
│
