import pandas as pd

def convert_units(input_file, output_file):
    """
    Convert height from inches to cm and weight from pounds to kg
    """
    # Read the original data
    df = pd.read_csv(input_file)
    
    # Convert units
    df['Height(cm)'] = df['Height(Inches)'] * 2.54
    df['Weight(kg)'] = df['Weight(Pounds)'] * 0.453592
    
    # Drop original columns
    df = df.drop(['Height(Inches)', 'Weight(Pounds)'], axis=1)
    
    # Save to new file
    df.to_csv(output_file, index=False)
    print(f"Converted data saved to {output_file}")

if __name__ == "__main__":
    input_file = "data/SOCR-HeightWeight.csv"
    output_file = "data/SOCR-HeightWeight_metric.csv"
    convert_units(input_file, output_file)