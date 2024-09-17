#The Chamber of Strings Part 2

def decrypt_caesar_cipher(ciphertext, shift):
    """
    Decrypts a ciphertext using a Caesar cipher with a given shift.
    Shifts each alphabetic character by 'shift' positions backwards in the alphabet.
    Non-alphabetic characters are not altered.
    """
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            # Determine whether the character is uppercase or lowercase to handle the ASCII correctly
            start = ord('A') if char.isupper() else ord('a')
            # Compute the new character position after shifting
            offset = (ord(char) - start - shift) % 26
            decrypted_char = chr(offset + start)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char  # Non-alphabetic characters are added as-is
    return decrypted_text

def try_all_shifts(ciphertext):
    """
    Tries decrypting the ciphertext with all possible shifts from 0 to 25.
    Prints the output of each decryption attempt.
    """
    print("Trying all shifts from 0 to 25:")
    for shift in range(26):
        decrypted_message = decrypt_caesar_cipher(ciphertext, shift)
        print(f"Shift {shift}: {decrypted_message}")

# Example cryptogram to be decrypted
cryptogram = "VZ FRYSVFU VZCNVGAG NAQ NY VGGVR VAPVQRFR V ZNVK ZRFGVKFR V NZ BHG BS PRAGEBY"
try_all_shifts(cryptogram)
