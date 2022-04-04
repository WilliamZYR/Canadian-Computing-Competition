# https://dmoj.ca/problem/ccc02s2

numerator = int(input())
denominator = int(input())
if numerator % denominator == 0:
    print(int(numerator / denominator))
else:
    integer = numerator // denominator
    remainder = numerator % denominator
    gcd = 1  # greatest common divisor
    for i in range(1, denominator + 1):
        if remainder % i == 0 and denominator % i == 0 and i > gcd:
            gcd = i
    if integer == 0:
        print(str(int(remainder/gcd)) + "/" + str(int(denominator/gcd)))
    else:
        print(integer, str(int(remainder/gcd)) + "/" + str(int(denominator/gcd)))
