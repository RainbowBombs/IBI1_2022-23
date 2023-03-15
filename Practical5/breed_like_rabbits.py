'''
Initialize rabbit_num to 2
Initialize generation to 0

WHILE rabbit_num is less than or equal to 100:
    Increment generation by 1
    Double the value of rabbit_num

Return the value of generation
'''
def rabbit_bleeding():
    # Initialize the number of rabbits to 2
    rabbit_num = 2
    # Initialize the generation count to 0
    generation = 0
    # While the number of rabbits is less than or equal to 100:
    while rabbit_num <= 100:
        # Increment the generation count by 1
        generation += 1
        # Double the number of rabbits
        rabbit_num = rabbit_num * 2
    # Once the number of rabbits exceeds 100, return the generation count
    return generation

# Call the rabbit_bleeding function to execute the code and print the result
print(rabbit_bleeding())
#result:6
