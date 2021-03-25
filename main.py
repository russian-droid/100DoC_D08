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

def caesar(start_text, shift_amount, cipher_direction):
  #creating new list for a new text
  end_text = ""
  #if user's choice do this
  if cipher_direction == "decode":
      #take shift number and multiply by '-1'
      shift_amount *= -1 #same is: shift_amount *= shift_amount * -1
  #otherwise just do this: loop through
  for char in start_text:
    #only if charachter is in alphabet list
    if char in alphabet:
      #using index method:finds number of the elemnt in the list and assign it to var position
      position = alphabet.index(char)
      #shift the position for every element and assign it to a new var
      new_position = position + shift_amount
      #adding decoded letters(symbols) to the list
      end_text += alphabet[new_position]
    #for all other charachters and symbols
    else:
      #adding decoded letters(symbols) to the list
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

#run loop until the condition changes
should_end = False
while not should_end:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  #if number > 26 (letters in the alphabet), bting it back to within 26 range
  shift = shift % 26

  #run main function
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)

  #ask if user wants to rub again
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  #react to his choice
  if restart == "no":
    should_end = True
    print("Goodbye")
