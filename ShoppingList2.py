#Make a list to hold onto items
shopping_list = []

def show_help():
    #Print out instructions on how to use the app
    print("What should we buy at the shop?")
    print("Enter DONE to exit the app")
    print("Enter HELP to show this help")
    print("Enter SHOW to show the list")

def show_list():
    #Print out list
    print ("Here's your list: ")
    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    #Add new items to list
    shopping_list.append(new_item)
    print("Added {}. List now has {} items".format(new_item, len(shopping_list)))


show_help()

#Ask for new items
while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    elif new_item == "HELP":
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()
    

