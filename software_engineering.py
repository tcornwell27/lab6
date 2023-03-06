# Tyler Cornwell

def main():                        #Main function for menu
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    org = [int(x) for x in str(password)]      # Takes input from user and converts to list.
    res = []      # Creates an empty list to append results into.
    for i in org:   # Takes values from the list provided by user and adds 3 to each value.
        i += 3
        res.append(i)   # After adding 3 to each value in list 'org', appends new values into list 'res'
    return res

def decode(password):
    pass


loop = True

if __name__ == "__main__":                  # if dunder statement, prints menu and allows user to choose option menu.
    while loop == True:                     # Also allows user to input password for encoding.
        main()
        menu_selection= int(input("Please enter an option: "))
        if menu_selection == 1:
            password = int(input("Please enter your password to encode: "))
            encode(password)
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            pass
        if menu_selection == 3:             # Option 3 exits the program.
            quit()
