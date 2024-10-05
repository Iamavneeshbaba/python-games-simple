def is_lucky_number(number):
    str_num = str(number)
    p = len(str_num)
    total_sum = sum(int(digit) ** p for digit in str_num)
    if total_sum == number:
        return "Lucky"
    else:
        return "Not Lucky"
num = int(input("Enter a number: "))
result = is_lucky_number(num)
print(result)
