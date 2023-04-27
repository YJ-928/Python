# creating functions with outputs
def function_with_output(f_name, l_name):
    if f_name == "" or l_name == "":
        return "You didnt provide valid inputs"
    full_name = f_name + " " + l_name
    return print(full_name.title())


function_with_output(f_name=input("Enter your First Name "),
                     l_name=input("Enter your Last Name "))
