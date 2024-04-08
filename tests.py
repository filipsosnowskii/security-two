# import unittest
import ctypes
# from aes.aes import AES, encrypt, decrypt

rijndael = ctypes.CDLL('./rijndael.so')

buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
block = ctypes.create_string_buffer(buffer) 

# class TestBlock(unittest.TestCase):

def test_aes_encrypt():
        key_buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
        key_buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
        key = ctypes.create_string_buffer(key_buffer)
        # print(*key, *block)
        # result = ctypes.string_at(rijndael.expand_key(*key), 176)
        variable = rijndael.aes_encrypt_block(block, key)
        variable = ctypes.c_void_p(variable)
        print("Python variable")
        print(variable)
        print(type(variable))
        result = ctypes.string_at(variable, 1)
        # result = ctypes.wstring_at(rijndael.expand_key(key), 16)
        # print(*key)
        print(result)

test_aes_encrypt()