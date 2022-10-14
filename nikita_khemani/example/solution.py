test_case = [9, 1, 8, 16]


def find_exponent(base, to_equal):
    exp_ = 1
    tmp_ = base
    print(f"Base : {base} to match {to_equal}")
    while tmp_ != to_equal:
        print(f" base: {base} - tmp {tmp_} - exp - {exp_}")
        tmp_ = tmp_ * base
        exp_ += 1
        if exp_ == 100: #to prevent infinite run
            break
    return exp_


def calculate_power(list_):
    result = []

    for each_case in list_:
        if each_case == 1:
            result.append(1)
        elif each_case % 2 == 0:
            result.append([2, find_exponent(2, each_case)])
        elif each_case % 3 == 0:
            result.append([3, find_exponent(3, each_case)])
        elif each_case % 5 == 0:
            result.append([5, find_exponent(5, each_case)])
    print("Final Answer")
    return result


print(calculate_power(test_case))