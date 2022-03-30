'''
Do Now 4.01

1. In your console
Type the following Code
    single_fruit = ['apple', 'banana', 'watermelon', 'grape']
    multi_fruit = []
    multi_fruit.append(single_fruit[0] + 's')
    multi_fruit.append(single_fruit[1] + 's')
    multi_fruit.append(single_fruit[2] + 's')
    multi_fruit.append(single_fruit[3] + 's')
    print(multi_fruit)

In your notebook
Respond to the following
Briefly write down what happened. it printed the fruits list with s at the end to make it plural
 What would happen if you added 100 items to the list single_fruit? it would only update the first 4 to be plural
Write down how you would update multi_fruit. add it until single_fruit[99]

2. In your console
Type the following
    list_of_numbers = [3, 5, 10, 23]
    for num in list_of_numbers:
        print(f"num is " + {num})
        
Continue in your notebook
Respond to the following
Briefly write down what happened. it printed num is + each number in list
 How would this change if you added 100 items to list_of_numbers? would print num is + all 100 numbers

3. In your console
Rewrite the code from part 1 using knowledge from part 2.
'''

single_fruit = ['apple','banana','watermelon','grape']
for item in single_fruit:
    print(f"{item}s")



list_of_numbers = [3, 5, 10, 23]
for num in list_of_numbers:
    print(f"num is {num}")


