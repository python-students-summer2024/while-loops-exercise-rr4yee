def get_starting_number():
    num_bottles = int(input("How many bottles of beer on the wall? "))
    return num_bottles

def sing(num_bottles):
    while num_bottles > 0:
        print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
        num_bottles -= 1
        if num_bottles > 0:
            print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall.\n")
        else:
            print("Take it down, pass it around, no more bottles of beer on the wall!\n")
# def sing(num_bottles):
#     while num_bottles > 0:
#         print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
#         print("Take one down, pass it around, ", end="")
#         num_bottles -= 1
#         if num_bottles == 1:
#                 print("1 bottle of beer on the wall!\n")
#         else:
#             print(f"{num_bottles} bottles of beer on the wall.\n")
#     print("No more bottles of beer on the wall.")