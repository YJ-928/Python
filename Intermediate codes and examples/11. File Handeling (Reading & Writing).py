# NOTE:- opening the files using open and close
file = open("11.my_file.txt", "w")
# write to the file
file.write("Hello this is python writing.")
# close the file
file.close()

# reading from our written file
file = open("11.my_file.txt", "r")
contents = file.read()
print(contents)
file.close()


# NOTE:-# Opening the file with with open
# no need to close the file here
# we use mode = a to append it, works same as list
with open("11.my_file.txt", "a") as file:
    file.write("\nHello, this is python again,\nwriting using with open now")

with open("11.my_file.txt", "r") as file:
    contents = file.read()
    print(contents)
