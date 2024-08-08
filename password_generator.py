from random import *
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!','@','#','$','&']

def pass_generator(len, alp, num, sym):
    if len == (alp + num + sym):

        alpha = [choice(alphabets) for i in range(alp)]
        num = [choice(numbers) for i in range(num)]
        sym = [choice(symbols) for i in range(sym)]

        pas_list = alpha + num + sym
        shuffle(pas_list)
        result = "".join(pas_list)
        return result
    else:
        return 'password length not satisfied'

def main():
    print("WELCOME TO PASSWORD GENERATOR")
    while True:

        len = int(input("Enter the length of password: "))
        al = int(input("No.of alphabets in your password: "))
        nu = int(input("No.of numbers in your password: "))
        sy = int(input("No.of symbols in your password: "))
        result = pass_generator(len,al, nu, sy)
        print(result)

        while True:
            next = input("type 'again' for generate another or 'exit' to exit: ").lower()
            if next == 'again':
                break
            elif next == 'exit':
                return
            else:
                print("Wrong input")



if __name__ == '__main__':
    main()






