#Import the required package:
#Create a dictionary containing film genres and their corresponding popularity:

#Create a dictionary called "dict" with keys as film genres (strings) and values as the number of students who like the genre (integers)
#Get the user's input for a type of film:
#Prompt the user to input a type of film and store the input in the variable "users_input"
#Print the popularity of the chosen film genre:
#Use the inputted film genre as a key to access the value in the dictionary, and print the value along with the chosen genre
#Prepare the data for the pie chart:
#Extract the keys of the dictionary and store them in the variable "keys"
#Extract the values of the dictionary and store them in the variable "values"
#Create and display the pie chart:
#Create a figure and axis using the "subplots()" function from the pyplot module
#Create a pie chart using the "pie()" function from the axis object, with the values as data and the keys as labels
#Display the pie chart using the "show()" function from the pyplot module
#Print the dictionary:
#Print the dictionary to display the film genres and their popularity


# Import the pyplot module from the matplotlib library, and give it the alias "plt"
import matplotlib.pyplot as plt

# Create a dictionary with keys as film genres and values as the number of students who like the genre
dict = {
    "Comedy": 73,
    "Action": 42,
    "Romance": 38,
    "Fantasy": 28,
    "Science-fiction": 22,
    "Horror": 19,
    "Crime": 18,
    "Documentary": 12,
    "History": 8,
    "War": 7
}

# Prompt the user to input a type of film and store the input in the variable "users_input"
users_input = input("Please give me a type of film: ")

# Print the popularity of the chosen film genre
print(dict[users_input], f"students like {users_input}")

# Extract the keys and values of the dictionary
keys = dict.keys()
values = dict.values()

# Create a figure and axis using the "subplots()" function from the pyplot module
fig, ax = plt.subplots()

# Create a pie chart using the "pie()" function from the axis object, with the values as data and the keys as labels
ax.pie(values, labels=keys)

# Display the pie chart using the "show()" function from the pyplot module
plt.show()

# Print the dictionary to display the film genres and their popularity
print(dict)