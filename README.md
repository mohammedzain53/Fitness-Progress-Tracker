# 🏋️‍♂️ Fitness Progress Tracker Dashboard

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Plotly](https://img.shields.io/badge/Plotly-5.17+-purple.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**A stunning, modern dashboard for visualizing and analyzing your Fitbit activity data**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Documentation](docs/)  

</div>

---

## ✨ Features

### 🎨 Modern UI/UX
- **Glassmorphism Design** - Beautiful frosted glass effects with gradient backgrounds
- **Responsive Layout** - Optimized for all screen sizes
- **Smooth Animations** - Hover effects and transitions for better user experience
- **Custom Styling** - Professional color schemes and typography

### 📊 Advanced Visualizations
- **Interactive Gauge Charts** - Track your daily goals for steps, calories, and sleep
- **Trend Analysis** - 7-day and 30-day moving averages for better insights
- **Calendar Heatmaps** - GitHub-style activity visualization
- **Activity Patterns** - Analyze performance by day of week
- **Correlation Analysis** - Understand relationships between metrics
- **Distribution Charts** - Histograms and box plots for statistical insights

### 🎯 Key Metrics
- Total & Average Steps
- Total & Average Calories Burned
- Average Sleep Duration
- Total Distance Traveled
- Activity Intensity Distribution
- Weekly Performance Trends

### 🔧 Powerful Features
- **Multi-File Upload** - Upload multiple CSV files simultaneously
- **Smart Data Merging** - Automatically combines activity and sleep data
- **Date Range Filtering** - Focus on specific time periods
- **Data Export** - Download filtered datasets
- **Real-time Statistics** - Comprehensive summary tables

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd fitness-tracker
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
# or
source .venv/bin/activate  # macOS/Linux
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 💻 Usage

### Running the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default browser at `http://localhost:8501`

### Using Your Data

1. **Export your Fitbit data** from the Fitbit website
2. **Upload CSV files** using the file uploader in the dashboard
3. **Explore your data** across different tabs:
   - 📊 **Overview** - Goal progress and weekly trends
   - 🚶 **Steps Analysis** - Detailed step tracking with moving averages
   - 🔥 **Calories** - Calorie burn analysis and correlations
   - 📅 **Activity Patterns** - Day-of-week insights and intensity distribution
   - 🗓️ **Calendar View** - Heatmap visualizations
   - 📈 **Summary** - Statistical overview and data export

### Supported Data Files
- `dailyActivity_merged.csv` - Daily activity metrics
- `sleepDay_merged.csv` - Sleep tracking data
- Any Fitbit CSV export with standard column names

---

## 📸 Screenshots

### Dashboard Overview
Beautiful metric cards with gradient effects and goal tracking gauges

### Trend Analysis
Interactive charts with moving averages and goal lines

### Calendar Heatmaps
GitHub-style activity visualization for steps and calories

### Activity Patterns
Radar charts and day-of-week analysis

---

## 🎨 Customization

### Changing Goals
Edit the goal values in `src/config.py`:
```python
STEPS_GOAL = 10000      # Daily steps goal
CALORIES_GOAL = 2500    # Daily calories goal
SLEEP_GOAL = 8          # Sleep hours goal
```

### Modifying Colors
Update the gradient colors in `src/config.py`:
```python
PRIMARY_COLOR_START = "#667eea"
PRIMARY_COLOR_END = "#764ba2"
```

### Adding New Metrics
The modular component-based design makes it easy to add new visualizations and metrics.

---

## 📁 Project Structure

```
fitness-tracker/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── src/                            # Source code package
│   ├── __init__.py
│   ├── config.py                   # Configuration settings
│   ├── styles.py                   # Custom CSS styles
│   ├── data_processor.py           # Data processing utilities
│   └── components/                 # UI components
│       ├── __init__.py
│       ├── charts.py               # Chart components
│       ├── metrics.py              # Metric card components
│       └── tabs.py                 # Tab components
├── data/                           # Data directory
│   └── fitbit_dataset/             # Fitbit CSV files
│       └── README.md               # Data instructions
├── docs/                           # Documentation
│   ├── README.md                   # Project overview
│   ├── QUICK_START.md              # Quick start guide
│   ├── PROJECT_DOCUMENTATION.md    # Detailed documentation
│   ├── FEATURES.md                 # Feature showcase
│   ├── CHANGELOG.md                # Version history
│   ├── UPGRADE_GUIDE.md            # Upgrade guide
│   └── SUMMARY.md                  # Project summary
└── fitbit_analysis.ipynb           # Jupyter notebook for analysis
```

---

## 🛠️ Technologies Used

- **Streamlit** - Web application framework
- **Plotly** - Interactive visualizations
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Python** - Core programming language

---

## 📝 License

This project is licensed under the MIT License - feel free to use it for your own fitness tracking!

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 💡 Tips for Best Results

1. **Upload multiple months of data** for better trend analysis
2. **Use date filters** to focus on specific periods
3. **Check the Summary tab** for statistical insights
4. **Download filtered data** for external analysis
5. **Set realistic goals** based on your baseline metrics

---

## 🎯 Future Enhancements

- [ ] Dark/Light theme toggle
- [ ] Export visualizations as images
- [ ] Predictive analytics and forecasting
- [ ] Social sharing features
- [ ] Mobile app integration
- [ ] Custom goal setting UI
- [ ] Achievement badges and milestones

---

## 📂 Project Organization

This project follows a clean, component-based architecture:

- **`src/`** - All source code (config, styles, data processing, components)
- **`docs/`** - All documentation (guides, features, technical docs)
- **`data/`** - Data directory for your Fitbit CSV files
- **Root** - Main app and essential files only

See [PROJECT_TREE.txt](PROJECT_TREE.txt) for complete structure visualization.

---

## 📋 Quick Navigation

- **New User?** → [SETUP.md](SETUP.md) → [docs/QUICK_START.md](docs/QUICK_START.md)
- **Developer?** → [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md)
- **Need Reference?** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)
- **All Docs?** → [INDEX.md](INDEX.md)

---

<div align="center">

**Made with ❤️ for fitness enthusiasts**

⭐ Star this repo if you find it helpful!

**Project Status:** ✅ Complete and Production-Ready

</div>
