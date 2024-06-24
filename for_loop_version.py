def get_starting_number():
    num_bottles = int(input("How many bottles of beer on the wall? "))
    return num_bottles

def sing(num_bottles):
    for i in range(num_bottles, 0, -1):
        if i > 1:
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.")
            print(f"Take one down, pass it around, {i-1} bottles of beer on the wall!\n")
        else:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")