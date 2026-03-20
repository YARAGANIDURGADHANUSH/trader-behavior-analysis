import os
import matplotlib.pyplot as plt
import seaborn as sns
from src.data_loader import load_and_merge_data
from src.analysis_engine import calculate_insights, get_top_performing_phase

def main():
    # Pointing exactly to the files you uploaded (with the .zip extension)
    SENTIMENT_FILE = "data/fear_greed_index.csv"
    TRADER_FILE = "data/historical_data.zip"

    print("--- Starting Trader Behavior Insights Analysis ---")

    if not os.path.exists(SENTIMENT_FILE) or not os.path.exists(TRADER_FILE):
        print(f"Error: Please ensure {SENTIMENT_FILE} and {TRADER_FILE} are in the 'data/' folder.")
        return

    # 1. Load and Merge
    df = load_and_merge_data(SENTIMENT_FILE, TRADER_FILE)
    print(f"Data Successfully Merged: {len(df)} records found.")

    # 2. Run Analysis (Using Size USD instead of leverage)
    pnl_stats, size_stats = calculate_insights(df)
    top_phase = get_top_performing_phase(df)

    # 3. Print Results
    print("\nAverage PnL per Sentiment Phase:")
    print(pnl_stats)
    print(f"\nKey Finding: Traders show highest performance during '{top_phase}' periods.")

    # 4. Generate Visualization
    plt.figure(figsize=(10, 6))
    sns.barplot(x=pnl_stats.index, y=pnl_stats.values, palette="mako")
    plt.title("Trader Performance (PnL) vs. Bitcoin Market Sentiment")
    plt.ylabel("Average Closed PnL (USD)")
    plt.xlabel("Sentiment Classification")
    
    os.makedirs("outputs", exist_ok=True)
    plt.savefig("outputs/sentiment_pnl_chart.png")
    print("\nAnalysis complete. Visualization saved to 'outputs/sentiment_pnl_chart.png'.")

if __name__ == "__main__":
    main()
