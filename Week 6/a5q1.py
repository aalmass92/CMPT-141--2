# Name Ahmed Almass
# NSID:ana597
# instructors: Mark Keil , Kim Mackey, Marina Schmidt
# Student Number: 11240547

print("Welcome to Super Shopper!")

groceryList = []

intialItem = input("What would you like to add to your shopping list?: ")

groceryList.append(intialItem)
print('Item '+intialItem+' added.')
while True:
    ask = input("Would you like to add something to your list (y/n)?: ")

    if ask == 'y':
        item = input("Item name: ")
        groceryList.append(item)
        print('Item '+item+' added.')
    elif ask =='n':
        print("Items in your list:")
        print(groceryList)
        break

while True:
    itemRemove = input('What item would you like to delete?: ')
    groceryList.remove(itemRemove)

    if groceryList:
        print(groceryList)
    else:
        break
print("Shopping Complete! Goodbye.")



