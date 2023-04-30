def format_name(f_name,l_name):
    """This function is used to join first and last name and
    return in title case"""
    if f_name == "" or l_name == "":
        return "You didn't provide the inputs"
    formated_fname =f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"

f_name = input("Enter you first name:")
l_name = input("Enter you last name:")
final_output = format_name(f_name,l_name)
print(final_output)