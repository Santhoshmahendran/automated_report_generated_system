import pandas as pd
import matplotlib.pyplot as plt

def generate_report(data_file, output_file):
    # Step 1: Load the Data
    try:
        data = pd.read_csv(data_file)
    except Exception:
        data = pd.read_excel(data_file)
    
    # Step 2: Perform Basic Analysis
    report = {}
    report['Summary'] = data.describe().transpose()  # Summary statistics
    report['Missing Values'] = data.isnull().sum()  # Missing values
    report['Columns'] = list(data.columns)  # Column names
    
    # Step 3: Identify Trends (Example: Create a Bar Plot for a Column)
    if 'Category' in data.columns:
        category_counts = data['Category'].value_counts()
        report['Category Distribution'] = category_counts
        
        # Plot and save the graph
        category_counts.plot(kind='bar', title='Category Distribution', color='skyblue')
        plt.xlabel('Category')
        plt.ylabel('Count')
        plt.savefig('category_distribution.png')
        plt.close()
    
    # Step 4: Write Analysis to an Excel File
    with pd.ExcelWriter(output_file) as writer:
        for key, value in report.items():
            if isinstance(value, pd.DataFrame):
                value.to_excel(writer, sheet_name=key)
            elif isinstance(value, pd.Series):
                value.to_frame().to_excel(writer, sheet_name=key)
    
    print(f"Report generated: {output_file}")

# Example Usage
data_file = 'example_dataset.csv'  # Replace with your data file path
output_file = 'report.xlsx'
generate_report(data_file, output_file)
