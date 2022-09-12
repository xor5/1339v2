import os,sys,random,secrets,string,marshal,base64,subprocess
if len(sys.argv) < 2:
    print("add some args bitch")
    exit(-1337)

input = sys.argv[1]
filename = input.split('.')
output = "{}_1339v2.py".format(filename[0])

def semifuscate(payload):
    var1 = 64
    payloadname = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(16))
    b64 = r'\x62\x61\x73\x65\x36\x34'
    bbreak = base64.b16encode(b"break")
    bnone = base64.b16encode(b"None")

    data = payload
    bdata = base64.b16encode(data.encode('utf-8'))
    bdata = [bdata[i:i+8] for i in range(0, len(bdata), 8)]
    data = "None;" * var1 + f"{payloadname} = '';"
    for i in range(len(bdata)):
        n1 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(16))
        n2 = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(16))
        r1 = random.randint(0, 256)
        r2 = random.randint(256, 512)
        data = data + f"{n1} = {r1}; {n2} = {r2}\n"
        data = data + "None;" * var1 + f"\ntry:\n\twhile True:\n\t\tif {n1} < {n2}:" + f"{payloadname} += \"" + bdata[i].decode('utf-8') + f"\";__import__(\"builtins\").exec(__import__('{b64}').b16decode({bbreak}{bnone*random.randint(0, 256)}))" + "\nexcept: pass;" + "None;" * var1 + "\n"
    data = data + "None;" * var1 + f'__import__("builtins").exec(__import__("{b64}").b16decode({payloadname}))' + ";None" * var1
    return data

def obfuscate():
    with open(input, 'rb+') as f1:
        with open(output, 'w') as f2:
            al = string.ascii_letters + string.digits
            al2 = string.ascii_letters

            r1 = ''.join(secrets.choice(al) for i in range(128))
            r2 = ''.join(secrets.choice(al2) for i in range(128))
            r3 = ''.join(secrets.choice(al2) for i in range(128))

            s1 = random.randint(0, 1000000000)
            s2 = random.randint(0, 1000000000)
            
            clr = '__import__("builtins").exec(__import__("base64").b16decode(b"5F5F696D706F72745F5F282273797322292E6D6F64756C65735B5F5F6E616D655F5F5D2E5F5F646963745F5F2E636C6561722829"))'

            payload = f1.read() + bytes(f';{clr}'.encode('utf-8'))

            payload = base64.a85encode(marshal.dumps(compile(payload, r1, "exec")))
            payload = "{} = {}; {} = {} + {};\nif {} < {}:\n while True:\n   __import__(\"builtins\").exec(__import__(\"marshal\").loads(__import__(\"base64\").a85decode({})));break".format(r2,s1,r3,r2,s2,r2,r3,payload)
            payload = semifuscate(payload)
            payload = base64.b16encode(payload.encode('utf-8'))
            payload = "if \"fishhook\" not in __import__(\"sys\").modules:\n\t__import__(\"builtins\").exec(__import__(\"base64\").b16decode({}))\nelse: __import__(\"builtins\").exec(\"del fishhook\")".format(payload)
            payload = base64.a85encode(marshal.dumps(compile(payload, '__file__ = __main__', "exec")))
            payload = "'''\nleet hax0r code\n'''\n\n" * 64 + f'__import__("builtins").exec(__import__("marshal").loads(__import__("base64").a85decode({payload})))'

            f1.close()
            
            f2.write(payload)
            print(f"Sucessfully obfuscated {input}")
            print(f"Result wrote in {output}")

            f2.close()

def init():
    print("1337v2 x7733 @udp:587 || ratted")
    obfuscate()
    
if __name__ == "__main__":
    init()
