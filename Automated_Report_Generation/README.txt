# Instructions to Run the Automated Report Generation System

1. **Setup Environment**:
   Ensure you have Python installed and install the required libraries by running:
   ```bash
   pip install pandas matplotlib openpyxl
   ```

2. **Prepare Dataset**:
   - Use the provided `example_dataset.csv` or replace it with your own dataset.

3. **Run the Script**:
   Execute the Python script to generate the report:
   ```bash
   python generate_report.py
   ```

4. **Output**:
   - The report will be saved as `report.xlsx` in the current directory.
   - If the dataset has a `Category` column, a bar chart will be saved as `category_distribution.png`.

5. **Customizations**:
   - Modify the script to analyze other columns or include additional plots.

6. **Example Dataset**:
   - A sample dataset (`example_dataset.csv`) is provided for testing.

