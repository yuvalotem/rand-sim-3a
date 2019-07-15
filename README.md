# Running/Environment

- Make sure you **fork** this repository to your own Github, then clone it to your computer
- You will have to download + install Python on your machine 
    - If you have a Mac, use `brew`, otherwise good luck =]
    - After your install is complete, close then open your VSCode/terminal again
    - You can check that the installation worked by typing `python` in the command line/terminal - this should start an interactive Python runtime (like typing `node` in the command line)
- From the project root directory, run `python main.py` to execute the script

# Features

This Python script executes a simple task:
- Read a CSV file (like Excel, but just data; no formatting)
    - The file is `articles.csv`; it has four columns: `title`, `date`, `category`, and `author`
    - Each row has data about one article; `t1` stands for "title1", `a1` for "author1" etc
- Store the data in a list (array) of dicts (in Python, _objects_ are called _dicts_, short for _dictionary_)
- Filter the data based on some input

# To Do
- Add a new method to `CSV_Manager` that reads the CSV and stores it as a single object that maps each author to his/her articles, and each category to all the articles with that category. Ultimately, your data should look like this:
```
    {
        author1_name: [{data on article1 by author1}, {data on article2 by author1}, {etc}],
        author2_name: [{data on article1 by author2}, {data on article2 by author2}, {etc}],
        etc,
        category1_name: [{data on article1 in category1}, {data on article2 in category1}, {etc}],
        category2_name: [{data on article1 in category2}, {data on article2 in category2}, {etc}],
        etc
    }
```
- Update the `run` function in `main` to handle either the old version or new version of the data
    - For instance, running `run('author', 'author2')` should work, and running `run('author2')` should also work and return the same data
    - In other words, you should add another method to `Manipulator` that can extract the relevant data from your new object in O(1), given either the author name or category name
    - In `main`, you need to add some code that handles both your new method in `Manipulator`, and the original `find_by` method

# Extra
- Add a `filter_by_date` method in `manipulator` - it should filter on the original list of dicts (not on the new one you will create)
- Use `pip` (the equivalent of `npm` in Python) to find a package that manages dates for you, use that instead

# Python Tips & Tricks
- The `print` function is equivalent to `console.log`
    - That said, debugging works the same on VSCode
- In Python, **indentation matters** - you will run into syntax errors if you have incorrect indentation
    - Let VSCode take care of this for you with auto-formatting
- The following syntax is known as [_list comprehension_](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python) in Python:
```python
nums = [1, 2, 3]
doubleNums = [x * 2 for x in nums]
```

# Goal
In this simulation the aim is to expose you to a new programming language, set of conventions, concept (reading files), and to underscore the fact that syntax doesn't matter - you know how to code! So code Python now =]