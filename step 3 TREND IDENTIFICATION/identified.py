# Step 4: Exploratory Data Analysis (Trend Identification)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("Step-2.csv")  # Replace with your actual file name

# 2. Basic inspection
print("Dataset info:")
print(df.info())
print("\nSample rows:")
print(df.head())

# 3. Clean and preprocess
df['Post_Date'] = pd.to_datetime(df['Post_Date'])
df.dropna(subset=['Hashtag', 'Likes', 'Views', 'Shares'], inplace=True)

# 4. Identify Top 10 Hashtags by Total Likes
top_hashtags = (
    df.groupby('Hashtag')['Likes']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print("\nTop 10 Hashtags by Likes:\n", top_hashtags)

# 5. Visualize Trends Over Time for Top Hashtags
top_tags = top_hashtags.index.tolist()

plt.figure(figsize=(12, 6))
for tag in top_tags:
    tag_df = df[df['Hashtag'] == tag]
    tag_df = tag_df.groupby('Post_Date')['Likes'].sum().reset_index()
    plt.plot(tag_df['Post_Date'], tag_df['Likes'], label=tag)

plt.title("Trending Hashtags Over Time (by Likes)")
plt.xlabel("Date")
plt.ylabel("Likes")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. Platform-Wise Hashtag Likes
platform_summary = df.groupby(['Platform', 'Hashtag'])['Likes'].sum().reset_index()
print("\nTop Platform-Hashtag Combinations:\n", platform_summary.sort_values(by='Likes', ascending=False).head(10))

# 7. Content Type vs Likes
content_summary = df.groupby('Content_Type')['Likes'].mean().sort_values(ascending=False)
print("\nAverage Likes by Content Type:\n", content_summary)

# 8. Region-Wise Total Likes
region_summary = df.groupby('Region')['Likes'].sum().sort_values(ascending=False)
print("\nTotal Likes by Region:\n", region_summary)

# 9. Export Aggregated Hashtag Data for Power BI (Optional)
export_df = df.groupby(['Post_Date', 'Hashtag'])[['Likes', 'Views', 'Shares']].sum().reset_index()
export_df.to_csv("eda_output_for_powerbi.csv", index=False)
print("\nExported summary data to 'eda_output_for_powerbi.csv'")
