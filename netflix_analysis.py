import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================
# Question 1 - Load Dataset
# ==========================
df = pd.read_csv("netflix_titles.csv")

# ==========================
# Question 2 - Display First 10 Records
# ==========================
print("First 10 Records:")
print(df.head(10))

# ==========================
# Question 3 - Dataset Information
# ==========================
print("\nShape of Dataset:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

# ==========================
# Question 4 - Missing Values
# ==========================
print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Question 5 - Remove Duplicate Records
# ==========================
print("\nDuplicate Rows Before Removing:")
print(df.duplicated().sum())

df = df.drop_duplicates()

print("\nDuplicate Rows After Removing:")
print(df.duplicated().sum())

# ==========================
# Question 6 - Fill Missing Values
# ==========================
df["Director"] = df["Director"].fillna("Unknown")
df["Country"] = df["Country"].fillna("Unknown")

print("\nMissing Values After Filling:")
print(df[["Director", "Country"]].isnull().sum())


# ==========================
# Question 7 - Convert Date_Added to Date Format
# ==========================
df["Date_Added"] = pd.to_datetime(df["Date_Added"], errors="coerce")

print("\nData Type of Date_Added:")
print(df["Date_Added"].dtype)


# ==========================
# Question 8 - Extract Year and Month
# ==========================
df["Year_Added"] = df["Date_Added"].dt.year
df["Month_Added"] = df["Date_Added"].dt.month_name()

print("\nYear and Month Added:")
print(df[["Date_Added", "Year_Added", "Month_Added"]].head())


# ==========================
# Question 9 - Rename Column Names
# ==========================
df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")

print("\nUpdated Column Names:")
print(df.columns)


# ==========================
# Question 10 - Save Cleaned Dataset
# ==========================
df.to_csv("cleaned_netflix_data.csv", index=False)

# ==========================
# Question 11 - Total Number of Netflix Titles
# ==========================
print("\nTotal Number of Netflix Titles:")
print(len(df))


# ==========================
# Question 12 - Count Movies and TV Shows
# ==========================
print("\nMovies and TV Shows Count:")
print(df["type"].value_counts())


# ==========================
# Question 13 - Oldest and Newest Release Year
# ==========================
print("\nOldest Release Year:")
print(df["release_year"].min())

print("\nNewest Release Year:")
print(df["release_year"].max())


# ==========================
# Question 14 - Average Release Year
# ==========================
print("\nAverage Release Year:")
print(df["release_year"].mean())


# ==========================
# Question 15 - Count Content by Rating
# ==========================
print("\nContent by Rating:")
print(df["rating"].value_counts())

# ==========================
# Question 16 - Top 10 Genres
# ==========================
print("\nTop 10 Genres:")
print(df["genre"].value_counts().head(10))


# ==========================
# Question 17 - Top 10 Countries
# ==========================
print("\nTop 10 Countries:")
print(df["country"].value_counts().head(10))


# ==========================
# Question 18 - Top 10 Directors
# ==========================
print("\nTop 10 Directors:")
print(df["director"].value_counts().head(10))


# ==========================
# Question 19 - Year with Highest Releases
# ==========================
print("\nYear with Highest Releases:")
print(df["release_year"].value_counts().idxmax())


# ==========================
# Question 20 - Month with Highest Content Added
# ==========================
print("\nMonth with Highest Content Added:")
print(df["month_added"].value_counts().idxmax())

# ==========================
# Question 21 - Movies Released After 2020
# ==========================
print("\nMovies Released After 2020:")
movies_after_2020 = df[(df["type"] == "Movie") & (df["release_year"] > 2020)]
print(movies_after_2020[["title", "release_year"]])


# ==========================
# Question 22 - TV Shows with More Than 3 Seasons
# ==========================
print("\nTV Shows with More Than 3 Seasons:")

tv_shows = df[df["type"] == "TV Show"].copy()
tv_shows["season_count"] = tv_shows["duration"].str.extract("(\d+)").astype(int)

tv_shows = tv_shows[tv_shows["season_count"] > 3]

print(tv_shows[["title", "duration"]])


# ==========================
# Question 23 - Content Released in India
# ==========================
print("\nContent Released in India:")
india_content = df[df["country"] == "India"]
print(india_content[["title", "country"]])


# ==========================
# Question 24 - Content Directed by A. Kumar
# ==========================
print("\nContent Directed by A. Kumar:")
director_content = df[df["director"] == "A. Kumar"]
print(director_content[["title", "director"]])


# ==========================
# Question 25 - Titles Containing 'Love'
# ==========================
print("\nTitles Containing 'Love':")

love_titles = df[df["title"].str.contains("Love", case=False, na=False)]

print(love_titles[["title"]])

# ==========================
# Question 26 - Count Movies and TV Shows Year-wise
# ==========================
print("\nMovies and TV Shows Year-wise:")
print(df.groupby(["release_year", "type"]).size())


# ==========================
# Question 27 - Most Common Content Rating
# ==========================
print("\nMost Common Content Rating:")
print(df["rating"].mode()[0])


# ==========================
# Question 28 - Longest Movie
# ==========================
print("\nLongest Movie:")

movies = df[df["type"] == "Movie"].copy()

movies["movie_duration"] = movies["duration"].str.extract("(\d+)").astype(int)

longest_movie = movies.loc[movies["movie_duration"].idxmax()]

print(longest_movie[["title", "duration"]])


# ==========================
# Question 29 - Shortest Movie
# ==========================
print("\nShortest Movie:")

shortest_movie = movies.loc[movies["movie_duration"].idxmin()]

print(shortest_movie[["title", "duration"]])


# ==========================
# Question 30 - Top 10 Latest Releases
# ==========================
print("\nTop 10 Latest Releases:")

latest_releases = df.sort_values(by="release_year", ascending=False)

print(latest_releases[["title", "release_year"]].head(10))

# ==========================
# Question 31 - Oldest 10 Titles
# ==========================
print("\nOldest 10 Titles:")

oldest_titles = df.sort_values(by="release_year", ascending=True)

print(oldest_titles[["title", "release_year"]].head(10))


# ==========================
# Question 32 - Genre-wise Content Count
# ==========================
print("\nGenre-wise Content Count:")

print(df.groupby("genre").size())


# ==========================
# Question 33 - Country-wise Average Release Year
# ==========================
print("\nCountry-wise Average Release Year:")

print(df.groupby("country")["release_year"].mean())


# ==========================
# Question 34 - Number of Unique Directors
# ==========================
print("\nNumber of Unique Directors:")

print(df["director"].nunique())


# ==========================
# Question 35 - Number of Unique Genres
# ==========================
print("\nNumber of Unique Genres:")

print(df["genre"].nunique())

# ==========================
# Question 36 - Pie Chart (Movies vs TV Shows)
# ==========================

type_count = df["type"].value_counts()

plt.figure(figsize=(6, 6))
plt.pie(
    type_count,
    labels=type_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Movies vs TV Shows")
plt.tight_layout()
plt.savefig("Charts/movie_vs_tvshow.png")
plt.show()
plt.close()


# ==========================
# Question 37 - Top 10 Genres (Bar Chart)
# ==========================

top_genres = df["genre"].value_counts().head(10)

plt.figure(figsize=(8, 5))
plt.bar(top_genres.index, top_genres.values)

plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/top_genres.png")
plt.show()
plt.close()


# ==========================
# Question 38 - Top 10 Countries (Bar Chart)
# ==========================

top_countries = df["country"].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_countries.index, top_countries.values)

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/top_countries.png")
plt.show()
plt.close()


# ==========================
# Question 39 - Release Year Histogram
# ==========================

plt.figure(figsize=(8, 5))
plt.hist(df["release_year"], bins=10)

plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("Charts/release_year_histogram.png")
plt.show()
plt.close()


# ==========================
# Question 40 - Ratings Count Plot
# ==========================

plt.figure(figsize=(8, 5))

sns.countplot(data=df, x="rating")

plt.title("Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/ratings_count.png")
plt.show()
plt.close()

# ==========================
# Question 41 - Top 10 Directors (Horizontal Bar Chart)
# ==========================

top_directors = df["director"].value_counts().head(10)

plt.figure(figsize=(8,5))
plt.barh(top_directors.index, top_directors.values)

plt.title("Top 10 Directors")
plt.xlabel("Number of Titles")
plt.ylabel("Director")

plt.tight_layout()
plt.savefig("Charts/top_directors.png")
plt.show()
plt.close()


# ==========================
# Question 42 - Releases by Year (Line Chart)
# ==========================

year_count = df["release_year"].value_counts().sort_index()

plt.figure(figsize=(10,5))
plt.plot(year_count.index, year_count.values, marker="o")

plt.title("Netflix Releases by Year")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")

plt.tight_layout()
plt.savefig("Charts/releases_by_year.png")
plt.show()
plt.close()


# ==========================
# Question 43 - Movie Duration Box Plot
# ==========================

movies = df[df["type"] == "Movie"].copy()
movies["movie_duration"] = movies["duration"].str.extract("(\d+)").astype(int)

plt.figure(figsize=(6,5))
plt.boxplot(movies["movie_duration"])

plt.title("Movie Duration Distribution")
plt.ylabel("Duration (Minutes)")

plt.tight_layout()
plt.savefig("Charts/movie_duration_boxplot.png")
plt.show()
plt.close()


# ==========================
# Question 44 - Correlation Heatmap
# ==========================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(6,4))
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("Charts/correlation_heatmap.png")
plt.show()
plt.close()


# ==========================
# Question 45 - Save Cleaned Dataset
# ==========================

df.to_csv("output/cleaned_netflix_data.csv", index=False)

print("\nCleaned Dataset Saved Successfully!")

print("\n========================================")
print(" Netflix Analytics Project Completed ")
print("========================================")