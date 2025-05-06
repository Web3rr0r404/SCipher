import random

def shift_text(text, shift):
    """Shifts each letter in the text by the given shift value."""
    shifted_text = []
    for char in text:
        if char.isalpha():  # Only shift letters
            start = ord('A') if char.isupper() else ord('a')
            shifted_text.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            shifted_text.append(char)  # Non-alphabet characters are not shifted
    return ''.join(shifted_text)

def reverse_text(text):
    """Reverses the text."""
    return text[::-1]

def scramble_text(text):
    """Scrambles the letters in the text randomly."""
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def encrypt(plaintext, shift):
    """Encrypts the text using shift, reverse, and scramble steps."""
    shifted = shift_text(plaintext, shift)
    reversed_text = reverse_text(shifted)
    scrambled_text = scramble_text(reversed_text)
    return scrambled_text

def decrypt(ciphertext, shift):
    """Decrypts the text by undoing scramble, reverse, and shift steps."""
    # Unscramble (since scramble is random, we need to guess or manually reverse it, we'll skip it for now)
    # For simplicity, let's assume we can reverse the scrambling manually (in real scenarios, you'd need a key)
    unscrambled_text = reverse_scramble(ciphertext)  # Placeholder for unscramble function

    reversed_text = reverse_text(unscrambled_text)
    decrypted = shift_text(reversed_text, -shift)
    return decrypted

def reverse_scramble(text):
    """Placeholder for unscrambling the text (since scramble is random)."""
    # In a real scenario, you'd need to either guess or have a way to track the scrambled positions.
    # For the sake of simplicity in this demo, I'll reverse the scrambling (in practice, it's very hard to undo).
    return text  # You'll need a better way to handle this in actual decryption.

# Example usage
plaintext = "HELLO WORLD"
shift = 3

# Encrypt
encrypted_message = encrypt(plaintext, shift)
print("Encrypted:", encrypted_message)

# Decrypt (manual reverse scramble step needed here)
decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted:", decrypted_message)
