import seaborn as sns
import matplotlib.pyplot as plt
from data_basic_analysis import analyze_basic
from data_advanced_analysis import analyze_advanced

df_count_type, max_year, df_most_released, max_content, max_content_year, top10c, rate_count = analyze_basic()
df_director, df_actor, top5_genres, mean_time, mean_season, times_movie, actors, directors = analyze_advanced()

sns.set_theme(style='whitegrid', palette='rocket')

# 1.  Number of films and TV series
ax = sns.barplot(data=df_count_type, x='Category', y='Count', palette='magma')
for container in ax.containers:
    ax.bar_label(container)
plt.xlabel('Category')
plt.ylabel('Count')
plt.title('Count of Movies and TV Shows')
plt.show()


# 2.  Top 10 countries in terms of the amount of content
ax = sns.barplot(data=top10c, x='Country', y='Count', palette='magma')
for container in ax.containers:
    ax.bar_label(container)
plt.xlabel('Country')
plt.ylabel('Count')
plt.title('TOP 10 countries by count of content')
plt.show()


# 3.  Distribution by rating
ax = sns.barplot(data=rate_count, x='Rating', y='Count', palette='rocket')
for container in ax.containers:
    ax.bar_label(container)
plt.xlabel('Ratings')
plt.ylabel('Count')
plt.title('TOP of age-ratings')
plt.show()


# 4.  Duration of films
sns.histplot(data=times_movie['duration_value'],
             bins=30,
             kde=True,
             color=sns.color_palette('rocket')[1],
             label='Movies'
)
plt.xlabel('Timing')
plt.ylabel('Count')
plt.title('Duration of films')
plt.legend()
plt.show()


# 5.  Directors and actors
# Actors
ax = sns.barplot(data=actors, x='Count', y='Actor', palette='rocket')
for container in ax.containers:
    ax.bar_label(container)
plt.title('TOP-10 Popular actors')
plt.xlabel('Count of mentions')
plt.ylabel("Actor's name")
plt.show()

# Directors
ax = sns.barplot(data=directors, x='Count', y='Director', palette='rocket')
for container in ax.containers:
    ax.bar_label(container)
plt.title('TOP-10 Popular directors')
plt.xlabel('Count of mentions')
plt.ylabel("Director's name")
plt.show()


# 6.  Popular genres
wedges, texts, autotexts = plt.pie(
    top5_genres['Count'],
    labels=top5_genres['Genre'],
    autopct='%1.1f%%',
    startangle=140,
    colors=sns.color_palette('rocket'),
    textprops={'fontsize': 12}
)

for autotext in autotexts: #White percentages inside the circle
    autotext.set_color('white')
    autotext.set_weight('bold')

plt.legend(
    wedges,
    top5_genres['Genre'],
    title='Genres',
    loc='upper right'

)

plt.axis('equal')
plt.show()

