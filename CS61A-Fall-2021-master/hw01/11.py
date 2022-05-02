def k_in_num(k, num):
    while num != 0:
        if k == num % 10:
            return True
    return False

k_in_num(3,123)