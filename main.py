def main():
    print("hello world")

    print( )

    # Declare variables 
    age = 17
    teacher = "Ms. Navab"
    is_fav_class = True   
    my_grade = 99.99 

    # Check the type of variable
    type_of_age = type(age)
    print(type_of_age)

    # String formatting with f-strings
    print(f"The tye of variable age is: {type_of_age}")

    # Declare Variables + Check Types
    x = 42
    type_of_x = type(x)
    print(type_of_x)

    y = 3/4
    type_of_y = type(y)
    print(type_of_y)

    a = float
    type_of_a = type(a)
    print(type_of_a)

    name = "Nina"
    type_of_name = type(name)
    print(type_of_name)

    print(f"My age in 10 years: {age +10}")

    print( )
    
    # Initialize args for function
    ingredients_list =["chocolate chips", "cinnamons", "flour", "sugar", "butter", "eggs"]
    snickerdoodle = "mix everything and put it in oven!"
    temp = 300

    # Call a function
    bake_cookie(ingredients_list, snickerdoodle, temp) 

    # Call a function with an optional argument 
    bake_cookie (ingredients_list, snickerdoodle, temp, cutter = "heart")

    print()

    # Reviewing optional keyword arguments
    print(calculate_numbers(2, 3))
    print(calculate_numbers(2, 3, "subtract"))
    print(calculate_numbers(2, 3, operation = "subtract"))

    # you can mix data types in the same list
    numbers = [5, 5, 6, 5.5, 7, 42, "hi"]
    list_iteration(numbers)

def bake_cookie (ingredients, instructions, tempature, cutter = "circle"): 
    # Print the list of ingredients
    for item in ingredients: 
        print(item)
    
    # Print the oven tempature
    print(f"Set the oven to {tempature} degrees Kelvin")

    # Print the instructions
    print(instructions, end="\n")

    # Specify which cookie cutter to use
    print(f"Now use a {cutter} cutter")

def calculate_numbers(x, y, operation="add"):
    if operation == "add":
        return x + y
    # Means else if
    elif operation == "subtract":
        return x - y

# Different ways to modify values whle itterating
def list_iteration(input_list):
    # 1. create a new list from 
    new_list = []
    for item in input_list: 
        new_list.append(item *2)
    print(new_list)

    # 2. LIST COMPERHENSION --> extra useful in data science (going through rows/columns)
    input_list =  [item * 2 for item in input_list]
    print(input_list)

if __name__ == "__main__":
    main() 