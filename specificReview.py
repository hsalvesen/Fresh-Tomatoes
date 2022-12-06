# Import libraries
import printReview
import helpMe

# Function that determines the specific review to print
def specificReview(reviews):
    # Check if reviews has entries
    if len(reviews) > 0:
        print("\nSelect a review by index to print the full review!")
        # Call function to print the review 
        printReview.printReview(reviews)
        while True:
            # Determine the index
            index = int(input()) 
            # If the index provided is invalid
            if ((index) > len(reviews)) or (index < 1):
                print("Invalid index, try again!")
            else:
                # Print reviews
                print()
                print("Printing selected review...")
                print(f"{reviews[index-1][0]} {round(int(reviews[index-1][1]))}/10")
                print(f"Reviewer: {reviews[index-1][3]}")
                print(f"Review: {reviews[index-1][2]}")
                break
    # If no reviews are found
    else:
        print("No reviews found.")
