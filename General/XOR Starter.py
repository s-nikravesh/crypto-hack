string = "label"
integer = 13

unicode_repr = [ord(c) for c in string]
xor_unicode = [13 ^ i for i in unicode_repr]
xor_string = "".join(chr(o) for o in xor_unicode)

flag = "crypto{" + xor_string + "}"
print("Flag:")
print(flag)
