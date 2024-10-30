def armstrong_checker(number):
    count_numbers = len(str(number))
    current_number = number
    sum_of_all_numbers = 0

    while current_number != 0:
        last_number = current_number % 10
        sum_of_all_numbers = sum_of_all_numbers + (last_number ** count_numbers)
        current_number = current_number // 10

    if sum_of_all_numbers == number:
        print(f"{number} is an Armstong number.")
    else:
        print(f"{number} is NOT an Armstrong number.")

user_input = int(input("Enter a number to check: "))
armstrong_checker(user_input)
