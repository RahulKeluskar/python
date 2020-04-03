'''
Draw turtle graphics from turtle module using the input file 
'''
# importing the turtle module
import turtle


def main():
    ''' Main function to be executed in module and taking input from the user '''
    filename = input('Please enter the drawing file name:')

    # Create turtle graphics window to draw in it
    t = turtle.Turtle()

    # The screen to be used at the end of the program
    screen = t.getscreen()

    # The next line opens the file for reading using the option "r"
    # For writing into a file th eoption used is "w" and to append is "a"

    file = open(filename, "r")

    # The folloowing for loop reads each line of the file one at a time
    # It then executes the body of the loop once for each line in the file
    for line in file:

        # The strip methos strips off the newline character at the end of the line
        # It adds any blank spaces that might be at the beginning or at the end
        text = line.strip()

        # The following line splits the text variable into pieces.
        # For instance if text contined "goto, 10, 20, 1, black" then
        # commandList will be equal to ['goto', '10', '20', '1', 'black']
        # after splitting the text
        commanList = text.split(',')

        # get drawing command
        command = commandList[0]

        if command == 'goto':
