import csv
import matplotlib.pyplot as plt

location = {}
earthquakes_lessthan_5= 0
earthquakes_morethan_5= 0
shallow_earthquakes = 0
intermediate_earthquakes = 0
deep_earthquakes = 0
magnitude = []
the_max_location = None
the_min_location = None

with open("Data_Gempabumi_2023_2024.csv", "r") as csvfile:
    csv_reader = [*csv.reader(csvfile)]

    for row in csv_reader:
        # Membuat list nilai magnitudo
        magnitude.append(float(row[5]))

        # Menghitung jumlah gempabumi yang memiliki magnitudo kurang dari 5 dan lebih dari 5
        if float(row[5]) <= 5:
            earthquakes_lessthan_5 += 1
        else:
            earthquakes_morethan_5 += 1
        
        # Menghitung jumlah gempabumi yang terjadi pada suatu lokasi
        if row[10] in location.keys():
            location[row[10]] += 1
        else:
            location[row[10]] = 1

        # Menyortir jenis gempa berdasarkan kedalamannya
        if int(row[7]) <= 70:
            shallow_earthquakes += 1
        elif 70 < int(row[7]) <= 300:
            intermediate_earthquakes += 1
        else:
            deep_earthquakes += 1

    # Mencari nilai magnitudo tertinggi dan terendah
    max_magnitude = max(magnitude)
    min_magnitude = min(magnitude)

    # Mencari lokasi dengan nilai magnitudo tertinggi dan terendah
    for row in csv_reader:
        if float(row[5]) == max_magnitude:
            the_max_location = row[10]
        elif float(row[5]) == min_magnitude:
            the_min_location = row[10]


# Mengurutkan lokasi dari yang paling banyak terjadi gempabumi ke paling sedikit terjadi gempa bumi
sorted_location = dict(sorted(location.items(), key=lambda item: item[1]))
location_most = list(sorted_location.keys())[-1]


print(f"Number of earthquakes with magnitude greater than 5 = {earthquakes_morethan_5}")
print(f"Number of earthquakes with magnitude less than 5 = {earthquakes_lessthan_5}")
print(f"Highest magnitude is M {max_magnitude}, occured in {the_max_location}")
print(f"Lowest magnitude is M {min_magnitude}, occured in {the_min_location}")
print(f"Number of shallow earthquakes = {shallow_earthquakes}")
print(f"Number of intermediate earthquakes = {intermediate_earthquakes}")
print(f"Number of deep earthquakes = {deep_earthquakes}")
print(f"The location where earthquakes occur most frequently is {location_most}.")
print(sorted_location)

x_loc = list(sorted_location.keys())[-15:]
y_num = list(sorted_location.values())[-15:]

# plt.barh(x_loc, y_num, color="#124559", height=0.8)
# plt.barh(x_loc, y_num, color="gray", height=0.8, alpha=0.3, left=[v + 1 for v in y_num])
# plt.subplots_adjust(top=0.9, bottom=0.1, left=0.3)
# plt.gca().spines["top"].set_linestyle("None")
# plt.gca().spines["right"].set_linestyle("None")
# plt.xticks(rotation=45)
# pie_color = ["#124559", "#598392", "#AEC3B0"]
# pie_label = ["Gempabumi Dangkal", "Gempabumi Menengah", "Gempabumi Dalam"]
# pie_explode = [0, 0.1, 0.2]
# plt.pie([shallow_earthquakes, intermediate_earthquakes, deep_earthquakes],
#         labels=pie_label, explode=pie_explode,
#         colors=pie_color, shadow=False, startangle=0)
# plt.axis("equal")
# plt.legend(loc="upper right")


# plt.show()