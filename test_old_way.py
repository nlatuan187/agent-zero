
import pandas as pd
import matplotlib.pyplot as plt

# Simulate "Old Agent" behavior: Basic, generic analysis without domain-specific formatting
try:
    df = pd.read_csv('sales_data.csv')
    
    # Generic calculations
    print("Basic Description:")
    print(df.describe())
    
    # Generic plot (likely unformatted)
    plt.figure()
    df.plot()
    plt.title("Data Plot")
    plt.savefig('old_way_plot.png')
    print("Plot saved to old_way_plot.png")
    
    # Generic summary
    with open('old_way_report.txt', 'w') as f:
        f.write("Data Analysis Report\n")
        f.write(str(df.describe()))

except Exception as e:
    print(f"Error: {e}")
