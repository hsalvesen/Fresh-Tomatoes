# Fresh-Tomatoes
A simple program that creates a database of film reviews; appending subsequent reviews to a growing text document.

Each movie review has 4 attributes - the title of the movie, a numerical rating out of 10, the name of the reviewer, and the actual textual review.
The database will support 4 basic operations; printing an overview of all reviews, selecting a single review and printing it in full, adding reviews, and deleting reviews. In addition, the database will support two additional commands - 'help' and 'exit'.

Help

On startup, the program will print a welcome message.

Hello, welcome to Fresh Tomatoes! For a list of commands, enter 'help'. To exit, enter 'exit'
When the 'help' command is input, the program will print a help message (a list of the 4 basic operations and their corresponding numbers, example below).

Enter the corresponding number to access that command.
1 : Print all reviews, 2 : Choose a review by index and print the full review, 3 : Add a review, 4 : Delete a review, Exit

When the 'exit' command is input, the program will print an exit message and terminate: Exiting. Goodbye!

When any command besides 'help', 'exit' or the numbers 1-4 is input, print an error message (which itself contains the user's invalid input) and prompt the user again. Example below. 

Special case - when the user enters empty or whitespace input, print the message Sorry, empty input is not a valid command.


1 : Print all reviews.

This command will print, for all movie reviews in the database, 4 fields - its index, title, rating, and reviewer. Note that the index field is simply a number - reviews that are added later will have a larger index, with the first review having an index of 1. After printing the overview, it will print the help message.

If there are no reviews in the database, the program will print an error message, followed by the help message.

Note: If a review is deleted, then all reviews after it will have their indices "moved up", leaving no numbers "skipped". 

If the 'demo' command line argument is given, then a few dummy reviews should be in the database by default as opposed to the database initialising empty 


2 : Choose a review by index and print the full review

This command will first print a brief message.

Select a review by index to print the full review!
Printing all reviews...
Then it will print an overview of all reviews (similar to the first command), then allow the user to select a review by index. The selected review will be printed in full (this includes the movie title, rating, reviewer name, and textual review), followed by the help message. If an invalid index is input, the program will print an error message Invalid index, try again! and allow the user to try again. Note that since we have not formally covered exceptions, it is fine to only handle numerical input for the movie index selection. 

If a valid index is given, the review data for the corresponding review will be printed in the format below, followed by the help message.

Printing selected review...
Adult Driver 10/10
Reviewer: Gio P
Review: Great movie with fast cars, starring Adult Driver Adam Driver.

If there are no movies in the database, an error message will be printed, followed by the help message.


3 : Add a review

This command will allow the user to add a review to the database. 

The command will first print a brief message.

Review add mode...
Then, each field (movie title, rating, name, textual review) will be asked from the user sequentially. Input prompt messages in the example output below.


Whitespace or blank input for the title, name and textual review fields should make the program print an error message and prompt the user for input again, until valid input is given. For the rating field, only accept numbers >= 0 and <= 10. Numeric inputs are expected.

After all 4 fields are input, the program will print the full input review, and ask the user for confirmation (y/n) on whether or not the review should be added. Depending on the user's response to the confirmation, the program will either add the review to the database and print a success message, or not add the review and print a message confirming that the review has been dumped. 

Invalid input for the confirmation question should make the program print an error message and prompt the user again. Following this, the program will print the help message.

Error messages are as follows.

Invalid title. Please enter the title of the movie:

Invalid rating. Please enter the rating of the movie out of 10:

Invalid reviewer name. Please enter the name of the reviewer:

Invalid textual review. Please enter the textual review:

Invalid input: Do you want to add the following review to the database? y/n



4 : Delete a review

This command will allow the user to delete reviews. 

It will first print a brief message.

Review delete mode...
Select a review by index to delete it.
Printing all reviews...
Then it will print out an overview of all reviews (similar to the first command), then prompt the user to enter the index of the review they want to delete. An invalid input index should make the program print an error message, then prompt the user for input again. Once a valid input index is given, the program should print the full review of the corresponding review (similar to the 2nd command), then ask the user for confirmation of deletion (y/n). Depending on the user's input, the review will either be deleted or kept in the database, with a confirmation message printed. 
