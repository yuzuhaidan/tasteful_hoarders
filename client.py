# App by Josephine Lyou
# CS361 App Tasteful Hoarders Tracker App
# Python - Flask REST API - pyFiglet

# Description: This is the client_scratch.py file for this app.
# You can find the following:
# Welcome Page, Home Page (after login)
# Nav Panel: Add Item, Remove Item, View Item, Help, FAQ

import pyfiglet
import textwrap
import json
import shutil
#import requests

API_URL = "http://127.0.0.1:5005"

##################################################################
# formatting -------------------------
flower_border = "   |+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
border = "   | "
slash_border = "  /////////////////////////////////////////////////////////////////////////////\n"
nav = (f"{border}  ┌───────────────────────────────────────────────────┐\n"
       f"{border}  │  ADD ITEM * REMOVE ITEM * VIEW ITEM * HELP * FAQ  │ \n"
       f"{border}  └───────────────────────────────────────────────────┘")
wrapper = textwrap.TextWrapper(width=50)
##################################################################

### WELCOME PAGE #################################################
title = pyfiglet.figlet_format("Tasteful Hoarders\nTracker App", font = "ogre", justify="center")
print(title)
print(f"{slash_border}"
      f"{border}\n"
      f"{border}0SKULLPANDA L'impressionisme Series  \n"
      f"{border}\n"
      f"{border}Teakwood * Blossom * Pond * Lightning * \n"
      f"{border}\n"
      f"{border}Windflower * Dawn * Mist * Dew * Amber \n"
      f"{border}\n"
      f"{flower_border}\n"
      f"{border}\n"
      f"{border}THE MONSTERS Exciting Macaron Series \n"
      f"{border}\n"
      f"{border}Soymilk * Lychee Berry * Green Grape *\n"
      f"{border}\n"
      f"{border}Sea Salt Coconut * Toffee * Sesame Bean * \n"
      f"{border}\n"
      f"{border}24 Karat Gold * Dubai Chocolate Matcha Latte\n"
      f"{border}\n"
      f"{flower_border}\n"
      f"{border}\n"
      f"{border}Tamagotchi Connection 2024 Japan Replicas\n"
      f"{border}\n"
      f"{border}Melon Soda * Pearl Flower * Pink Glitter *\n"
      f"{border}\n"
      f"{border}Water Color Glitter * Strawberry Pearl Milk *\n"
      f"{border}\n"
      f"{border}OJ * White Clover * Pearl Milk Tea\n"
      f"{border}\n"
      f"{flower_border}\n"
      f"{border}Orange is the New Black\n"
      f"{border}Tasteful Hoarding is the new Minimalism\n"
      f"{border}Track your collection progress of a curated\n"
      f"{border}list and view your statistics any time, anywhere.\n"
      f"       ┌───────┐            ┌────────────────┐      \n"
      f"       | LOGIN |            | CREATE ACCOUNT |             \n"
      f"       └───────┘            └────────────────┘    \n")
#################################################
logged_in = False
name = ""
new_acc = False
acc_match = False
##################################################
with open('db.json', 'r+') as file:
    data = json.load(file)

while not logged_in:
    log_or_create = input("")

    if (log_or_create.lower() == "create account" or
        log_or_create.lower() == "create"):

        name = input("Enter a new name to start your new hoard: ")

        # Check to see if this acc already exists
        for acc in data:
            if acc["username"] == name:
                print(f"This account already exists, logging in for {name}...")
                acc_match = True
                break
        # Copy template, rename to new account, append to db.json,
        # commit changes so homepage prints correctly
        if not acc_match:
            setup_msg = "Creating a new collection for {name}..."
            print(f"{setup_msg:/^8}")
            template = data[0].copy()
            template["username"] = name
            data.append(template)
            acc_match = True

    if log_or_create.lower() == "login":
        name = input("Enter your username:")
        for acc in data:
            if acc["username"] == name:
                acc_match = True

    # PRINT ACCOUNT'S NAME BEFORE HOME PAGE
    # end the while loop with logged_in true
    if acc_match:
        account = pyfiglet.figlet_format(name, font="rectangles", justify="center")
        print(f"{slash_border}")
        print(account)
        logged_in = True
    else:
        print("Either enter login or create.")

# PRINT THE USER'S HOME PAGE
##################################################
    result = ""
    subtotal = 0
    total = 0
    complete_coll = 0
    hoard_total = 0
    completionist = 0
    for acc in data:
        if acc["username"] == name:
            for series in acc["series"]:
                print(f"{border}{series['name']}\n"
                      f"{border}")
                for colors, count in series["colors"].items():
                    if count > 0:
                        result = result + f"\U00002713{colors} * "
                        subtotal += 1
                        total += 1
                        completionist += 1
                    else:
                        result = result + f"{colors} * "
                        total += 1
                        completionist += 1
                # remove last asterisk, print the color results,
                # reset result
                result = result[:-2]
                print(f"{border}{result}\n"
                      f"{border}\n"
                      f"{border} +++++ Collected: {subtotal}/{total} +++++ \n"
                      f"{flower_border}\n"
                      f"{border}")
                if subtotal == total:
                    complete_coll += 1
                hoard_total = hoard_total + subtotal
                result = ""
    print(f"{border} COMPLETED COLLECTIONS: {complete_coll}  TOTAL ITEMS: {hoard_total}/{completionist}\n"
          f"{nav}\n")
