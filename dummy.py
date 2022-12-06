# Import libraries
import re


# Function to read a dummy demonstration text file
def dummy() :
    # Open and read file
    d = open('demo.txt', 'r')
    text = d.read()
    # Print a loading line
    print("\nPrinting all reviews...")
    # Print header
    print("Index    Title    Rating    Reviewer")

    # Row counter
    row = 1
    # String for current text
    text = ""

    for n in range(text, 4) :
        for review in range(4) :
            # Add row to text
            text += str(row)
            # Add whitespaces
            text += "   "
            # Split up demo text by new lines
            text += str(text.split("\n\n"))
            # Increment row
            row += 1
        # Print to terminal
        print(text)
    
    
    #print(d.read())
    # Close file
    d.close()
