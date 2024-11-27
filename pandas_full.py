import pandas as pd

df = ''

# 1. Чтение данных из CSV-файла
def read_csv(file_path):
    global df
    #pd.set_option('display.max_columns', None)  # Максимально отображаемое число столбцов
    # для отображения всех столбцов
    pd.set_option('display.max_columns', None)

    # для отображения всех строк.
    pd.set_option('display.max_rows', None)

    # для увеличения ширины вывода, чтобы избежать переноса строк.
    pd.set_option('display.width', 1000)

    df = pd.read_csv(file_path)

    # Указываем нужные столбцы
    columns_to_show = ['country', 'price', 'province', 'region_1', 'variety', 'winery']
    print(df[columns_to_show].head(20))  # вывод первых 30 строк


# 2. Фильтрация данных
def filter_data(df):
    filtered_df = df[df['country'] == 'France']  # фильтруем по столбцу 'country'
    columns_to_show = ['country', 'price', 'province', 'region_1', 'variety', 'winery']
    print(filtered_df[columns_to_show].head(20))  # вывод первых 20 строк
    return filtered_df


# 3. Группировка и агрегация данных
def group_data(df):
    filtered_df = filter_data(df)
    grouped_df = filtered_df.groupby('variety')['price'].count()
    print(grouped_df.head(30))  # вывод первых 30 строк


# Пример вызова

read_csv('wine_reviews.csv')  # прочитать из CSV
filter_data(df)  # фильтрация
group_data(df)  # группировка
