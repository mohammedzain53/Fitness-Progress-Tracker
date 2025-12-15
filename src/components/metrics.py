"""
Metric card components for the dashboard
"""

import streamlit as st
from typing import Dict


def render_metric_cards(metrics: Dict[str, float], record_count: int):
    """
    Render metric cards showing key statistics with enhanced animations
    
    Args:
        metrics: Dictionary of calculated metrics
        record_count: Number of records in the dataset
    """
    # Display record count badge with animation
    st.markdown(
        f'<span class="stats-badge">📊 {record_count} Records Loaded</span>', 
        unsafe_allow_html=True
    )
    
    # Add spacing
    st.markdown('<div style="margin: 1.5rem 0;"></div>', unsafe_allow_html=True)
    
    # Create metric cards with enhanced styling
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card" style="animation-delay: 0.1s;">
            <div class="metric-icon" style="animation: bounce 2s infinite;">🚶</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                                             -webkit-background-clip: text;
                                             -webkit-text-fill-color: transparent;">
                {metrics['total_steps']:,}
            </div>
            <div class="metric-label">Total Steps</div>
            <div style="color: #888; font-size: 0.9rem; margin-top: 0.5rem; font-weight: 500;">
                Avg: {metrics['avg_steps']:,}/day
            </div>
        </div>
        <style>
            @keyframes bounce {{
                0%, 100% {{ transform: translateY(0); }}
                50% {{ transform: translateY(-10px); }}
            }}
        </style>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card" style="animation-delay: 0.2s;">
            <div class="metric-icon" style="animation: bounce 2s infinite 0.2s;">🔥</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
                                             -webkit-background-clip: text;
                                             -webkit-text-fill-color: transparent;">
                {metrics['total_calories']:,}
            </div>
            <div class="metric-label">Total Calories</div>
            <div style="color: #888; font-size: 0.9rem; margin-top: 0.5rem; font-weight: 500;">
                Avg: {metrics['avg_calories']:,}/day
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card" style="animation-delay: 0.3s;">
            <div class="metric-icon" style="animation: bounce 2s infinite 0.4s;">🛏️</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
                                             -webkit-background-clip: text;
                                             -webkit-text-fill-color: transparent;">
                {metrics['avg_sleep']}h
            </div>
            <div class="metric-label">Avg Sleep</div>
            <div style="color: #888; font-size: 0.9rem; margin-top: 0.5rem; font-weight: 500;">
                Per night
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card" style="animation-delay: 0.4s;">
            <div class="metric-icon" style="animation: bounce 2s infinite 0.6s;">📍</div>
            <div class="metric-value" style="background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
                                             -webkit-background-clip: text;
                                             -webkit-text-fill-color: transparent;">
                {metrics['total_distance']}
            </div>
            <div class="metric-label">Total Distance (km)</div>
            <div style="color: #888; font-size: 0.9rem; margin-top: 0.5rem; font-weight: 500;">
                Avg: {metrics['avg_distance']}/day
            </div>
        </div>
        """, unsafe_allow_html=True)
