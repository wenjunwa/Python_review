# indexing = accessing elements of a sequence using [] (indexing operator)
#           [Start: end : step]

credit_number = "1234-5678-912-3456"
#access elements of string
print(credit_number[4])
print(credit_number[:4])
print(credit_number[5:9])
print(credit_number[10:])
print(credit_number[-5:])
print(credit_number[6::3])

#print last 4 digits
last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXX-{last_digits}")

#revers the string
reverse_string = credit_number[::-1]
print(f"{reverse_string}")