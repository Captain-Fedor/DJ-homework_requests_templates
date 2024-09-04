# CONTENT = [i for i in range(1000)]
# print(CONTENT)
import csv
from pprint import pprint
with open('test_data.csv', encoding='UTF-8') as file:
    file_reader = csv.DictReader(file, delimiter=',')
    count = 0
    st_list =[]
    for row in file_reader:
        st_list.append(row)

    print(st_list)


