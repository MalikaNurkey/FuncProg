#1
string = input("Введите число: ")
if string.isnumeric():
    number = int(string)
    print(number)


#2
name = "hello.py"
starts = name.startswith("hello")
ends = name.endswith("exe")
print(starts)
print(ends)


#3
string = "   hello  world!  "
string = string.strip()
print(string)


#4
text = "Hello world! Goodbye world!"
index = text.find("wor")
print(index)


#5
name = "malika"
edited_name = name.replace("a", "O")
print(edited_name)


#6
word = "a,n,t,o,n"
split_word = word.split(',')
print(split_word)


#7
word = "cfsaajnaud"
length = word.count('a')
print(length)


#8
word = word.lower()
print(word)


#9
word = word.capitalize()
print(word)


#10
word = word.upper()
print(word)

