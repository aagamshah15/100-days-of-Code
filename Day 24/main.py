# import csv
#
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(row[1])
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
#
# # How to get a column
# temp_data = data["temp"]
# print(temp_data)
#
# # Max value function
# max_val = data["temp"].max()
# print(max_val)
#
# # How to get a row
# row = data[data["day"] == "Monday"]
# print(row)
#
# max_temp = data[data["temp"] == max_val]
# print(max_temp)
#
# monday = data[data["day"] == "Monday"]
# temp_c = monday["temp"]
# temp_f = temp_c * 9/5 + 32
# print(temp_f)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(gray_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_data")
