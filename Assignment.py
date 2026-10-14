# Say "Hello, World!" With Python
if __name__ == '__main__':
    print("Hello, World!")

#Python If-Else

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
if n in range(1, 101):
    resto = n % 2
    if resto == 1 or n in range(6, 21):
        print("Weird")
    elif resto == 0:
        print("Not Weird")
else:
    pass
    
#Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a + b)
print(a - b)
print(a * b)
#Python: Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a //b)
print(a/b)
#Loops
if __name__ == '__main__':
    n = int(input())
for number in range(0, (n)):
    print(number*number)
#Write a function
def is_leap(year):
    leap = False
    if (year%4) == 0:
        leap = True
    if year %400 != 0 and year%100 == 0:
        leap = False
    return leap

#Print Function
if __name__ == '__main__':
    n = int(input())
    stringa = ""
    for i in range (1, n+1):
        stringa +=(str(i))
    print(stringa)
#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    myarray = [
        [i, j, k]
        for i in range(x + 1)
        for j in range(y + 1)
        for k in range(z + 1)
        if i + j + k != n
    ]
    print(myarray)
#Find the Runner-Up Score!if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
uniq = []
for number in arr:
    if number in uniq:
        pass
    else:
        uniq.append(number)

uniq.sort()


run = uniq[(len(uniq)-2)]

print(run)
#Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg_score = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg_score:.2f}")
#nested lists
if __name__ == '__main__':
    scorelist = []
    nested = []
    names = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scorelist.append(score)
        student = [name, score]
        nested.append(student)
        
    second_lowest = sorted(list(set(scorelist)))[1]
    for i in nested:
        if i[1] == second_lowest:
            names.append(i[0])
    names=sorted(names)
    for i in names:
        print(i)
        
#Lists
if __name__ == "__main__":
    N = int(input())
    ar = []
    for _ in range(N):
        command_args = input().strip().split(" ")
        cmd = command_args[0]
        if cmd == "print":
            print(ar)
        elif cmd == "sort":
            ar.sort()
        elif cmd == "reverse":
            ar.reverse()
        elif cmd == "pop":
            ar.pop()
        elif cmd == "remove":
            val = int(command_args[1])
            ar.remove(val)
        elif cmd == "append":
            val = int(command_args[1])
            ar.append(val)
        elif cmd == "insert":
            pos = int(command_args[1])
            val = int(command_args[2])
            ar.insert(pos, val)
#What's Your Name?
def print_full_name(first, last):
    print(f"Hello {first} {last}! You just delved into python.")
#Mutations
def mutate_string(string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)
    
#Find a string
def count_substring(string, sub_string):
    count_sub_string = 0
    for i in range(len(string) - len(sub_string) + 1):
        if string[i : i + len(sub_string)] == sub_string:
            count_sub_string += 1
    return count_sub_string

#String Validators
if __name__ == '__main__':
    s = input()
    flag_alnum = False
    flag_alpha = False
    flag_digit = False
    flag_lower = False
    flag_upper = False
    for i in s:
        if i.isalnum():
            flag_alnum = True
        if i.isalpha():
            flag_alpha = True
        if i.isdigit():
            flag_digit = True
        if i.islower():
            flag_lower = True
        if i.isupper():
            flag_upper = True

    print(flag_alnum)
    print(flag_alpha)
    print(flag_digit)
    print(flag_lower)
    print(flag_upper)
#split and join


def split_and_join(x):
    x = "-".join( x.split() )
    return x
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#String Formatting
def print_formatted(number):
    x = len(bin(number)[2:])
    for i in range(1, number + 1):
        o = oct(i)[2:]
        h = hex(i)[2:]
        h = h.upper()
        b = bin(i)[2:]
        d = str(i)
        print(f"{d:>{x}} {o:>{x}} {h:>{x}} {b:>{x}}")


#sWap cASE
def swap_case(s):
    swappdstrng = ""
    for char in s:
        if char.isupper():
            swappdstrng += char.lower()
        elif char.islower():
            swappdstrng += char.upper()
        else :
            swappdstrng += char
    return swappdstrng

#Text alignment
thickness = int(input())
c = "H"
# Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

# Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

# Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

# Bottom Cone
for i in range(thickness):
    print(
        (
            (c * (thickness - i - 1)).rjust(thickness)
            + c
            + (c * (thickness - i - 1)).ljust(thickness)
        ).rjust(thickness * 6)
    )
