"""
Chart components for the dashboard
"""

import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from src.config import (
    STEPS_GOAL, CALORIES_GOAL, SLEEP_GOAL,
    GAUGE_HEIGHT, MAIN_CHART_HEIGHT, SECONDARY_CHART_HEIGHT, SMALL_CHART_HEIGHT,
    STEPS_COLOR, CALORIES_COLOR, SLEEP_COLOR,
    MA_SHORT_WINDOW, MA_LONG_WINDOW,
    HISTOGRAM_BINS, STEPS_HEATMAP_SCALE, CALORIES_HEATMAP_SCALE
)


def create_gauge_chart(value: float, goal: float, title: str, color: str) -> go.Figure:
    """Create an enhanced gauge chart for goal tracking with better visuals"""
    # Calculate percentage
    percentage = (value / goal) * 100 if goal > 0 else 0
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={
            'text': f"<b>{title}</b><br><span style='font-size:14px; color:gray'>{percentage:.1f}% of goal</span>",
            'font': {'size': 18, 'family': 'Inter'}
        },
        delta={
            'reference': goal,
            'increasing': {'color': "#38ef7d"},
            'decreasing': {'color': "#f5576c"},
            'font': {'size': 16}
        },
        number={'font': {'size': 32, 'family': 'Inter', 'color': color}},
        gauge={
            'axis': {
                'range': [None, goal * 1.5],
                'tickwidth': 2,
                'tickcolor': color,
                'tickfont': {'size': 12}
            },
            'bar': {'color': color, 'thickness': 0.8},
            'bgcolor': "rgba(255, 255, 255, 0.8)",
            'borderwidth': 3,
            'bordercolor': color,
            'steps': [
                {'range': [0, goal * 0.5], 'color': 'rgba(255, 87, 108, 0.15)'},
                {'range': [goal * 0.5, goal], 'color': 'rgba(255, 193, 7, 0.15)'},
                {'range': [goal, goal * 1.5], 'color': 'rgba(56, 239, 125, 0.15)'}
            ],
            'threshold': {
                'line': {'color': "#f5576c", 'width': 5},
                'thickness': 0.85,
                'value': goal
            }
        }
    ))
    
    fig.update_layout(
        height=GAUGE_HEIGHT,
        margin=dict(l=20, r=20, t=60, b=20),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'family': 'Inter'}
    )
    return fig



def create_weekly_performance_chart(df: pd.DataFrame) -> go.Figure:
    """Create weekly performance dual-axis chart"""
    weekly = df.groupby('week').agg({
        'totalsteps': 'sum',
        'calories': 'sum',
        'totaldistance': 'sum'
    }).reset_index()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=weekly['week'],
        y=weekly['totalsteps'],
        name='Steps',
        marker_color=STEPS_COLOR,
        yaxis='y',
        hovertemplate='Week %{x}<br>Steps: %{y:,}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=weekly['week'],
        y=weekly['calories'],
        name='Calories',
        marker_color=CALORIES_COLOR,
        yaxis='y2',
        mode='lines+markers',
        line=dict(width=3),
        hovertemplate='Week %{x}<br>Calories: %{y:,}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Weekly Steps & Calories Trend',
        xaxis=dict(title='Week Number'),
        yaxis=dict(title='Total Steps', side='left'),
        yaxis2=dict(title='Total Calories', overlaying='y', side='right'),
        hovermode='x unified',
        template='plotly_white',
        height=SECONDARY_CHART_HEIGHT,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig


