# This is a sample Python script.
from typing import List, Any


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
class VendingMachine:

    def __init__(self):
        self.vending_balance = \
            [
                ["Pennies", 0],
                ["Nickels", 0],
                ["Dimes", 0],
                ["Quarters", 0],
                ["Dollars", 0],
            ]
        self.history = \
            [
                #List of transactions, including name of item, what currency was used
                #Format: Name, num of dollars, num of quarters, num of dimes
                #num of nickles, num of pennies
                #["coke", 0, 2, 3, 3, 5]
                #Leaving this here as an example of what it should look like
            ]
        # We're going to use a similar list to the currency list
        # This will allow esssentially objects to be created and encapsulated within
        # Their own list, as opposed to having to reference multiple separate lists
        # format for entry is: Name, Quantity, Price
        self.items = \
            [
                #["coke", 5, 1.0]
                #also leaving this here as an example
            ]

    # Getting inventory of the vending machine
    def inventory(self):
        print("The inventory of this vending machine is as follows: ", self.items)

    # Getting the balance of currency present in this vending machine
    def balance(self):
        print("The remaining balance of this vending machine is ", self.vending_balance)

    # Getting the history of transactions for this vending machine
    def transaction_history(self):
        print("The history of transactions for this vending machine is as follows: ", self.history)

    def add_item(self, name, qty, price):
        for x in self.items:
             if name == self.items[x[0]]:
                self.items[x[1]] = self.items[x[1]] + qty

        self.items.append([name, qty, price])

    def buy_item(self, name, dollars, quarters, dimes, nickles, pennies):
        item_selected = 0
        totalSumOfCurrency = dollars + (quarters * .25) + (dimes * .1) + (nickles * 0.05) + (pennies * .01)
        #Finding the item in the list
        for index, x in enumerate(self.items):
            if name == x[0]:
                item_selected = index
        #Making sure we have that item in stock
        if self.items[item_selected][1] == 0:
            print("We apologize, but we are out of: ", self.items[item_selected][0])
        #Making sure they got the dough for it
        if totalSumOfCurrency < self.items[item_selected][2]:
            print("We apologize, but you do not have enough money for this item")
        else:
            self.items[item_selected][1] = self.items[item_selected][1] - 1
            transactionToAdd = [name, dollars, quarters, dimes, nickels, pennies]
            self.history.append(transactionToAdd)
            self.vending_balance[0][1] += pennies
            self.vending_balance[1][1] += nickels
            self.vending_balance[2][1] += dimes
            self.vending_balance[3][1] += quarters
            self.vending_balance[4][1] += dollars


            #What if they need change?

    def help(self):
        print("Commands: \n Command Syntax,     Example     Description \n")
        print("balance:     balance     shows the balance")
        print("history:     history     prints the list of transactions")
        print("inventory:   inventory   prints available items with name and ID")
        print("add item <str> <int> <float>:    add item chips 2 $1.00  add an item name qty price")
        print("buy item <str> {5}<int>:     buy item chips 1 2 2 4 3 ")
        print("buys an item with #dollars, quarters, dimes, nickles, pennies")
        print("help         help        display help menu with these commands")
        print("exit         exit        exit the vending machine")




machine = VendingMachine()

while True:
    user_input = input("Please type command, enter 'help' for list of commands")

    if user_input.lower() == 'exit':
        break
    elif user_input.lower() == 'balance':
        machine.balance()
    elif user_input.lower() == 'history':
        machine.transaction_history()
    elif user_input.lower() == 'inventory':
        machine.inventory()
    elif user_input.lower() == 'help':
        machine.help()
    elif user_input.lower().startswith("buy"):
        #I know the name will begin at index 9
        remainingInput = user_input[9:]
        tokens = user_input.lower().split()

        #since items can have varying lengths in terms of their names, I need to
        #be able to sort through the input and determine what denominations of
        #currency they're using. Chips has 5 characters, Donuts has six, so I need
        #to be able to tell when I should start looking.

        #So, where does the item name end?
        item_end_index = -1
        for i, token in enumerate(tokens):
            if not token.isdigit():
                item_end_index = i
            else:
                break
        #Since I spent all that time sorting through the input to get to the currency
        #I may as well save the actual NAME of the item to a string, rather than
        #sort through it all over again
        desired_item_name = " ".join(tokens[item_end_index])

        #Now, did they enter in the command correctly? Before, I couldn't check b/c
        #I didn't know how long the name of the item was going to be. Therefore,
        #now that I do know how long it is, I can check to be sure they entered
        #all the digits correctly.
        if len(tokens) - item_end_index - 1 < 5:
            print("Invalid input format, please type 'help' if you require assistance")
        else:
            dollars = int(tokens[item_end_index + 1])
            quarters = int(tokens[item_end_index + 2])
            dimes = int(tokens[item_end_index + 3])
            nickels = int(tokens[item_end_index + 4])
            pennies = int(tokens[item_end_index + 5])
            machine.buy_item(desired_item_name, dollars, quarters, dimes, nickels, pennies)

        #Now we have the name of the item, along with all the currency we're going
        #To use to buy the item.

        #First, see if they have enough money;
        #Then, see if they have too much, and can we give change
        #Also remember, If they give too much, and we don't have change;
        #We can always return some of the coins or dollars they gave
        #For example, a Coke costs a dollar, a user enters a dollar and two quarters
        #We can just take the dollar, and give them back their two quarters



    #Now to add items
    elif user_input.lower().startswith("add"):
        #Same as before, please refer to buy items comments if any confusion arises
        remainingInput = user_input.lower()[9:]
        tokens = user_input.lower().split()

        item_end_index = -1
        for i, token in enumerate(tokens):
            if not token.isdigit():
                item_end_index = i
            else:
                break

        #Now to get the item and add it to the inventory
        itemToAdd = " ".join(tokens[item_end_index])

        #Now to ensure the command was entered correctly
        if len(tokens) - item_end_index < 2:
            print("Invalid input format, please type 'help' if you require assistance")
        else:
            itemQuantity = int(tokens[item_end_index + 1])
            itemPrice = float(tokens[item_end_index + 2][1:])
             #Removing the dollar sign
            machine.add_item(itemToAdd, itemQuantity, itemPrice)

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
#    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
