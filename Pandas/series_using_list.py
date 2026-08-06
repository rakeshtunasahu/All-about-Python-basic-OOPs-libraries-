import pandas as pd

## 1.series using list

numbers = [10, 20, 30, 40, 50]

s = pd.Series(numbers)

print(s)

##2. Creating a Series using Strings

fruits = ["Apple", "Banana", "Mango", "Orange"]

s = pd.Series(fruits)

print(s)

## 3. Creating a Series with Custom Index

marks = [85, 90, 78, 92]

s = pd.Series(marks, index=["A", "B", "C", "D"])

print(s)

## 4. Creating a Series with a Name

marks = [85, 90, 78, 92]

s = pd.Series(marks, name="Student Marks")

print(s)

##5. Creating a Series using a Dictionary

student = {
    "Rakesh": 85,
    "Rahul": 90,
    "Amit": 78,
    "Neha": 92
}

s = pd.Series(student)

print(s)