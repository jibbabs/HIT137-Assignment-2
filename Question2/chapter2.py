#The Chamber of Strings

#Input long string
s = "9jRk48HjY3H8K04Kpkj0kh4"

#Separating the numbers and letters
numbers = ''.join([char for char in s if char.isdigit()])
letters = ''.join([char for char in s if char.isalpha()])

#Output separates the numbers and letters
print("Numbers:", numbers)
print("Letters:", letters)

#Take out even numbers and convert them to ASCII decimal values
even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]  
ascii_numbers = [ord(str(num)) for num in even_numbers]  

#Output even numbers to ASCII decimal values
print("Even numbers to ASCII Decimal Values:", ascii_numbers)

#Take out uppercase letters and convert them to ASCII decimal values
uppercase_letters = [char for char in letters if char.isupper()]  
ascii_letters = [ord(char) for char in uppercase_letters] 

#Output uppercase letters to ASCII decimal values
print("Uppercase letters to ASCII decimal values:", ascii_letters)
