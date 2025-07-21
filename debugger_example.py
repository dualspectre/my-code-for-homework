
def is_odd(number: int) -> bool:
    """
    Function that receives a number and return True if it is odd
    """
    return number % 2 != 0
    

#print_odd_numbers
def print_odd_numbers(number_list):
    """
    A function that receive odd numbers from list
    """
    for number in number_list:
        if number % 2 != 0:
            print(number)

# numbers = [1,2,3,4,5,6, 7, 8, 9]
# print_odd_numbers(numbers)

print(is_odd("Hello"))

