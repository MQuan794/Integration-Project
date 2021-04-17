""""
Program serves as a textbook for Python

"""


# Mike Quan
# COP 1500
# Professor Vanselow
# Integration Project: Personal Textbook
# Purpose and project: Create a textbook type guide for python


def menu():
    """
    Function is a menu
    """
    # Introduction to the program
    print(
        "Welcome to Mike's Python Textbook.")
    choice = input(
        "Please select 1-5 for a topic. ")

    if choice == "1":
        demonstrate_numeric_ops()
    elif choice == "2":
        demonstrate_string_ops()
    elif choice == "3":
        loops()
    elif choice == "4":
        demonstrate_boolean_ops()
    elif choice == "5":
        exit()
    else:
        print("Please choose 1,2,3,4,5")
        menu()  # make loop


def demonstrate_string_ops():
    """"
    Function serves as a menu for string operations

    """
    lesson_2 = input("Please select from the following operations, + or *")
    if lesson_2 == "+":
        demonstrate_string_add()
    elif lesson_2 == "*":
        demonstrate_string_mul()
    else:
        print("Invalid selection please try again")


def demonstrate_string_mul():
    """"
    Function shows how to use * with strings
    """""

    print("You can use the * symbol with strings to multiple a word")
    word_choice = str(input("Please type a word"))
    word_number = str(11)
    print(word_choice, word_number, sep=" * ")
    word_answer2 = input("How many times will your word be printed?")
    if word_answer2 == "11":
        print("Excellent now you know how to use * in terms of strings.")
        path_10 = input("Press 1 for string menu or 2 for main menu ")
        if path_10 == "1":
            demonstrate_string_ops()
        elif path_10 == "2":
            menu()  # make loop
    else:
        print("I'm sorry that is wrong")
        demonstrate_string_mul()


def demonstrate_string_add():
    """"
    Function explains how to use + in terms of string.
    """
    print("You can use the + symbol with strings to add two words together")
    word1 = str(input("Enter a Word "))
    word2 = str(input("Enter a second Word "))
    word3 = str(word1 + word2)  # + adds the two words together
    word_blank = input("What will the word become after adding.")
    if word_blank == word3:
        print("Excellent now you know how to use + in terms of strings.")
        path_11 = input("Press 1 for string menu or 2 for main menu ")
        if path_11 == "1":
            demonstrate_string_ops()
        elif path_11 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        demonstrate_string_add()

    # Function allows users to navigate operations


def demonstrate_numeric_ops():
    """"
    Function serves as menu for numeric operations.
    """
    print("Numeric operations are fairly simple,")
    print("Numeric Operations include the following; +,-,*,**,%,/,// ")
    lesson = input(
        "Please select from the following operations, + - * ** % / // ")
    if lesson == "+":
        addition()
    elif lesson == "-":
        subtraction()
    elif lesson == "*":
        multiply()
    elif lesson == "/":
        divide()
    elif lesson == "**":
        exponent()
    elif lesson == "//":
        floor_divide()
    elif lesson == "%":
        modulus()
    else:
        print("Error going back, please select from the list!")
        demonstrate_numeric_ops()


def addition():
    """
    Function explains the + sign for numeric operations.
    """
    print(
        "The + sign is the same as the basic addition symbol, ")
    number = int(input("Before we begin select a number "))
    answer = int(number + 4)  # + adds the number by 4
    print("For example take your number", number, "and add 4 to it. ")
    answer_2 = int(input("What is the answer"))
    if answer_2 == answer:
        print("Excellent work now you know how to use the +! ")
        path = input(
            "Press 1 for string menu or 2 for main menu ")
        if path == "1":
            demonstrate_numeric_ops()
        elif path == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        addition()


def subtraction():
    """"
    Function explains how to use the - sign for numeric operations.
    """
    print(
        "The - sign is the normal subtraction sign. ")
    sub_num = int(input("Before we begin please choose a number."))
    print("Now take that number", sub_num, "and subtract it by 2. ")
    sub_answer = int(sub_num - 2)  # - subtracts the number by 2
    sub_choice = int(input("What is the answer "))
    if sub_choice == sub_answer:
        print("Excellent now you know how to use the - symbol ")
        path_2 = input(
            "Press 1 for string menu or 2 for main menu ")
        if path_2 == "1":
            demonstrate_numeric_ops()
        elif path_2 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        subtraction()


def multiply():
    """
    Function shows how to use the * sign with numeric operations.
    """
    print(
        "The * symbol means multiplication. ")
    mul_num = int(input("Please select a number. "))
    mul_answer = int(mul_num * 3)  # * multiplies the number by 3
    print("Now take that number", mul_num, "and * (multiply) it by 3")
    mul_choice = int(input("What is the answer"))
    if mul_choice == mul_answer:
        print("Excellent work now you know how to use the * symbol! ")
        path_3 = input(
            "Press 1 for string menu or 2 for main menu  ")
        if path_3 == "1":
            demonstrate_numeric_ops()
        elif path_3 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        multiply()