#Text Wrap

    
def wrap(string, max_width):
    return textwrap.fill(string, max_width)

#Capitalize!


def solve(s):
    # Split the string into words
    words = s.split(' ')
    
    # Capitalize each word
    capitalized_words = []
    for word in words:
        if word:  # Check if word is not empty
            # Capitalize first letter if it's alphabetic, keep rest as is
            capitalized = word[0].upper() + word[1:] if len(word) > 1 else word[0].upper()
            capitalized_words.append(capitalized)
        else:
            capitalized_words.append(word)
    
    # Join the words back with spaces
    return ' '.join(capitalized_words)


#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    t = tuple(integer_list)
    print(hash(t))

#introduction to sets
def average(array):
    heightsset = set(array)
    average = sum(heightsset) / len(heightsset)
    return average


#Symmetric Difference

first = int(input())
first = set(map(int, input().split()))
second = int(input())
second = set(map(int, input().split()))
symmetric_diff = first.symmetric_difference(second)
for element in sorted(symmetric_diff):
    print(element)

#linear algebra

import numpy as np


if __name__ == "__main__":
    np.set_printoptions(legacy="1.13")
    n = int(input())
    array = np.array([input().split() for _ in range(n)], float)
    print(np.linalg.det(array))

#designer door mat
N, M = map(int, input().split())
for i in range(1, N, 2):
    print(int((M - 3 * i) / 2) * "-" + (i * ".|.") + int((M - 3 * i) / 2) * "-")
print(int((M - 7) / 2) * "-" + "WELCOME" + int((M - 7) / 2) * "-")
for i in range(N - 2, -1, -2):
    print(int((M - 3 * i) / 2) * "-" + (i * ".|.") + int((M - 3 * i) / 2) * "-")

#alphabet rangoli
import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    
    lines = []
    
    # Generate all lines for the top half + middle
    for i in range(size):
        # For row i, we need letters from index (size-1) down to (size-1-i) and back
        left = []
        for j in range(i + 1):
            left.append(alphabet[size - 1 - j])
        
        # Create the line: left part + right part (mirror without center)
        right = left[-2::-1]  # Reverse left, excluding the center letter
        line = '-'.join(left + right)
        lines.append(line)
    
    # Calculate width based on the last (middle) line
    width = len(lines[-1])
    
    # Center all lines with dashes
    centered_lines = [line.center(width, '-') for line in lines]
    
    # Create full rangoli: top half + middle + bottom half (mirror)
    full_rangoli = centered_lines + centered_lines[-2::-1]
    
    print('\n'.join(full_rangoli))

#the minion game
def minion_game(string):
    vowels = 'AEIOU'
    kevin_score = 0
    stuart_score = 0
    length = len(string)
    
    for i in range(length):
        if string[i] in vowels:
            kevin_score += length - i
        else:
            stuart_score += length - i
    
    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")

#merge the tools!
def merge_the_tools(string, k):
    n = len(string)
    
    for i in range(0, n, k):
        substring = string[i:i+k]
        
        seen = set()
        result = []
        
        for char in substring:
            if char not in seen:
                result.append(char)
                seen.add(char)
        
        print(''.join(result))
#set add
n = int(input())
country_set = set()
for i in range(n):
    country = input()
    country_set.add(country)
print(len(country_set))
#set.union operation
en_subs = input()
en_set = set(map(int, input().split()))
fr_subs = input()
fr_set = set(map(int, input().split()))
united = (en_set.union(fr_set))
print(len(united))
#set.intersection operation
en_subs = input()
en_set = set(map(int, input().split()))
fr_subs = input()
fr_set = set(map(int, input().split()))
united = (en_set.intersection(fr_set))
print(len(united))
#set.symmetricdifference operation
en_subs = input()
en_set = set(map(int, input().split()))
fr_subs = input()
fr_set = set(map(int, input().split()))
diff = (en_set.symmetric_difference(fr_set))
print(len(diff))
#set.difference operation
en_subs = input()
en_set = set(map(int, input().split()))
fr_subs = input()
fr_set = set(map(int, input().split()))
diff = (en_set.difference(fr_set))
print(len(diff))
#check subset
cases = int(input())
for _ in range(cases):
    set1size = int(input())
    set1 = set(map(int, input().split()))
    set2size = int(input())
    set2 = set(map(int, input().split()))
    print(set1.issubset(set2))
