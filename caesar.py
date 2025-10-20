def caesar_encrypt(text, shift):
    """
    Encrypts the given text using Caesar Cipher with the specified shift value.
    """
    result = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            # Determine the starting ASCII value based on case
            start = ord('A') if char.isupper() else ord('a')
            # Calculate the shifted position
            shifted_pos = (ord(char) - start + shift) % 26
            # Convert back to character
            result += chr(start + shifted_pos)
        else:
            # Keep non-alphabetic characters as they are
            result += char
    
    return result

def caesar_decrypt(ciphertext, shift):
    """
    Decrypts the given ciphertext using Caesar Cipher with the specified shift value.
    """
    # Decryption is just encryption with a negative shift
    return caesar_encrypt(ciphertext, -shift)

def main():
    print("Caesar Cipher Program")
    print("---------------------")
    
    while True:
        print("\nOptions:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                encrypted = caesar_encrypt(message, shift)
                print(f"Encrypted message: {encrypted}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            try:
                shift = int(input("Enter the shift value (integer): "))
                decrypted = caesar_decrypt(message, shift)
                print(f"Decrypted message: {decrypted}")
            except ValueError:
                print("Invalid shift value. Please enter an integer.")
        
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()