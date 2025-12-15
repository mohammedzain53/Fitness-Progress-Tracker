# 🚀 Quick Reference Guide

## Installation & Running

```bash
# Install dependencies
pip install -r requirements.txt

# Run the dashboard
streamlit run app.py
```

## Project Structure

```
fitness-progress-tracker/
├── app.py                      # Main entry point
├── src/                        # Source code
│   ├── config.py               # Settings
│   ├── styles.py               # CSS
│   ├── data_processor.py       # Data utilities
│   └── components/             # UI components
├── data/                       # Data files
├── docs/                       # Documentation
└── fitbit_analysis.ipynb       # Analysis notebook
```

## Configuration

Edit `src/config.py`:

```python
# Goals
STEPS_GOAL = 10000
CALORIES_GOAL = 2500
SLEEP_GOAL = 8

# Colors
PRIMARY_COLOR_START = "#667eea"
PRIMARY_COLOR_END = "#764ba2"

# Chart Settings
MA_SHORT_WINDOW = 7
MA_LONG_WINDOW = 30
```

## Common Tasks

### Add a New Chart
1. Create function in `src/components/charts.py`
2. Import in `src/components/tabs.py`
3. Call in appropriate tab function

### Add a New Metric
1. Update `calculate_metrics()` in `src/data_processor.py`
2. Update `render_metric_cards()` in `src/components/metrics.py`

### Add a New Tab
1. Create function in `src/components/tabs.py`
2. Import in `app.py`
3. Add to tabs list

### Change Colors
Edit `src/config.py`:
```python
PRIMARY_COLOR_START = "#your_color"
STEPS_COLOR = "#your_color"
```

### Change Goals
Edit `src/config.py`:
```python
STEPS_GOAL = 12000
CALORIES_GOAL = 3000
```

## File Locations

| What | Where |
|------|-------|
| Main app | `app.py` |
| Configuration | `src/config.py` |
| Styling | `src/styles.py` |
| Data processing | `src/data_processor.py` |
| Charts | `src/components/charts.py` |
| Metrics | `src/components/metrics.py` |
| Tabs | `src/components/tabs.py` |
| Documentation | `docs/` |
| Data files | `data/fitbit_dataset/` |

## Import Examples

```python
# Configuration
from src.config import STEPS_GOAL, PRIMARY_COLOR_START

# Styling
from src.styles import get_custom_css

# Data processing
from src.data_processor import calculate_metrics, load_and_process_files

# Charts
from src.components.charts import create_gauge_chart, create_steps_trend_chart

# Metrics
from src.components.metrics import render_metric_cards

# Tabs
from src.components.tabs import render_overview_tab, render_steps_tab
```

## Documentation

| Document | Purpose |
|----------|---------|
| [README.md](README.md) | Project overview |
| [SETUP.md](SETUP.md) | Installation guide |
| [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md) | Comprehensive overview |
| [RESTRUCTURE_SUMMARY.md](RESTRUCTURE_SUMMARY.md) | What was changed |
| [docs/QUICK_START.md](docs/QUICK_START.md) | 5-minute guide |
| [docs/FEATURES.md](docs/FEATURES.md) | Feature list |
| [docs/PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md) | Technical docs |

## Troubleshooting

### Import Error
```bash
# Make sure you're in the project root
cd fitness-progress-tracker
streamlit run app.py
```

### Module Not Found
```bash
# Reinstall dependencies
pip install -r requirements.txt
```

### Charts Not Showing
- Check CSV column names
- Verify data format
- Check browser console

## Quick Commands

```bash
# Install
pip install -r requirements.txt

# Run
streamlit run app.py

# Run with auto-reload
streamlit run app.py --server.runOnSave true

# Check version
streamlit --version
```

## Key Features

- 📊 6 organized tabs
- 🎯 Goal tracking with gauges
- 📈 15+ visualizations
- 🎨 Modern glassmorphism UI
- ⚙️ Easy configuration
- 📱 Responsive design
- 💾 Data export
- 🔧 Component-based

## Support

- **Setup Issues:** See [SETUP.md](SETUP.md)
- **Usage Help:** See [docs/QUICK_START.md](docs/QUICK_START.md)
- **Technical Details:** See [docs/PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md)
- **Features:** See [docs/FEATURES.md](docs/FEATURES.md)

---

**Need more help?** Check the full documentation in the `docs/` folder!
