#!/usr/bin/python


def digit_sum(number):
    sum_ = 0
    for digit in str(number):
        sum_ += int(digit)
    return sum_

a = digit_sum(1234)
print a