"""
Customer Segment Sales Summary Analysis

This script performs a simple sales analysis by customer segment.
It calculates total revenue, average order value, total orders, and each
segment's contribution to overall revenue.
"""

import pandas as pd


def load_sales_data(file_path: str) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    return pd.read_csv(file_path)


def summarize_by_segment(df: pd.DataFrame) -> pd.DataFrame:
    """Create a customer segment summary table."""
    summary = (
        df.groupby("customer_segment")
        .agg(
            total_revenue=("revenue", "sum"),
            avg_order_value=("revenue", "mean"),
            total_orders=("order_id", "nunique"),
        )
        .reset_index()
        .sort_values("total_revenue", ascending=False)
    )

    total_revenue = summary["total_revenue"].sum()
    summary["revenue_share_pct"] = (
        summary["total_revenue"] / total_revenue * 100
    ).round(2)

    summary["avg_order_value"] = summary["avg_order_value"].round(2)

    return summary


def main() -> None:
    df = load_sales_data("data/sales_data.csv")
    summary = summarize_by_segment(df)

    print("Customer Segment Sales Summary")
    print(summary.to_string(index=False))

    summary.to_csv("customer_segment_summary.csv", index=False)
    print("\nSummary exported to customer_segment_summary.csv")


if __name__ == "__main__":
    main()
