
def encode(password):
    encoded = ""
    for digit in password:
        new = int(digit)
        new += 3
        encoded += str(new)
    return encoded

def decode(encoded):
    pass

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        menu_opt = int(input("Please enter an option: "))
        if menu_opt == 1:
            ini_pass = input("Please enter your password to encode: ")
            encoded_pass = encode(ini_pass)
            print("Your password has been encoded and stored! ")
            print()
        if menu_opt == 3:
            break

if __name__ == '__main__':
    main()