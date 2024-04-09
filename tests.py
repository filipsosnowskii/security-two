import unittest
import ctypes
from aes.aes import AES, encrypt, decrypt

rijndael = ctypes.CDLL('./rijndael.so')

buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
block = ctypes.create_string_buffer(buffer) 

key_buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
key_buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
key = ctypes.create_string_buffer(key_buffer)

block2 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
key2 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

class TestBlock(unittest.TestCase):

        def test_aes_encrypt(self):
        # print(*key, *block)
        # result = ctypes.string_at(rijndael.expand_key(*key), 176)
                rijndael.aes_encrypt_block.restype = ctypes.c_void_p
                rijndael.aes_decrypt_block.restype = ctypes.c_void_p
        # variable = rijndael.aes_encrypt_block(block, key)
        # variable = ctypes.c_void_p(variable)
        # print("Python variable")
        # print(variable)
        # print(type(variable))
                results = ctypes.string_at(rijndael.aes_encrypt_block(block, key), 16)
        # result = ctypes.wstring_at(rijndael.expand_key(key), 16)
        # print(*key)
        # print(hex(*results))
                # for result in results:
                #         print(hex(ctypes.c_ubyte(result).value))
                results2 = AES(bytes(key2)).encrypt_block(bytes(block2))
                d1 = ctypes.string_at(rijndael.aes_decrypt_block(results, key), 16)
                d2 = AES(bytes(key2)).decrypt_block(bytes(results2))
                self.assertEqual(d1, d2)
      

# test_aes_encrypt()
def run():
    unittest.main()

if __name__ == '__main__':
    run()