import functools
def count_substring(string, sub_string):
    substring_count = 0
    j = 0
    while j < len(string) - len(sub_string):
        new_substring = ""
        for i in string[j:len(sub_string) - 1 + j]:
            j += 1
            new_substring = new_substring + i
            print(new_substring)
        if new_substring == sub_string:
            substring_count += 1
    return substring_count


def string_problem():
    alpha_num_found = False
    alpha_found = False
    is_lower = False
    is_supper = False
    digit_found = False
    s = input()
    for i in s:
        if i.isalnum():
            print('True')
            alpha_num_found = True
            break
    if not alpha_num_found:
        print('False')

    for i in s:
        if i.isalpha():
            print('True')
            alpha_found = True
            break
    if not alpha_found:
        print('False')

    for i in s:
        if i.isdigit():
            print(True)
            digit_found = True
            break
    if not digit_found:
        print('False')

    for i in s:
        if i.islower():
            print('True')
            is_lower = True
            break
    if not is_lower:
        print('False')

    for i in s:
        if i.isupper():
            print('True')
            is_supper = True
            break
    if not is_supper:
        print('False')


def string_problem_s2():
    s = input()
    print(any(x.isalnum for x in s))
    print(any(x.isalpha for x in s))
    print(any(x.isdigit for x in s))
    print(any(x.islower for x in s))
    print(any(x.isupper for x in s))


string_problem_s2()


def string_problem_s3():
    str = input()
    arr = [False] * 5

    for letter in str:
        if letter.isalnum():
            arr[0] = True
        if letter.isalpha():
            arr[1] = True
        if letter.isdigit():
            arr[2] = True
        if letter.islower():
            arr[3] = True
        if letter.isupper():
            arr[4] = True

    print(arr[0])
    print(arr[1])
    print(arr[2])
    print(arr[3])
    print(arr[4])

def string_problem_s4():
    a = raw_input()
    print(any(map(lambda str: str.isalnum(), list(a))))
    print(any(map(lambda str: str.isalpha(), list(a))))
    print(any(map(lambda str: str.isdigit(), list(a))))
    print(any(map(lambda str: str.islower(), list(a))))
    print(any(map(lambda str: str.isupper(), list(a))))


def string_problem_s4():
    a = input()
    print(any(map(lambda str: str.isalnum(), list(a))))
    print(any(map(lambda str: str.isalpha(), list(a))))
    print(any(map(lambda str: str.isdigit(), list(a))))
    print(any(map(lambda str: str.islower(), list(a))))
    print(any(map(lambda str: str.isupper(), list(a))))


def string_problem_s5():
    S = input().strip()
    print('hi')
    print(functools.reduce(lambda x, y: x | y, map(lambda x: x.isalnum(), S)))
    print(functools.reduce(lambda x, y: x | y, map(lambda x: x.isalpha(), S)))
    print(functools.reduce(lambda x, y: x | y, map(lambda x: x.isdigit(), S)))
    print(functools.reduce(lambda x, y: x | y, map(lambda x: x.islower(), S)))
    print(functools.reduce(lambda x, y: x | y, map(lambda x: x.isupper(), S)))


string_problem_s5()