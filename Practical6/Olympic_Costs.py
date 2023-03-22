# 1. Prepare data for the bar chart:
# - Create a list "costs" with integers representing the costs of the Olympic Games in billions
costs = [1, 8, 15, 7, 5, 14, 43, 40]

# - Sort the "costs" list in ascending order
costs.sort()
print(costs)

# - Create a list "Olympic_Games" with strings representing the names of the Olympic Games
Olympic_Games = [
    "Los_Angeles_1984",
    "Seoul_1988",
    "Barcelona_1992",
    "Atlanta_1996",
    "Sydney_2000",
    "Athens_2003",
    "Beijing_2008",
    "London_2012"
]

# 2. Import the required package:
# - Import the pyplot module from the matplotlib library, and give it the alias "plt"
import matplotlib.pyplot as plt

# 3. Create and display the bar chart:
# - Set the size of the figure using the "figure()" function from the pyplot module
plt.figure(figsize=(15, 5))

# - Create a bar chart using the "bar()" function from the pyplot module, with the Olympic Games as labels and the sorted costs as data
plt.bar(Olympic_Games, costs, width=0.6, edgecolor="white", linewidth=0.4)

# - Add y-axis label and title to the chart
plt.ylabel('Cost (in $ billions)')
plt.title('Olympic_Costs')

# - Display the bar chart using the "show()" function from the pyplot module
plt.show()