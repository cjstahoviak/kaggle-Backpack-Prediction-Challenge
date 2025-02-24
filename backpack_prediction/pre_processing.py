import pandas as pd

# Load the train dataset
train_df = pd.read_csv('./data/raw/train.csv')

# Display the first few rows of the dataframe
print(train_df.head())
print()

## CREATE DROPPED DATASET ##
train_df_dropped = train_df.dropna()
remaining_percentage = (train_df_dropped.shape[0] / train_df.shape[0]) * 100
print(f"Dropped dataset created. {train_df_dropped.shape[0]}/{train_df.shape[0]} instances remaining ({remaining_percentage:.2f}%)")
train_df_dropped.to_csv('./data/processed/train_dropped.csv', index=False)
