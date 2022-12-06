# Function to print reviews
def printReview(reviews) :
    if len(reviews) > 0 :
        # Print reviews
        print("Printing all reviews...")
        # Print header
        print("Index    Title    Rating    Reviewer")
        # Loop through reviews
        for i in range(len(reviews)):
            print(f"{i + 1}    {reviews[i][0]}    {round(int(reviews[i][1]))}/10    {reviews[i][3]}")

    else :
        print("No reviews found.")
