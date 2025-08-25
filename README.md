# Netflix-Data-Analysis-Project-
## 📌 Описание проекта
Этот проект представляет собой анализ датасета Netflix с целью выявления интересных закономерностей, таких как:
- Распределение контента по типам (фильмы или сериалы)
- Популярные актеры
- Наиболее часто встречающиеся жанры
- Анализ рейтингов
- Топовые годы по выпуску контента

Проект выполнен на Python с использованием библиотек:
- Pandas (обработка данных)
- Seaborn и Matplotlib (визуализация)
- Python scripts

## 🛠 Технологии
- Python 3.10+
- Pandas
- Seaborn
- Matplotlib

## 📂 Структура проекта
```bash
Netflix-Analysis/
│
├── Data/
│   ├── Processed/
│   │   └── cleaned_netflix_titles.csv  # очищенный датасет
│   └── Raw/
│       └── netflix_titles.csv          # очищенный датасет
│
├── Process/
│   ├── data_preprocessing.py     # Загрузка и предобработка данных
│   ├── data_basic_analysis.py    # Базовый анализ (типы контента, топ жанры, рейтинги)
│   ├── data_advanced_analysis.py # Продвинутый анализ (топ актеров, годовые тренды)
│   └── data_visualization.py     # Построение графиков
│
├── Reports/
│   ├── Figures                   # Графики 
│   ├── Report.pdf                
│   └── Report_eng.pdf
│
├── README.md
├── README_eng.md                 
└── requirements.txt             
```

## 🚀 Запуск проекта 
1. Установка
```bash
pip install pandas
pip install seaborn
pip install matplotlib
```
2. Запуск
```bash
data_visualizations.py
```

## 📊 Визуализации
 - Гистограмма распределения по рейтингам
 - Диаграмма количества фильмов и сериалов
 - Топ-5 жанров (pie chart)
 - Топ-10 актеров (barplot)
 - Топ-10 продюссеров (barplot)
 - Топ-10 стран по выпущенному контенту (barplot)
 - Распределение фильмов по длительности (histplot)

## 📌 Источник данных
Netflix Titles Dataset on Kaggle (https://www.kaggle.com/shivamb/netflix-shows)
## ✨ Автор
Александр | Дата-Аналитик (в процессе обучения)
 
