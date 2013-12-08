from random import choice

first_begin = ['bil', 'jil', 'sil', 'mil', 'led', 'kar', 'ig', 'gla']
first_end = ['fred', 'hed', 'sky', 'ron', 'ky', 'poop']

print choice(first_begin) + choice(first_end) + " Lastname"
raw_input("Hit enter to continue")
    
while True:
    print choice(first_begin) + choice(first_end) + " Lastname"
    raw_input()
    