#check strict superset
set1 = set(map(int, input().split()))
setsnumber = int(input())
supersbool = True
for _ in range(setsnumber):
    otherset = set(map(int, input().split()))
    if not set1.issuperset(otherset):
        supersbool = False
print(supersbool)
#set mutations
number_of_elements = int(input())
initial_set = set(map(int, input().split()))
number_of_other_sets = int(input())
for _ in range(number_of_other_sets):
    cmd = input().split()
    opt = cmd[0]
    other_set = set(map(int, input().split()))
    if opt == "difference_update":
        initial_set.difference_update(other_set)
    elif opt == "intersection_update":
        initial_set.intersection_update(other_set)
    elif opt == "symmetric_difference_update":
        initial_set.symmetric_difference_update(other_set)
    elif opt == "update":
        initial_set.update(other_set)
print(sum(initial_set))

#the captain's room
n = int(input())
numbers = list(map(int, input().split()))
numset = set(numbers)
numbersum = sum(numbers)
numsetsum = sum(numset) * n
diff = numsetsum - numbersum
for i in numset:
    if diff == ((n - 1) * i):
        print(i)
        break

#No idea!
from collections import Counter

n, m = map(int, input().split())
data = list(map(int, input().split()))
data_counter = Counter(data)
data_set = set(data)
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))
happiness = 0
for i in data_set & set_a:
    happiness += data_counter[i]
for i in data_set & set_b:
    happiness -= data_counter[i]
print(happiness)

#Collections.namedtuple()
from collections import namedtuple

n = int(input())
columns = ",".join(input().split())
Student = namedtuple("Student", columns)
data = []
for i in range(n):
    row = input().split()
    s = Student._make(row)
    data.append(s)
avg = sum(float(s.MARKS) for s in data) / n
print(f"{avg:.2f}")

#collections.Counter()
import collections


total_shoes = int(input())
shoe_sizes = list(map(int, input().split()))
inventory = collections.Counter(shoe_sizes)

total_customers = int(input())
total_revenue = 0

for _ in range(total_customers):
    size, price = map(int, input().split())
    if inventory.get(size) and inventory[size] > 0:
        total_revenue += price
        inventory[size] -= 1

print(total_revenue)

#Collections.OrderedDict()
from collections import OrderedDict

n = int(input())
items = OrderedDict()

for _ in range(n):
    line = input().rsplit(maxsplit=1)
    item_name = line[0]
    price = int(line[1])
    
    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item_name, net_price in items.items():
    print(item_name, net_price)

#Collections.deque()
import collections

n = int(input())
d = collections.deque()
for _ in range(n):
    cmd = list(input().strip().split())
    opt = cmd[0]
    if opt == "append":
        d.append(int(cmd[1]))
    elif opt == "appendleft":
        d.appendleft(int(cmd[1]))
    elif opt == "pop":
        d.pop()
    elif opt == "popleft":
        d.popleft()
for i in d:
    print(i, end=" ")

#Birthday Cake Candles
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    max_height = max(candles)
    return candles.count(max_height)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#DefaultDict Tutorial
from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    w = input()
    d[w].append(str(i + 1))
for _ in range(m):
    w = input()
    print(" ".join(d[w]) or -1)

#Word Order
from collections import Counter, OrderedDict


class OrderedCounter(Counter, OrderedDict):
    pass


word_ar = []
n = int(input())
for i in range(n):
    word_ar.append(input().strip())
word_counter = OrderedCounter(word_ar)
print(len(word_counter))
for word in word_counter:
    print(word_counter[word], end=" ")

#Company Logo
#!/bin/python3

import math
import os
import random
import re
import sys




from collections import Counter

s = input()

char_count = Counter(s)

sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))

for i in range(3):
    print(f"{sorted_chars[i][0]} {sorted_chars[i][1]}")

#piling up!
T = int(input())

for _ in range(T):
    n = int(input())
    cubes = list(map(int, input().split()))
    
    left = 0
    right = n - 1
    last_picked = float('inf')
    possible = True
    
    while left <= right:
        if cubes[left] >= cubes[right]:
            current = cubes[left]
            left += 1
        else:
            current = cubes[right]
            right -= 1
        
        if current <= last_picked:
            last_picked = current
        else:
            possible = False
            break
    
    print("Yes" if possible else "No")

