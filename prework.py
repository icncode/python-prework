# Question 1
def hello_name(user_name):
    print("Hello", user_name.title() + "!")

hello_name('jake')

# Question 2
def first_odds():
    for i in range(1,101):
        if i % 2 != 0:
            print(i)

first_odds()

# Question 3
def max_num_in_list(a_list):
    max = a_list[0]
    for num in a_list:
        if num > max:
            max = num
    return max

print(max_num_in_list([1, 2, 8, 16, 2, 4, 4]))

# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0):
        return True
    else:
        return False

leap_years = [2001, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, 2040]
print(is_leap_year(2004))

# Question 5
def is_consectutive(a_list):
    if len(a_list) > 1: 
        for i in range(len(a_list)-1):
            if a_list[i+1] - a_list[i] != 1:
                return False
    return True

print(is_consectutive([6, 7, 8, 9, 10]))