'''
###########
Lab 4.03
###########

Instructions
In this lab we will be drawing images using nested for loops.

For each of the following problems, you will write a function that will draw the desired output. You may use an extra function if you find it helpful.

1.  Write a function, draw_7, to draw the 7x7 square (shown below)

    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
    * * * * * * *
2.  Write a function stars_and_stripes, that will draw a 3 sets of rows. 1st a row of 7 stars followed by a row of 7 dashes (shown below)

    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
    * * * * * * *
    - - - - - - -
3.  Write a function, increasing_triangle that will print out the following:

    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
    1 2 3 4 5 6
    1 2 3 4 5 6 7

4. Write a function, vertical_stars_and_stripes that will print out the following:

    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -
    - * - * - * -

5.  Use a function to create your own pattern or drawing. Some possible pattern ideas:

    Write a function that will print a border around a 7x7 square (shown below)

        * * * * * * * *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * - - - - - - *
        * * * * * * * *
    Write a function that will print the following balanced_triangle.

        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5
        1 2 3 4 5 6
        1 2 3 4 5 6 7
        1 2 3 4 5 6
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1
    Write a function that will print the following triangle.

        *
        ***
        *****
    
'''
# Write the code for your custom function below:
def draw7():
    for i in range(7):
        mystr = ''
        for i in range(7):
            mystr += ' *'
        print(mystr)
   




def starsnstripes():
    for i in range(3):
        str1 = ''
        str2 = ''
        for i in range(7):
            str1 += ' *'
            str2 += ' -'
        print(str1)
        print(str2)
    

def incr_tri():
    tristr = ''
    for i in range(1,8):
        tristr += ' ' + str(i)
        print(tristr)
    



def vertsns():
    for i in range(6):
        str = ''
        for i in range(0,3):
            str += " * -"
        print(str)
        
vertsns()
    

def square():
    for i in range(8):
        str1 = '* * * * * * * *'
        str2 = '* - - - - - - *'
        for i in range(1):
            print(str1)
            print(str2)
    

def baltri():
    print(1)
    print(1,2)
    print(1,2,3)
    print(1,2,3,4)
    print(1,2,3,4,5)
    print(1,2,3,4,5,6)
    print(1,2,3,4,5,6,7)
    print(1,2,3,4,5,6)
    print(1,2,3,4,5)
    print(1,2,3,4)
    print(1,2,3)
    print(1,2)
    print(1)

def startri():
    print('*')
    print('***')
    print('*****')

