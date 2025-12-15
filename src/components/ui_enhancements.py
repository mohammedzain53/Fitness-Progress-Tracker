"""
UI/UX Enhancement Components
"""

import streamlit as st
import time


def show_welcome_screen():
    """Display an impressive welcome screen when no data is uploaded"""
    # Use simpler Streamlit components instead of complex HTML
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Header
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="text-align: center;">
            <div style="font-size: 5rem; margin-bottom: 1rem;">🏋️‍♂️</div>
            <h1 style="color: #667eea; margin-bottom: 1rem;">Welcome to Fitness Progress Tracker</h1>
            <p style="font-size: 1.2rem; color: #666;">Transform your fitness data into beautiful, actionable insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Feature cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📊</div>
            <div style="font-size: 1.2rem; font-weight: 600;">15+ Charts</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Interactive visualizations</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%); 
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">🎯</div>
            <div style="font-size: 1.2rem; font-weight: 600;">Goal Tracking</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Monitor your progress</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%); 
                    padding: 2rem; border-radius: 15px; color: white; text-align: center;">
            <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">📈</div>
            <div style="font-size: 1.2rem; font-weight: 600;">Trend Analysis</div>
            <div style="font-size: 0.9rem; opacity: 0.9;">Discover patterns</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Getting started section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("""
        <div style="background: rgba(102, 126, 234, 0.1); padding: 2rem; border-radius: 15px;">
            <h3 style="color: #667eea; margin-bottom: 1rem;">🚀 Getting Started</h3>
            <ol style="color: #666; line-height: 2;">
                <li>Upload your Fitbit CSV files using the uploader above</li>
                <li>Select a date range to filter your data (optional)</li>
                <li>Explore 6 different tabs with unique insights</li>
                <li>Download filtered data for further analysis</li>
            </ol>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.info("💡 Tip: You can upload multiple CSV files at once for comprehensive analysis")


def show_loading_animation(message="Processing your data..."):
    """Display a loading animation"""
    with st.spinner(message):
        time.sleep(0.5)  # Brief pause for visual feedback


def show_success_message(message, icon="✅"):
    """Display a success message with animation"""
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
                color: white; padding: 1rem 2rem; border-radius: 10px;
                margin: 1rem 0; animation: slideIn 0.3s ease-out;
                box-shadow: 0 4px 15px rgba(17, 153, 142, 0.3);">
        <span style="font-size: 1.5rem; margin-right: 0.5rem;">{icon}</span>
        <span style="font-size: 1.1rem; font-weight: 600;">{message}</span>
    </div>
    <style>
        @keyframes slideIn {{
            from {{ transform: translateY(-20px); opacity: 0; }}
            to {{ transform: translateY(0); opacity: 1; }}
        }}
    </style>
    """, unsafe_allow_html=True)


def show_info_tooltip(text, tooltip):
    """Display text with a tooltip"""
    st.markdown(f"""
    <div style="display: inline-block; position: relative; cursor: help;">
        {text}
        <span style="margin-left: 0.3rem; color: #667eea; font-size: 0.9rem;">ⓘ</span>
        <div style="position: absolute; background: #333; color: white; 
                    padding: 0.5rem 1rem; border-radius: 5px; font-size: 0.85rem;
                    white-space: nowrap; bottom: 100%; left: 50%; transform: translateX(-50%);
                    margin-bottom: 0.5rem; opacity: 0; pointer-events: none;
                    transition: opacity 0.3s;" class="tooltip-text">
            {tooltip}
        </div>
    </div>
    <style>
        div:hover .tooltip-text {{
            opacity: 1;
        }}
    </style>
    """, unsafe_allow_html=True)


