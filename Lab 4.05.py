'''
##########
Lab 4.05
##########

1. Read through the following code
    def print_numbers(list):
        for i in range(1, len(list)+1):
            print(list[i])
​
    num_list = [1, 2, 3, 4, 5, 6]
    print_numbers(num_list)
In your notebook
Write down any bugs that you see in the program

index out of range

2. Read through the following code
    def swapping_stars():
    line_str = ""
        for line in range(0, 6):
            for char in range(0,6):
                if line % 2 == char % 2:
                    line_str += "*"
                else:
                    line_str += "-"
    print(line_str)
Continue in your notebook
Write down any bugs that you see in the program

indents and for
3. In script mode
Fix the 2 programs above.
Create a program that asks the user which function they would like to run.
'''
def print_numbers(list):
    for i in range(len(list)):
        print(list[i])

num_list = [1,2,3,4,5,6]


def swapping_stars():
    line_str = ''
    for line in range(0,6):
        for char in range(0,6):
            if line % 2 == char %2:
                line_str += "*"
            else:
                line_str += "-"
    print(line_str)

def which_func():
    function = input("which function would you like to use? 1 = print numbers, 2 = swapping stars: ")
    if function == '1':
        print_numbers(num_list)
    elif function == '2':
        swapping_stars()
    else:
        print("sorry that command is invalid")

which_func()
