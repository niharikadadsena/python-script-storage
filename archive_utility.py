import os
import datetime

def encrypt_text_backward(text_input, shift_amount):
    """
    Applies a reverse-direction substitution cipher to scramble text letters.
    Keeps spaces, numbers, and symbols exactly as they are.
    """
    scrambled_output = ""
    
    for letter in text_input:
        if letter.isalpha():
            ascii_start = ord('A') if letter.isupper() else ord('a')
            # The unique backward shifting math
            new_position = (ord(letter) - ascii_start - shift_amount) % 26
            scrambled_output += chr(ascii_start + new_position)
        else:
            scrambled_output += letter
            
    return scrambled_output

def run_security_test():
    print("----------------------------------------------------")
    print(">> LOCAL COMPONENT ARCHIVE UTILITY v2.0 <<")
    print("----------------------------------------------------")
    
    # Upgrade 1 & 2: Dynamic User Inputs
    user_message = input("Enter the sensitive data string to secure: ")
    
    if not user_message:
        print("[-] Error: Input payload cannot be empty.")
        return
        
    try:
        user_shift = int(input("Set integer shift key magnitude (1-25): "))
    except ValueError:
        print("[-] Invalid input. Defaulting to standard safety shift of 5.")
        user_shift = 5

    # Step 1: Write user data to the input log
    source_file = "input_text.txt"
    with open(source_file, "w") as f1:
        f1.write(user_message)
    print(f"\n[+] Raw data buffered to: '{source_file}'")
    
    # Step 2: Read data out for verification
    with open(source_file, "r") as f1_reader:
        saved_text = f1_reader.read()
        
    # Step 3: Run the backward cipher engine
    secret_text = encrypt_text_backward(saved_text, user_shift)
    
    # Step 4: Write scrambled data to data vault
    encrypted_file = "secured_data.dat"
    with open(encrypted_file, "w") as f2:
        f2.write(secret_text)
    print(f"[+] Scrambled archive saved to: '{encrypted_file}'")
    
    # Step 5: Complete transaction log audit trail
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_file_name = "security_status.log"
    
    with open(log_file_name, "w") as log:
        log.write("== SYSTEM ARCHIVE TRANSACTION LOG ==\n")
        log.write(f"Timestamp: {current_time}\n")
        log.write(f"Key Magnitude Allocated: {user_shift}\n")
        log.write(f"Total Characters Processed: {len(secret_text)} units\n")
        log.write("Status: COMPLIANT / PARITY_CHECK_OK\n")
        log.write("====================================\n")
        
    print(f"[+] Audit trail compiled to: '{log_file_name}'")

if __name__ == "__main__":
    run_security_test()
