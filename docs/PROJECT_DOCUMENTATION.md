# Fitness Progress Tracker Dashboard v2.0

## Overview
This project is a modern, beautifully designed Streamlit-based dashboard for visualizing and analyzing Fitbit activity data. With a stunning glassmorphism UI, advanced visualizations, and comprehensive analytics, users can gain deep insights into their fitness journey.

## 🎨 Design Philosophy
The dashboard features a modern design with:
- **Glassmorphism Effects:** Frosted glass cards with backdrop blur
- **Gradient Backgrounds:** Beautiful purple gradient theme
- **Smooth Animations:** Hover effects and transitions
- **Professional Typography:** Inter font family
- **Responsive Layout:** Optimized for all screen sizes

## ✨ Core Features

### 📤 Data Management
- **Multi-file Upload:** Upload multiple Fitbit CSV files simultaneously
- **Smart Data Merging:** Automatically combines activity and sleep data
- **Date Range Filtering:** Focus on specific time periods via sidebar
- **Data Validation:** Automatic column name normalization
- **Export Functionality:** Download filtered datasets with timestamps

### 📊 Key Performance Indicators (KPIs)
Modern metric cards displaying:
- **Total Steps** with daily average
- **Total Calories** with daily average
- **Average Sleep Duration** in hours
- **Total Distance** with daily average
- **Record Count Badge** showing loaded data points

### 🎯 Goal Tracking
Interactive gauge charts for:
- **Steps Goal** (default: 10,000 steps/day)
- **Calories Goal** (default: 2,500 calories/day)
- **Sleep Goal** (default: 8 hours/night)

Each gauge shows:
- Current average value
- Progress towards goal
- Color-coded zones (red/yellow/green)
- Delta from target

### 📈 Advanced Visualizations

#### Tab 1: Overview
- **Goal Progress Gauges:** Three interactive circular gauges
- **Weekly Performance Chart:** Dual-axis chart showing steps (bars) and calories (line)
- **Trend Analysis:** Week-by-week aggregated data

#### Tab 2: Steps Analysis
- **Trend Chart:** Daily steps with 7-day and 30-day moving averages
- **Goal Reference Line:** Visual target at 10,000 steps
- **Area Fill:** Better visual representation of daily activity
- **Distribution Histogram:** Frequency distribution of step counts
- **Box Plot:** Statistical summary with quartiles and outliers

#### Tab 3: Calories Analysis
- **Correlation Scatter:** Calories vs Steps with trendline
- **Size Encoding:** Bubble size represents distance
- **Color Encoding:** Activity intensity shown via color
- **Time Series:** Daily calories with 7-day moving average
- **Bar + Line Combo:** Combined visualization

#### Tab 4: Activity Patterns
- **Day-of-Week Analysis:** Average steps and calories by weekday
- **Color-Coded Bars:** Gradient colors based on values
- **Radar Chart:** Activity intensity distribution
  - Very Active Minutes
  - Fairly Active Minutes
  - Lightly Active Minutes
  - Sedentary Minutes

#### Tab 5: Calendar View
- **Steps Heatmap:** GitHub-style calendar showing daily steps
- **Calories Heatmap:** Calendar view of daily calorie burn
- **Week-by-Week Layout:** Organized by week number
- **Rich Tooltips:** Date, value, and context on hover

#### Tab 6: Summary & Export
- **Statistical Table:** Complete descriptive statistics
- **Styled DataFrame:** Gradient background for better readability
- **Explanation Guide:** Understanding statistical measures
- **CSV Export:** Download filtered data with timestamp

## 🚀 Usage Guide

### Quick Start
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the dashboard:**
   ```bash
   streamlit run app.py
   ```

3. **Upload your data:**
   - Click the file uploader
   - Select one or more Fitbit CSV files
   - Supported files: `dailyActivity_merged.csv`, `sleepDay_merged.csv`

4. **Explore your data:**
   - Use sidebar filters for date ranges
   - Navigate through 6 organized tabs
   - Hover over charts for detailed information
   - Download filtered data when needed

### Navigation

#### 📊 Overview Tab
- View goal progress with interactive gauges
- Analyze weekly performance trends
- Get a quick snapshot of your fitness journey

#### 🚶 Steps Analysis Tab
- Track daily steps with moving averages
- Identify trends and patterns
- View statistical distribution

#### 🔥 Calories Tab
- Understand calorie burn patterns
- See correlation with steps and activity
- Track daily and weekly trends

#### 📅 Activity Patterns Tab
- Discover your most active days
- Analyze activity intensity
- Optimize your workout schedule

#### 🗓️ Calendar View Tab
- Visualize activity over time
- Spot streaks and gaps
- GitHub-style heatmap view

#### 📈 Summary Tab
- Review complete statistics
- Export data for external analysis
- Understand your metrics

## 📁 Project Structure

```
fitness-tracker/
├── app.py                      # Main Streamlit application (500+ lines)
├── config.py                   # Configuration settings
├── requirements.txt            # Python dependencies
├── README.md                   # Project overview
├── QUICK_START.md             # 5-minute setup guide
├── CHANGELOG.md               # Version history
├── PROJECT_DOCUMENTATION.md   # This file (detailed docs)
├── fitbit_analysis.ipynb      # Jupyter notebook for analysis
└── data/
    └── fitbit_dataset/        # Sample Fitbit CSV files
```

