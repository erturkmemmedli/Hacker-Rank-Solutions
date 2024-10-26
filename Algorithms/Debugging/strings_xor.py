# XOR Strings


def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:  # change 1
            res += '0';  # change 2
        else:
            res += '1';  # change 3

    return res

s = input()
t = input()
print(strings_xor(s, t))
