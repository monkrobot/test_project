#Testing of reloading the previous version

def function_decorator(decoration_function):
    def wrapper_function_decorator(arg1, arg2):
        print("First text")
        decoration_function(arg1, arg2)
        print("Last text")
    return wrapper_function_decorator

@function_decorator
def new_func_for_decoration(a, b):
    print("Text in the center " + str(a) + " and " + str(b))

new_func_for_decoration('hello', 'dear')