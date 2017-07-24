'''Write a function that takes an ordered list of numbers 
(a list where the elements are in order from smallest to largest) and another number. 
The function decides whether or not the given number is inside the list and returns 
(then prints) an appropriate boolean.

Extras: Use binary search.'''

ordered_list = [-9, -1, 0, 3, 34, 9402, 395024]

#Check to see user actually entered a number.
while True:
    number_in_question = input("Enter a number; to quit, type 00: ")
    if number_in_question == "00":
        quit()
    else:
        try:
            number_in_question = int(number_in_question)
        except:
            print("Not a valid number.")
            continue

#A function to compare the number you added from the list you previously saved.
    def number_exists(ordered_list,number_in_question):
        if number_in_question in ordered_list:
            return True
        else:
            return False

    if number_exists(ordered_list,number_in_question) == True:
        print(number_in_question, "is in the list")
    if number_exists(ordered_list,number_in_question) == False:
        print(number_in_question, "isn't on the list")