## 🛠️ Technical Stack

### Core Technologies
- **Streamlit 1.28+** - Web application framework
- **Plotly 5.17+** - Interactive visualizations
- **Pandas 2.0+** - Data manipulation
- **NumPy 1.24+** - Numerical computing
- **Statsmodels 0.14+** - Statistical analysis

### Visualization Libraries
- **Plotly Express** - High-level charting
- **Plotly Graph Objects** - Custom visualizations
- **Matplotlib** - Additional plotting
- **Seaborn** - Statistical graphics

### Data Processing
- **Pandas** - DataFrame operations
- **NumPy** - Array computations
- **Datetime** - Time series handling

## ⚙️ Configuration

### Customizing Goals
Edit `config.py` or directly in `app.py`:
```python
STEPS_GOAL = 10000      # Daily steps target
CALORIES_GOAL = 2500    # Daily calories target
SLEEP_GOAL = 8          # Sleep hours target
```

### Customizing Colors
Modify the CSS gradient in `app.py`:
```python
PRIMARY_COLOR_START = "#667eea"
PRIMARY_COLOR_END = "#764ba2"
```

### Customizing Charts
Adjust chart settings in `config.py`:
```python
MA_SHORT_WINDOW = 7     # Short moving average
MA_LONG_WINDOW = 30     # Long moving average
MAIN_CHART_HEIGHT = 500 # Chart height in pixels
```

## 🎨 Design System

### Color Palette
- **Primary Gradient:** #667eea → #764ba2 (Purple)
- **Steps:** #667eea (Blue)
- **Calories:** #f093fb (Pink)
- **Sleep:** #4facfe (Light Blue)
- **Distance:** #43e97b (Green)

### Typography
- **Font Family:** Inter (Google Fonts)
- **Weights:** 300 (Light), 400 (Regular), 600 (Semibold), 700 (Bold)

### Spacing
- **Card Padding:** 2rem
- **Card Border Radius:** 20px
- **Element Margin:** 1rem

### Effects
- **Glassmorphism:** backdrop-filter: blur(10px)
- **Shadows:** 0 8px 32px rgba(0, 0, 0, 0.1)
- **Transitions:** 0.3s ease

## 🔧 Advanced Features

### Data Processing Pipeline
1. **Upload:** Multi-file CSV upload
2. **Normalize:** Column name standardization
3. **Merge:** Automatic activity + sleep merge
4. **Filter:** Date range filtering
5. **Aggregate:** Statistical computations
6. **Visualize:** Chart generation
7. **Export:** Filtered data download

### Moving Average Calculation
```python
df['steps_ma7'] = df['totalsteps'].rolling(window=7, min_periods=1).mean()
df['steps_ma30'] = df['totalsteps'].rolling(window=30, min_periods=1).mean()
```

### Gauge Chart Configuration
- **Mode:** gauge + number + delta
- **Range:** 0 to 1.5x goal
- **Zones:** Red (0-50%), Yellow (50-100%), Green (100-150%)
- **Threshold:** Goal line indicator

## 📊 Data Requirements

### Expected Columns (Activity)
- `ActivityDate` or `activitydate` - Date of activity
- `TotalSteps` or `totalsteps` - Daily step count
- `Calories` or `calories` - Calories burned
- `TotalDistance` or `totaldistance` - Distance traveled
- `VeryActiveMinutes` - High intensity activity
- `FairlyActiveMinutes` - Moderate intensity
- `LightlyActiveMinutes` - Light activity
- `SedentaryMinutes` - Inactive time

### Expected Columns (Sleep)
- `SleepDay` or `sleepday` - Date of sleep
- `TotalMinutesAsleep` or `totalminutesasleep` - Sleep duration

### Data Format
- **File Type:** CSV
- **Date Format:** Any standard format (auto-detected)
- **Encoding:** UTF-8
- **Separator:** Comma

## 🐛 Troubleshooting

### Common Issues

**Charts not displaying:**
- Verify CSV column names match expected format
- Check for missing or null values
- Ensure dates are in valid format

**Upload fails:**
- Confirm file is CSV format
- Check file size (< 200MB recommended)
- Verify file is not corrupted

**Slow performance:**
- Reduce date range filter
- Upload smaller datasets
- Close other browser tabs

**Styling issues:**
- Clear browser cache
- Try different browser
- Check Streamlit version

## 🚀 Performance Tips

1. **Filter data** before visualization
2. **Upload only needed files**
3. **Use date range filters** for large datasets
4. **Close unused tabs** in the dashboard
5. **Restart app** if memory issues occur

## 📚 Additional Resources

- **Streamlit Docs:** https://docs.streamlit.io
- **Plotly Docs:** https://plotly.com/python/
- **Fitbit Data Export:** https://www.fitbit.com/settings/data/export

## 🤝 Contributing

Contributions welcome! Areas for improvement:
- Additional visualizations
- New metrics and KPIs
- Performance optimizations
- UI/UX enhancements
- Documentation improvements

## 📄 License

MIT License - Free to use and modify

## 🎯 Future Roadmap

See [CHANGELOG.md](CHANGELOG.md) for planned features and upcoming releases.
