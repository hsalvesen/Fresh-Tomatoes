# Import libraries
import sys
import helpMe
import reviewCheck
import printReview
import specificReview

# Starup message
response = input("Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'\n")

# Master storage of reviews
reviews = []

# Insert the demo reviews on request
if len(sys.argv) > 1 :
    if sys.argv[1] == "demo" :
        # Append demo reviews to review master storage
        reviews.append(["The Boys","10","Hallmark of our generation, perfect film in every way.","Knopp B"])
        reviews.append(["Adult Driver","10","Great movie with fast cars, starring Adult Driver Adam Driver.","Gio P"])
        reviews.append(["End Of Neon Genesis","10","Gorgeous, deep plot, trippy visuals.","Michael Pod"])
        reviews.append(["Samurai Shampoo","10","Great soundtrack, even better plot and fight choreography.","Niruth B"])

# Enter loop
loop = True

# Continual loop to prompt user
while True :
    # If user asks for help 
    if(response == "help") :
        # Call help function
        response = helpMe.helpMe()

    # If user wishes to exit
    elif(response == "exit") :
        print("\nExiting. Goodbye!")
        # Break out of loop
        break

    # User responds with option 1
    elif(response == "1") :
        # If reviews are not empty
        if reviewCheck.reviewCheck(reviews) == True:
            # Call function  to print review
            print()
            printReview.printReview(reviews)
            # Call help function
            response = helpMe.helpMe()
        else : 
            # Print a message
            print("No reviews found.")
            # Call help function
            response = helpMe.helpMe()

    # User response with option 2
    elif(response == "2") :
        # Call function to print specific reivew
        specificReview.specificReview(reviews)
        # Call help function
        response = helpMe.helpMe()

    # User responds with option 3
    elif(response == "3") :
        # Print confirmation of option choice
        print("\nReview add mode...")

        # Ask user for review content
        # Ask user for title
        title = input("Please enter the title of the movie: ")
        # Continual loop in case of invalid user input for title
        while True :
            # If title is nil or whitespace
            if(len(title.strip()) == 0) :
                # Prompt user to input a valid title
                title = input("Invalid title. Please enter the title of the movie: ")
            # If a valid title was chosen
            else :
                # Break out of title loop
                break
       
        # Ask user for rating
        rating = float(input("Please enter the rating of the movie out of 10: "))
        # Continual loop in case of invalid user input for rating
        while True :
            # If the rating in invalid: nonnumerical or outside bounds of 0 to 10.
            try : 
                if rating > 10 or rating < 0:
                    # Ask the user for an appropriate rating
                    rating = float(input("Invalid rating. Please enter the rating of the movie out of 10: "))
                # If the criteria are met
                else :
                    break
            # If rating is nonnumerical
            except : 
                # Ask the user for an appropriate rating
                rating = float(input("Invalid rating. Please enter the rating of the movie out of 10: "))
        
        # Ask the user for the name of the reviewer
        name = input("Please enter the name of the reviewer: ")
        # Continual loop in case of invalid user input for author
        while True :
            # If rating is white space, empty, nonalphanumeric or contains numbers
            if len(name.strip()) == 0 : #and name.isalpha() == True and any(i.isdigit() for i in name == False) :
                # Ask the user for a valid author 
                name = input("Invalid reviewer name. Please enter the name of the reviewer: ")
            # If the criteria are met
            else :
                break

        # Ask the user for the textual review given by the author
        textualReview = input("Please enter the textual review: ")
        # Continual loop in case of invalid user input for review text
        while True :
            # If the review text is empty or whitespace
            if(len(textualReview.strip()) == 0) :
                # Prompt the user to enter an appropriate textual review
                textualReview = input("Invalid textual review. Please enter the textual review: ")
            else :
                break
        # Print the information that the user entered       
        print("Printing input review...")
        print(f"{title} {round(int(rating))}/10")
        print(f"Reviewer: {name}")
        print(f"Review: {textualReview}")
        # Ask user if the review entered should be added to the database
        accept = input("Do you want to add the following review to the database? y/n ")
        # Check if input is y or n
        if accept != "y" and accept != "n" :
            # Prompt user to try again
            accept = input("Invalid input: Do you want to add the following review to the database? y/n ")
        # If the user accepts
        if accept == "y" :
            # Append the review to list of reviews
            reviews.append([title,rating,textualReview,name])
            # Print confirmation message
            print("Review added!")
            # Print exiting message
            print("Exiting review add mode...")
            # Call help function
            response = helpMe.helpMe()
        else :
            # Print message to terminal that review has been discarded
            print("Review dumped")
            # Print exiting message
            print("Exiting review add mode...")
            # Call help function
            response = helpMe.helpMe()

    # User responds with option 4
    elif(response == "4") :
        # Check that reviews has content
        if len(reviews) > 0 :
            # Confirmation of user input
            print("\nReview delete mode...")
            # Print a message
            print("Select a review by index to delete it.")
            # Print all reviews
            printReview.printReview(reviews)
            # Continual loop in case of invalid user input
            while True:
                # Access the index
                index = int(input())
                # Check index chosen is valid
                if ((index) > len(reviews)) or (index < 1):
                    print("Invalid index, try again!")
                # If index chosen is appropriate
                else:
                    # Ask for confirmation 
                    print("\nDelete the selected review? y/n")
                    print(f"{reviews[index-1][0]} {round(int(reviews[index-1][1]))}/10")
                    print(f"Reviewer: {reviews[index-1][3]}")
                    print(f"Review: {reviews[index-1][2]}")
                    
                    break
            # Store user input 
            delete = input()
            # If user input is invalid
            if delete != "y" and delete != "n":
                # Print a message asking user to try again
                delete = input("Invalid input: Do you want to delete the selected review? y/n ")
            # If user input is yes
            if delete == "y":
                # Pop review
                reviews.pop(index-1)
                # Print confirmation message
                print("Review deleted.")
                # Print exiting message
                print("Exiting review delete mode...")
                # Call help function
                response = helpMe.helpMe()
            else:
                # Print confirmation message
                print("Review not deleted.")
                # Print exiting message
                print("Exiting review delete mode...")
                # Call help function
                response = helpMe.helpMe()
        # If there are no reviews present
        else :
            # Print a message
            print("No reviews found.")
            # Call help function
            response = helpMe.helpMe()
    # If user requests to exit
    elif(response == "exit"):
        # Print exiting message and leave continual loop
        print("Exiting. Goodbye!")
        break
    # If response if empty or whitespace   
    elif (len(response.strip()) == 0):
        # Print a unique error message
        response = input("Sorry, empty input is not a valid command.\n")
    # If user response is invalid
    else:
        # Print a message
        response = input(f"Sorry, {response} is not a valid command.\n")
    # Cease loop    
    loop = False
