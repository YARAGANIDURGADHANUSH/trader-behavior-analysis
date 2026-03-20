import pandas as pd

def load_and_merge_data(sentiment_path, trader_path):
    """Loads CSV/ZIP files and synchronizes dates for analysis."""
    sentiment_df = pd.read_csv(sentiment_path)
    trader_df = pd.read_csv(trader_path)

    # Use the exact lowercase 'date' column from sentiment data
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['date']).dt.date
    
    # Use the exact 'Timestamp' column from trader data
    trader_df['Date'] = pd.to_datetime(trader_df['Timestamp'], unit='ms').dt.date

    # Merge on the newly created 'Date' column
    merged_df = pd.merge(trader_df, sentiment_df, on='Date', how='inner')
    return merged_df