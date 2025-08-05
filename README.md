# Cafe Sales Analysis

## Project Overview
This project provides tools for analyzing cafe sales data and visualizing the results in both Power BI and an interactive web dashboard. The analysis includes sales trends, product performance, and revenue metrics.

## Features
- Automated data cleaning and preprocessing
- Comprehensive sales analysis with visualizations
- One-click export to Power BI format
- Interactive web dashboard with Streamlit
- Responsive design for all devices

## Quick Start

### Prerequisites
- Python 3.8+
- Power BI Desktop (optional)
- Git (for deployment)

### Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/Mustafa1998-tech/Cafe-Sales-Data-Analysis-and-Dashboard.git
   cd Cafe-Sales-Data-Analysis-and-Dashboard
   ```

2. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or run the batch file which will handle the installation:
   ```
   run_analysis.bat
   ```

## Usage

### Running the Analysis
1. Place your sales data in CSV format in the project directory
2. Run the analysis:
   - **Windows**: Double-click `run_analysis.bat`
   - **Command Line**: `python run_analysis.py`

3. The script will:
   - Process the sales data
   - Generate analysis results
   - Create a `powerbi_data` directory with the processed data
   - Optionally open Power BI Desktop with the results

### Web Dashboard (Streamlit)
Run the interactive web dashboard locally:
```bash
streamlit run dashboard.py
```

Or use the batch file:
```
run_dashboard.bat
```

### Power BI Integration
1. The first time you run the analysis, a basic Power BI template will be created
2. The processed data will be saved as `powerbi_data/cafe_sales_powerbi.csv`
3. Open `powerbi_data/cafe_sales_dashboard.pbix` in Power BI Desktop
4. Set up the data source to point to the generated CSV file

## Web Deployment

### Streamlit Cloud Deployment
1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Click "New app" → "From existing repo"
4. Select your repository and branch
5. Set the main file path to `dashboard.py`
6. Click "Deploy"

Your dashboard will be available at:  
`https://share.streamlit.io/your-username/your-repo-name`

## Project Structure
```
.
├── analyzed_cafe_sales.csv    # Processed sales data
├── dashboard.py              # Streamlit web dashboard
├── run_analysis.py           # Main analysis script
├── run_analysis.bat          # Windows batch file for analysis
├── run_dashboard.bat         # Windows batch file for dashboard
├── requirements.txt          # Python dependencies
└── powerbi_data/             # Power BI files
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
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
