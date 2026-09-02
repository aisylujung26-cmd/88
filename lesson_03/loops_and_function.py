from lesson_02.type_collections import numbers

fruits2 = ["apple", "banana", "cherry"]
for fruit in fruits2:
    print("I like " , fruit)

for letter in "banana":
    print(letter)

for i in range(5):
    print(i)

for i in range(1, 5):
    print(i)


for i in range(1, 10, 2):
    print(i)

count = 1
while count < 10:
    print(count)
    count += 1

n = 5
while n > 1:
    print(n)
    n -= 1


cash = 0
while cash < 100:
    cash += 10
    print("My cash --> ", cash)

for num in [2,5,6,7,7,9,8,4]:
    if num == 9:
        print("I found 9")
        break
    print(num)

for number in range(1,11):
    if number % 2 == 0:
        continue
    print("Ungerade Zahlen",number)

for number2 in range(1,21):
    if number2 % 3 == 0:
        print("Diese Zahlen /3: ",number2)

def add(a,b):
    return a+b

res = add(3,4)
print(res)
print("Sum is -->", add(3,4))

def is_even(a):
    return a % 2 == 0

print(is_even(2))
print(is_even(5))

def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([7,0,3,15])
print(f"low ={low}, high = {high}")


def sum_list(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum
print(sum_list([5,4,84,8]))


def avg(numbers):
    return sum_list(numbers) / len(numbers)

print(avg([5,4,84,8]))

my_list = ["dog", "cat", "monkey", "mouse", "house", "field"]

def count_words_longer_three_chars(words):
    counter= 0
    for word in words:
        if len(word) > 3:
            counter += 1
    return counter
print(count_words_longer_three_chars(my_list))

def count_vowels(text):
    count = 0
    for char in text.lower():
        if char in "aeiou":
            count += 1
    return count

print(count_vowels("Privet"))
