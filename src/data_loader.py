import pandas as pd

def load_and_merge_data(sentiment_path, trader_path):
    """Loads CSVs and synchronizes dates for analysis."""
    # Load Bitcoin Market Sentiment Dataset [cite: 77]
    sentiment_df = pd.read_csv(sentiment_path)
    # Load Historical Trader Data [cite: 79]
    trader_df = pd.read_csv(trader_path)

    # Convert to datetime and normalize to daily (sentiment is usually daily)
    sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date']).dt.date
    
    # trader_df 'time' is usually in milliseconds [cite: 80]
    trader_df['time'] = pd.to_datetime(trader_df['time'], unit='ms')
    trader_df['Date'] = trader_df['time'].dt.date

    # Merge on common Date column 
    merged_df = pd.merge(trader_df, sentiment_df, on='Date', how='inner')
    return merged_df
