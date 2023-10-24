# Nicholas Groth
def encode(input):
    encode_list = list(str(input))
    for n in range(len(encode_list)):
        encode_list[n] = int(encode_list[n]) + 3
    for n in range(len(encode_list)):
        encode_list[n] = str(encode_list[n])
    return "".join(encode_list)

def decode(encoded_pass):
    decoded = ""
    for digit in encoded_pass:
        new = int(digit)
        new -= 3
        decoded += str(new)
    return decoded

def main():
    menu_option = 0

    while menu_option != 3:
        print("""Menu
-------------
1. Encode
2. Decode
3. Quit""")

        menu_option = int(input("Please enter an option: "))

        if menu_option == 1:
            user_input = int(input("Please enter your password to encode: "))
            encoded_password = encode(user_input)

        if menu_option == 2:
            decoded_password = decode(encoded_password)
            print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            print()

if __name__ == "__main__":
    main()
