## 3. Read the File Into a String ##

File = open("dq_unisex_names.csv", "r")
names = File.read()

## 4. Convert the String to a List ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split("\n")
first_five = names_list[0:5]
print(first_five)

## 5. Convert the List of Strings to a List of Lists ##

f = open('dq_unisex_names.csv', 'r')
names = f.read()
names_list = names.split('\n')
nested_list = []
for names in names_list:
    comma_list = names.split(',')
    nested_list.append(comma_list)
print(nested_list)

## 6. Convert Numerical Values ##

print(nested_list[0:5])
numerical_list = []
for num in nested_list:
    print(num)
    print(len(num))
    if len(num) == 2:
        name = num[0]
        number = float(num[1])
        numerical_list.append([name, number])
print(numerical_list[0:5])


## 7. Filter the List ##

# The last value is ~100 people
numerical_list[len(numerical_list)-1]
thousand_or_greater = []
count = 0
for num in numerical_list:
    if num[1] >= 1000:
        thousand_or_greater.append(num[0])
    count += 1
print(thousand_or_greater[0:10])