#Calendar module
import calendar
import datetime

m, d, y = map(int, input().split())
input_date = datetime.date(y, m, d)
print(calendar.day_name[input_date.weekday()].upper())
#Time Delta
import datetime

cas = int(input())
time_format = "%a %d %b %Y %H:%M:%S %z"
for _ in range(cas):
    timestamp1 = input().strip()
    timestamp2 = input().strip()
    time_second1 = datetime.datetime.strptime(timestamp1, time_format)
    time_second2 = datetime.datetime.strptime(timestamp2, time_format)
    print(int(abs((time_second1 - time_second2).total_seconds())))



#Shape and Reshape
import numpy

arr = list(map(int, input().split()))
np_arr = numpy.array(arr)
print(numpy.reshape(np_arr, (3, 3)))

#Arrays


def arrays(arr):
    nuar = numpy.array(arr, float)
    return nuar[::-1]

#transpose and flatten
import numpy

n, m = map(int, input().split())
arr = []
for _ in range(n):
      row = list(map(int, input().split()))
      arr.append(row)

np_arr = numpy.array(arr)
print(numpy.transpose(np_arr))
print(np_arr.flatten())

#concatenate
import numpy as np



n, m, p = map(int, input().split())

arr1 = []
arr2 = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    arr1.append(tmp)
for _ in range(m):
    tmp = list(map(int, input().split()))
    arr2.append(tmp)
np_arr1 = np.array(arr1)
np_arr2 = np.array(arr2)
print(np.concatenate((np_arr1, np_arr2), axis=0))


#Zeros and Ones
import numpy as np

dimensions = tuple(map(int, input().split()))

zeros_array = np.zeros(dimensions, dtype=int)
ones_array = np.ones(dimensions, dtype=int)

print(zeros_array)
print(ones_array)


#Eye and Identity
import numpy as np



np.set_printoptions(legacy="1.13")
n, m = map(int, input().split())
print(np.eye(n, m, k=0))


#Array Mathematics
import numpy as np 
n, m = map(int, input().split())

ar1 = np.array([input().split() for _ in range(n)], int)
ar2 = np.array([input().split() for _ in range(n)], int)

