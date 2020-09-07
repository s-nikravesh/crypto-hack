k1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
k2_k1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
k2_k3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
flag_k1_k3_k2 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

k1_ord = [o for o in bytes.fromhex(k1)]
k2_k3_ord = [o for o in bytes.fromhex(k2_k3)]
flag_k1_k3_k2_ord = [o for o in bytes.fromhex(flag_k1_k3_k2)]

flag_k1_ord = [
    o_f132 ^ o23 for (o_f132, o23) in zip(flag_k1_k3_k2_ord, k2_k3_ord)
]
flag_ord = [o_f1 ^ o1 for (o_f1, o1) in zip(flag_k1_ord, k1_ord)]
flag = "".join(chr(o) for o in flag_ord)

print("Flag:")
print(flag)
