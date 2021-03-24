#following Udemy course: 100 days of code by Angela Yu

def how_much_paint (test_h, test_w):
    import math
    coverage_per_can = 5
    number_of_cans = (test_h * test_w) / coverage_per_can
    number_of_cans = math.ceil(number_of_cans)

    return number_of_cans

how_much_paint (test_h = 2, test_w = 4)
print(how_much_paint (test_h = 2, test_w = 4))


#-------------------------------------------
def prime_checker(number):
    #set main statement
    is_prime = True
    #it'll go via all the numbers to see if anywhere делится нацело
    #no point trying to 
    for i in range(2, number):
        #if yes, it's not a prime number
        if number % i == 0:
            #so we'll change main statement to false
            is_prime = False
    #print what we found out
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")
        
#-------------------------------------------
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
  #list for encoded text
  cipher_text = ""
  #go via letters in the original text
  for letter in plain_text:
    
    position = alphabet.index(letter)
    new_position = position + shift_amount
    new_letter = alphabet[new_position]
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
encrypt(plain_text=text, shift_amount=shift)
