base_62 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"



# Traceback (most recent call last):
#   File "/home/runner/unit_tests.py", line 26, in test_to_base_10
#     self.assertEquals(to_base_10('LpuPe81bc2w'), 18327995462734721974)
# AssertionError: None != 18327995462734721974


# 1. For our first problem, write a function that converts a given base-62 string
#    into an integer. Only a single string will be provided, and it will be up to
#    11 characters in length.


# determine the value that the letter reprenents done
# determine the index postion for 62^n
# multiple value by representation and 62^index
# def to_base_10(videoId):
#
#     bits = len(videoId)
#     index = 0
#     total = 0
#
#     for item in videoId:
#         #determing the value
#         numeric_value = base_62.index(item)
#         #determine the index
#         n = bits - index - 1
#         #add all the values together
#         total = total + (numeric_value * 62 ** n)
#         index += 1
#
#     return total



#take number and divide it by 62 and take the find remainder at that division


# Traceback (most recent call last):
#   File "/home/runner/unit_tests.py", line 36, in test_to_base_62
#     self.assertEquals(to_base_62(18327995462734721974), 'LpuPe81bc2w')
# AssertionError: None != 'LpuPe81bc2w'

def to_base_62(number):
    value = number
    bits = len(str(number))
    list_of_bits =['0'] * bits

    index = 0

    while value > 0:
        rem = value % 62
        lsb = base_62[rem]
        list_of_bits[bits - index - 1] = lsb

        value = value // 62

        index += 1


    del list_of_bits[0: -index]


    return ''.join(list_of_bits)












to_base_62(18327995462734721974)



