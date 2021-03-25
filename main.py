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
  #new list for encoding text
  cipher_text = ""
  #go via letters in the original text
  for letter in plain_text:
    #using index method:finds number of the elemnt in the list and assign it to var position
    position = alphabet.index(letter)
    #shift the position for every element and assign it to a new var
    new_position = position + shift_amount
    #using new position to get a leter from old alphabet and assign it to a new var
    new_letter = alphabet[new_position]
    #adding encoded letters to the list
    cipher_text += new_letter
  print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
  #new list for decoding text
  plain_text = ""
  #go via letters in encoded text
  for letter in cipher_text:
    #using index method:finds number of the elemnt in the list and assign it to var position
    position = alphabet.index(letter)
    #shift the position for every element and assign it to a new var
    new_position = position - shift_amount
    #adding decoded letters to the list
    plain_text += alphabet[new_position]
  print(f"The decoded text is {plain_text}")

#after user decided
if direction == "encode":
  #Call the encrypt function and pass in the user inputs.
  encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
  #Call the decrypt function and pass in the user inputs.
  decrypt(cipher_text=text, shift_amount=shift)
