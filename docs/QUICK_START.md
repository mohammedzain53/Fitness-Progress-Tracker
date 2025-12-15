# 🚀 Quick Start Guide

Get your Fitness Progress Tracker up and running in 5 minutes!

## Step 1: Install Dependencies

Open your terminal and run:

```bash
pip install -r requirements.txt
```

## Step 2: Launch the Dashboard

```bash
streamlit run app.py
```

The dashboard will automatically open in your browser at `http://localhost:8501`

## Step 3: Upload Your Data

1. Click the **"Browse files"** button in the file uploader
2. Select your Fitbit CSV files:
   - `dailyActivity_merged.csv`
   - `sleepDay_merged.csv`
   - Or any other Fitbit export files
3. You can upload multiple files at once!

## Step 4: Explore Your Data

### 📊 Overview Tab
- View your goal progress with interactive gauges
- See weekly performance trends
- Track steps, calories, and sleep metrics

### 🚶 Steps Analysis Tab
- Daily steps with 7-day and 30-day moving averages
- Steps distribution histogram
- Statistical box plots

### 🔥 Calories Tab
- Calories vs Steps correlation
- Daily calorie burn trends
- Activity intensity analysis

### 📅 Activity Patterns Tab
- Average performance by day of week
- Activity intensity radar chart
- Identify your most active days

### 🗓️ Calendar View Tab
- GitHub-style heatmaps
- Visual activity calendar
- Spot patterns and streaks

### 📈 Summary Tab
- Complete statistical overview
- Download filtered data
- Export for further analysis

## Step 5: Filter Your Data

Use the sidebar to:
- Select custom date ranges
- Focus on specific time periods
- Compare different weeks/months

## 🎯 Pro Tips

1. **Upload at least 30 days of data** for meaningful trends
2. **Use the date filter** to compare different periods
3. **Check the gauges** to see how you're tracking against goals
4. **Look for patterns** in the day-of-week charts
5. **Download your filtered data** for backup or external analysis

## 🔧 Customizing Goals

Edit these values in `app.py` (around line 280):

```python
steps_goal = 10000      # Change to your daily steps goal
calories_goal = 2500    # Change to your daily calories goal
sleep_goal = 8          # Change to your sleep hours goal
```

## 📱 Getting Your Fitbit Data

1. Go to [fitbit.com](https://www.fitbit.com)
2. Log in to your account
3. Navigate to Settings → Data Export
4. Request your data archive
5. Download and extract the CSV files
6. Upload to the dashboard!

## ❓ Troubleshooting

### Dashboard won't start
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check Python version: `python --version` (needs 3.8+)

### Files won't upload
- Ensure files are in CSV format
- Check that column names match Fitbit's standard format
- Try uploading one file at a time

### Charts not displaying
- Verify your CSV files contain the required columns
- Check the browser console for errors
- Try refreshing the page

## 🎉 You're All Set!

Enjoy tracking your fitness progress with beautiful visualizations!

---

**Need help?** Check out the full [README.md](README.md) or [PROJECT_DOCUMENTATION.md](PROJECT_DOCUMENTATION.md)
