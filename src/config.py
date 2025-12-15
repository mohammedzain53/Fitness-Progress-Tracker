# 🎨 Fitness Tracker Configuration
# Customize your dashboard settings here

# ============================================
# GOAL SETTINGS
# ============================================
STEPS_GOAL = 10000          # Daily steps target
CALORIES_GOAL = 2500        # Daily calories burn target
SLEEP_GOAL = 8              # Sleep hours target (in hours)
DISTANCE_GOAL = 5           # Daily distance target (in km)

# ============================================
# COLOR SCHEMES
# ============================================
# Primary gradient colors (used in backgrounds and headers)
PRIMARY_COLOR_START = "#667eea"
PRIMARY_COLOR_END = "#764ba2"

# Chart colors
STEPS_COLOR = "#667eea"
CALORIES_COLOR = "#f093fb"
SLEEP_COLOR = "#4facfe"
DISTANCE_COLOR = "#43e97b"

# ============================================
# CHART SETTINGS
# ============================================
# Moving average windows
MA_SHORT_WINDOW = 7         # Short-term moving average (days)
MA_LONG_WINDOW = 30         # Long-term moving average (days)

# Chart heights
GAUGE_HEIGHT = 300
MAIN_CHART_HEIGHT = 500
SECONDARY_CHART_HEIGHT = 400
SMALL_CHART_HEIGHT = 350

# ============================================
# UI SETTINGS
# ============================================
PAGE_TITLE = "Fitness Progress Tracker"
PAGE_ICON = "🏋️"
DASHBOARD_TITLE = "🏋️‍♂️ Fitness Progress Tracker"
DASHBOARD_SUBTITLE = "Transform Your Data Into Insights"

# ============================================
# DATA SETTINGS
# ============================================
# Expected column names (lowercase)
ACTIVITY_DATE_COL = "activitydate"
SLEEP_DATE_COL = "sleepday"
STEPS_COL = "totalsteps"
CALORIES_COL = "calories"
DISTANCE_COL = "totaldistance"
SLEEP_MINUTES_COL = "totalminutesasleep"

# Activity intensity columns
VERY_ACTIVE_COL = "veryactiveminutes"
FAIRLY_ACTIVE_COL = "fairlyactiveminutes"
LIGHTLY_ACTIVE_COL = "lightlyactiveminutes"
SEDENTARY_COL = "sedentaryminutes"

# ============================================
# FEATURE FLAGS
# ============================================
SHOW_TRENDLINES = True      # Show trendlines in scatter plots
SHOW_GOAL_LINES = True      # Show goal reference lines
SHOW_MOVING_AVERAGES = True # Show moving average lines
ENABLE_DATA_EXPORT = True   # Allow data download

# ============================================
# ADVANCED SETTINGS
# ============================================
# Date format for exports
EXPORT_DATE_FORMAT = "%Y%m%d"

# Number of bins for histograms
HISTOGRAM_BINS = 30

# Heatmap color scales
STEPS_HEATMAP_SCALE = "Oranges"
CALORIES_HEATMAP_SCALE = "Greens"
SLEEP_HEATMAP_SCALE = "Purples"

# ============================================
# CUSTOM MESSAGES
# ============================================
UPLOAD_MESSAGE = "Please upload your Fitbit dataset files to begin."
NO_DATA_MESSAGE = "No data available for this visualization."
LOADING_MESSAGE = "Loading your fitness data..."

# ============================================
# TIPS & INSIGHTS
# ============================================
TIPS = [
    "💡 Aim for at least 10,000 steps per day for optimal health",
    "💡 Consistency is key - try to maintain regular activity patterns",
    "💡 Quality sleep (7-9 hours) is crucial for recovery and performance",
    "💡 Track your progress weekly to identify trends and patterns",
    "💡 Set realistic, achievable goals and celebrate small wins"
]
