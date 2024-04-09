import unittest
import ctypes
import sys
sys.path.append("aes")
from aes import AES, encrypt, decrypt

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

        def test_aes_encrypt_and_decrypt(self):
                rijndael.aes_encrypt_block.restype = ctypes.c_void_p
                rijndael.aes_decrypt_block.restype = ctypes.c_void_p
                encryptedTextC = ctypes.string_at(rijndael.aes_encrypt_block(block, key), 16)
                encryptedTextPython = AES(bytes(key2)).encrypt_block(bytes(block2))
                decryptedTextC = ctypes.string_at(rijndael.aes_decrypt_block(encryptedTextC, key), 16)
                decryptedTextPython = AES(bytes(key2)).decrypt_block(bytes(encryptedTextPython))
                self.assertEqual(decryptedTextC, decryptedTextPython)
      

def run():
    unittest.main()

if __name__ == '__main__':
    run()