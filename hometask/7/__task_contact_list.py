# Write a simple contact list
# On start program should print available list of commands (example below)
# 1. Add contact
# 2. Find contact
# 3. Print all
# 4. Exit
#
# By selecting 1. program asks for contact info to add
# Name
# Phone number
#
# On successful save it should print - New contact has been added
#
# By selecting 2. Program asks for search term. If list of contacts contains required data it should print it to the
# console (example below)
# 1. Ivan - 034567678
# 2. Petr - 345434534
#
# By selecting 3. Program prints a list of all saved contacts to the
# console (example below)
# 1. Ivan - 034567678
# 2. Petr - 345434534
#
# By selecting 4. Program exit

# Split Contact list program for HW 4 by packages
# Extend contact list program. Add phone and email validation for user input
# Add validation for name. Name length can not be less than 3 letters
# Add delete contact functionality
# Add tabular output

from App import App

if __name__ == "__main__":
    App().process_command_line()






