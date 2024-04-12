                print(encryptedTextPython)
                print(encryptedTextC)
                self.assertEqual(encryptedTextC.hex(), encryptedTextPython.hex())