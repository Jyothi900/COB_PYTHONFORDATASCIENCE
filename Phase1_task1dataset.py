# -*- coding: utf-8 -*-
"""DS1A.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Zx9mNth-NS2DjGsxWE5VftlJR_Mr5_d0
"""

import pandas as pd
import requests

# Fetch student data from the Random User Generator API
url = 'https://randomuser.me/api/?results=10&nat=us'
response = requests.get(url)
data = response.json()

# Extract relevant data from the API response
students = []
for item in data['results']:
    student = {
        'Name': item['name']['first'] + ' ' + item['name']['last'],
        'Gender': item['gender'],
        'Email': item['email'],
        'Age': item['dob']['age'],
        'Grade': 9 + int(item['dob']['age'] / 3),  # Assuming a basic grade estimation
        'Math_Score': 50 + item['dob']['age'] % 50,  # Mocking some scores
        'Science_Score': 60 + item['dob']['age'] % 40,
        'Literature_Score': 55 + item['dob']['age'] % 45
    }
    students.append(student)

# Create a DataFrame from the student data
df = pd.DataFrame(students)

# Save the DataFrame to a CSV file
df.to_csv('student_academic_evaluation.csv', index=False)

print("CSV dataset 'student_academic_evaluation.csv' has been successfully created.")
