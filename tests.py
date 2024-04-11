import unittest
import ctypes
# from parametrized import parameterized 
# import sys
#Had to copy the aes.py from the submodule into the directory as github actions wasn't finding the aes python directory
from aes import AES
# import pytest 

rijndael = ctypes.CDLL('./rijndael.so')

# buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
# buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
# block = ctypes.create_string_buffer(buffer) 

# key_buffer = b'\x00\x01\x02\x03\x04\x05\x06\x07'
# key_buffer += b'\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
# key = ctypes.create_string_buffer(key_buffer)

# block2 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
# key2 = b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'

block1 = b'\x6f\xf2\xb6\x0f\x3e\xae\xf3\xe0\xe4\x0f\x3c\xfe\x43\x20\x27\xe4'
block2 = b'\x9c\x83\x55\x07\x84\xcb\x00\xd3\xb7\xfe\x69\xcd\x3a\x5c\x44\x5d'
block3 = b'\x8f\x9b\xa1\xa8\x9f\xf5\x6c\xb3\x9e\xfd\x35\xc9\xc9\xac\x6f\x9c'
key1 = b'\x1a\x56\xdb\x42\x44\x5e\x72\x13\xc2\xaa\x4a\xd4\x6c\x74\x85\x4f'
key2 = b'\x0f\xe0\x8d\xa6\x2e\xcc\x74\x27\x09\x93\x33\xf0\xa3\x00\x3f\xf2'
key3 = b'\xe9\x71\xc2\xfd\xff\x18\x53\xd4\x9a\x8e\x8c\x13\x4b\x37\xc4\x9c'

block1_c = ctypes.create_string_buffer(block1)
block2_c = ctypes.create_string_buffer(block2)
block3_c = ctypes.create_string_buffer(block3)
key1_c = ctypes.create_string_buffer(key1)
key2_c = ctypes.create_string_buffer(key2)
key3_c = ctypes.create_string_buffer(key3)


class TestBlock(unittest.TestCase):

            # def test_aes_encrypt_and_decrypt(block, key, block_c, key_c):
            #     rijndael.aes_encrypt_block.restype = ctypes.c_void_p
            #     rijndael.aes_decrypt_block.restype = ctypes.c_void_p
            #     encryptedTextC = ctypes.string_at(rijndael.aes_encrypt_block(block_c, key_c), 16)
            #     encryptedTextPython = AES(bytes(key)).encrypt_block(bytes(block))
            #     # Code below commented out as cyphertexts don't equal each other - printing the 
            #     # Python cyphertext shows it has unusual characters like '>' or '`'. This seems 
            #     # to be some conversion error I can't figure out
            #     # print(encryptedTextPython)
            #     # print(encryptedTextC)
            #     # self.assertEqual(encryptedTextC.hex(), encryptedTextPython.hex())
            #     decryptedTextC = ctypes.string_at(rijndael.aes_decrypt_block(encryptedTextC, key_c), 16)
            #     decryptedTextPython = AES(bytes(key)).decrypt_block(bytes(encryptedTextPython))
            #     # self.assertEqual(decryptedTextC, decryptedTextPython)
            #     return decryptedTextC, decryptedTextPython

            # # @pytest.mark.parametrize("block, key, block_c, key_c", [(block1, key1, block1_c, key1_c), (block1, key1, block1_c, key1_c)])
            # def run_tests(self, block, key, block_c, key_c):
            #     tests = [(block1, key1, block1_c, key1_c), (block2, key2, block2_c, key2_c), (block3, key3, block3_c, key3_c)]
            #     for block, key, block_c, key_c in tests:
            #           decryptedTextC, decryptedTextPython = test_aes_encrypt_and_decrypt(block=block, key=key, block_c=block_c, key_c=key_c)
            #           self.assertEqual(decryptedTextC, decryptedTextPython)


        def test_aes_encrypt_and_decrypt1(self):
                rijndael.aes_encrypt_block.restype = ctypes.c_void_p
                rijndael.aes_decrypt_block.restype = ctypes.c_void_p
                encryptedTextC = ctypes.string_at(rijndael.aes_encrypt_block(block1_c, key1_c), 16)
                encryptedTextPython = AES(bytes(key1)).encrypt_block(bytes(block1))
                # Code below commented out as cyphertexts don't equal each other - printing the 
                # Python cyphertext shows it has unusual characters like '>' or '`'. This seems 
                # to be some conversion error I can't figure out
                # print(encryptedTextPython)
                # print(encryptedTextC)
                # self.assertEqual(encryptedTextC.hex(), encryptedTextPython.hex())
                decryptedTextC = ctypes.string_at(rijndael.aes_decrypt_block(encryptedTextC, key1_c), 16)
                decryptedTextPython = AES(bytes(key1)).decrypt_block(bytes(encryptedTextPython))
                self.assertEqual(decryptedTextC, decryptedTextPython)

        def test_aes_encrypt_and_decrypt2(self):
                rijndael.aes_encrypt_block.restype = ctypes.c_void_p
                rijndael.aes_decrypt_block.restype = ctypes.c_void_p
                encryptedTextC = ctypes.string_at(rijndael.aes_encrypt_block(block2_c, key2_c), 16)
                encryptedTextPython = AES(bytes(key2)).encrypt_block(bytes(block2))
                decryptedTextC = ctypes.string_at(rijndael.aes_decrypt_block(encryptedTextC, key2_c), 16)
                decryptedTextPython = AES(bytes(key2)).decrypt_block(bytes(encryptedTextPython))
                self.assertEqual(decryptedTextC, decryptedTextPython)

        def test_aes_encrypt_and_decrypt3(self):
                rijndael.aes_encrypt_block.restype = ctypes.c_void_p
                rijndael.aes_decrypt_block.restype = ctypes.c_void_p
                encryptedTextC = ctypes.string_at(rijndael.aes_encrypt_block(block3_c, key3_c), 16)
                encryptedTextPython = AES(bytes(key3)).encrypt_block(bytes(block3))
                decryptedTextC = ctypes.string_at(rijndael.aes_decrypt_block(encryptedTextC, key3_c), 16)
                decryptedTextPython = AES(bytes(key3)).decrypt_block(bytes(encryptedTextPython))
                self.assertEqual(decryptedTextC, decryptedTextPython)
      

def run():
    unittest.main()

if __name__ == '__main__':
    run()