import pandas as pd

def calculate_insights(df):
    """Calculates key metrics like PnL and Position Size per sentiment phase."""
    # Use exact 'classification' and 'Closed PnL' columns
    pnl_summary = df.groupby('classification')['Closed PnL'].mean().sort_values()
    
    # Use 'Size USD' to show risk appetite
    size_summary = df.groupby('classification')['Size USD'].mean()
    
    return pnl_summary, size_summary

def get_top_performing_phase(df):
    """Identifies which sentiment phase yields the highest trader PnL."""
    return df.groupby('classification')['Closed PnL'].mean().idxmax()