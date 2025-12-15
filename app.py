"""
Fitness Progress Tracker Dashboard
A modern, component-based Streamlit application for analyzing Fitbit data
"""

import streamlit as st
from src.config import PAGE_TITLE, PAGE_ICON, DASHBOARD_TITLE, DASHBOARD_SUBTITLE, UPLOAD_MESSAGE
from src.styles import get_custom_css
from src.data_processor import (
    load_and_process_files, find_date_column, filter_by_date_range,
    calculate_metrics, add_time_features
)
from src.components.metrics import render_metric_cards
from src.components.tabs import (
    render_overview_tab, render_steps_tab, render_calories_tab,
    render_patterns_tab, render_calendar_tab, render_summary_tab
)
from src.components.ui_enhancements import (
    show_welcome_screen, show_loading_animation, show_success_message,
    add_floating_action_button, show_progress_bar
)

# Page configuration
st.set_page_config(
    page_title=PAGE_TITLE,
    layout='wide',
    initial_sidebar_state='expanded',
    page_icon=PAGE_ICON
)

# Apply custom CSS
st.markdown(get_custom_css(), unsafe_allow_html=True)

# Dashboard Header
st.markdown(f"""
<div class="dashboard-header">
    <h1 class="dashboard-title">{DASHBOARD_TITLE}</h1>
    <p class="dashboard-subtitle">{DASHBOARD_SUBTITLE}</p>
</div>
""", unsafe_allow_html=True)

# File upload
uploaded_files = st.file_uploader(
    'Upload your Fitbit CSV files', 
    type=['csv'], 
    accept_multiple_files=True
)

if uploaded_files:
    # Show loading animation
    with st.spinner('🔄 Processing your fitness data...'):
        # Load and process data
        df = load_and_process_files(uploaded_files)
    
    # Show success message
    show_success_message(f"Successfully loaded {len(uploaded_files)} file(s)!", "✅")
    
    # Sidebar filters
    st.sidebar.header('Filters')
    date_col = find_date_column(df)
    
    if date_col:
        # Date range filter
        date_range = st.sidebar.date_input('Select Date Range', [])
        if len(date_range) == 2:
            df = filter_by_date_range(df, date_range[0], date_range[1], date_col)
    
    # Add time features
    if date_col:
        df = add_time_features(df, date_col)
    
    # Calculate metrics
    metrics = calculate_metrics(df)
    
    # Render metric cards
    render_metric_cards(metrics, len(df))
    
    # Create tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        '📊 Overview', 
        '🚶 Steps Analysis', 
        '🔥 Calories', 
        '📅 Activity Patterns', 
        '🗓️ Calendar View', 
        '📈 Summary'
    ])
    
    with tab1:
        render_overview_tab(df, metrics)
    
    with tab2:
        render_steps_tab(df)
    
    with tab3:
        render_calories_tab(df)
    
    with tab4:
        render_patterns_tab(df)
    
    with tab5:
        render_calendar_tab(df)
    
    with tab6:
        render_summary_tab(df)

else:
    # Show welcome screen when no data is uploaded
    show_welcome_screen()

# Add floating action button for better UX
add_floating_action_button()

# Add footer
st.markdown("""
<div style="margin-top: 5rem; padding: 2rem; text-align: center; 
            background: rgba(255, 255, 255, 0.05); border-radius: 15px;
            border-top: 2px solid rgba(102, 126, 234, 0.2);">
    <p style="color: #666; font-size: 0.9rem; margin-bottom: 0.5rem;">
        Made with ❤️ for fitness enthusiasts
    </p>
    <p style="color: #999; font-size: 0.8rem;">
        Fitness Progress Tracker v2.0 | Powered by Streamlit & Plotly
    </p>
</div>
""", unsafe_allow_html=True)