def create_steps_trend_chart(df: pd.DataFrame) -> go.Figure:
    """Create clean and simple steps trend chart"""
    df_sorted = df.sort_values('activitydate')
    df_sorted['steps_ma7'] = df_sorted['totalsteps'].rolling(window=MA_SHORT_WINDOW, min_periods=1).mean()
    df_sorted['steps_ma30'] = df_sorted['totalsteps'].rolling(window=MA_LONG_WINDOW, min_periods=1).mean()
    
    fig = go.Figure()
    
    # Daily steps - simple line with area fill
    fig.add_trace(go.Scatter(
        x=df_sorted['activitydate'],
        y=df_sorted['totalsteps'],
        name='Daily Steps',
        fill='tozeroy',
        fillcolor='rgba(102, 126, 234, 0.2)',
        line=dict(color='#667eea', width=1.5),
        hovertemplate='<b>%{x|%b %d, %Y}</b><br>Steps: <b>%{y:,}</b><extra></extra>',
        mode='lines'
    ))
    
    # 7-day moving average
    fig.add_trace(go.Scatter(
        x=df_sorted['activitydate'],
        y=df_sorted['steps_ma7'],
        name=f'{MA_SHORT_WINDOW}-Day Average',
        line=dict(color='#4facfe', width=3),
        hovertemplate=f'<b>%{{x|%b %d, %Y}}</b><br>{MA_SHORT_WINDOW}-Day Avg: <b>%{{y:,.0f}}</b><extra></extra>',
        mode='lines'
    ))
    
    # 30-day moving average
    fig.add_trace(go.Scatter(
        x=df_sorted['activitydate'],
        y=df_sorted['steps_ma30'],
        name=f'{MA_LONG_WINDOW}-Day Average',
        line=dict(color='#764ba2', width=3, dash='dash'),
        hovertemplate=f'<b>%{{x|%b %d, %Y}}</b><br>{MA_LONG_WINDOW}-Day Avg: <b>%{{y:,.0f}}</b><extra></extra>',
        mode='lines'
    ))
    
    # Goal line - simple and clean
    fig.add_hline(
        y=STEPS_GOAL,
        line_dash="dash",
        line_color="#f5576c",
        line_width=2,
        annotation_text=f"Goal: {STEPS_GOAL:,}",
        annotation_position="right"
    )
    
    fig.update_layout(
        title='Daily Steps Trend & Moving Averages',
        xaxis_title='Date',
        yaxis_title='Steps',
        height=500,
        hovermode='x unified',
        showlegend=True,
        legend=dict(x=0, y=1.1, orientation='h')
    )
    
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        showline=True,
        linewidth=2,
        linecolor='black'
    )
    
    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='lightgray',
        showline=True,
        linewidth=2,
        linecolor='black'
    )
    
    return fig



