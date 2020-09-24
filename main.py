from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)

def count_articles(key, value):
    count = 0
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    for i in articles:
        if i[key] == value:
            count = count+1
    return count

def is_article(key, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    for i in articles:
        if i[key] == value:
            return True
    return False

def longest_article(key, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    longest = articles[1]
    for i in articles:
        if i[key] == value:
            if i['pages'] > longest['pages']:
                longest = i
    return longest

def edit_data():
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    new_data = {}
    for i in articles:
        if i['author'] not in new_data:
            new_data[i['author']] = []
        new_data[i['author']].append({i['title'], i['date'], i['category'], i['pages']})
        if i['category'] not in new_data:
            new_data[i['category']] = []
        new_data[i['category']].append({i['title'], i['date'], i['author'], i['pages']})
    print(new_data)

# print("Articles with a title of t4:")
# print(filter_CSV("title", "t4"))
# print('')
# print("Articles of a1 author:")
# print(filter_CSV("author", "a1"))
# print(count_articles('title', 't4'))
# print(count_articles('author', 'a1'))
# print(is_article('title', 't4'))
# print(is_article('author', 'a0'))
# print(longest_article('author', 'a1'))
edit_data()

