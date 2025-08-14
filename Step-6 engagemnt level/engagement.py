import pandas as pd

# Step 1: Load the CSV
df = pd.read_csv("Step-2.csv")

# Step 2: Clean & filter columns (optional, based on your structure)
df = df[['Engagement_Level', 'Likes', 'Shares', 'Comments', 'Views']]

# Step 3: Group by Engagement_Level and calculate average metrics
summary = df.groupby('Engagement_Level').agg({
    'Likes': 'mean',
    'Shares': 'mean',
    'Comments': 'mean',
    'Views': 'mean'
}).reset_index()

# Step 4: Add total number of posts per level
summary['Post_Count'] = df['Engagement_Level'].value_counts().reindex(summary['Engagement_Level']).values

# Step 5: Round the numbers for clean visuals
summary = summary.round(2)

# Step 6: Export to CSV
summary.to_csv("engagement_level_summary.csv", index=False)

# Preview the result
print(summary)
