"""
Data processing utilities for Fitness Progress Tracker
"""

import pandas as pd
from typing import Dict, List, Optional, Tuple
from src.config import ACTIVITY_DATE_COL, SLEEP_DATE_COL


def normalize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Normalize column names to lowercase with underscores"""
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
    return df


def load_and_process_files(uploaded_files) -> pd.DataFrame:
    """
    Load and process uploaded CSV files
    
    Args:
        uploaded_files: List of uploaded file objects
        
    Returns:
        Merged and processed DataFrame
    """
    dataframes = {}
    
    for file in uploaded_files:
        df = pd.read_csv(file)
        df = normalize_columns(df)
        dataframes[file.name] = df
    
    # Merge activity + sleep data if available
    if 'dailyactivity_merged.csv' in dataframes and 'sleepday_merged.csv' in dataframes:
        activity = dataframes['dailyactivity_merged.csv']
        sleep = dataframes['sleepday_merged.csv']
        
        if ACTIVITY_DATE_COL in activity.columns:
            activity[ACTIVITY_DATE_COL] = pd.to_datetime(activity[ACTIVITY_DATE_COL])
        if SLEEP_DATE_COL in sleep.columns:
            sleep[SLEEP_DATE_COL] = pd.to_datetime(sleep[SLEEP_DATE_COL])
        
        merged = pd.merge(activity, sleep, left_on=ACTIVITY_DATE_COL, 
                         right_on=SLEEP_DATE_COL, how='outer')
    else:
        # If only one file uploaded, just pick the first
        merged = list(dataframes.values())[0]
    
    return merged


def filter_by_date_range(df: pd.DataFrame, start_date, end_date, 
                         date_col: str) -> pd.DataFrame:
    """
    Filter DataFrame by date range
    
    Args:
        df: Input DataFrame
        start_date: Start date for filtering
        end_date: End date for filtering
        date_col: Name of the date column
        
    Returns:
        Filtered DataFrame
    """
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    return df[(df[date_col] >= start) & (df[date_col] <= end)]


def find_date_column(df: pd.DataFrame) -> Optional[str]:
    """
    Find the date column in the DataFrame
    
    Args:
        df: Input DataFrame
        
    Returns:
        Name of the date column or None
    """
    for col in [ACTIVITY_DATE_COL, SLEEP_DATE_COL]:
        if col in df.columns:
            return col
    return None


def calculate_metrics(df: pd.DataFrame) -> Dict[str, float]:
    """
    Calculate key metrics from the DataFrame
    
    Args:
        df: Input DataFrame
        
    Returns:
        Dictionary of calculated metrics
    """
    metrics = {}
    
    # Steps metrics
    if 'totalsteps' in df.columns:
        metrics['total_steps'] = int(df['totalsteps'].sum())
        metrics['avg_steps'] = int(df['totalsteps'].mean())
    else:
        metrics['total_steps'] = 0
        metrics['avg_steps'] = 0
    
    # Calories metrics
    if 'calories' in df.columns:
        metrics['total_calories'] = int(df['calories'].sum())
        metrics['avg_calories'] = int(df['calories'].mean())
    else:
        metrics['total_calories'] = 0
        metrics['avg_calories'] = 0
    
    # Sleep metrics
    if 'totalminutesasleep' in df.columns:
        metrics['avg_sleep'] = round(df['totalminutesasleep'].mean() / 60, 1)
    else:
        metrics['avg_sleep'] = 0
    
    # Distance metrics
    if 'totaldistance' in df.columns:
        metrics['total_distance'] = round(df['totaldistance'].sum(), 2)
        metrics['avg_distance'] = round(df['totaldistance'].mean(), 2)
    else:
        metrics['total_distance'] = 0
        metrics['avg_distance'] = 0
    
    return metrics


def add_time_features(df: pd.DataFrame, date_col: str) -> pd.DataFrame:
    """
    Add time-based features to the DataFrame
    
    Args:
        df: Input DataFrame
        date_col: Name of the date column
        
    Returns:
        DataFrame with added time features
    """
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    
    if df[date_col].notnull().any():
        df['day_of_week'] = df[date_col].dt.day_name()
        df['week'] = df[date_col].dt.isocalendar().week
        df['month'] = df[date_col].dt.month
        df['date'] = df[date_col].dt.date
    
    return df


def add_moving_averages(df: pd.DataFrame, column: str, 
                       windows: List[int]) -> pd.DataFrame:
    """
    Add moving averages to the DataFrame
    
    Args:
        df: Input DataFrame
        column: Column to calculate moving averages for
        windows: List of window sizes
        
    Returns:
        DataFrame with added moving average columns
    """
    df_sorted = df.sort_values(df.columns[0])  # Sort by first column (usually date)
    
    for window in windows:
        col_name = f'{column}_ma{window}'
        df_sorted[col_name] = df_sorted[column].rolling(window=window, min_periods=1).mean()
    
    return df_sorted
