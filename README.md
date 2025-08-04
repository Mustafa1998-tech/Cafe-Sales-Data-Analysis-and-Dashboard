# Cafe Sales Analysis

## Project Overview
This project provides tools for analyzing cafe sales data and visualizing the results in Power BI. The analysis includes sales trends, product performance, and revenue metrics.

## Features
- Automated data cleaning and preprocessing
- Comprehensive sales analysis with visualizations
- One-click export to Power BI format
- Automated Power BI dashboard generation

## Quick Start

### Prerequisites
- Python 3.8+
- Power BI Desktop (optional)

### Installation
1. Clone this repository:
   ```bash
   git clone [repository-url]
   cd data-analysis-project
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

### Power BI Integration
1. The first time you run the analysis, a basic Power BI template will be created
2. Open the generated `powerbi_data/cafe_sales_dashboard.pbix` in Power BI Desktop
3. Create your visualizations and save the file
4. Future runs will update the data while preserving your visualizations

## Project Structure
```
data-analysis-project/
├── data/                    # Raw data files
│   └── sales.csv           # Example sales data
├── analysis_results/        # Generated analysis outputs
├── powerbi_data/            # Power BI compatible files
│   ├── cafe_sales_powerbi.csv  # Processed data for Power BI
│   └── cafe_sales_dashboard.pbix  # Power BI dashboard template
├── analyze_cafe_sales.py    # Main analysis script
├── clean_cafe_sales.py      # Data cleaning utilities
├── run_analysis.py          # Power BI integration script
├── run_analysis.bat         # One-click execution (Windows)
└── README.md
```

## Dependencies
- Python 3.8+
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter (for development)

## Data Sources
- `dirty_cafe_sales.csv`: Raw sales data
- `cleaned_cafe_sales.csv`: Processed data after cleaning
- `analyzed_cafe_sales.csv`: Analysis results

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Support
For support, please open an issue in the GitHub repository.
