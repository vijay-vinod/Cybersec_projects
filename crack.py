import hashlib
import itertools
import string

# Hash function (using SHA-256)
def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

# Dictionary Attack
def dictionary_attack(hashed_password, wordlist_file):
    with open(wordlist_file, 'r') as f:
        for word in f:
            word = word.strip()
            if hash_password(word) == hashed_password:
                print(f"[+] Password found: {word}")
                return word
    print("[-] Password not found in the wordlist.")
    return None

# Brute Force Attack
def brute_force_attack(hashed_password, max_length=4):
    characters = string.ascii_lowercase + string.digits  # Alphabet + numbers
    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            if hash_password(guess_password) == hashed_password:
                print(f"[+] Password found: {guess_password}")
                return guess_password
    print("[-] Password not found using brute force.")
    return None

# Main function
if __name__ == '__main__':
    # Hash of the password to crack
    target_password = "pass123"  # Example password
    hashed_password = hash_password(target_password)
    print(f"Hashed Password: {hashed_password}")
    
    # File path to the wordlist (for dictionary attack)
    wordlist_file = 'wordlist.txt'  # Provide the path to your wordlist file

    print("\n[*] Starting Dictionary Attack...")
    result = dictionary_attack(hashed_password, wordlist_file)
    
    if not result:
        print("\n[*] Starting Brute Force Attack...")
        brute_force_attack(hashed_password, max_length=4)
