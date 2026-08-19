"""
DecodeLabs - Project 2: Basic Encryption & Decryption
Caesar Cipher (mono-alphabetic shift cipher)

Core idea (IPO model):
  INPUT   -> Plaintext / Ciphertext
  PROCESS -> Algorithm (shift) + Key (n)
  OUTPUT  -> Ciphertext / Plaintext

Formulas:
  Encryption: E(x) = (x + n) % 26
  Decryption: D(x) = (x - n) % 26
where x = letter position (A/a = 0) and n = shift key.
"""


def encrypt(text: str, shift: int) -> str:
    """Encrypt text using a Caesar shift. Non-letters are left unchanged."""
    result = []
    for char in text:
        if char.isupper():
            # 'A' = 65 in ASCII, so subtract 65 to normalize to 0-25
            shifted = (ord(char) - 65 + shift) % 26 + 65
            result.append(chr(shifted))
        elif char.islower():
            # 'a' = 97 in ASCII
            shifted = (ord(char) - 97 + shift) % 26 + 97
            result.append(chr(shifted))
        else:
            # Spaces, punctuation, digits, symbols -> passed through untouched
            result.append(char)
    return "".join(result)


def decrypt(text: str, shift: int) -> str:
    """Decrypt text using the same shift key (symmetric encryption)."""
    return encrypt(text, -shift)


def main():
    print("=" * 50)
    print(" DecodeLabs | Project 2: Caesar Cipher Tool")
    print("=" * 50)

    plaintext = input("\nEnter the text to encrypt: ")

    while True:
        try:
            shift = int(input("Enter shift key (e.g. 3): "))
            break
        except ValueError:
            print("Please enter a whole number for the shift key.")

    encrypted = encrypt(plaintext, shift)
    decrypted = decrypt(encrypted, shift)

    print("\n--- Results ---")
    print(f"Plaintext   (Input)      : {plaintext}")
    print(f"Ciphertext  (Encrypted)  : {encrypted}")
    print(f"Recovered   (Decrypted)  : {decrypted}")

    # Sanity check: decrypting the ciphertext should always return the original
    print("\nValidation:", "PASSED ✅" if decrypted == plaintext else "FAILED ❌")


if __name__ == "__main__":
    main()
