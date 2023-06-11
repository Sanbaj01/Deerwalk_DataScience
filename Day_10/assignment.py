#Excercise
# names = ['ram', 'shyam', 'hari', 'rita', 'bryn', 'cyndy', 'vyndy']
#print the first three names
#print all the names
#print all the names that has vowels present in it
#print the first ten even numbers starting from 2
#print the first ten even numbers starting from 0
# num = [1,2,3,4,5,6,7,8,9,10]
# use loop find the sum of all the numbers in the list num
#take a user input and print even numbers upto that number
#Yesterday's code should not end


#print the first three names

# names = ['ram', 'shyam', 'hari', 'rita', 'bryn', 'cyndy', 'vyndy']
# i = 0
# while i < 3:
#     print(names[i])
#     i = i + 1

#Using for
# for item in range(3):
#     print(names[item])

#print all the names
# names = ['ram', 'shyam', 'hari', 'rita', 'bryn', 'cyndy', 'vyndy']
# for name in names:
#     print(name)

# print all the names that has vowels present in it
# names = ['ram', 'shyam', 'hari', 'rita', 'bryn', 'cyndy', 'vyndy']
# for name in names:
#     if 'a' in name or 'e' in name or 'i' in name or 'o' in name or 'u' in name :
#         print(name)

# print('a','e' in names[0])


#print the first ten even numbers starting from 2
# i = 2
# while i <= 20:
#     print(i)
#     i = i + 2

# using for loop
# for item in range(2,20,2):
#     print(item)

#print the first ten even numbers starting from 0
# i = 0
# while i < 20:
#     print(i)
#     i = i + 2

# Using For loop
# for item in range(0,11,2):
#     print(item)


# use loop find the sum of all the numbers in the list num
# num = [1,2,3,4,5,6,7,8,9,10]
# sum = 0
# for i in num:
#     sum = sum + i
# print(sum)


#take a user input and print even numbers upto that number
# while True:
#     num = int(input('Enter a number - '))
#     for i in range(0, num+1, 2):
#         print(i)


# Print names with no vowels.
# names = ['ram', 'shyam', 'hari', 'rita', 'bryn', 'cyndy', 'vyndy']
# for name in names:
#     if 'a' not in name and 'e' not in name and 'i' not in name and 'o' not in name and 'u' not in name :
#         print(name)

# Calculate the number of vowels and consonants in a string

while True:
    string = input('Enter a string - ')
    vowel = 0
    consonant = 0
    for i in string:
        if 'a' in i or 'e' in i or 'i' in i or 'o' in i or 'u' in i :
            vowel = vowel + 1
        else:
            consonant = consonant + 1
    print(f'There are {vowel} vowels in the string.')
    print(f'There are {consonant} in the string.')




