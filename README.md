# Customer Segment Sales Summary Analysis

This project analyzes sales performance by customer segment using Python and pandas.

The goal is to identify which customer segments generate the highest revenue, compare average order value, and calculate each segment's contribution to total sales.

## Skills demonstrated

- Python
- pandas
- Data aggregation
- GroupBy analysis
- Revenue share calculation
- CSV import and export
- Basic portfolio documentation

## Project structure

```text
Customer-segment-sales-summary-analysis/
│
├── customer_sales_summary.py
├── customer_segment_summary.csv
├── requirements.txt
└── data/
    └── sales_data.csv
```

## How it works

The script reads a sales dataset from `data/sales_data.csv`, groups the data by `customer_segment`, and calculates:

- Total revenue
- Average order value
- Total number of unique orders
- Revenue share percentage

## How to run

Install the required library:

```bash
pip install -r requirements.txt
```

Run the script:

```bash
python customer_sales_summary.py
```

## Output

The script prints the customer segment summary in the terminal and exports the results to:

```text
customer_segment_summary.csv
```

## Next improvement

A future version could add a bar chart using matplotlib or seaborn to visualize total revenue by customer segment.
