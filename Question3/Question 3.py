#Question 3
#Group Name: CAS003
#Group Members:
#[Alex Tarrant] - [S255441]
#[Jason Yun] - [S364369]

"""----- 3.1 -----"""
#Key code generator for Encryption/decryption functions      
def getkey(): #The original code was converted into a function to ouput a key value when called.
    total = 0
    for i in range(5):
        for j in range(3):
            if i + j == 5:
                total += i + j
            else:
                total -= (i - j)

    counter = 0
    while counter <5:
        if total < 13:
            total += 1
        elif total > 13:
            total -= 1
        else:
            counter += 2  
    
    return total  

#Encrypt code function.
def encrypt(text, key):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + key
            if char.islower():
                if shifted >ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text


"""----- 3.2 -----"""
#Decrypt code function.
#The original encryption code was reversed to create the decryption code. Some changes were required to seperate the letters and carry out the isalpha function.
def decrypt(text, key):
    decrypted_text = ""
    count = 0
    for lines in text:
        words = lines.split()
        for words in text:
            letters = [x for x in words]
            for i in letters:
                if i.isalpha():
                    shifted = ord(i) - key
                    if i.islower():
                        if shifted < ord('a'):
                            shifted += 26
                        elif shifted > ord('z'):
                            shifted -= 26
                    elif i.isupper():
                        if shifted < ord('A'):
                            shifted += 26
                        elif shifted > ord('Z'):
                            shifted -= 26
                    decrypted_text += chr(shifted)
                else:
                    decrypted_text += i
                    print(i)
    return decrypted_text 

key = getkey()
#The decryption code opens a text file named encrypted_code that contains the encrypted code.
readtext = open("HIT137-Assignment-2\Question3\encrypted_code.txt",'r')

#The decryption code then decrypts the code with the key and writes it to another text file name Decoded_text.
decrypted_code = decrypt(readtext, key)
writefile = open("HIT137-Assignment-2\Question3\Decoded_text.txt", 'w')
writefile.write(decrypted_code)
writefile.close  
 
"""----- 3.3 -----"""
#Decrypted Code
#The decrypted code was extracted from the Decoded_text file from the previous function and entered below.
#The corrections are outlined in the comments.
my_dict = {'ke11': 'value1', 'ke12': 'value2', 'ke13': 'value3'}

global_variable = 0 #Moved the definition of global_variable out of the function.

def process_numbers():
    local_variable = 5
    numbers= [1, 2, 3, 4, 5]
    
    while local_variable > 1: #Fixed a typo and added maximum value of 1 to while statement. 
        if local_variable % 2 == 0: 
            numbers.remove(local_variable)
        local_variable = 1
    
    return numbers
    
my_set = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
result = process_numbers () #Removed the argument given to the function.

def modify_dict(new_value): #Added a parameter to the function.
    local_variable = new_value #Removed the local_variable set value of 10 , made it equal to new_value which gets assigned a value when the function is called.
    my_dict['ke14'] = local_variable
    
modify_dict(5) 

def update_global():
    global global_variable
    global_variable += 10
 
update_global() #Added to carry out the function.
    
for i in range(5): #Changed uppercase I to lower case i.
    print(i)
    i += 1

if my_set is not None and my_dict['ke14'] == 10: #Corrected m1 typo for both variables to my.
    print("Condition met!")
    
if 5 not in my_dict.values(): #Added values attribute to check the my_dict Values instead of keys.
    print("5 not found in the dictionary!")
    
print(global_variable)
print(my_dict)
print(my_set)