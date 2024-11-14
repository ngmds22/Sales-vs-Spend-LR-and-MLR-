# This function takes another function as an arg
def uppercase_decorator(function):
    # New wrapper() function
    def wrapper():
        # Calls the original function to get its output
        func = function()
        # Converts the output to uppercase
        make_uppercase = func.upper()
        # Returns the modified output
        return make_uppercase
    # The uppercase_decorator returns teh wrapper function, when we call the decorated
    # function, we will be calling the wrapper and not the original function.
    return wrapper

# Shorthand to call the deco
# Equivalent to: welcome_msg = uppercase_decorator(welcome_msg)
# When we define welcome_msg(), it gets passed to the deco automatically
# Then returns the wrapper func
@uppercase_decorator
def welcome_msg():
    return 'make this uppercase'

msg = welcome_msg()
print(msg)