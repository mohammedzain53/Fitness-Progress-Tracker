"""
Custom CSS styles for the Fitness Progress Tracker dashboard
"""

from src.config import PRIMARY_COLOR_START, PRIMARY_COLOR_END


def get_custom_css():
    """Returns the custom CSS for the dashboard"""
    return f"""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');
    
    /* Global Styles */
    * {{
        font-family: 'Inter', sans-serif;
    }}
    
    /* Main container */
    .main {{
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        padding: 2rem;
    }}
    
    /* Metric cards */
    .metric-card {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(255, 255, 255, 0.18);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        margin: 1rem 0;
    }}
    
    .metric-card:hover {{
        transform: translateY(-5px);
        box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);
    }}
    
    .metric-value {{
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }}
    
    .metric-label {{
        font-size: 1rem;
        color: #666;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 1px;
        margin-top: 0.5rem;
    }}
    
    .metric-icon {{
        font-size: 3rem;
        margin-bottom: 1rem;
    }}
    
    /* Header */
    .dashboard-header {{
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        text-align: center;
    }}
    
    .dashboard-title {{
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
    }}
    
    .dashboard-subtitle {{
        color: #666;
        font-size: 1.2rem;
        margin-top: 0.5rem;
    }}
    
    /* Sidebar */
    [data-testid="stSidebar"] {{
        background: linear-gradient(180deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
    }}
    
    [data-testid="stSidebar"] .css-1d391kg {{
        color: white;
    }}
    
    /* Tabs */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 8px;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 0.5rem;
    }}
    
    .stTabs [data-baseweb="tab"] {{
        background: transparent;
        border-radius: 10px;
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
    }}
    
    .stTabs [aria-selected="true"] {{
        background: rgba(255, 255, 255, 0.95);
        color: {PRIMARY_COLOR_START};
    }}
    
    /* File uploader */
    [data-testid="stFileUploader"] {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        border: 2px dashed {PRIMARY_COLOR_START};
    }}
    
    /* Drag and drop area text */
    [data-testid="stFileUploader"] section {{
        color: white !important;
    }}
    
    [data-testid="stFileUploader"] section span {{
        color: white !important;
    }}
    
    [data-testid="stFileUploader"] section small {{
        color: rgba(255, 255, 255, 0.8) !important;
    }}

    /* File uploader text - make file names visible */
    [data-testid="stFileUploader"] label {{
        color: #1a1a1a !important;
    }}
    
    [data-testid="stFileUploader"] span {{
        color: #1a1a1a !important;
    }}
    
    [data-testid="stFileUploader"] small {{
        color: #666 !important;
    }}
    
    /* Uploaded file names */
    [data-testid="stFileUploader"] div {{
        color: #1a1a1a !important;
    }}
    
    /* File uploader delete button */
    [data-testid="stFileUploader"] button {{
        color: #ff4b4b !important;
    }}
    
    /* Buttons */
    .stDownloadButton button {{
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        transition: transform 0.2s ease;
    }}
    
    .stDownloadButton button:hover {{
        transform: scale(1.05);
    }}
    
    /* Chart containers */
    .chart-container {{
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        margin: 1rem 0;
    }}
    
    /* Stats badge */
    .stats-badge {{
        display: inline-block;
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 20px;
        font-weight: 600;
        margin: 0.5rem;
        animation: fadeInUp 0.5s ease-out;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.3);
    }}
    
    /* Animations */
    @keyframes fadeInUp {{
        from {{
            opacity: 0;
            transform: translateY(20px);
        }}
        to {{
            opacity: 1;
            transform: translateY(0);
        }}
    }}
    
    @keyframes fadeIn {{
        from {{ opacity: 0; }}
        to {{ opacity: 1; }}
    }}
    
    @keyframes slideInLeft {{
        from {{
            opacity: 0;
            transform: translateX(-30px);
        }}
        to {{
            opacity: 1;
            transform: translateX(0);
        }}
    }}
    
    @keyframes pulse {{
        0%, 100% {{ transform: scale(1); }}
        50% {{ transform: scale(1.05); }}
    }}
    
    /* Enhanced metric cards with staggered animation */
    .metric-card {{
        animation: fadeInUp 0.6s ease-out backwards;
    }}
    
    .metric-card:nth-child(1) {{ animation-delay: 0.1s; }}
    .metric-card:nth-child(2) {{ animation-delay: 0.2s; }}
    .metric-card:nth-child(3) {{ animation-delay: 0.3s; }}
    .metric-card:nth-child(4) {{ animation-delay: 0.4s; }}
    
    /* Chart containers with fade in */
    .chart-container {{
        animation: fadeIn 0.8s ease-out;
    }}
    
    /* Improved scrollbar */
    ::-webkit-scrollbar {{
        width: 10px;
        height: 10px;
    }}
    
    ::-webkit-scrollbar-track {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb {{
        background: linear-gradient(135deg, {PRIMARY_COLOR_START} 0%, {PRIMARY_COLOR_END} 100%);
        border-radius: 10px;
    }}
    
    ::-webkit-scrollbar-thumb:hover {{
        background: linear-gradient(135deg, {PRIMARY_COLOR_END} 0%, {PRIMARY_COLOR_START} 100%);
    }}
    
    /* Loading spinner */
    .stSpinner > div {{
        border-top-color: {PRIMARY_COLOR_START} !important;
    }}
    
    /* Enhanced file uploader */
    [data-testid="stFileUploader"]:hover {{
        border-color: {PRIMARY_COLOR_START};
        box-shadow: 0 8px 24px rgba(102, 126, 234, 0.2);
        transform: translateY(-2px);
        transition: all 0.3s ease;
    }}
    
    /* Tab animation */
    .stTabs [data-baseweb="tab"] {{
        transition: all 0.3s ease;
    }}
    
    .stTabs [data-baseweb="tab"]:hover {{
        transform: translateY(-2px);
    }}
    
    /* Success message */
    .success-message {{
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        color: white;
        padding: 1rem 2rem;
        border-radius: 10px;
        margin: 1rem 0;
        animation: slideInLeft 0.5s ease-out;
        box-shadow: 0 4px 15px rgba(17, 153, 142, 0.3);
    }}
    
    /* Info box */
    .info-box {{
        background: rgba(102, 126, 234, 0.1);
        border-left: 4px solid {PRIMARY_COLOR_START};
        padding: 1.5rem;
        border-radius: 10px;
        margin: 1.5rem 0;
        animation: fadeInUp 0.5s ease-out;
    }}
    
    /* Tooltip */
    .tooltip {{
        position: relative;
        display: inline-block;
        cursor: help;
    }}
    
    .tooltip .tooltiptext {{
        visibility: hidden;
        background-color: #333;
        color: white;
        text-align: center;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        transform: translateX(-50%);
        opacity: 0;
        transition: opacity 0.3s;
        white-space: nowrap;
        font-size: 0.85rem;
    }}
    
    .tooltip:hover .tooltiptext {{
        visibility: visible;
        opacity: 1;
    }}
    
    /* Improved button hover */
    .stButton button {{
        transition: all 0.3s ease;
    }}
    
    .stButton button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
    }}
    
    /* Data frame styling */
    .dataframe {{
        animation: fadeIn 0.8s ease-out;
    }}
    
    /* Sidebar animation */
    [data-testid="stSidebar"] > div {{
        animation: slideInLeft 0.5s ease-out;
    }}
</style>
"""
