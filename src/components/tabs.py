"""
Tab components for the dashboard
"""

import streamlit as st
import pandas as pd
from datetime import datetime
from src.components.charts import (
    create_gauge_chart, create_weekly_performance_chart,
    create_steps_trend_chart, create_steps_distribution_chart,
    create_steps_boxplot, create_calories_scatter,
    create_calories_timeline, create_day_of_week_chart,
    create_activity_radar, create_calendar_heatmap
)
from src.config import (
    STEPS_GOAL, CALORIES_GOAL, SLEEP_GOAL,
    STEPS_COLOR, CALORIES_COLOR, SLEEP_COLOR,
    STEPS_HEATMAP_SCALE, CALORIES_HEATMAP_SCALE,
    EXPORT_DATE_FORMAT, ENABLE_DATA_EXPORT
)


def render_overview_tab(df: pd.DataFrame, metrics: dict):
    """Render the Overview tab"""
    # Add section header with animation
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #667eea; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            📊 Performance Overview
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Track your progress towards daily goals and weekly trends
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    # Goal progress gauges
    st.subheader('🎯 Daily Goals Progress')
    goal_col1, goal_col2, goal_col3 = st.columns(3)
    
    with goal_col1:
        fig_steps = create_gauge_chart(
            metrics['avg_steps'], STEPS_GOAL, "Steps Goal", STEPS_COLOR
        )
        st.plotly_chart(fig_steps, use_container_width=True)
    
    with goal_col2:
        fig_cal = create_gauge_chart(
            metrics['avg_calories'], CALORIES_GOAL, "Calories Goal", CALORIES_COLOR
        )
        st.plotly_chart(fig_cal, use_container_width=True)
    
    with goal_col3:
        fig_sleep = create_gauge_chart(
            metrics['avg_sleep'], SLEEP_GOAL, "Sleep Goal (hrs)", SLEEP_COLOR
        )
        st.plotly_chart(fig_sleep, use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Weekly summary
    if 'activitydate' in df.columns and 'week' in df.columns:
        st.markdown('<div class="chart-container">', unsafe_allow_html=True)
        st.subheader('📅 Weekly Performance')
        fig_weekly = create_weekly_performance_chart(df)
        st.plotly_chart(fig_weekly, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)



def render_steps_tab(df: pd.DataFrame):
    """Render the Steps Analysis tab"""
    # Add section header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #667eea; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            🚶 Steps Deep Dive
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Track your daily steps with advanced trend analysis and moving averages
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    if 'activitydate' in df.columns and 'totalsteps' in df.columns:
        # Enhanced trend chart - now takes full width
        fig_trend = create_steps_trend_chart(df)
        st.plotly_chart(fig_trend, use_container_width=True)
    else:
        st.warning("Steps data not available for analysis.")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_calories_tab(df: pd.DataFrame):
    """Render the Calories tab"""
    # Add section header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #f093fb; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            🔥 Calorie Burn Analysis
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Understand your energy expenditure and activity correlation
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    if 'calories' in df.columns and 'totalsteps' in df.columns:
        # Scatter plot
        fig_scatter = create_calories_scatter(df)
        st.plotly_chart(fig_scatter, use_container_width=True)
        
        # Timeline
        if 'activitydate' in df.columns:
            fig_timeline = create_calories_timeline(df)
            st.plotly_chart(fig_timeline, use_container_width=True)
    else:
        st.warning("Calories data not available for analysis.")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_patterns_tab(df: pd.DataFrame):
    """Render the Activity Patterns tab"""
    # Add section header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #4facfe; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            📅 Activity Patterns
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Discover your weekly patterns and activity intensity distribution
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    if 'activitydate' in df.columns and 'totalsteps' in df.columns:
        df['activitydate'] = pd.to_datetime(df['activitydate'], errors='coerce')
        
        if df['activitydate'].notnull().any():
            col1, col2 = st.columns(2)
            
            with col1:
                # Steps by day
                fig_steps_day = create_day_of_week_chart(
                    df, 'totalsteps', '📅 Average Steps by Day of Week', 'Viridis'
                )
                st.plotly_chart(fig_steps_day, use_container_width=True)
            
            with col2:
                # Calories by day
                if 'calories' in df.columns:
                    fig_cal_day = create_day_of_week_chart(
                        df, 'calories', '🔥 Average Calories by Day of Week', 'Plasma'
                    )
                    st.plotly_chart(fig_cal_day, use_container_width=True)
        else:
            st.warning("Could not detect valid dates for pattern analysis.")
    else:
        st.warning("Activity date column not found in dataset.")
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_calendar_tab(df: pd.DataFrame):
    """Render the Calendar View tab"""
    # Add section header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #43e97b; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            🗓️ Calendar Heatmaps
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Visualize your activity across weeks with GitHub-style heatmaps
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    
    if 'activitydate' in df.columns:
        df['activitydate'] = pd.to_datetime(df['activitydate'], errors='coerce')
        df['date'] = df['activitydate'].dt.date
        
        # Steps heatmap
        if 'totalsteps' in df.columns:
            st.subheader('🗓️ Steps Calendar Heatmap')
            fig_steps_cal = create_calendar_heatmap(
                df, 'totalsteps', 'Daily Steps Activity', STEPS_HEATMAP_SCALE
            )
            st.plotly_chart(fig_steps_cal, use_container_width=True)
        
        # Calories heatmap
        if 'calories' in df.columns:
            st.subheader('🔥 Calories Calendar Heatmap')
            fig_cal = create_calendar_heatmap(
                df, 'calories', 'Daily Calories Burned', CALORIES_HEATMAP_SCALE
            )
            st.plotly_chart(fig_cal, use_container_width=True)
    else:
        st.warning('Activity date data not found for calendar view.')
    
    st.markdown('</div>', unsafe_allow_html=True)


def render_summary_tab(df: pd.DataFrame):
    """Render the Summary tab"""
    # Add section header
    st.markdown("""
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #764ba2; font-size: 2rem; font-weight: 700; margin-bottom: 0.5rem;">
            📈 Statistical Summary
        </h2>
        <p style="color: #666; font-size: 1.1rem;">
            Complete statistical overview and data export options
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="chart-container">', unsafe_allow_html=True)
    st.subheader('📊 Data Summary Statistics')
    
    # Select only numeric columns for statistics to avoid Arrow issues
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
    df_numeric = df[numeric_cols]
    
    # Display statistics
    summary_df = df_numeric.describe().transpose()
    summary_df = summary_df.round(2)  # Round to 2 decimal places
    
    st.dataframe(
        summary_df.style.background_gradient(cmap='Blues'), 
        use_container_width=True
    )
    
    st.markdown("""
    <div style="background: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-top: 1rem; color: #1a1a1a;">
    <h4 style="color: #1a1a1a;">📖 Understanding Your Stats</h4>
    <ul style="color: #333;">
        <li><b>count:</b> Number of recorded values</li>
        <li><b>mean:</b> Average value across all days</li>
        <li><b>std:</b> Standard deviation (consistency of your data)</li>
        <li><b>min/max:</b> Your lowest and highest recorded values</li>
        <li><b>25%/50%/75%:</b> Percentile distribution of your performance</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)
    
    # Download button
    if ENABLE_DATA_EXPORT:
        st.markdown('<br>', unsafe_allow_html=True)
        st.download_button(
            '📥 Download Filtered Data as CSV',
            df.to_csv(index=False),
            file_name=f'fitbit_data_{datetime.now().strftime(EXPORT_DATE_FORMAT)}.csv',
            mime='text/csv'
        )
    
    st.markdown('</div>', unsafe_allow_html=True)
