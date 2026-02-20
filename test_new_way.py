
import pandas as pd
import matplotlib.pyplot as plt

# Simulate "New Agent" behavior: Strict adherence to SKILL.md instructions
try:
    df = pd.read_csv('sales_data.csv')
    
    # 1. Metric Calculation (Per Skill Instructions)
    df['Net Profit'] = df['Revenue'] - df['Expenses']
    df['Profit Margin'] = (df['Net Profit'] / df['Revenue']) * 100
    df['MoM Growth'] = df['Revenue'].pct_change() * 100
    
    # 2. Visualization (Per Skill Instructions)
    plt.figure(figsize=(10, 6))
    plt.plot(df['Month'], df['Revenue'], label='Revenue', marker='o')
    plt.plot(df['Month'], df['Expenses'], label='Expenses', marker='x', linestyle='--')
    plt.title('Financial Overview: Revenue vs Expenses')
    plt.xlabel('Month')
    plt.ylabel('Amount ($)')
    plt.legend()
    plt.grid(True)
    plt.savefig('financial_overview.png')
    print("Specialized Plot saved to financial_overview.png")
    
    # 3. Reporting (Per Skill Instructions)
    top_month = df.loc[df['Profit Margin'].idxmax()]
    low_month = df.loc[df['Profit Margin'].idxmin()]
    
    report = f"""# Executive Financial Summary

## Financial Metrics
| Month | Revenue | Expenses | Net Profit | Margin (%) | MoM Growth (%) |
|-------|---------|----------|------------|------------|----------------|
"""
    for index, row in df.iterrows():
        growth = f"{row['MoM Growth']:.2f}%" if pd.notnull(row['MoM Growth']) else "N/A"
        report += f"| {row['Month']} | ${row['Revenue']:,.2f} | ${row['Expenses']:,.2f} | ${row['Net Profit']:,.2f} | {row['Profit Margin']:.2f}% | {growth} |\n"

    report += f"\n## Highlights\n"
    report += f"- **Top Performing Month**: {top_month['Month']} (Margin: {top_month['Profit Margin']:.2f}%)\n"
    report += f"- **Lowest Performing Month**: {low_month['Month']} (Margin: {low_month['Profit Margin']:.2f}%)\n"
    
    report += f"\n## Strategic Recommendations\n"
    report += f"- Revenue shows a consistent upward trend, peaking in December.\n"
    report += f"- Expense growth is slower than revenue growth, improving margins.\n"
    report += f"- Capitalize on Q4 momentum for next year's planning.\n"
    
    with open('executive_summary.md', 'w') as f:
        f.write(report)
    print("Executive Report saved to executive_summary.md")

except Exception as e:
    print(f"Error: {e}")
