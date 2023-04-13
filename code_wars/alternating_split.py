# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates 
# all the odd-indexed characters of S with all the even-indexed characters of S, this process 
# should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which 
# reverses the process.

# If the string S is an empty value or the integer N is not positive, return the first argument 
# without changes.

def decrypt(encrypted_text, n):
    if n <= 0:
        return encrypted_text
    text_list = list(encrypted_text)
    length = len(text_list)
    
    if length % 2 == 0:
        split_part = length // 2
    else:
        split_part = (length - 1) // 2
    
    first = text_list[0:split_part]
    second = text_list[split_part:length]
    result_list = [ second[i // 2] if i % 2 == 0 else first[(i - 1) // 2] for i in range(0, length) ]
    result = ''.join(result_list)
    
    return decrypt(result, n - 1)

def encrypt(text, n):
    if n <= 0:
        return text
    
    text_list = list(text)
    first = text_list[::2]
    second = text_list[1::2]
    encrypted = second + first
    result = ''.join(encrypted)
    
    return encrypt(result, n - 1)

# test.describe('Basic Tests')
# test.assert_equals(encrypt("This is a test!", 0), "This is a test!")
# test.assert_equals(encrypt("This is a test!", 1), "hsi  etTi sats!")
# test.assert_equals(encrypt("This is a test!", 2), "s eT ashi tist!")
# test.assert_equals(encrypt("This is a test!", 3), " Tah itse sits!")
# test.assert_equals(encrypt("This is a test!", 4), "This is a test!")
# test.assert_equals(encrypt("This is a test!", -1), "This is a test!")
# test.assert_equals(encrypt("This kata is very interesting!", 1), "hskt svr neetn!Ti aai eyitrsig")

# test.assert_equals(decrypt("This is a test!", 0), "This is a test!")
# test.assert_equals(decrypt("hsi  etTi sats!", 1), "This is a test!")
# test.assert_equals(decrypt("s eT ashi tist!", 2), "This is a test!")
# test.assert_equals(decrypt(" Tah itse sits!", 3), "This is a test!")
# test.assert_equals(decrypt("This is a test!", 4), "This is a test!")
# test.assert_equals(decrypt("This is a test!", -1), "This is a test!")
# test.assert_equals(decrypt("hskt svr neetn!Ti aai eyitrsig", 1), "This kata is very interesting!")

# test.assert_equals(encrypt("", 0), "")
# test.assert_equals(decrypt("", 0), "")
# test.assert_equals(encrypt(None, 0), None)
# test.assert_equals(decrypt(None, 0), None)
