def get_starting_number():
    while True:
        num_bottles = input("How many bottles of beer on the wall? ")
        if num_bottles.isnumeric() and num_bottles != "0":
            return int(num_bottles)
        else:
            print("Invalid input. Please enter a number. ")

def sing(num_bottles):
    bottles = True
    while bottles:
         if num_bottles > 1:
              print(f"{num_bottles} bottles of beer on the wall, {num_bottles} bottles of beer.")
              num_bottles -= 1
              if num_bottles == 1:
                print(f"Take one down, pass it around, {num_bottles} bottle of beer on the wall!\n")
              else: 
                print(f"Take one down, pass it around, {num_bottles} bottles of beer on the wall!\n")
         else:
              print("1 bottle of beer on the wall, 1 bottle of beer.")
              print("Take it down, pass it around, no more bottles of beer on the wall!\n")
              bottles = False