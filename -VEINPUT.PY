def take_input():
    num = int(input("Enter a number: "))
    
    if num < 0:
        print("Negative number entered. Stopping recursion.")
        return
    else:
        take_input()

# Start the recursive input process
take_input()
