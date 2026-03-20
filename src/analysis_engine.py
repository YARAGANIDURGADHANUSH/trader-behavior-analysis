import pandas as pd

def calculate_insights(df):
    """Calculates key metrics like PnL and leverage per sentiment phase."""
    # Calculate average PnL per sentiment category [cite: 78, 81]
    pnl_summary = df.groupby('Classification')['closedPnL'].mean().sort_values()
    
    # Calculate average leverage per sentiment category [cite: 81]
    leverage_summary = df.groupby('Classification')['leverage'].mean()
    
    return pnl_summary, leverage_summary

def get_top_performing_phase(df):
    """Identifies which sentiment phase yields the highest trader PnL."""
    return df.groupby('Classification')['closedPnL'].mean().idxmax()
