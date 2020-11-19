# encoding: UTF-8
import hmac
import threading
import time
import hashlib
import struct
import base64
import math

source_key = 'abcdefghijklmnop'

while True:
    key = base64.b32decode('ABCDEFGHIJKLMNOP')
    current_time = math.floor(time.time())
    seed = int(current_time / 30)
    print("time seed：", seed)
    digested_key = hmac.new(key, seed.to_bytes(8, byteorder="big"), hashlib.sha1).digest()
    print("key length：", len(digested_key))
    offset = digested_key[19] & 0xf
    print("offset：", offset)
    splitted_bytes = digested_key[offset: offset + 4]
    print("After splitted bytes：", bytes(splitted_bytes))
    unpacked_bytes = struct.unpack(">i", splitted_bytes)
    print("unpacked bytes：", unpacked_bytes[0])
    last_bytes = unpacked_bytes[0] & 0x7fffffff
    print("last bytes：", last_bytes)
    code1 = last_bytes % (10 ** 6)
    print("verify code：%06d" % code1)

    time.sleep(5)
