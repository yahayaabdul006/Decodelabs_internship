"""
DecodeLabs Industrial Training Kit - Project 1
Password Strength Checker

Goal: Classify a password as WEAK, MEDIUM, or STRONG based on
length and character variety (uppercase, lowercase, digits, symbols).

Key skills demonstrated: string handling, condition checks, security basics.
Design follows the "Logic Skeleton" IPO model from the brief:
  INPUT -> PROCESS (O(n) linear scan) -> OUTPUT (risk classification)
"""

import string

MIN_LENGTH = 8
STRONG_LENGTH = 12
COMMON_LEAKED_PASSWORDS = {
    "password", "123456", "12345678", "qwerty", "abc123",
    "password1", "111111", "123456789", "letmein", "iloveyou",
}


def check_password_strength(password: str) -> dict:
    """
    Evaluate a password and return a dict with the breakdown and verdict.
    Uses any() generator checks instead of manual loops (C-optimized,
    short-circuit execution) as recommended in the brief.
    """
    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    variety_score = sum([has_upper, has_lower, has_digit, has_symbol])
    is_common = password.lower() in COMMON_LEAKED_PASSWORDS

    # --- Classification logic ---
    if is_common or length < MIN_LENGTH:
        strength = "WEAK"
    elif length >= STRONG_LENGTH and variety_score >= 3:
        strength = "STRONG"
    elif length >= MIN_LENGTH and variety_score >= 2:
        strength = "MEDIUM"
    else:
        strength = "WEAK"

    return {
        "password": password,
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "variety_score": variety_score,
        "is_common_leaked": is_common,
        "strength": strength,
    }


def print_report(result: dict) -> None:
    """Pretty-print the strength check result."""
    bar = {"WEAK": "🔴", "MEDIUM": "🟠", "STRONG": "🟢"}[result["strength"]]
    print(f"\nPassword: {'*' * result['length']}")
    print(f"Length: {result['length']} chars")
    print(f"Uppercase: {'✔' if result['has_upper'] else '✘'}  "
          f"Lowercase: {'✔' if result['has_lower'] else '✘'}  "
          f"Digit: {'✔' if result['has_digit'] else '✘'}  "
          f"Symbol: {'✔' if result['has_symbol'] else '✘'}")
    if result["is_common_leaked"]:
        print("⚠ Warning: this is a commonly leaked password.")
    print(f"Verdict: {bar} {result['strength']}")


def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type 'quit' to exit.\n")
    while True:
        pwd = input("Enter a password to check: ")
        if pwd.lower() == "quit":
            print("Goodbye!")
            break
        if not pwd:
            print("Please enter a non-empty password.")
            continue
        result = check_password_strength(pwd)
        print_report(result)


if __name__ == "__main__":
    main()
