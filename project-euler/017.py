#!/usr/bin/env python3
def letter_count_for_number(x):
    one_digit = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
    }

    two_digits = {
        2: 'twenty',
        3: 'thirty',
        4: 'forty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }

    def resulting_length(res):
        result = res.replace(" ", "")
        return len(result)

    number_length = len(str(x))

    if number_length == 1:
        return len(one_digit[x])

    if number_length == 2 and x < 20:
        return len(one_digit[x])

    if number_length == 2:
        res = ''
        res += two_digits[int(str(x)[0])]
        if int(str(x)[1]) == 0:
            return len(res)
        res += ' '
        res += one_digit[int(str(x)[1])]
        return resulting_length(res)

    if number_length == 3:
        res = ''
        res += one_digit[int(str(x)[0])]
        res += ' '
        res += 'hundred'
        if int(str(x)[1]) == 0 and int(str(x)[2]) == 0:
            return resulting_length(res)
        res += ' '
        res += 'and'
        res += ' '
        if int(str(x)[1]) == 0:
            res += one_digit[int(str(x)[2])]
            return resulting_length(res)

        # 110-119
        if int(str(x)[1]) == 1:
            number = int(str(x)[1] + str(x)[2])
            res += one_digit[number]
            return resulting_length(res)

        # 120, 130...
        if int(str(x)[2]) == 0:
            res += two_digits[int(str(x)[1])]
            return resulting_length(res)

        res += two_digits[int(str(x)[1])]
        res += ' '
        res += one_digit[int(str(x)[2])]
        return resulting_length(res)

    if number_length == 4:
        return resulting_length('one thousand')


def solve():
    letter_count = 0
    for x in range(1, 1001):
        letter_count += letter_count_for_number(x)

    return letter_count


if __name__ == '__main__':
    result = solve()
    print(result)
