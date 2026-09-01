from calendar import month

age = 18 #int
price = 19.98 #float
name = "Aisic" #string
is_name =  True #bool

fruits = ["apple", "banana", "cherry"] # list
coordinats=[1,2,3] # tuple
student = {"name": "Aisic", "age":18} #dict
unique_numbers = {1,2,9,6,9,2,0,1}
print(unique_numbers)
print(student)

s1 = 'Victor'
s2= "I want to say\"Hi\""
print(s1+s2)
s3 = "First string\nSecond string"
print(s3)

first_name = "Sveta"
last_name = "Svetlana"
full_name = first_name + " " + last_name
print(full_name)
long_string = "Hello World"*5
print(long_string)
city = "New York"
temperature = 27.8
text = f"Today in {city} the temperature is {temperature}"
print(text)

word = "Privet"
print(word[0])
print(word[3])
print(word[1:4])
print(word[1:len(word)])
print(word[:2])
print(word[::-1])
print(word[-1])
text3 = " I like walking "
text4 = "i like walking "
print(text3)
print(text3.lower())
print(text3.upper())
print(text3.title())
print(text4.capitalize())

print(text3.strip())
print(text3.lstrip())
print(text3.rstrip())

print(text3.strip().replace('walking','hiking'))

text5 ="I like walking"
parts = text5.split(" ")
print(parts)
print(",".join(parts))
print(text5.find("walking"))

print("abracadabra".count("a"))
print("34586".isdigit())
print("fgrjt".isalpha())

#31.08.2026 "Year: 2026, month: 08, day: 31"
date_str = '31.08.2026'
day, month, year = date_str.split('.')
print(f"Year: {year}, Month: {month}, Day: {day}")