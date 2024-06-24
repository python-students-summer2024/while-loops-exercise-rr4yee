def get_starting_number():
    while True:
        num_bottles = input("How many bottles of beer on the wall? ")
        if num_bottles.isnumeric() and num_bottles != "0":
            return int(num_bottles)
        else:
            print("Invalid input. Please enter a number. ")

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            if i == 2:
                print(f"Take one down, pass it around, {i-1} bottle of beer on the wall!\n")
            else: 
                print(f"Take one down, pass it around, {i-1} bottles of beer on the wall!\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")