def create_steps_distribution_chart(df: pd.DataFrame) -> go.Figure:
    """Create beautiful steps distribution histogram with gradient colors"""
    # Calculate statistics
    mean_steps = df['totalsteps'].mean()
    median_steps = df['totalsteps'].median()
    
    fig = go.Figure()
    
    # Create histogram with gradient colors
    fig.add_trace(go.Histogram(
        x=df['totalsteps'],
        nbinsx=HISTOGRAM_BINS,
        name='Frequency',
        marker=dict(
            color=df['totalsteps'],
            colorscale='Viridis',
            line=dict(color='white', width=2),
            opacity=0.85,
            showscale=False
        ),
        hovertemplate='<b>Steps:</b> %{x:,.0f}<br><b>Days:</b> %{y}<extra></extra>'
    ))
    
    # Add mean line
    fig.add_vline(
        x=mean_steps,
        line_dash="solid",
        line_color="#38ef7d",
        line_width=4,
        annotation_text=f"📊 Mean: {mean_steps:,.0f}",
        annotation_position="top",
        annotation=dict(
            font=dict(size=12, color="#38ef7d", family='Inter'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#38ef7d',
            borderwidth=2,
            borderpad=4
        )
    )
    
    # Add median line
    fig.add_vline(
        x=median_steps,
        line_dash="dash",
        line_color="#f093fb",
        line_width=3,
        annotation_text=f"📍 Median: {median_steps:,.0f}",
        annotation_position="bottom",
        annotation=dict(
            font=dict(size=11, color="#f093fb", family='Inter'),
            bgcolor='rgba(255,255,255,0.9)',
            bordercolor='#f093fb',
            borderwidth=2,
            borderpad=4
        )
    )
    
    fig.update_layout(
        title={
            'text': '<b>📊 Steps Distribution Pattern</b>',
            'font': {'size': 18, 'family': 'Inter', 'color': '#2c3e50'},
            'x': 0.5,
            'xanchor': 'center'
        },
        xaxis=dict(
            title=dict(text='<b>📏 Daily Steps</b>', font=dict(size=15, color='#000000', family='Inter')),
            showgrid=True,
            gridcolor='rgba(100,100,100,0.3)',
            gridwidth=2,
            showline=True,
            linewidth=5,
            linecolor='#000000',
            mirror=True,
            ticks='outside',
            tickwidth=3,
            tickcolor='#000000',
            ticklen=7,
            tickfont=dict(size=12, color='#000000', family='Inter')
        ),
        yaxis=dict(
            title=dict(text='<b>📈 Number of Days</b>', font=dict(size=15, color='#000000', family='Inter')),
            showgrid=True,
            gridcolor='rgba(100,100,100,0.3)',
            gridwidth=2,
            showline=True,
            linewidth=5,
            linecolor='#000000',
            mirror=True,
            ticks='outside',
            tickwidth=3,
            tickcolor='#000000',
            ticklen=7,
            tickfont=dict(size=12, color='#000000', family='Inter')
        ),
        template='plotly_white',
        height=SMALL_CHART_HEIGHT + 30,
        showlegend=False,
        plot_bgcolor='#fafafa',
        paper_bgcolor='white',
        font={'family': 'Inter'},
        margin=dict(t=60, b=60, l=60, r=60)
    )
    return fig


def create_steps_boxplot(df: pd.DataFrame) -> go.Figure:
    """Create stunning box plot with violin overlay and statistics"""
    # Calculate statistics
    q1 = df['totalsteps'].quantile(0.25)
    median = df['totalsteps'].median()
    q3 = df['totalsteps'].quantile(0.75)
    mean = df['totalsteps'].mean()
    
    fig = go.Figure()
    
    # Add violin plot for distribution shape
    fig.add_trace(go.Violin(
        y=df['totalsteps'],
        name='Distribution',
        box_visible=True,
        meanline_visible=True,
        fillcolor='rgba(102, 126, 234, 0.3)',
        line_color='#667eea',
        opacity=0.8,
        x0='Steps',
        hovertemplate='<b>Steps:</b> %{y:,}<extra></extra>'
    ))
    
    # Add box plot overlay
    fig.add_trace(go.Box(
        y=df['totalsteps'],
        name='Box Plot',
        marker=dict(
            color='#764ba2',
            size=8,
            line=dict(color='white', width=2)
        ),
        boxmean='sd',
        fillcolor='rgba(118, 75, 162, 0.5)',
        line=dict(color='#764ba2', width=3),
        hovertemplate='<b>Steps:</b> %{y:,}<extra></extra>',
        showlegend=False
    ))
    
    fig.update_layout(
        title={
            'text': '<b>📦 Steps Statistical Analysis</b>',
            'font': {'size': 18, 'family': 'Inter', 'color': '#2c3e50'},
            'x': 0.5,
            'xanchor': 'center'
        },
        yaxis=dict(
            title=dict(text='<b>📊 Daily Steps</b>', font=dict(size=15, color='#000000', family='Inter')),
            showgrid=True,
            gridcolor='rgba(100,100,100,0.3)',
            gridwidth=2,
            showline=True,
            linewidth=5,
            linecolor='#000000',
            mirror=True,
            ticks='outside',
            tickwidth=3,
            tickcolor='#000000',
            ticklen=7,
            tickfont=dict(size=12, color='#000000', family='Inter'),
            zeroline=True,
            zerolinecolor='rgba(0,0,0,0.4)',
            zerolinewidth=2
        ),
        xaxis=dict(
            title=dict(text='<b>📦 Distribution</b>', font=dict(size=15, color='#000000', family='Inter')),
            showgrid=False,
            showline=True,
            linewidth=5,
            linecolor='#000000',
            mirror=True,
            ticks='outside',
            tickwidth=3,
            tickcolor='#000000',
            ticklen=7,
            tickfont=dict(size=12, color='#000000', family='Inter')
        ),
        template='plotly_white',
        height=SMALL_CHART_HEIGHT + 30,
        showlegend=False,
        plot_bgcolor='#fafafa',
        paper_bgcolor='white',
        font={'family': 'Inter'},
        margin=dict(t=60, b=60, l=80, r=60),
        annotations=[
            dict(
                x=0.15, y=median,
                text=f"<b>Median:</b> {median:,.0f}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#764ba2',
                ax=-60,
                ay=0,
                font=dict(size=11, color='#764ba2', family='Inter'),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#764ba2',
                borderwidth=2,
                borderpad=4
            ),
            dict(
                x=0.15, y=mean,
                text=f"<b>Mean:</b> {mean:,.0f}",
                showarrow=True,
                arrowhead=2,
                arrowsize=1,
                arrowwidth=2,
                arrowcolor='#38ef7d',
                ax=60,
                ay=0,
                font=dict(size=11, color='#38ef7d', family='Inter'),
                bgcolor='rgba(255,255,255,0.9)',
                bordercolor='#38ef7d',
                borderwidth=2,
                borderpad=4
            )
        ]
    )
    return fig


def create_calories_scatter(df: pd.DataFrame) -> go.Figure:
    """Create enhanced calories vs steps scatter plot"""
    fig = px.scatter(
        df, x='totalsteps', y='calories',
        color='veryactiveminutes' if 'veryactiveminutes' in df.columns else None,
        size='totaldistance' if 'totaldistance' in df.columns else None,
        title='🔥 Calories Burned vs Steps Taken',
        labels={
            'totalsteps': 'Total Steps',
            'calories': 'Calories',
            'veryactiveminutes': 'Very Active Minutes',
            'totaldistance': 'Distance (km)'
        },
        color_continuous_scale='Sunset'
    )
    
    fig.update_traces(
        marker=dict(
            size=14,
            line=dict(width=2, color='white'),
            opacity=0.7
        ),
        hovertemplate='<b>Steps:</b> %{x:,}<br><b>Calories:</b> %{y:,}<br><extra></extra>'
    )
    
    fig.update_layout(
        title={
            'text': '<b>🔥 Calories Burned vs Steps Taken</b>',
            'font': {'size': 20, 'family': 'Inter'}
        },
        xaxis=dict(
            title='<b>Total Steps</b>',
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)'
        ),
        yaxis=dict(
            title='<b>Calories Burned</b>',
            showgrid=True,
            gridcolor='rgba(0,0,0,0.05)'
        ),
        template='plotly_white',
        height=MAIN_CHART_HEIGHT,
        plot_bgcolor='rgba(250,250,250,0.5)',
        font={'family': 'Inter'},
        coloraxis_colorbar=dict(
            title="<b>Active<br>Minutes</b>",
            thickness=15,
            len=0.7
        )
    )
    return fig


