import re

with open(r"C:\Users\admin\Downloads\employee_data.txt", "r") as file:
    text = file.read()
    print(text)
original_number=re.findall("\d{10}",text)
number=original_number
print("Original Number : Masked Number")
for number in original_number:
    result=re.sub(r"\d{10}+","xxxxxxxxxx",number)
    print(f"{number}:{result}")