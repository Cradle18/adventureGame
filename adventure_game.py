"""
This is a text based adeventure game, takes the user through a story and reacting to the users choices.
"""
#------Imports------#
from scene import Welcome, Part1

#------Define scence objects in the main------#
class Main():

    welcome = Welcome("Welcome")
    welcome.print_welcome()

    print("END OF PART 1")
    


#Let the adventure begin
Main()