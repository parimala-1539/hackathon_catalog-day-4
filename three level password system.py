import hashlib
import time
import random
import getpass
from itertools import permutations

# First Level: Encrypted Textual Password
def encrypt_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def textual_password():
    stored_password = encrypt_password("secure123")  # Example encrypted password
    attempt = getpass.getpass("Enter the textual password: ")
    if encrypt_password(attempt) == stored_password:
        print("Textual password correct.")
        return True
    else:
        print("Textual password incorrect.")
        return False

# Second Level: Image-Based Pattern Recognition
def image_pattern_password():
    images = ['🔺', '🔹', '⭐', '🔲']
    correct_pattern = ['🔺', '⭐', '🔹']  # The correct sequence

    print("Image-Based Pattern Recognition: Identify the correct sequence of images.")
    for i, img in enumerate(images):
        print(f"{i+1}: {img}")
    
    permutations_list = list(permutations(images))
    for i, perm in enumerate(permutations_list):
        print(f"{i+1}: {' '.join(perm)}")
    
    attempt_index = int(input("Enter the pattern number (1-24): ")) - 1
    attempt = permutations_list[attempt_index]
    
    if list(attempt) == correct_pattern:
        print("Pattern recognition correct.")
        return True
    else:
        print("Pattern recognition incorrect.")
        return False

# Third Level: Keystroke Dynamics
def keystroke_dynamics():
    reference_timing = [0.12, 0.18, 0.15]  # Simulated ideal timing intervals (in seconds)
    
    print("Keystroke Dynamics: Type the word 'security' and your typing rhythm will be analyzed.")
    input("Press Enter to start...")
    
    word = "security"
    timings = []
    previous_time = time.time()
    
    for char in word:
        input_char = getpass.getpass(f"Type '{char}': ")
        current_time = time.time()
        timings.append(current_time - previous_time)
        previous_time = current_time
    
    # Compare timing differences
    differences = [abs(rt - ut) for rt, ut in zip(reference_timing, timings[:len(reference_timing)])]
    if all(diff <= 0.05 for diff in differences):
        print("Keystroke dynamics analysis passed.")
        return True
    else:
        print(f"Keystroke dynamics failed. Your timings: {timings}")
        return False

def three_level_password_system():
    print("Welcome to the Enhanced Three-Level Password System.")
    
    if textual_password():
        if image_pattern_password():
            if keystroke_dynamics():
                print("Access Granted!")
            else:
                print("Access Denied at Level 3.")
        else:
            print("Access Denied at Level 2.")
    else:
        print("Access Denied at Level 1.")

if __name__ == "__main__":
    three_level_password_system()
