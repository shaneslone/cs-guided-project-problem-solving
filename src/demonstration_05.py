"""
Challenge #5:

Create a function that returns the data type of a given argument. There are
seven data types this challenge will be testing for:

- List
- Dictionary
- String
- Integer
- Float
- Boolean
- Date

Examples:
- data_type([1, 2, 3, 4]) ➞ "list"
- data_type({'key': "value"}) ➞ "dictionary"
- data_type("This is an example string.") ➞ "string"
- data_type(datetime.date(2018,1,1)) ➞ "date" 

Notes:
- Return the name of the data type as a lowercase string.
"""
def data_type(value):
    if type(value) is list:
        return "List"
    elif type(value) is dict:
        return "Dictionary"
    elif type(value) is str:
        return "String"
    elif type(value) is int:
        return "Integer"
    elif type(value) is float:
        return "Float"
    elif type(value) is bool:
        return "Boolean"
    else:
        return "Date"

print(data_type([1, 2, 3, 4]))
print(data_type({'key': "value"}))
print(data_type(datetime.date(2018,1,1)))

