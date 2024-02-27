import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller

# Step 1: Read the data from CSV files
cnepu_data = pd.read_excel("cnepu_daily_18_june_2022_updated.xlsx")
stock_399808_data = pd.read_csv("399808_1d.csv")
stock_000941_data = pd.read_csv("000941_1d.csv")
stock_399976_data = pd.read_csv("399976_1d.csv")

# Step 2: Divide the new sequences y(GP) and y(GF) into sub-sequences
def divide_sequences(sequence, n):
    N = len(sequence)
    Nn = int(N / n)
    sub_sequences = []
    for i in range(N - 1, Nn - 1, -1):
        sub_sequences.append(sequence[i-Nn:i])
    return sub_sequences

# Step 3: Define the lambda-th subsequence of length n
def calculate_cumulative_sum(sub_sequences):
    cumulative_sums = []
    for sub_sequence in sub_sequences:
        cumulative_sum = np.cumsum(sub_sequence)
        cumulative_sums.append(cumulative_sum)
    return cumulative_sums

# Step 4: Perform the Tucca forms analysis
def tucca_forms_analysis(data):
    print("Performing Tucca forms analysis...")
    # Placeholder code
    print("Tucca forms analysis results")

# Perform Tucca forms analysis for Cnepu data
tucca_forms_analysis(cnepu_data["CNEPU_Daily"])

# Step 5: Analyze the relationship between Cnepu and stocks 399808 and 000941 using MF-ADCCA
def mf_adcca_analysis(stock1_data, stock2_data, name1, name2):
    print(f"MF-ADCCA Analysis between {name1} and {name2}:")

# Analyze the relationship between Cnepu and stock 399808
try:
    mf_adcca_analysis(cnepu_data["CNEPU_Daily"], stock_399808_data["close"], "Cnepu", "Stock 399808")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_399808_data: {e}")
    print(f"Available columns in stock_399808_data: {stock_399808_data.columns}")

# Analyze the relationship between Cnepu and stock 000941
try:
    mf_adcca_analysis(cnepu_data["CNEPU_Daily"], stock_000941_data["close"], "Cnepu", "Stock 000941")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_000941_data: {e}")
    print(f"Available columns in stock_000941_data: {stock_000941_data.columns}")

# Add 399976 data to the analysis and analyze its relationship using MF-ADCCA
# Analyze the relationship between Cnepu and stock 399976
try:
    mf_adcca_analysis(cnepu_data["CNEPU_Daily"], stock_399976_data["close"], "Cnepu", "Stock 399976")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_399976_data: {e}")
    print(f"Available columns in stock_399976_data: {stock_399976_data.columns}")

# Step 6: Perform ADF analysis for stocks 399808, 000941, and 399976
def adf_analysis(data, name):
    try:
        result = adfuller(data)
        print(f"ADF Test Results for {name}:")
        print("Test Statistic:", result[0])
        print("p-value:", result[1])
        print("Critical Values:")
        for key, value in result[4].items():
            print(f"\t{key}: {value}")
    except Exception as e:
        print(f"Error occurred while performing ADF analysis for {name}: {e}")

# ADF analysis for stock 399808
try:
    adf_analysis(stock_399808_data["close"], "Stock 399808")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_399808_data: {e}")
    print(f"Available columns in stock_399808_data: {stock_399808_data.columns}")

# ADF analysis for stock 000941
try:
    adf_analysis(stock_000941_data["close"], "Stock 000941")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_000941_data: {e}")
    print(f"Available columns in stock_000941_data: {stock_000941_data.columns}")

# ADF analysis for stock 399976
try:
    adf_analysis(stock_399976_data["close"], "Stock 399976")
except KeyError as e:
    print(f"Error accessing 'close' column in stock_399976_data: {e}")
    print(f"Available columns in stock_399976_data: {stock_399976_data.columns}")


gold_spot_returns = np.random.rand(100)
gold_futures_returns = np.random.rand(100)

# Number of subsequences
n = 10

# Divide sequences into sub-sequences
sub_sequences_gold_spot = divide_sequences(gold_spot_returns, n)
sub_sequences_gold_futures = divide_sequences(gold_futures_returns, n)

# Calculate cumulative sum for each subsequence
cumulative_sum_gold_spot = calculate_cumulative_sum(sub_sequences_gold_spot)
cumulative_sum_gold_futures = calculate_cumulative_sum(sub_sequences_gold_futures)


print("Cumulative sum of gold spot sub-sequences:")
for i, cumulative_sum in enumerate(cumulative_sum_gold_spot):
    print(f"Sub-sequence {i+1}: {cumulative_sum}")

print("Cumulative sum of gold futures sub-sequences:")
for i, cumulative_sum in enumerate(cumulative_sum_gold_futures):
    print(f"Sub-sequence {i+1}: {cumulative_sum}")