def divide():
    """
    Function shows how to use the / sign for numeric operations.
    """
    print(
        "The / symbol means division.")
    div_num = int(input("Please select a number "))
    div_answer = int(div_num / 1)  # divides the number by 1
    print("Now take that number", div_num, "and / (divide) it by 1")
    div_choice = int(input("What is the answer"))
    if div_choice == div_answer:
        print("Excellent work now you know how to use the / symbol! ")
        path_4 = input(
            "Press 1 for string menu or 2 for main menu  ")
        if path_4 == "1":
            demonstrate_numeric_ops()
        elif path_4 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        divide()


def floor_divide():
    """
    Function shows how to use the // (floor division) for numeric operations.
    """
    print(
        "The // symbol means floor division.")
    floor_num = int(input("Please select an even number "))
    floor_answer = int(
        floor_num // 2)  # floor divides the number by 2.
    print("Now take that number", floor_num,
          "and // (floor divide) it by 2.")
    floor_choice = int(input("What is the answer"))
    if floor_choice == floor_answer:
        print("Excellent work now you know how to use the // symbol! ")
        path_6 = input(
            "Press 1 for string menu or 2 for main menu  ")
        if path_6 == "1":
            demonstrate_numeric_ops()
        elif path_6 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        floor_divide()


def exponent():
    """
    Function explains how to the use the ** (exponent) for numeric operations.
    """
    print(
        "The ** symbol means multiplication.")
    ex_num = int(input("Please select a number "))
    ex_answer = int(ex_num ** 3)  # ** raises the number by 3
    print("Now take that number", ex_num, "and ** (exponent or raise) it by 3",
          end=". ")
    # end= puts a period and a space at the end of the sentence
    ex_choice = int(input("What is the answer"))
    if ex_choice == ex_answer:
        print("Excellent work now you know how to use the ** symbol! ")
        path_7 = input(
            "Press 1 for string menu or 2 for main menu  ")
        if path_7 == "1":
            demonstrate_numeric_ops()
        elif path_7 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        exponent()


def modulus():
    """
    Function explains how to get the remainder (modulus) (%) for numeric ops.
    """
    print(
        "The % symbol means modulus. ")
    div_num_2 = int(12)
    div_answer_2 = int(
        div_num_2 % 5)  # % shows the remainder of the division problem
    print(
        "For this example our number will be 12 ")
    print(
        "now by doing 12 % 5 it will divide the two numbers ")
    print(
        "and print the remainder.")
    div_choice_2 = int(input("What is the answer"))
    if div_choice_2 == div_answer_2:
        print("Excellent work now you know how to use the % symbol! ")
        path_5 = input(
            "Press 1 for string menu or 2 for main menu  ")
        if path_5 == "1":
            demonstrate_numeric_ops()
        elif path_5 == "2":
            menu()
    else:
        print("I'm sorry that is wrong")
        modulus()


def demonstrate_boolean_ops():
    """
    Function is a menu to boolean operations.
    """
    print(
        "You chose to learn about True and False operators aka and,or,and not")
    demonstrate_boolean_ops1 = input(
        "Type 1 for And, 2 for Or, 3 for Not, 4 for Menu. ")
    if demonstrate_boolean_ops1 == "1":
        and_op()
    elif demonstrate_boolean_ops1 == "2":
        or_op()
    elif demonstrate_boolean_ops1 == "3":
        not_op()
    elif demonstrate_boolean_ops1 == "4":
        menu()
    else:
        print("Please type 1,2,3,4")
        demonstrate_boolean_ops()


def loops():
    """
    Function is a menu for loops.
    """
    loop_choice = input(
        "For while loops (1), for For loops (2), for main menu (3). ")
    if loop_choice == "1":
        while_loops()
    if loop_choice == "2":
        for_loops()
    if loop_choice == "3":
        menu()


def for_loops():
    """
    Function explain how to use for loops.
    """
    print(
        "For loops serve as a way to loop certain codes. ")
    print(
        "For loops goes really well with the range() function. ")
    print("for x in range(0,?):")
    print("     print(L)")
    print("     x+=1")
    x = input(
        "How many times would the range function be set to print 4 L's? ")
    if x == "3":
        for x in range(0, 4):
            print("L")
            x += 1
        print("Correct you now know how to use for loops!")
        loop_choice2 = input(
            "For loops menu (1), for while loops (2), for menu (3) ")
        if loop_choice2 == "1":
            loops()
        elif loop_choice2 == "2":
            while_loops()
        elif loop_choice2 == "3":
            menu()
        else:
            print("Please choose between 1,2,3")
            return loop_choice2
    else:
        print("I'm sorry that is wrong please try again")
        for_loops()


def while_loops():
    """
    Function explains how to use while loops.
    """
    print(
        "While loops are exactly like for loops, it's mostly for preference. ")
    print(
        "While loops specialize in using the <, >, <=,>= or ==. ")
    print("while (x<=5:")
    print("     print(L)")
    print("     x+=1")
    x_2 = input("How many times will this while loop run if x=0 ")
    if x_2 == "6":
        x_3 = 0
        while x_3 <= 5:
            print("L")
            x_3 += 1
        print("Congratulations you now know how to use while loops. ")
        loop_choice3 = input(
            "For For loo[s (1), for loops menu (2), for menu (3). ")
        if loop_choice3 == "1":
            for_loops()
        elif loop_choice3 == "2":
            loops()
        elif loop_choice3 == "3":
            menu()
        else:
            print("Please choose between 1,2,3")
            return loop_choice3
    else:
        print("I'm sorry that is wrong please try again")
        while_loops()


def and_op():
    """
    Function explains how to use the and boolean operation.
    """
    print(
        "The and operator is used for True and False")
    print("1:f 2:t = False")
    print("1:t 2:f = False")
    print("1:t 2:t = True")
    print("1:f 2:f = False")
    demonstrate_boolean_ops2 = input(
        "What would be the output if state 1 is false and state 2 is true?")
    if (demonstrate_boolean_ops2 == "f") or (demonstrate_boolean_ops2 == "f"):
        x = 5
        print((x == 5) and (x > 10))
        print("Great job now you know how to use the and operator")
        demonstrate_boolean_ops3 = input(
            "For Or (1), for Not (2), for Boolean Menu (3), for Menu (4)")
        if demonstrate_boolean_ops3 == "1":
            or_op()
        elif demonstrate_boolean_ops3 == "2":
            not_op()
        elif demonstrate_boolean_ops3 == "3":
            demonstrate_boolean_ops()
        elif demonstrate_boolean_ops3 == "4":
            menu()
        else:
            print("Please choose between 1 and 4")
            return demonstrate_boolean_ops3
    else:
        print("I'm sorry that is wrong try again")
        and_op()


def or_op():
    """
    Function explains how to use the or boolean operation.
    """
    print(
        "The and operator Or is used for True and False.")
    print("1:f 2:t = True")
    print("1:t 2:f = True")
    print("1:t 2:t = True")
    print("1:f 2:f = False")
    demonstrate_boolean_ops4 = input(
        "What would be the outcome if state 1 is true and state 2 is false? ")
    if (demonstrate_boolean_ops4 == "t") or (demonstrate_boolean_ops4 == "T"):
        x_4 = 5
        print((x_4 == 5) or (x_4 > 10))
        print("Great job now you know how to use the or operator")
        demonstrate_boolean_ops5 = input(
            "For And (1), for Not (2), for Boolean Menu (3), for Menu (4)")
        if demonstrate_boolean_ops5 == "1":
            and_op()
        elif demonstrate_boolean_ops5 == "2":
            not_op()
        elif demonstrate_boolean_ops5 == "3":
            demonstrate_boolean_ops()
        elif demonstrate_boolean_ops5 == "4":
            menu()
        else:
            print("Please choose between 1 and 4")
            return demonstrate_boolean_ops5
    else:
        print(
            "I'm sorry that is incorrect try again. ")
        or_op()


def not_op():
    """
    Function explains how to use the not boolean operation.
    """
    print(
        "The Not operator is simple, ")
    print(
        "It just prints the opposite for an equation.")
    demonstrate_boolean_ops6 = input(
        "What would be the outcome be if the statement lines up to be false? ")
    if (demonstrate_boolean_ops6 == "t") or (demonstrate_boolean_ops6 == "T"):
        x_5 = 5
        print(not (x_5 > 10))
        print("Great job now you know how to use the not operator")
        demonstrate_boolean_ops7 = input(
            "For And (1), for Or (2), for Boolean Menu (3), for Menu (4)")
        if demonstrate_boolean_ops7 == "1":
            and_op()
        elif demonstrate_boolean_ops7 == "2":
            or_op()
        elif demonstrate_boolean_ops7 == "3":
            demonstrate_boolean_ops()
        elif demonstrate_boolean_ops7 == "4":
            menu()
        else:
            print("Please choose between 1 and 4")
            return demonstrate_boolean_ops7
    else:
        print("I'm sorry that is incorrect try again. ")
        not_op()


menu()
demonstrate_numeric_ops()
addition()
subtraction()
multiply()
divide()
floor_divide()
exponent()
modulus()
demonstrate_string_mul()
loops()
for_loops()
while_loops()
demonstrate_boolean_ops()
and_op()
or_op()
not_op()
