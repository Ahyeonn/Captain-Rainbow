#Reusable Function
# def my_fun_function(say_this):
#     print(say_this)

# my_fun_function('Hello World')

checklist = []

#CREATE



def create(item):
    checklist.append(item)

# checklist.append('fun')
# print(checklist)


# READ
def read(index):
    item = checklist[int(index)]
    return item

# print(read(2))

# UPDATE
def update(index, item):
    checklist[int(index)] = item

# update(3,'food')
# print(checklist)

# DESTROY
def destroy(index):
    checklist.pop(index)

# destroy(3)
# print(checklist)


def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index):
    index = int(index)
    checklist[index] = "√" + checklist[index]
    print(checklist[index])


def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item:")
        create(input_item)

    # Read item
    elif function_code == "R":
        item_index = user_input("Index Number?")
        if int(item_index) >= len(checklist):
            print(f"Need to enter less than {len(checklist)-1}")
        else:
            print(read(item_index))
        # Remember that item_index must actually exist or our program will crash.

    # Print all items
    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        # This is where we want to stop our loop
        return False

    elif function_code == "M":
        item_index = user_input("Mark down on which index?")
        if int(item_index) >= len(checklist):
            print(f"Need to enter less than {len(checklist)-1}")
        else:
            mark_completed(item_index)



    elif function_code == "D":
        item_index = int(user_input("Which index to destroy?"))
        if int(item_index) >= len(checklist):
            print(f"Need to enter less than {len(checklist)-1}")
        else:
            destroy(item_index)

    elif function_code == "U":
        item_index = int(user_input("Which index you want to update?"))
        input_item = input("What word do you want to replace it with?")
        if int(item_index) >= len(checklist):
            print(f"Need to enter less than {len(checklist)-1}")
        else:
            update(item_index, input_item)

    # Catch all
    else:
        print("Unknown Option")

def user_input(prompt):
    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

running = True
while running:
    selection = user_input(
        "\n Press C to add to list, \n R to Read from list, \n P to display list, \n M to mark down, \n D to delete, \n U to update, \n and Q to quit")
    if selection == "Q":
        running = False
    else:
        select(selection.upper())

def test():
    create("purple sox")
    create("red cloak")

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    print(checklist)

    list_all_items()

    # Call your new function with the appropriate value
    # select("C")
    # # View the results
    # list_all_items()
    # # Call function with new value
    # select("R")
    #  # View results
    # list_all_items()
    # # Continue until all code is run
    # user_value = user_input("Please Enter a value:")
    # print(user_value)

