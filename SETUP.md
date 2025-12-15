# 🚀 Setup Guide

Complete setup instructions for the Fitness Progress Tracker.

## Prerequisites

- Python 3.8 or higher
- pip package manager
- Git (optional, for cloning)

## Installation Steps

### 1. Clone or Download the Repository

```bash
git clone <your-repo-url>
cd fitness-progress-tracker
```

Or download and extract the ZIP file.

### 2. Create a Virtual Environment (Recommended)

**Windows:**
```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (web framework)
- plotly (interactive charts)
- pandas (data processing)
- numpy (numerical computing)
- matplotlib & seaborn (additional plotting)
- scikit-learn (machine learning utilities)
- statsmodels (statistical analysis)
- kaggle (dataset access)

### 4. Verify Installation

```bash
streamlit --version
```

You should see the Streamlit version number.

## Running the Dashboard

### Start the Application

```bash
streamlit run app.py
```

The dashboard will automatically open in your default browser at `http://localhost:8501`

### Upload Your Data

1. Export your Fitbit data from [fitbit.com](https://www.fitbit.com)
2. Place CSV files in the `data/fitbit_dataset/` folder (optional)
3. Use the file uploader in the dashboard to upload your files
4. Explore your fitness data!

## Project Structure

```
fitness-progress-tracker/
├── app.py                      # Main application entry point
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore rules
├── SETUP.md                    # This file
├── README.md                   # Project overview
│
├── src/                        # Source code
│   ├── config.py               # Configuration settings
│   ├── styles.py               # Custom CSS
│   ├── data_processor.py       # Data utilities
│   └── components/             # UI components
│       ├── charts.py           # Chart components
│       ├── metrics.py          # Metric cards
│       └── tabs.py             # Tab components
│
├── data/                       # Data directory
│   └── fitbit_dataset/         # Your Fitbit CSV files
│
├── docs/                       # Documentation
│   ├── QUICK_START.md          # 5-minute guide
│   ├── PROJECT_DOCUMENTATION.md # Detailed docs
│   ├── FEATURES.md             # Feature list
│   ├── CHANGELOG.md            # Version history
│   ├── UPGRADE_GUIDE.md        # Upgrade info
│   └── SUMMARY.md              # Project summary
│
└── fitbit_analysis.ipynb       # Jupyter notebook
```

## Configuration

### Customizing Goals

Edit `src/config.py`:

```python
STEPS_GOAL = 10000          # Your daily steps target
CALORIES_GOAL = 2500        # Your daily calories target
SLEEP_GOAL = 8              # Your sleep hours target
```

### Customizing Colors

Edit `src/config.py`:

```python
PRIMARY_COLOR_START = "#667eea"  # Start color of gradient
PRIMARY_COLOR_END = "#764ba2"    # End color of gradient
STEPS_COLOR = "#667eea"          # Steps chart color
CALORIES_COLOR = "#f093fb"       # Calories chart color
```

### Customizing Chart Settings

Edit `src/config.py`:

```python
MA_SHORT_WINDOW = 7         # Short moving average (days)
MA_LONG_WINDOW = 30         # Long moving average (days)
HISTOGRAM_BINS = 30         # Number of histogram bins
```

## Troubleshooting

### Dashboard Won't Start

**Issue:** `streamlit: command not found`

**Solution:** Make sure you've activated your virtual environment and installed dependencies:
```bash
.venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### Import Errors

**Issue:** `ModuleNotFoundError: No module named 'src'`

**Solution:** Make sure you're running the app from the project root directory:
```bash
cd fitness-progress-tracker
streamlit run app.py
```

### Charts Not Displaying

**Issue:** Charts appear blank or show errors

**Solution:** 
1. Verify your CSV files have the correct column names
2. Check that dates are in a valid format
3. Ensure you have data in the required columns (totalsteps, calories, etc.)

### File Upload Issues

**Issue:** Files won't upload or show errors

**Solution:**
1. Ensure files are in CSV format
2. Check file size (< 200MB recommended)
3. Verify column names match Fitbit's standard format
4. Try uploading one file at a time

### Performance Issues

**Issue:** Dashboard is slow or unresponsive

**Solution:**
1. Reduce the date range filter
2. Upload smaller datasets
3. Close other browser tabs
4. Restart the Streamlit server

## Getting Your Fitbit Data

1. Go to [fitbit.com](https://www.fitbit.com)
2. Log in to your account
3. Navigate to **Settings** → **Data Export**
4. Request your data archive
5. Wait for the email (can take a few hours)
6. Download and extract the ZIP file
7. Look for these CSV files:
   - `dailyActivity_merged.csv`
   - `sleepDay_merged.csv`
8. Upload them to the dashboard!

## Development

### Running in Development Mode

```bash
streamlit run app.py --server.runOnSave true
```

This enables auto-reload when you save changes to the code.

### Adding New Features

The modular structure makes it easy to extend:

1. **New Charts:** Add functions to `src/components/charts.py`
2. **New Metrics:** Update `src/data_processor.py`
3. **New Tabs:** Add functions to `src/components/tabs.py`
4. **New Config:** Add settings to `src/config.py`

### Code Style

- Follow PEP 8 guidelines
- Use type hints where appropriate
- Add docstrings to functions
- Keep functions focused and modular

## Additional Resources

- **Quick Start:** See `docs/QUICK_START.md` for a 5-minute guide
- **Features:** See `docs/FEATURES.md` for complete feature list
- **Documentation:** See `docs/PROJECT_DOCUMENTATION.md` for detailed docs
- **Streamlit Docs:** https://docs.streamlit.io
- **Plotly Docs:** https://plotly.com/python/

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Review the documentation in the `docs/` folder
3. Ensure all dependencies are installed correctly
4. Verify your data format matches the expected structure

## Next Steps

1. ✅ Complete installation
2. ✅ Run the dashboard
3. ✅ Upload your Fitbit data
4. ✅ Explore the visualizations
5. ✅ Customize settings in `src/config.py`
6. ✅ Read the full documentation in `docs/`

Happy tracking! 🏋️‍♂️💪
