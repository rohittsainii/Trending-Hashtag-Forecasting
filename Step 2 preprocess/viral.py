import pandas as pd

# Load original data
df1 = pd.read_csv("Cleaned_Viral_Social_Media_Trends.csv")

# Preprocessing
df1['Post_Date'] = pd.to_datetime(df1['Post_Date'])
numeric_cols = ['Views', 'Likes', 'Shares', 'Comments']
df1[numeric_cols] = df1[numeric_cols].apply(pd.to_numeric, errors='coerce')
df1.dropna(subset=numeric_cols, inplace=True)
df1.drop_duplicates(inplace=True)
df1.dropna(inplace=True)
df1['Hashtag'] = df1['Hashtag'].str.strip().str.lower()
df1['Platform'] = df1['Platform'].str.strip().str.title()

#Save file
df1.to_csv("Step-2.csv", index=False)






