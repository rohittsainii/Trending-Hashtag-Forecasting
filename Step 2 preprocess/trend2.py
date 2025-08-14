import pandas as pd

# Load your cleaned hashtag data
df = pd.read_csv("cleaned_hashtag_trends.csv")

# Define related hashtag groups (you can expand this)
hashtag_groups = {
    'ai': ['ai', 'chatgpt', 'machinelearning', 'deeplearning', 'artificialintelligence'],
    'fitness': ['fitness', 'workout', 'gym', 'fitlife'],
    'dance': ['dance', 'dancer', 'dancing', 'hiphop', 'choreography'],
    'fashion': ['fashion', 'ootd', 'style', 'trendy'],
    'food': ['foodie', 'food', 'cooking', 'yum', 'recipes'],
}

# Create an empty list to store grouped DataFrames
grouped_rows = []

# Go through each topic group and extract matching rows
for keywords in hashtag_groups.values():
    pattern = '|'.join(keywords)
    matches = df[df['hashtag'].str.contains(pattern, case=False, na=False)]
    grouped_rows.append(matches)

# Concatenate all groups into a single DataFrame
final_df = pd.concat(grouped_rows).drop_duplicates()

# Save the grouped data into one CSV
final_df.to_csv("grouped_hashtag_trends.csv", index=False)

print("Done! Saved all related hashtags in one file: grouped_hashtag_trends.csv")





