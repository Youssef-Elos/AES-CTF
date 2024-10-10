from pwn import xor

a = bytes.fromhex("3b294664354dee891482a6be796db6713d7f0f4f4f17441fb02419ea2ee7ad56d5378e8376822218f3e1fa97ff2ad436bf1a3c1a94a41a0909217aa092a7ec118a34e32812014251b91e94b1cd09ba48a1f81aec7d55deddb7301143b643200fab0d0ef44c830bd7691f7575de5ee4be737fe0fa3a03d4465e78b878b9196cec9da44ff3afe0227764546e1bcff0a2664ed9")
b = bytes.fromhex("36341f66284be1986b9eb9f36c6bad6e2d7e0f146f1d4900f53319ff7afbac1898259c833780294dfdf6f186ff2ac236a6156e4ebd846967251b5ba9")

test = b"No right of private conversation was enumerated in the Constitution. I don't suppose it occurred to anyone at the time that it could be prevented."

key = xor(a, test)
result = xor(key, b)

print(result[:len(b)].decode('utf-8'))
