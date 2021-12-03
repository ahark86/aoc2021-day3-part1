with open('input.txt') as input_file:
    input = [item.strip() for item in input_file.readlines()]


def bin_to_dec(bin_num):
    dec_num = 0
    power = len(str(bin_num)) - 1
    for digit in str(bin_num):
        to_add = int(digit) * 2 ** power
        dec_num += to_add
        power -= 1
    return dec_num


def calc_gamma_rate(input_list):
    gamma_rate = ''
    total_0 = 0
    total_1 = 0
    for n in range(0, len(input[0])):
        for reading in input_list:
            if reading[n] == '0':
                total_0 += 1
            else:
                total_1 += 1
        if total_0 > total_1:
            gamma_rate += '0'
        else:
            gamma_rate += '1'
        total_0 = 0
        total_1 = 0
    return gamma_rate


def calc_epsilon_rate(gr):
    eps_rate = ''
    for digit in gr:
        if digit == '1':
            eps_rate += '0'
        else:
            eps_rate += '1'
    return eps_rate


gamma_rate = calc_gamma_rate(input)
dec_gamma_rate = bin_to_dec(gamma_rate)
print(gamma_rate)

epsilon_rate = calc_epsilon_rate(gamma_rate)
dec_epsilon_rate = bin_to_dec(epsilon_rate)
print(epsilon_rate)

print(dec_gamma_rate)
print(dec_epsilon_rate)
print(dec_gamma_rate * dec_epsilon_rate)