def show_metric_card_enhanced(icon, value, label, sublabel, color_start, color_end):
    """Enhanced metric card with better animations"""
    return f"""
    <div class="metric-card-enhanced">
        <div class="metric-icon-enhanced">{icon}</div>
        <div class="metric-value-enhanced" style="background: linear-gradient(135deg, {color_start} 0%, {color_end} 100%);
                                                   -webkit-background-clip: text;
                                                   -webkit-text-fill-color: transparent;">
            {value}
        </div>
        <div class="metric-label-enhanced">{label}</div>
        <div class="metric-sublabel-enhanced">{sublabel}</div>
    </div>
    <style>
        .metric-card-enhanced {{
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            padding: 2rem;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.18);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            margin: 1rem 0;
            cursor: pointer;
        }}
        
        .metric-card-enhanced:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 20px 60px rgba(102, 126, 234, 0.3);
        }}
        
        .metric-icon-enhanced {{
            font-size: 3.5rem;
            margin-bottom: 1rem;
            animation: bounce 2s infinite;
        }}
        
        .metric-value-enhanced {{
            font-size: 3.5rem;
            font-weight: 700;
            margin: 0.5rem 0;
            animation: countUp 1s ease-out;
        }}
        
        .metric-label-enhanced {{
            font-size: 1rem;
            color: #666;
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1.5px;
            margin-top: 0.5rem;
        }}
        
        .metric-sublabel-enhanced {{
            color: #999;
            font-size: 0.9rem;
            margin-top: 0.5rem;
            font-weight: 500;
        }}
        
        @keyframes bounce {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-10px); }}
        }}
        
        @keyframes countUp {{
            from {{ opacity: 0; transform: scale(0.5); }}
            to {{ opacity: 1; transform: scale(1); }}
        }}
    </style>
    """


def add_floating_action_button():
    """Add a floating action button for quick actions"""
    st.markdown("""
    <div class="fab-container">
        <button class="fab" onclick="window.scrollTo({top: 0, behavior: 'smooth'})">
            ↑
        </button>
    </div>
    <style>
        .fab-container {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            z-index: 1000;
        }
        
        .fab {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            box-shadow: 0 8px 24px rgba(102, 126, 234, 0.4);
            transition: all 0.3s ease;
        }
        
        .fab:hover {
            transform: scale(1.1) rotate(180deg);
            box-shadow: 0 12px 32px rgba(102, 126, 234, 0.6);
        }
    </style>
    """, unsafe_allow_html=True)


def show_progress_bar(progress, label="Processing"):
    """Show an animated progress bar"""
    st.markdown(f"""
    <div style="margin: 2rem 0;">
        <div style="color: #667eea; font-weight: 600; margin-bottom: 0.5rem;">
            {label}... {progress}%
        </div>
        <div style="background: #e0e0e0; border-radius: 10px; overflow: hidden; height: 8px;">
            <div style="background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
                        width: {progress}%; height: 100%; transition: width 0.3s ease;
                        border-radius: 10px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def add_section_divider(text=""):
    """Add a stylish section divider"""
    st.markdown(f"""
    <div style="display: flex; align-items: center; margin: 3rem 0 2rem 0;">
        <div style="flex: 1; height: 2px; background: linear-gradient(90deg, transparent, #667eea, transparent);"></div>
        {f'<span style="padding: 0 2rem; color: #667eea; font-weight: 600; font-size: 1.1rem;">{text}</span>' if text else ''}
        <div style="flex: 1; height: 2px; background: linear-gradient(90deg, transparent, #667eea, transparent);"></div>
    </div>
    """, unsafe_allow_html=True)


def show_empty_state(icon, title, description, action_text=""):
    """Display an empty state with call to action"""
    st.markdown(f"""
    <div style="text-align: center; padding: 4rem 2rem; 
                background: rgba(102, 126, 234, 0.05); border-radius: 20px;
                border: 2px dashed rgba(102, 126, 234, 0.3);">
        <div style="font-size: 4rem; margin-bottom: 1rem; opacity: 0.5;">{icon}</div>
        <h3 style="color: #667eea; margin-bottom: 1rem;">{title}</h3>
        <p style="color: #666; font-size: 1.1rem; margin-bottom: 1.5rem;">{description}</p>
        {f'<p style="color: #999; font-size: 0.9rem;">💡 {action_text}</p>' if action_text else ''}
    </div>
    """, unsafe_allow_html=True)
