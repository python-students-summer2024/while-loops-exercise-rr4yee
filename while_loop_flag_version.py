def get_starting_number():
    num_bottles = int(input("How many bottles of beer on the wall? "))
    return num_bottles

def sing(num_bottles):
    bottles = True
    while bottles:
         if num_bottles > 1:
              print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
              print(f"Take one down, pass it around, {num_bottles-1} bottles of beer on the wall.\n")
         else:
              print("1 bottle of beer on the wall, 1 bottle of beer.")
              print("Take it down, pass it around, no more bottles of beer on the wall!\n")
              bottles = False
         bottles -= 1
         if bottles == 0:
              bottles = False