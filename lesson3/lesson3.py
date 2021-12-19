import csv
import json
#1 Calculates the value of function f1(x) = x/(x+100)
f_1 = lambda x: x/(x+100)
#1 Calculates the value of function f2(x) = 1/x
f_2 = lambda x: 1/x
#2 Calculates the value of function f3(x) = 20*(f1(x) + f2(x))/x
f_3 = lambda x: 20 *( f_1(x) + f_2(x) ) / x

# range from 5 to 90
my_range = range(5,90+1)

# create a generator of values
def generator():
    for i in my_range:
        yield i
test = generator()
# create a dictionary
dict_of_val_funct = {}

#3 Present the result in the form of a dictionary
for x in test:
    dict_of_val_funct[x] =  f_1(x), f_2(x), f_3(x)
# print a dictionary    
print(dict_of_val_funct)

#4 Saves the result of calculations to a CSV file 
with open('functs.csv', 'w') as file:
    csv_writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL)
    # with a header (columns) which are the values ​​x, f1(x), f2(x), f3(x)
    csv_writer.writerow(["x", "F1(x)", "F2(x)", "F3(x)"])
    # sort the values ​​and add them to CSV-file
    for x, values in dict_of_val_funct.items():
        F1 = values[0]
        F2 = values[1]
        F3 = values[2]
        X = x
        csv_writer.writerow([X, F1, F2, F3])

#5 Reads the written CSV file and presents the result as a list
with open('functs.csv', 'r') as file:
    csv_reader = csv.reader(file,quoting=csv.QUOTE_MINIMAL)
    for row in csv_reader:
        print(row)

#6 Saves the list in JSON file
with open('data.json', 'w') as f_j:
    for x, values in dict_of_val_funct.items():
        F1 = values[0]
        F2 = values[1]
        F3 = values[2]
        X = x
        data = [{"X": X, "F1(x)": F1, "F2(x)":F2, "F3(x)": F3}]
        json.dump(data, f_j, indent=4)
