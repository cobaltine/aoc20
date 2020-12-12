from datetime import datetime
from main import (
    decode_seats,
    find_my_seat,
    read_input,
)

# [TEST1] Verify that highest ID is correctly found from test dataset
input = read_input(path='input_test.txt')
decoded_file = decode_seats(enc=input)
if decoded_file[-1] != 820:
    raise Exception(
        f'{datetime.now()} - ERROR: Highest value should be 820, but got \'{decoded_file[-1]}\'')

# [TEST2] Verify that missing id '3' (my seat) is correctly found from test dataset
decoded_sim = [1, 2, 4, 5, ]
if find_my_seat(seats=decoded_sim) != 3:
    raise Exception(f'{datetime.now()} - ERROR: My seat was not found')

print(f'{datetime.now()} - OK: all tests passed!')
