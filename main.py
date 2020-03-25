from csv_manager import CSV_Manager
from manipulator import Manipulator
import json

def filter_CSV(filter_field, value):
    reader = CSV_Manager("./articles.csv")
    articles = reader.get_csv_as_dicts()
    manipulator = Manipulator(articles)

    filtered = manipulator.filter_by(filter_field, value)
    return list(filtered)


print("Articles with a title of t4:")
print(filter_CSV("title", "t4"))
print('')
print("Articles of a1 author:")
print(filter_CSV("author", "a1"))
