📊 Trader Behavior Insights: Market Sentiment Analysis
A fully automated data science pipeline that analyzes the relationship between Bitcoin Market Sentiment and actual trader performance using high-frequency execution data from Hyperliquid.

🚀 Project Overview
This project implements an analytical workflow using Python and Pandas that performs:

Extraction of large-scale, compressed Hyperliquid trader execution data

Synchronization with daily Bitcoin Fear/Greed Index data

Datetime normalization and DataFrame merging

Calculation of trader profitability (PnL) across different market phases

Analysis of risk appetite (Size USD) based on market sentiment

Automated data visualization generation

The entire pipeline runs programmatically from raw data → merged datasets → statistical insights → final visualization.

⚙️ Data Pipeline Architecture
Data Extraction & Zipped Loading → Datetime Normalization → DataFrame Merging → Aggregation & Metric Calculation → Insight Generation → Data Visualization

🧠 Tech Stack
Python 3.x – Core programming language

Pandas – Data manipulation, synchronization, and aggregation

Seaborn & Matplotlib – Data visualization and statistical graphics

Jupyter Notebook – Interactive exploratory data analysis

📊 Visual Insights
Watch the generated data visualization output:
outputs/sentiment_pnl_chart.png (Automatically generated upon running the pipeline)

📁 Repository Contents
data/hyperliquid_data.zip — Compressed historical trader execution data

data/bitcoin_sentiment.csv — Daily market sentiment classifications

notebooks/exploration.ipynb — Jupyter notebook containing EDA

src/ — Modularized core analytical logic and data loading functions

main.py — Main execution script

requirements.txt — Python dependencies

.gitignore — Git ignore rules

🔐 Environment Setup
Note on Data Handling: To adhere to standard version control practices, the large Hyperliquid dataset has been compressed. The Python script reads the data directly from the .zip archive on the fly. No manual extraction is required.

Clone the repository and navigate to the project directory:

Bash
git clone https://github.com/YARAGANIDURGADHANUSH/trader-behavior-analysis.git
cd trader-behavior-analysis
Install the required dependencies:

Bash
pip install -r requirements.txt
Execute the analysis pipeline:

Bash
python main.py
🔄 Key Findings
The workflow automatically uncovers that traders achieved their highest average profitability (Avg ~$87 PnL) during standard "Greed" market phases, but performance dropped significantly during "Extreme Greed" phases (Avg ~$25 PnL), indicating potential over-leveraging or poor risk management at market tops.

👨‍💻 Author
Durga Dhanush Yaragani