def create_calories_timeline(df: pd.DataFrame) -> go.Figure:
    """Create calories timeline chart"""
    df_sorted = df.sort_values('activitydate')
    df_sorted['calories_ma7'] = df_sorted['calories'].rolling(window=MA_SHORT_WINDOW, min_periods=1).mean()
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=df_sorted['activitydate'],
        y=df_sorted['calories'],
        name='Daily Calories',
        marker_color='rgba(240, 147, 251, 0.6)',
        hovertemplate='%{x}<br>Calories: %{y:,}<extra></extra>'
    ))
    fig.add_trace(go.Scatter(
        x=df_sorted['activitydate'],
        y=df_sorted['calories_ma7'],
        name=f'{MA_SHORT_WINDOW}-Day Average',
        line=dict(color=CALORIES_COLOR, width=3),
        hovertemplate=f'%{{x}}<br>{MA_SHORT_WINDOW}-Day Avg: %{{y:,.0f}}<extra></extra>'
    ))
    
    fig.update_layout(
        title='Daily Calories Burned Over Time',
        xaxis_title='Date',
        yaxis_title='Calories',
        template='plotly_white',
        hovermode='x unified',
        height=SECONDARY_CHART_HEIGHT,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    return fig



def create_day_of_week_chart(df: pd.DataFrame, metric: str, title: str, 
                             colorscale: str) -> go.Figure:
    """Create day of week analysis chart"""
    days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    metric_by_day = df.groupby('day_of_week', dropna=True)[metric].mean().reset_index()
    metric_by_day['day_of_week'] = pd.Categorical(
        metric_by_day['day_of_week'], categories=days_order, ordered=True
    )
    metric_by_day = metric_by_day.sort_values('day_of_week')
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=metric_by_day['day_of_week'],
        y=metric_by_day[metric],
        marker=dict(
            color=metric_by_day[metric],
            colorscale=colorscale,
            showscale=True,
            colorbar=dict(title=metric.capitalize())
        ),
        text=metric_by_day[metric].round(0),
        textposition='outside',
        hovertemplate=f'<b>%{{x}}</b><br>Avg {metric.capitalize()}: %{{y:,.0f}}<extra></extra>'
    ))
    fig.update_layout(
        title=title,
        xaxis_title='',
        yaxis_title=f'Average {metric.capitalize()}',
        template='plotly_white',
        height=SECONDARY_CHART_HEIGHT
    )
    return fig


