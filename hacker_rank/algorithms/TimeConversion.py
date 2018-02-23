#!/usr/bin/env python3
import sys


def timeConversion(s):
    hour = s[:2]
    rest = s[2:8]
    period = s[8:]

    result = "{hour}{rest}".format(hour=hour, rest=rest)

    if int(hour) == 12 and period == 'AM':
        result = "00{rest}".format(rest=rest)

    if period == 'PM':
        if int(hour) == 12:
            pass
        else:
            hour = str(int(hour) + 12)
            result = "{hour}{rest}".format(hour=hour, rest=rest)

    return result


s = input().strip()
result = timeConversion(s)
print(result)
