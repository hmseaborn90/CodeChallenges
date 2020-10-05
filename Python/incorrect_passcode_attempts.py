def incorrectPasscodeAttempts(passcode, attempts):
    count = 0
    for password in attempts:
        failed = False
        if password != passcode:
            count += 1
            failed = True
        if count == 10:
            return True
        if not failed:
            count = 0
    return False

passcode = "1111"
attempts = ["1111", 
 "4444", 
 "9999", 
 "3333", 
 "8888", 
 "2222", 
 "7777", 
 "0000", 
 "6666", 
 "7285", 
 "5555", 
 "1111"]

print(incorrectPasscodeAttempts(passcode, attempts))