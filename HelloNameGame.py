name = input("What is your name? ")
print("Hello " + name + " here are some movies I like!")
# Open the file in read mode
with open('MovieList.txt', 'r') as file:

    # Read the contents of the file
    contents = file.read()

    # Print the contents to the terminal
    print(contents)