def create_activity_radar(df: pd.DataFrame) -> go.Figure:
    """Create enhanced activity intensity radar chart"""
    activity_avg = {
        'Very Active': df['veryactiveminutes'].mean(),
        'Fairly Active': df['fairlyactiveminutes'].mean(),
        'Lightly Active': df['lightlyactiveminutes'].mean(),
        'Sedentary': df['sedentaryminutes'].mean()
    }
    
    fig = go.Figure()
    
    # Add filled area
    fig.add_trace(go.Scatterpolar(
        r=list(activity_avg.values()),
        theta=list(activity_avg.keys()),
        fill='toself',
        fillcolor='rgba(102, 126, 234, 0.4)',
        line=dict(color=STEPS_COLOR, width=3),
        marker=dict(size=10, color=STEPS_COLOR),
        hovertemplate='<b>%{theta}</b><br>Average: <b>%{r:.0f} minutes</b><extra></extra>',
        name='Activity Level'
    ))
    
    fig.update_layout(
        title={
            'text': '<b>⚡ Activity Intensity Distribution</b>',
            'font': {'size': 18, 'family': 'Inter'}
        },
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(activity_avg.values()) * 1.2],
                showline=True,
                linewidth=2,
                gridcolor='rgba(0,0,0,0.1)',
                tickfont=dict(size=11)
            ),
            angularaxis=dict(
                linewidth=2,
                showline=True,
                gridcolor='rgba(0,0,0,0.1)'
            ),
            bgcolor='rgba(250,250,250,0.5)'
        ),
        showlegend=False,
        template='plotly_white',
        height=SECONDARY_CHART_HEIGHT,
        font={'family': 'Inter'}
    )
    return fig


def create_calendar_heatmap(df: pd.DataFrame, metric: str, title: str, 
                            colorscale: str) -> go.Figure:
    """Create calendar heatmap"""
    metric_by_day = df.groupby('date')[metric].sum().reset_index()
    metric_by_day['dow'] = pd.to_datetime(metric_by_day['date']).dt.dayofweek
    metric_by_day['week'] = pd.to_datetime(metric_by_day['date']).dt.isocalendar().week
    
    pivot = metric_by_day.pivot(index='dow', columns='week', values=metric)
    z = pivot.values
    x = pivot.columns.astype(str)
    y = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    
    # Create hover text
    hovertext = []
    for i, dow in enumerate(y):
        hovertext.append([])
        for j, week in enumerate(x):
            val = z[i][j] if j < len(z[i]) else None
            date = metric_by_day[(metric_by_day['dow'] == i) & 
                                (metric_by_day['week'].astype(str) == week)]
            if not date.empty:
                date_str = str(date.iloc[0]['date'])
                hovertext[i].append(
                    f"<b>{date_str}</b><br>{metric.capitalize()}: {val:,.0f}" 
                    if pd.notnull(val) else "No data"
                )
            else:
                hovertext[i].append("No data")
    
    fig = go.Figure(data=go.Heatmap(
        z=z,
        x=x,
        y=y,
        colorscale=colorscale,
        colorbar=dict(title=metric.capitalize(), len=0.7, thickness=20),
        hoverinfo='text',
        text=hovertext,
        showscale=True
    ))
    fig.update_layout(
        title=f'<b>{title}</b>',
        xaxis_title='Week of Year',
        yaxis_title='Day of Week',
        template='plotly_white',
        height=SMALL_CHART_HEIGHT,
        margin=dict(l=40, r=40, t=60, b=40)
    )
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(showgrid=False)
    return fig