print(ar1 + ar2)
print(ar1 - ar2)
print(ar1 * ar2)
print(ar1 // ar2)
print(ar1 % ar2)
print(ar1**ar2)



#Floor, Ceil and Rint
import numpy as np

np.set_printoptions(legacy="1.13")
arr = np.array(input().split(), float)
print(np.floor(arr))
print(np.ceil(arr))
print(np.rint(arr))





#Sum and Prod
import numpy as np 

n, m = map(int, input().split())

arr = np.array([input().split() for _ in range(n)], int)

s = np.sum(arr, axis = 0)
print(np.prod(s))



#Min and Max
import numpy as np

n, m = map(int, input().split())
arr = np.array([input().split() for _ in range(n)], int)
result = np.max(np.min(arr, axis=1))
print(result)


#Mean, Var, and Std
import numpy



n, m = map(int, input().split())
arr = numpy.array([input().split() for _ in range(n)], int)

print(numpy.mean(arr, axis=1))
print(numpy.var(arr, axis=0))
print(round(numpy.std(arr, axis=None), 11))



#Dot and Cross
import numpy



n = int(input())

arr1 = numpy.array([input().split() for _ in range(n)], int)
arr2 = numpy.array([input().split() for _ in range(n)], int)

print(numpy.dot(arr1, arr2))



#Inner and Outer
import numpy as np



arr1 = np.array(list(map(int, input().split())))
arr2 = np.array(list(map(int, input().split())))

print(np.inner(arr1, arr2))
print(np.outer(arr1, arr2))


#Polynomials
import numpy as np



p = np.array(list(map(float, input().split())), float)
x = float(input())
print(np.polyval(p, x))


#set.discard(), remove() & pop()
n = int(input())
s = set(map(int, input().split()))
numberofcommands = int(input())
for i in range(numberofcommands):
    currentcommand = list(input().split())
    if currentcommand[0] == "pop":
        s.pop()
    elif currentcommand[0] == "discard":
        s.discard(int(currentcommand[1]))
    elif currentcommand[0] == "remove":
        s.remove(int(currentcommand[1]))
print(sum(s))
    


#Detect floating point number
from re import compile, match

pattern = compile("^[-+]?\d*\.\d+$")
for _ in range(int(input())):
    print(bool(pattern.match(input())))


#group(), groups() & groupdict()
import re

s = input()
res = re.search(r"([A-Za-z0-9])\1", s)
if res is None:
    print(-1)
else:
    print(res[1])


#re.findall() & re.finditer()
import re

s = input()
result = re.findall(
    r"(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])",
    s,
)
if result:
    for i in result:
        print(i)
else:
    print(-1)


#re.start() & re.end()
import re

s = input().strip()
k = input().strip()
s_len = len(s)
found_flag = False
for i in range(s_len):
    match_result = re.match(k, s[i:])
    if match_result:
        start_index = i + match_result.start()
        end_index = i + match_result.end() - 1
        print((start_index, end_index))
        found_flag = True
if found_flag == False:
    print("(-1, -1)")


#validating roman numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

#validating phone numbers
from re import compile, match

n = int(input())
for _ in range(n):
    phone_number = input()
    condition = compile(r"^[7-9]\d{9}$")
    if bool(match(condition, phone_number)):
        print("YES")
    else:
        print("NO")


#validating and parsing email addresses
import email.utils
import re

n = int(input())
for _ in range(n):
    s = input()
    parsed_email = email.utils.parseaddr(s)[1].strip()
    match_result = bool(
        re.match(
            r"(^[A-Za-z][A-Za-z0-9\._-]+)@([A-Za-z]+)\.([A-Za-z]{1,3})$", parsed_email
        )
    )
    if match_result:
        print(s)


#Hexadecimal Color Code
import re

n = int(input())
inside_block = False

for _ in range(n):
    line = input()
    
    if '{' in line:
        inside_block = True
        
    if '}' in line:
        inside_block = False
        
    if inside_block and '{' not in line:
        matches = re.findall(r'#[0-9a-fA-F]{3,6}', line)
        
        for match in matches:
            if len(match) == 4 or len(match) == 7:
                print(match)


#html parser - part 1
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_attr(self, attrs):
        for attr_val_tuple in attrs:
            print("->", attr_val_tuple[0], ">", attr_val_tuple[1])

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        self.handle_attr(attrs)

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        self.handle_attr(attrs)


parser = CustomHTMLParser()

n = int(input())

s = "".join(input() for _ in range(n))
parser.feed(s)


#html parser - part 2
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_comment(self, data):
        number_of_line = len(data.split("\n"))
        if number_of_line > 1:
            print(">>> Multi-line Comment")
        else:
            print(">>> Single-line Comment")
        if data.strip():
            print(data)

    def handle_data(self, data):
        if data.strip():
            print(">>> Data")
            print(data)


parser = CustomHTMLParser()

n = int(input())

html_string = "".join(input().rstrip() + "\n" for _ in range(n))
parser.feed(html_string)
parser.close()



#Detect HTML Tags, Attributes and Attribute Values
from html.parser import HTMLParser


class CustomHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)

    def handle_startendtag(self, tag, attrs):
        print(tag)
        self.handle_attrs(attrs)

    def handle_attrs(self, attrs):
        for attrs_pair in attrs:
            print("->", attrs_pair[0].strip(), ">", attrs_pair[1].strip())


n = int(input())
html_string = "".join(input() for _ in range(n))
customHTMLParser = CustomHTMLParser()
customHTMLParser.feed(html_string)
customHTMLParser.close()


#Validating UID
import re

n = int(input())
upper_check = r".*([A-Z].*){2,}"
digit_check = r".*([0-9].*){3,}"
alphanumeric_and_length_check = r"([A-Za-z0-9]){10}$"
repeat_check = r".*(.).*\1"
for _ in range(n):
    uid_string = input().strip()
    upper_check_result = bool(re.match(upper_check, uid_string))
    digit_check_result = bool(re.match(digit_check, uid_string))
    alphanumeric_and_length_check_result = bool(
        re.match(alphanumeric_and_length_check, uid_string)
    )
    repeat_check_result = bool(re.match(repeat_check, uid_string))
    if (
        upper_check_result
        and digit_check_result
        and alphanumeric_and_length_check_result
        and not repeat_check_result
    ):
        print("Valid")
    else:
        print("Invalid")


