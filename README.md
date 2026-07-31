# Netflix Analytics Project

## Project Overview
This project analyzes the Netflix Titles dataset using Python. It includes data cleaning, exploratory data analysis (EDA), and data visualization to gain insights into Netflix content.

## Tools & Libraries
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Dataset
- Dataset Name: netflix_titles.csv
- Total Records: 100+
- File Format: CSV

## Project Features
- Data Cleaning
- Missing Value Handling
- Duplicate Removal
- Date Conversion
- Feature Extraction
- Exploratory Data Analysis
- Statistical Analysis
- Data Visualization
- Export Cleaned Dataset

## Charts Generated
- Movies vs TV Shows
- Top Genres
- Top Countries
- Top Directors
- Ratings Count
- Release Year Distribution
- Releases by Year
- Movie Duration Boxplot
- Correlation Heatmap

## Project Structure

```text
Netflix_Analytics_Project/
│
├── Charts/
│   ├── correlation_heatmap.png
│   ├── movie_duration_boxplot.png
│   ├── movie_vs_tvshow.png
│   ├── ratings_count.png
│   ├── release_year_histogram.png
│   ├── releases_by_year.png
│   ├── top_countries.png
│   ├── top_directors.png
│   └── top_genres.png
│
├── output/
│   └── cleaned_netflix_data.csv
│
├── netflix_analysis.py
├── netflix_titles.csv
├── requirements.txt
└── README.md
```

## How to Run

1. Install dependencies

```bash
pip install -r requirements.txt
```

2. Run the project

```bash
python netflix_analysis.py
```

## Output
- Cleaned dataset saved in output folder.
- Charts saved in Charts folder.

## Conclusion
This project demonstrates data cleaning, exploratory data analysis, and visualization skills using Python and popular data analysis libraries.