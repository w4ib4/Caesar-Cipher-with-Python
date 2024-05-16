def welcome():
    '''
    Printing Welcome Message
    '''
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cypher.")

def enter_message():
    '''
    Requesting input from the user to determine the mode of comnversion
    and the message that the user would like to encrypt or decrypt.
    '''
    while True:
        
        mode = input("Would you like to encrypt (e) or decrypt (d):").lower()
        if mode == 'e':
            message = input("Enter the message that you would like to encrypt:").upper()
        
        elif mode == 'd':
            message = input("Enter the message that you would like to decrypt:").upper()
            
        else:
            print("Invalid Input, Please enter 'e' or 'd':")

            continue
        
        try:
            shift = int(input("What is the shift number:"))
            if 0 <= shift <= 25:
                return mode, message, shift
            else:
                print("Invalid Shift")
        except ValueError as e:
            print(e)


def encrypt(message, shift):
    '''
    This fucntion is created to encrypt the message the user enters
    '''
    encrypt_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord (char) + shift
            if char.isupper():
                if shifted > ord ('Z'):
                    shifted -= 26
            elif char.islower():
                if shifted > ord ('z'):
                    shifted -= 26
            encrypt_message += chr(shifted)
        else:
            encrypt_message += char
    return encrypt_message        
              
def decrypt(message, shift):
    '''
    This function is created to decrypt the message that the user enters.
    '''
    decrypt_message = ""
    for char in message:
        if char.isalpha():
            shifted = ord (char) - shift
            if char.isupper():
                if shifted < ord ('A'):
                    shifted += 26
            elif char.islower():
                if shifted < ord ('a'):
                    shifted += 26
            decrypt_message += chr (shifted)
        else:
             decrypt_message += char
    return decrypt_message

def process_file(filename, mode, shift):
    '''
    This function is created if the user chooses encrpyt or decrypt through a file.
    '''
    messages = []
    try:
        with open (filename,'r') as file :
            for line in file:
                line = line.strip().upper()
                if mode == 'e':
                    messages.append(encrypt(line, shift))
                elif mode == 'd':
                    messages.append(decrypt(line, shift))
    except FileNotFoundError as e:
        print(e)
    return messages

def is_file(filename):
    '''
    This function opens the file in reading mode and prints error if invalid file name is provided.
    '''
    try:
        with open (filename, 'r'):
            pass
    except FileNotFoundError:
        return False
    return True

        
def write_messages(messages):
    '''
    Writing messages to results.txt

    '''
    with open ('results.txt', 'w') as file:
        for message in messages:
            file.write(message + '\n')
            
def message_or_file():
    '''
    This function prompts the user for encryption/decryption
    

    Returns:
        tuple: A tuple containing the mode ('e' for encryption and 'd' for decryption)
        the message (if input method is console), the filename (if input method is file), 
        and the shift number.
    '''
    
    while True:
        mode = input("Would you like to encrypt (e) or decrypt(d)?").lower()
        
        if mode == 'e':
            method_prompt = "encrypt"
        elif mode == 'd':
            method_prompt = "decrypt"
        else:
            print("Invalid Input, Please enter 'e' or 'd':")
            continue
        
        input_method = input("Would you like to read a file (f) or the console (c)?").lower()

        if input_method == 'f':
            while True:
                filename = input("Enter file name:")
                if is_file(filename):
                    shift = int(input("What is the shift number?"))
                    if 0 <= shift <=25:
                        return mode, None, filename, shift
                    else:
                        print("Invalid input")
                        continue
                else:
                    print("File Not Found")
        elif input_method == 'c':
            shift = int(input("What is the shift number?"))
            message = input(f"What message would you like to {method_prompt}?").upper()
            return mode, message, None, shift
        else:
            print ("Invalid Input")


def main():
    '''
    Runs the Caesar Cipher program.

    This function coordinates the execution of the Caesar Cipher program by calling other functions.

    '''

    welcome()
    while True:
        mode, message, filename, shift = message_or_file()
        
        if filename:
            messages = process_file(filename, mode, shift)
            write_messages(messages)
            print("Output written to results.txt")
        else:
            if mode == 'e':
                print(encrypt(message, shift))
            elif mode == 'd':
                print(decrypt(message, shift))
        
        another = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        while another not in ['y', 'n']:
            another = input("Would you like to encrypt or decrypt another message? (y/n): ").lower()
        if another == 'n':
            print("Thanks for using the program, goodbye!")
            break

main()
            
     

    

                    
            
        
        
