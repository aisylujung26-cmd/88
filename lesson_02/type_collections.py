#list  изменяемые

fruits = ['apple', 'banana', 'orange']
numbers = [1, 2, 3, 4, 5,6,7,8,9,10]
mix = ["text", 56, 34.7, True, True]
empty = []

print(type(empty))
print(type(numbers))
print(type(mix))

print("length of fruits: ", len(fruits))
print("length of numbers: ", len(numbers))

print(fruits[1])
print(fruits[::-1])
print(numbers[-1])

fruits[1] = "zitrone"
print(fruits)

fruits.append("peach")
print(fruits)

fruits.insert(1, "melon")
print(fruits)


fruits.remove("zitrone")
print(fruits)


last =fruits.pop()
print(last)
print(fruits)


numbers2 = [156, 45, 85,45,75,96,4,8,20,467]
print(sorted(numbers2))
print(sorted(numbers2, reverse=True))
print(min(numbers2), max(numbers2),sum(numbers2))
print("Is 45 in number -->",45 in numbers2)

numbers2.sort()
print(numbers2)

for fruit in fruits:
    print("I like ",  fruit)


#tuple
coordinates = (10, 20)
single = (34,)
print(type(coordinates))
print(type(single))
tuple1 = 1,2,3
print(type(tuple1))

print(coordinates[0])
print(coordinates[-1])
print(len(coordinates))

x, y, = coordinates
print(f"x={x}, y={y}")

#dict
person ={
    "name" : "Aisy",
    "age" : 26,
    "city" : "Hagenow"
}
print(person)
print("Length in my dict: ", len(person))

print(person["name"])
print(person["city"])
print(person["age"])

print(person.get("email"))
print(person.get("email", "not found"))

person["email"] = "aisy12@mail.ru"
print(person)
person["age"] = 27
print(person)

del person["city"]
print(person)

print("name" in person)
print("phone" in person)

dict_any = {
    1:"pas",
    "two": 2,
    (0,1): "rtfyu"
}
dict_any[(True, False)] = True
print(dict_any)
dict_any[(False, True)] = False
print(dict_any)

print((True, False) == (1,0))

prices = {
    "apple": 1,
    "banana": 2,
    "orange": 3,
}

for product in prices:
    print("Product: ", product)
for product, price in prices.items():
    print(f"Product: {product}, Price: {price}$")

print(list(prices.keys()))
print(list(prices.values()))

print(sum(prices.values()))

#set
colors= {"red", "green", "blue", "yellow"}
print(colors)
colors.discard("yellow")
print(colors)
print("red" in colors)
numbers_set = {1, 2, 1, 3, 4, 5, 6, 6, 7, 8, 9, 10}
print(numbers_set)


empty_dict = {}
print(type(empty_dict))

empty_set = set()
print(type(empty_set))

colors.add("pink")
print(colors)

names = ["Ivan", "Jose", "Jose", "Nina", "Ivan"]
print(names)

unique_names =set(names)
print(unique_names)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print(set1|set2)
print(set1&set2)
print(set1^set2)






