import base64
import codecs
import json
import telnetlib

import Crypto.Util.number

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)


def readline():
    return tn.read_until(b"\n")


def json_recv():
    line = readline()
    return json.loads(line.decode())


def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)


for i in range(100):
    recieved = json_recv()
    encoding = recieved['type']
    encoded = recieved['encoded']

    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif encoding == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif encoding == "rot13":
        decoded = codecs.decode(encoded, "rot13")
    elif encoding == "bigint":
        decoded = Crypto.Util.number.long_to_bytes(int(encoded, 16)).decode()
    elif encoding == "utf-8":
        decoded = "".join(chr(o) for o in encoded)

    print(f"{i + 1}) {encoding}:")
    print(f"{encoded} ---> {decoded}\n")

    json_send(
        {"decoded": decoded}
    )

flag = readline()
flag = json.loads(flag.decode())
print("\nFlag:")
print(str(flag["flag"]))
