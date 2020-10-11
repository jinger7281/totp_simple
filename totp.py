# encoding: UTF-8
import hmac
import threading
import time
import hashlib
import struct
import base64
import math

source_key = 'abcdefghijklmnop'

def DT(_str):
    offsetBits = _str[19] & 0xf
    print("Offset:", offsetBits)
    splited_bytes = _str[offsetBits: offsetBits + 4]
    print("splited_bytes:", splited_bytes)
    p = struct.unpack('>i', splited_bytes)
    print("unpacked string:", p[0])
    p = p[0]
    return p & 0x7fffffff

def gen_origin_key(k):
    c = str(round(round(time.time()) / 30))
    mac = hmac.new(k, c.encode(), hashlib.sha1).digest()
    # mac = b'\x1f\x86\x98\x69\x0e\x02\xca\x16\x61\x85\x50\xef\x7f\x19\xda\x8e\x94\x5b\x55\x5a'
    Sbits = DT(mac)
    print(Sbits % (10 ** 6))
    print(len(mac))
    print(mac)
print(str(round(time.time())))
while True:
    key = base64.b32decode('ABCDEFGHIJKLMNOP')
    current_time = math.floor(time.time())
    seed = int(current_time / 30)
    print("时间种子：", seed)
    digested_key = hmac.new(key, seed.to_bytes(8, byteorder="big"), hashlib.sha1).digest()
    print("key长度：", len(digested_key))
    offset = digested_key[19] & 0xf
    print("偏移量：", offset)
    splitted_bytes = digested_key[offset: offset + 4]
    print("切割后字符：", bytes(splitted_bytes))
    unpacked_bytes = struct.unpack(">i", splitted_bytes)
    print("解包后字符：", unpacked_bytes[0])
    last_bytes = unpacked_bytes[0] & 0x7fffffff
    print("最后需要的字符：", last_bytes)
    code1 = last_bytes % (10 ** 6)
    print("验证码：", code1)

    time.sleep(5)