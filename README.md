# Cafe Sales Analysis

## Project Overview
This project provides tools to analyze cafe sales data and visualize the results through Power BI reports and an interactive web dashboard built with Streamlit. The analysis covers sales trends, product performance, and revenue metrics.

## Features
- Automated data cleaning and preprocessing
- Comprehensive sales analysis with detailed visualizations
- One-click export to Power BI format
- Interactive web dashboard powered by Streamlit
- Responsive design for all devices

## Quick Start

### Prerequisites
- Python 3.8 or higher
- Power BI Desktop (optional)
- Git (for deployment)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/Mustafa1998-tech/Cafe-Sales-Data-Analysis-and-Dashboard.git
   cd Cafe-Sales-Data-Analysis-and-Dashboard
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or run the batch file to install dependencies automatically:
   ```
   run_analysis.bat
   ```

## Usage

### Running the Analysis
1. Place your sales data CSV file in the project directory
2. Run the analysis:
   - **Windows**: Double-click `run_analysis.bat`
   - **Command line**:
     ```bash
     python run_analysis.py
     ```
3. The script will:
   - Process the sales data
   - Generate analysis reports and visualizations
   - Create a `powerbi_data` folder with processed data
   - Optionally launch Power BI Desktop with the results

### Web Dashboard (Streamlit)
Run the interactive dashboard locally:
```bash
streamlit run dashboard.py
```

Or use the batch file:
```
run_dashboard.bat
```

### Power BI Integration
1. On the first run, a basic Power BI template will be created
2. Processed data will be saved as `powerbi_data/cafe_sales_powerbi.csv`
3. Open `powerbi_data/cafe_sales_dashboard.pbix` in Power BI Desktop
4. Update the data source to point to the generated CSV file

## Web Deployment

### Deploying on Streamlit Cloud
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Create a new app → select your repo and branch
4. Set the main file path to `dashboard.py`
5. Click "Deploy"

Your dashboard will be available at:  
`https://share.streamlit.io/your-username/your-repo-name`

## Project Structure
```
.
├── analyzed_cafe_sales.csv          # Processed sales data  
├── dashboard.py                     # Streamlit web dashboard  
├── run_analysis.py                  # Main analysis script  
├── run_analysis.bat                 # Windows batch file to run analysis  
├── run_dashboard.bat                # Windows batch file to run dashboard  
├── requirements.txt                 # Python dependencies  
└── powerbi_data/                   # Power BI files  
    ├── cafe_sales_dashboard.pbix  
    └── cafe_sales_powerbi.csv  
```

## Requirements
- Python 3.8+
- See `requirements.txt` for Python package dependencies

## Data Sources
- `analyzed_cafe_sales.csv`: Processed sales data
- Raw data should be in CSV format with appropriate columns

## Contributing
Contributions are welcome! Feel free to submit a Pull Request.

## License
This project is licensed under the MIT License — see the LICENSE file for details.