############################################
    app_exit = False
    while not app_exit:
        menu_nav = input("You have taste! Where would you like to go? ")

        if (menu_nav.lower() == "add item" or
            menu_nav.lower() == "add"):
            add_item = input("Item Name: ")
            found = False
            found_series = None
            for acc in data:
                if found:
                    break
                if acc["username"] == name:
                    for series in acc["series"]:
                        if found:
                            break
                        for colors, count in series["colors"].items():
                            if add_item == colors:
                                found = True
                                found_series = series
                                break
            # base case: no match
            if not found:
                print(f"Item not found.")
            # matched: confirm, add, break out back to nav
            else:
                confirm = input(f"You want to add {add_item} from {found_series["name"]}? Y/N: ")
                if (confirm == "Y" or
                    confirm == "y"):
                    found_series["colors"][add_item] += 1
                    print(f"{add_item} HAS BEEN COLLECTED!\n"
                          f"{nav}\n")
                    found = False

        if (menu_nav.lower() == "remove" or
            menu_nav.lower() == "remove item"):
            remove_item = input("Item Name: ")
            found = False
            found_series = None
            for acc in data:
                if found:
                    break
                if acc["username"] == name:
                    for series in acc["series"]:
                        if found:
                            break
                        for colors, count in series["colors"].items():
                            if remove_item == colors:
                                found = True
                                found_series = series
                                break
            # base case: no match
            if not found:
                print(f"Item not found.")
            # matched: confirm, add, break out back to nav
            else:
                confirm = input(f"You want to remove {remove_item} from {found_series["name"]}? You will need to add this again later. Y/N: ")
                if (confirm == "Y" or
                        confirm == "y"):
                    if found_series["colors"][remove_item] > 0:
                        found_series["colors"][remove_item] -= 1
                    print(f"{remove_item} HAS BEEN REMOVED!\n"
                          f"{nav}\n")
                    found = False

        if (menu_nav.lower() == "view" or
            menu_nav.lower() == "view item"):
            view_item = input("Item Name: ")
            with open('info.json', 'r') as f:
                info = json.load(f)
            for series in info:
                for color in series["colors"]:
                    if view_item == color:
                        found = True
                        descrip = series["colors"][color]
                        wrap_descrip = wrapper.wrap(text=descrip)
                        print(f"{border}")
                        for line in wrap_descrip:
                            print(f"{border} {line}")
                        print(f"{border}\n"
                              f"{nav}\n")
            if not found:
                print("Item not found.")
            found = False

        if menu_nav.lower() == "help":
            print(f"\n{border} Welcome to Tasteful Hoarders Tracker App!\n"
                  f"{border}\n"
                  f"{border} To track your items, you can do the following:\n"
                  f"{border} --- Add Items ---\n"
                  f"{border} Type 'Add item' (not case sensitive).\n"
                  f"{border} Type the name of the item. The app will match the item\n"
                  f"{border} name and ask you to confirm. Type Yes to add.\n"
                  f"{border} --- Remove Items ---\n"
                  f"{border} Type 'Remove item' (not case sensitive).\n"
                  f"{border} Type the name of the item. The app will match the item\n"
                  f"{border} name and ask you to confirm. Type Yes to remove.\n"
                  f"{border} --- View Item ---\n"
                  f"{border} To see more detail for a specific item, type the name\n"
                  f"{border} of the item. The app will match the item name and ask\n"
                  f"{border} you to confirm. Type Yes to see the details.\n"
                  f"{border} --- HELP ---\n"
                  f"{border} If you would like instructions, please type Help to\n"
                  f"{border} view the HELP information for this app.\n"
                  f"{border} --- FAQ ---\n"
                  f"{border} For frequently asked questions from users, please type\n"
                  f"{border} FAQ to view the list we have answered ahead of time.\n"
                  f"{border} \n"
                  f"{border} --- EXIT ---\n"
                  f"{border} Type exit to exit the app.\n"
                  f"{nav}\n")

        if menu_nav.lower() == "faq":
            print(f"\n{border} Q: I want you to add a collection that I'm interested in!\n"
                  f"{border} A: If I think the collection is tasteful, I will consider\n"
                  f"{border}   adding it. Only tasteful collections are allowed on this app.\n"
                  f"{border}\n"
                  f"{border} Q: Why don't you add the secret colors of each collection?\n"
                  f"{border} A: Because I don't want to encourage the gambling aspect of the\n"
                  f"{border}   secret color. Therefore, I don't care if my users own them or not.\n"
                  f"{border}\n"
                  f"{border} Q: Why are there only a few collections to track on this app?\n"
                  f"{border} A: Because I want to only add those collections.\n"
                  f"{border}\n"
                  f"{border} Q: Something isn't working right! Can you fix it?\n"
                  f"{border} A: Yes, please email me at lyouj@oregonstate.edu\n"
                  f"{border}   for all bug fix requests. Thanks for helping keep the app\n"
                  f"{border}   running well\n"
                  f"{border}\n"
                  f"{nav}")

        if menu_nav.lower() == "exit":
            with open('db.json', 'w') as file:
                json.dump(data, file, indent=2)
            app_exit = True

