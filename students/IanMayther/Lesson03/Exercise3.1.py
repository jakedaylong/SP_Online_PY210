#Exercise3.1.py

#Exercise 3.1 Objective:
"""
Write some functions that take a sequence as an argument, and return a copy of that sequence:

    #1 - with the first and last items exchanged.
    #2 - with every other item removed.
    #3 - with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
    #4 - with the elements reversed (just with slicing).
    #5 - with the last third, then first third, then the middle third in the new order.
"""

#1 - with the first and last items exchanged function
def swap_first_last(seq):
    first = seq[:1]
    middle = seq[1:-1]
    last = seq[-1:]
    return last + middle + first

#2 - with every other item removed.
def remove_every_other(seq):
    return seq[::2]

#3 - with the first 4 and the last 4 items removed, and then every other item in the remaining sequence.
def FirstFour_LastFour_EveryOther(seq):
    return seq[4:-4:2]

#4 - with the elements reversed (just with slicing).
def reverse_it(seq):
    return seq[::-1]

if __name__ == "__main__":
    # run some tests
    a_string = "this is a string"
    a_tuple = (2, 54, 13, 12, 5, 32) 

    print(swap_first_last(a_string))
    print(swap_first_last(a_tuple))
    print(remove_every_other(a_string))
    print(remove_every_other(a_tuple))
    print(FirstFour_LastFour_EveryOther(a_string))
    print(FirstFour_LastFour_EveryOther(a_tuple))
    print(reverse_it(a_string))
    print(reverse_it(a_tuple))
    #assert swap_first_last(a_string) == "ghis is a strint"
    #assert swap_first_last(a_tuple) == (32, 54, 13, 12, 5, 2)