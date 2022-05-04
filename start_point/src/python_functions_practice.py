def return_10():
    return 10

def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2
    
def divide(num_1, num_2):
    return num_1 / num_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(num_1, num_2):
    int_1 = int(num_1)
    int_2 = int(num_2)
    return int_1 +int_2

def number_to_full_month_name(num):
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
    return months[num - 1]

def number_to_short_month_name(num):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
          'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    return months[num - 1]

def measure_volume(num):
    return num ** 3 

def reverse(string):
    return string[::-1]

def temp_convert(temp_f):
    temp_c = temp_f - 32
    num = 5/9
    temp_c = temp_c * num
    return temp_c