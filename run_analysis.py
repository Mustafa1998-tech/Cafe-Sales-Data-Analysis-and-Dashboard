import os
import subprocess
import pandas as pd
import analyze_cafe_sales  # Import your existing analysis
from pathlib import Path

def prepare_powerbi_data():
    """
    Run the cafe sales analysis and prepare data for Power BI
    """
    # Create output directories
    output_dir = Path("powerbi_data")
    output_dir.mkdir(exist_ok=True)
    
    # Run the analysis (importing the module will run the analysis)
    # The analysis results should be in the 'analysis_results' directory
    
    # Prepare data for Power BI
    # Assuming your analysis saves to analyzed_cafe_sales.csv
    if os.path.exists('analyzed_cafe_sales.csv'):
        df = pd.read_csv('analyzed_cafe_sales.csv')
        
        # Save a version optimized for Power BI
        powerbi_file = output_dir / 'cafe_sales_powerbi.csv'
        df.to_csv(powerbi_file, index=False)
        
        print(f"✅ Analysis complete! Data saved to: {powerbi_file}")
        return str(powerbi_file)
    else:
        print("❌ Could not find analyzed data. Please run the analysis first.")
        return None

def open_powerbi():
    """
    Open Power BI Desktop with the analysis results
    """
    # Common Power BI Desktop installation paths
    powerbi_paths = [
        r"C:\Program Files\Microsoft Power BI Desktop\bin\PBIDesktop.exe",
        r"C:\Program Files (x86)\Microsoft Power BI Desktop\bin\PBIDesktop.exe"
    ]
    
    # Path to the Power BI dashboard file
    pbix_file = Path("powerbi_data/cafe_sales_dashboard.pbix")
    
    if not pbix_file.exists():
        print("⚠️  Power BI template not found. Creating a basic one...")
        create_powerbi_template()
    
    # First try to open with the .pbix file directly
    try:
        print("🔁 Opening Power BI dashboard...")
        subprocess.Popen(['start', '', str(pbix_file.absolute())], shell=True)
        return
    except Exception as e:
        print(f"❌ Error opening Power BI file directly: {e}")
    
    # If direct open fails, try using the Power BI Desktop executable
    for path in powerbi_paths:
        if os.path.exists(path):
            try:
                print(f"🔁 Opening Power BI Desktop with the dashboard...")
                subprocess.Popen([path, str(pbix_file.absolute())])
                return
            except Exception as e:
                print(f"❌ Error opening Power BI Desktop: {e}")
    
    print("⚠️  Could not find Power BI Desktop. Please install it or open the file manually:")
    print(f"   {pbix_file.absolute()}")

def create_powerbi_template():
    """
    Create a basic Power BI template file
    """
    template = """{
        "version": "1.0",
        "sections": [
            {
                "displayName": "Cafe Sales Analysis",
                "position": {"x": 0, "y": 0, "z": 0},
                "visualContainers": [
                    {
                        "name": "visualContainer1",
                        "filters": {},
                        "config": "{\"name\":\"visualContainer1\",\"layouts\":[{\"id\":0,\"position\":{\"x\":0,\"y\":0,\"z\":0},\"width\":6,\"height\":6}],\"config\":\"{\\\"name\\\":\\\"visualContainer1\\\",\\\"singleVisual\\\":{\\\"visualType\\\":\\\"tableEx\\\",\\\"projections\\\":{\\\"Values\\\":[{\\\"queryRef\\\":\\\"Product\\\"},{\\\"queryRef\\\":\\\"Total Spent\\\"}]}}}\"}"
                    }
                ]
            }
        ]
    }"""
    
    # Create the directory if it doesn't exist
    os.makedirs("powerbi_data", exist_ok=True)
    
    # Save the template
    with open("powerbi_data/cafe_sales_dashboard.pbix", 'w') as f:
        f.write(template)
    
    print("✅ Created basic Power BI template")

if __name__ == "__main__":
    print("🚀 Starting Cafe Sales Analysis for Power BI...")
    
    # Run the analysis
    data_file = prepare_powerbi_data()
    
    if data_file:
        # Always try to open Power BI after successful analysis
        open_powerbi()
    
    print("\n🎉 Analysis complete! You can now create visualizations in Power BI.")
    print(f"   Data location: {os.path.abspath('powerbi_data')}")
    
    # Keep the console open
    if os.name == 'nt':  # Only for Windows
        os.system('pause')