#Validating credit card numbers
import re

n = int(input())
for _ in range(n):
    credit = input().strip()
    credit_removed_hiphen = credit.replace("-", "")
    valid = True
    length_16 = bool(re.match(r"^[4-6]\d{15}$", credit))
    length_19 = bool(re.match(r"^[4-6]\d{3}-\d{4}-\d{4}-\d{4}$", credit))
    consecutive = bool(re.findall(r"(?=(\d)\1\1\1)", credit_removed_hiphen))
    if length_16 == True or length_19 == True:
        if consecutive == True:
            valid = False
    else:
        valid = False
    if valid:
        print("Valid")
    else:
        print("Invalid")


#Matrix Script
import re

n, m = map(int, input().split())
character_ar = [""] * (n * m)
for i in range(n):
    line = input()
    for j in range(m):
        character_ar[i + (j * n)] = line[j]
decoded_str = "".join(character_ar)
final_decoded_str = re.sub(
    r"(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])", " ", decoded_str
)
print(final_decoded_str)


#Regex Substitution
import re
import sys

n = int(input())
for line in sys.stdin:
    remove_and = re.sub(r"(?<= )(&&)(?= )", "and", line)
    remove_or = re.sub(r"(?<= )(\|\|)(?= )", "or", remove_and)
    print(remove_or, end="")


#zipped!
x1, x2 = map(int, input().split())
scores = []
for _ in range(x2):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))


#ginortS
orig_str = input()
lowercase = []
uppercase = []
oddnums = []
evennums = []
for char in orig_str:
    if char.islower():
        lowercase.append(char)
    elif char.isupper():
        uppercase.append(char)
    elif char.isdigit():
        if int(char) % 2 == 1:
            oddnums.append(char)
        else:
            evennums.append(char)

lowercase.sort()
uppercase.sort()
oddnums.sort()
evennums.sort()

result = ''.join(lowercase + uppercase + oddnums + evennums)
print(result)


#athlete sort
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)

#Exeptions
n = int(input())
for _ in range(n):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print(f"Error Code: {e}")


#Map and Lambda Function
cube = lambda x: x * x * x

def fibonacci(n):
    ar = [0, 1]
    if n < 2:
        return ar[:n]
    for i in range(2, n):
        ar.append(ar[i - 1] + ar[i - 2])
    return ar



#XML 1 - Find the Score



def get_attr_number(node):
    total = len(node.attrib.keys())
    for child in node:
        if child:
            total += get_attr_number(child)
        else:
            total += len(child.attrib.keys())
    return total


#XML2 - Find the Maximum Depth


maxdepth = 0


def depth(elem, level):
    global maxdepth
    level = level + 1
    maxdepth = max(maxdepth, level)
    for child in elem:
        depth(child, level)



#Standardize mobile number
def wrapper(f):
    def fun(l):
        formatted = []
        for number in l:
            num = number[-10:]  # last 10 digits
            formatted.append(f"+91 {num[:5]} {num[5:]}")
        return f(formatted)
    return fun



#decorators 2 - name directory



def person_lister(func):
    def inner(people):
        return [func(p) for p in sorted(people, key=lambda x: (int(x[2])))]

    return inner


#number line jumps
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kangaroo' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER v1
#  3. INTEGER x2
#  4. INTEGER v2
#

def kangaroo(x1, v1, x2, v2):
    if v1 <= v2 and x1 < x2:
        return "NO"
    if (v1 != v2) and ((x2 - x1) % (v1 - v2) == 0):
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#viral advertising#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    shared = 5      
    cumulative = 0  

    for _ in range(n):
        liked = shared // 2          
        cumulative += liked          
        shared = liked * 3           

    return cumulative

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()


#recursive digit sum
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#

def superDigit(n, k):

    initial_sum = sum(int(d) for d in n) * k

    def find_super_digit(x):
        if x < 10:
            return x
        return find_super_digit(sum(int(d) for d in str(x)))

    return find_super_digit(initial_sum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()


#insertion sort - part 1
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    arr1[n-1] = n
    print(arr1)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


#insertion sort - part 2

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    value = arr[-1] 
    i = n - 2      
    while i >= 0 and arr[i] > value:
        arr[i + 1] = arr[i]
        print(*arr) 
        i -= 1

    arr[i + 1] = value  
    print(*arr)         

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)


