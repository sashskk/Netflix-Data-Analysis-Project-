# Netflix-Data-Analysis-Project-
## 📌 Project Description
This project focuses on analyzing a Netflix dataset to identify interesting patterns, such as:
- Distribution of content by type (movies or TV shows)
- Popular actors
- Most frequent genres
- Ratings analysis
- Top years by content release

The project is implemented in Python using the following libraries:
- Pandas (data processing)
- Seaborn and Matplotlib (visualization)
- Python scripts

## 🛠 Technologies
- Python 3.10+
- Pandas
- Seaborn
- Matplotlib

## 📂 Project Structure
```bash
Netflix-Analysis/
│
├── Data/
│   ├── Processed/
│   │   └── cleaned_netflix_titles.csv  # cleaned dataset
│   └── Raw/
│       └── netflix_titles.csv          # raw dataset
│
├── Process/
│   ├── data_preprocessing.py     # Data loading and preprocessing
│   ├── data_basic_analysis.py    # Basic analysis (content types, top genres, ratings)
│   ├── data_advanced_analysis.py # Advanced analysis (top actors, yearly trends)
│   └── data_visualization.py     # Plot generation
│
├── Reports/
│   ├── Figures                   # Charts
│   ├── Report.pdf                
│   └── Report_eng.pdf
│
├── README.md
├── README_eng.md                 
└── requirements.txt             
```

## 🚀 Running the Project
1. Installation
```bash
pip install pandas
pip install seaborn
pip install matplotlib
```
2. Run
```bash
data_visualizations.py
```

## 📊 Visualizations
 - Histogram of ratings distribution
 - Bar chart of movies vs TV shows
 - Top-5 genres (pie chart)
 - Top-10 actors (bar plot)
 - Top-10 producers (bar plot)
 - Top-10 countries by released content (bar plot)
 - Movie duration distribution (histogram)

## 📌 Data Source
Netflix Titles Dataset on Kaggle (https://www.kaggle.com/shivamb/netflix-shows)
## ✨ Author
Alexander | Data Analyst (in training)
 
