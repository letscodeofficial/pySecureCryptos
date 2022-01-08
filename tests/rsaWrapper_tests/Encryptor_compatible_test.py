from pySecureCryptos import rsaWrapper
import pytest
import repeatTimes
import secrets
import random
import pickle













def getAssetionMessage(locals , message):
    locals_stored = locals

    result = str(message) + "\n\n\nFunction Vars Dump -\n"
    count = 1

    for name,val in locals_stored.items():
        result = result + f"\n\n{count}. {name} is {type(val)} = \n{val}\n"
        count = count + 1

    return result






# function to generate a random byte
def getRandomByte():
    minByteLen = 1
    maxByteLen = 1000

    byte = secrets.token_bytes(random.randint(minByteLen , maxByteLen))

    return byte









# function to generate a random string
def getRandomString(minStringLen = 1 , maxStringLen = 10000):
    ascii_upperLimit = 126   
    ascii_lowerLimit = 20

    randomStr = ""
    for _ in range(random.randint(minStringLen , maxStringLen)):
        randomChar = chr(random.randint(ascii_lowerLimit , ascii_upperLimit))
        randomStr = randomStr + randomChar

    return randomStr







def test_compatible_encrypt_byte():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_byte_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for byte , keyPublic , keyPrivate , encByte in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        decryptedByte = obj.decrypt_byte(encByte)

        assert byte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")













def test_compatible_encrypt_byte_yield():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_byte_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for byte , keyPublic , keyPrivate , encByte in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        decryptedByte = obj.decrypt_byte(encByte)

        assert byte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")



    for byte , keyPublic , keyPrivate , encByte in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        gen = obj.decrypt_byte_yield(encByte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decryptedByte = ex.value
                break

        assert byte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")





















def test_compatible_encrypt_string():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_string_yield_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for string , keyPublic , keyPrivate , enc_string in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        decrypted_string = obj.decrypt_string(enc_string)

        assert string == decrypted_string , getAssetionMessage(locals() , "decrypted string does not match the original string")













def test_compatible_encrypt_string_yield():

    
    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_string_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for string , keyPublic , keyPrivate , enc_string in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        decrypted_string = obj.decrypt_string(enc_string)

        assert string == decrypted_string , getAssetionMessage(locals() , "decrypted string does not match the original string")




    for string , keyPublic , keyPrivate , enc_string in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        gen = obj.decrypt_string_yield(enc_string)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decrypted_string = ex.value
                break

        assert string == decrypted_string , getAssetionMessage(locals() , "decrypted string does not match the original string")




















def test_compatible_encrypt_lbyte():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_large_byte_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for randomByte , keyPublic , keyPrivate , enc_byte in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        gen = obj.decrypt_lbyte_yield(enc_byte)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decryptedByte = ex.value
                break

        assert randomByte == decryptedByte , getAssetionMessage(locals() , "decrypted Byte does not match the original Byte")

















def test_compatible_encrypt_lstring():

    fileName = "binFiles/rsaWrapper_testcases_bin/Encryptor_large_string_test_testCases.bin"

    with open(fileName , "rb") as file:
        data = file.read()

    pickledList = pickle.loads(data)


    for randomString , keyPublic , keyPrivate , enc_string in pickledList:
        obj = rsaWrapper.Encryptor(keyPublic , keyPrivate)

        gen = obj.decrypt_lstring_yield(enc_string)

        while(True):
            try:
                next(gen)
            except StopIteration as ex:
                decryptedString = ex.value
                break

        assert randomString == decryptedString , getAssetionMessage(locals() , "decrypted string does not match the original string")







