import os
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_and_merge_data
from src.analysis_engine import calculate_insights, get_top_performing_phase

def main():
    # File paths (Assuming they are in the 'data/' folder)
    SENTIMENT_FILE = "data/bitcoin_sentiment.csv"
    TRADER_FILE = "data/hyperliquid_data.csv"

    print("--- Starting Trader Behavior Insights Analysis ---")

    if not os.path.exists(SENTIMENT_FILE) or not os.path.exists(TRADER_FILE):
        print("Error: Please place your CSV files in the 'data/' folder.")
        return

    # 1. Load and Merge
    df = load_and_merge_data(SENTIMENT_FILE, TRADER_FILE)
    print(f"Data Merged: {len(df)} records found matching sentiment dates.")

    # 2. Run Analysis
    pnl_stats, lev_stats = calculate_insights(df)
    top_phase = get_top_performing_phase(df)

    # 3. Print Text Insights
    print("\n[INSIGHT] Average PnL by Sentiment:")
    print(pnl_stats)
    print(f"\n[RESULT] Traders are most profitable during: {top_phase}")

    # 4. Generate Visualization 
    plt.figure(figsize=(10, 6))
    sns.barplot(x=pnl_stats.index, y=pnl_stats.values, palette="viridis")
    plt.title("Trader Performance vs Market Sentiment")
    plt.ylabel("Average Closed PnL")
    plt.xlabel("Sentiment (Fear/Greed Index)")
    
    # Ensure 'outputs/' directory exists
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/performance_chart.png")
    print("\n[SUCCESS] Analysis complete. Chart saved to 'outputs/performance_chart.png'.")

if __name__ == "__main__":
    main()
