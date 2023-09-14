# sql_queries.py

# CREATE TABLE statement for the "bears" table
create_bears_table = """
CREATE TABLE bears (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    sex TEXT,
    color TEXT,
    temperament TEXT,
    alive INTEGER
);
"""

# Other SQL queries as previously provided
# ...

select_all_female_bears_return_name_and_age = """
    SELECT name, age FROM bears WHERE sex = 'female';
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    SELECT name FROM bears ORDER BY name ASC;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    SELECT name, age FROM bears WHERE alive = 1 ORDER BY age ASC;
"""

select_oldest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age DESC LIMIT 1;
"""

select_youngest_bear_and_returns_name_and_age = """
    SELECT name, age FROM bears ORDER BY age ASC LIMIT 1;
"""
