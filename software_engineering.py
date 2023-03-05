# Tyler Cornwell

def main():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    org = [int(x) for x in str(password)]
    res = []
    for i in org:
        i += 3
        res.append(i)
    return res

def decode(password):
    pass


loop = True

if __name__ == "__main__":
    while loop == True:
        main()
        menu_selection= int(input("Please enter an option: "))
        if menu_selection == 1:
            password = int(input("Please enter your password to encode: "))
            encode(password)
            print("Your password has been encoded and stored!")
        if menu_selection == 2:
            pass
        if menu_selection == 3:
            quit()
