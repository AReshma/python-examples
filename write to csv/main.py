import csv

# using csv.DictWriter()
# data as dicts
data = [
    {'Name': "jane", "Age": 21},
    {'Name': "rose", "Age": 26},
    {'Name': "jacob", "Age": 23, "Department": "Mathematics"},
    {'Name': "tom", "Age": 21},
    {'Name': "jane", "Age": 71},
    {'Name': "jose", "Age": 19},
    {'Name': "mary", "Age": 42, "Department": "Science"}
]
cols = ["Name", "Age", "Department"]
file_name = "users.csv"
# newline='', remove additional new line after each row
with open(file_name, "w", newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=cols)
    writer.writeheader()
    writer.writerows(data)
print('data is written to users.csv')


# Using csv.writer()
# data as a list of comma separeted list of each row
data = [["jane", 21],
        ["rose", 26],
        ["jacob", 23],
        ["tom", 21],
        ["jane", 71],
        ["jose", 19],
        ["mary", 42]
        ]
file_name = 'users_1.csv'
# newline='', remove additional new line after each row
with open(file_name, "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(cols)
    writer.writerows(data)

print('data is written to users_1.csv')
