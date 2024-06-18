import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Load the dataset
df = pd.read_csv("USvideos.csv")

# Display the first few rows, shape, and info of the dataframe
print(df.head())
print(df.shape)
print(df.info())

# Remove duplicate rows
df.drop_duplicates(inplace=True)
print(df.shape)

# Drop columns that are not essential for analysis
unessential_columns = ["thumbnail_link", "description"]
df.drop(unessential_columns, axis=1, inplace=True)
print(df.info())

# Display statistical summary
print(df.describe())

# Convert 'trending_date' to datetime format
df["trending_date"] = df["trending_date"].apply(lambda x: datetime.strptime(x, "%y.%d.%m"))

# Convert 'publish_time' to datetime format
df["publish_time"] = pd.to_datetime(df["publish_time"])
print(df.head(2))

# Add new columns for analysis based on 'publish_time'
df["publish_day"] = df["publish_time"].dt.day
df["publish_month"] = df["publish_time"].dt.month
df["publish_year"] = df["publish_time"].dt.year
df['publish_hour'] = df['publish_time'].dt.hour

# Total videos published per year
yearly_counts = df.groupby("publish_year")['video_id'].count()

# Plotting total videos published per year
plt.figure(figsize=(10, 6))
yearly_counts.plot(kind='bar', color='skyblue', edgecolor='black')
plt.xlabel("Year")
plt.ylabel("Total Publish Count")
plt.title("Total Videos Published per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Total views per year
yearly_views = df.groupby("publish_year")['views'].sum()

# Plotting total views per year
plt.figure(figsize=(10, 6))
yearly_views.plot(kind='bar', color='lightgreen', edgecolor='black')
plt.xlabel("Year")
plt.ylabel("Total Views")
plt.title("Total Views per Year")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Print unique category ids
print(sorted(df["category_id"].unique()))

# Mapping category ids to category names
category_mapping = {
    1: 'Film and Animation',
    2: 'Autos and Vehicles',
    10: 'Music',
    15: 'Pets and Animals',
    17: 'Sports',
    19: 'Travel and Events',
    20: 'Gaming',
    22: 'People and Blogs',
    23: 'Comedy',
    24: 'Entertainment',
    25: 'News and Politics',
    26: 'How to and Style',
    27: 'Education',
    28: 'Science and Technology',
    29: 'Non Profits and Activism',
    30: 'Movies',
    43: 'Shows'
}

# Add 'category_name' column to the dataframe
df['category_name'] = df['category_id'].map(category_mapping)

# Display the first few rows with the new 'category_name' column
print(df.head())

# Group by 'category_name' and sum the 'views'
categories_views = df.groupby("category_name")['views'].sum().reset_index()

# Sort and select the top 5 categories by total views
top_categories = categories_views.sort_values(by='views', ascending=False).head(5)

# Plotting the top 5 categories by total views
plt.figure(figsize=(12, 8))
sns.barplot(x='category_name', y='views', hue='category_name', data=top_categories, palette='viridis', dodge=False, edgecolor='black')
plt.xlabel("Category")
plt.ylabel("Total Views")
plt.title("Total Views by Top 5 Categories")
plt.legend([],[], frameon=False)  # Hide the legend
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# Plotting video count per category
plt.figure(figsize=(14, 8))
sns.countplot(x="category_name", hue='category_name', data=df, order=df['category_name'].value_counts().index, palette='coolwarm', dodge=False, edgecolor='black')
plt.xlabel("Category")
plt.ylabel("Video Count")
plt.title("Video Count by Category")
plt.legend([],[], frameon=False)  # Hide the legend
plt.xticks(rotation=20)
plt.tight_layout()
plt.show()

# Number of Videos Published per Hour
videos_per_hour = df['publish_hour'].value_counts().sort_index()

plt.figure(figsize=(12, 6))
sns.barplot(x=videos_per_hour.index, y=videos_per_hour.values, hue=videos_per_hour.index, palette='rocket', dodge=False, edgecolor='black')
plt.title('Number of Videos Published per Hour')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Videos')
plt.legend([],[], frameon=False)  # Hide the legend
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Creating a line plot for Videos Published Over Time
df['publish_date'] = df['publish_time'].dt.date
video_count_by_date = df.groupby('publish_date').size()

plt.figure(figsize=(12, 6))
sns.lineplot(data=video_count_by_date, color='blue')
plt.title("Videos Published Over Time")
plt.xlabel('Publish Date')
plt.ylabel('Number of Videos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Scatter plot between views and likes
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='views', y='likes', alpha=0.6, edgecolor=None)
plt.title('Views vs Likes')
plt.xlabel('Views')
plt.ylabel('Likes')
plt.tight_layout()
plt.show()

# Creating multiple subplots for different counts
plt.figure(figsize=(14, 8))
plt.subplots_adjust(wspace=0.4, hspace=0.4, top=0.9)

plt.subplot(2, 2, 1)
g = sns.countplot(x='comments_disabled', hue='comments_disabled', data=df, palette='Set2', dodge=False, edgecolor='black')
g.set_title("Comments Disabled", fontsize=16)
g.legend([],[], frameon=False)  # Hide the legend
g.set_xlabel("")

plt.subplot(2, 2, 2)
g1 = sns.countplot(x='ratings_disabled', hue='ratings_disabled', data=df, palette='Set2', dodge=False, edgecolor='black')
g1.set_title("Ratings Disabled", fontsize=16)
g1.legend([],[], frameon=False)  # Hide the legend
g1.set_xlabel("")

plt.subplot(2, 2, 3)
g2 = sns.countplot(x='video_error_or_removed', hue='video_error_or_removed', data=df, palette='Set2', dodge=False, edgecolor='black')
g2.set_title("Video Error or Removed", fontsize=16)
g2.legend([],[], frameon=False)  # Hide the legend
g2.set_xlabel("")

plt.tight_layout()
plt.show()

corr_matrix=df['views'].corr(df['likes'])
print(corr_matrix)