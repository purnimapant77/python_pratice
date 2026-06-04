def name():
    name="purnima"
    print(name)# name is local variable
    
full_name="Purnima_Pant" # this is global variable
def print_full_name():
    global full_name
    full_name="Rabi Pant"
    print(full_name)
    
name()
print_full_name()
