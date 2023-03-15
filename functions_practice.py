def hello():
    print("Welcome to Python!")

def pack(x,y,z):
    return[x,y,z]

def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is empty!")
    else: 
        for i in range(len(lunch_list)):
            if i == 0:
                print(f"First I eat my {lunch_list[0]}")
            else:
                print(f"Next I eat my {lunch_list[i]}")

hello()
print(pack("gloves", "shades", "snacks"))
eat_lunch({})
eat_lunch(["sandwich", "cookies", "apple"])