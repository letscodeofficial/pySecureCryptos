from shuffler import Shuffler
import hashlib
import onetimepad
import encoderDecoders

class StringEncryptor:

    @classmethod
    def encrypt(cls , string , password):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

        return result


    @classmethod
    def decrypt(cls , enc_string , password):

        # type checking the parameters
        if(type(enc_string) != str):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        return result




















class StringEncryptor_yield:

    @classmethod
    def encrypt(cls , string , password):

        # type checking the parameters
        if(type(string) != str):
            raise ValueError("string parameter expected to be of str type instead got {} type".format(type(string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        totalYields = int(lenString // hashedLength) * 2 + 1
        currentYield = 0

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

            yield currentYield , totalYields

            currentYield = currentYield + 1

        return result


    @classmethod
    def decrypt(cls , enc_string , password):

        # type checking the parameters
        if(type(enc_string) != str):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type".format(type(enc_string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        totalYields = int(lenString // hashedLength2) * 2 + 1
        currentYield = 0

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

            yield currentYield , totalYields

            currentYield = currentYield + 1


        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        return result


















class BytesEncryptor:

    @classmethod
    def encrypt(cls , byteObject , password , returnByteObject = True):

        # type checking the parameters
        if((type(byteObject) != bytes) and (type(byteObject) != bytearray)):
            raise ValueError("byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(byteObject)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        string = encoderDecoders.Byte2String.encode(byteObject)

        lenString = len(string)
        hashedLength = len(sha224_hashed_password_shuffled)

        for i in range(0 , lenString , hashedLength):
            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

        if(returnByteObject):
            result = encoderDecoders.String2Byte.encode(result)

        return result


    @classmethod
    def decrypt(cls , enc_string , password):

        # type checking the parameters
        if((type(enc_string) != str)):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type. If you returned byte type from encrytor for BytesEncryptor , then use decrypt_byte method".format(type(enc_string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        result = encoderDecoders.Byte2String.decode(result)

        return result


    @classmethod
    def decrypt_byte(cls , enc_byteObject , password):

        # type checking the parameters
        if((type(enc_byteObject) != bytes) and (type(enc_byteObject) != bytearray)):
            raise ValueError("enc_byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(enc_byteObject)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        enc_string = encoderDecoders.String2Byte.decode(enc_byteObject)

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

        result = encoderDecoders.Byte2String.decode(result)

        return result




















class BytesEncryptor_yield:

    @classmethod
    def encrypt(cls , byteObject , password , returnByteObject = True):

        # type checking the parameters
        if((type(byteObject) != bytes) and (type(byteObject) != bytearray)):
            raise ValueError("byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(byteObject)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)

        # deviding string into chunks each of half the size of sha224_hashed_password_shuffled
        # this is because , onetimepad is most effective then the key is longer than message
        chunkList = []
        chunkKeys = []

        lenString = int(len(byteObject)*3)
        hashedLength = len(sha224_hashed_password_shuffled)
        
        if(returnByteObject):
            totalYields = int(len(byteObject)) + (int(lenString // hashedLength) * 2 + 1) + int(lenString * 2)
        else:
            totalYields = int(len(byteObject)) + (int(lenString // hashedLength) * 2 + 1) 
        
        currentYield = 0

        genObj_b2s_encode = encoderDecoders.Byte2String_yield.encode(byteObject)

        while(True):
            try:
                _ , _ = next(genObj_b2s_encode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                string = ex.value
                break

        lenString = len(string)

        for i in range(0 , lenString , hashedLength):


            if((i+hashedLength) < lenString):
                chunkList.append(string[i : i + hashedLength]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password)
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

    
        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            encryptedChunk = onetimepad.encrypt(i , j)
            encryptedChunkShuffled = Shuffler.shuffle_string(encryptedChunk , md5_hashed_password)

            result = result + encryptedChunkShuffled

            yield currentYield , totalYields

            currentYield = currentYield + 1

        if(returnByteObject):
            genObj_s2b_encode = encoderDecoders.String2Byte_yield.encode(result)

            while(True):
                try:
                    _ , _ = next(genObj_s2b_encode)
                    yield currentYield , totalYields
                    currentYield = currentYield + 1

                except StopIteration as ex:
                    result = ex.value
                    break

        return result


    @classmethod
    def decrypt(cls , enc_string , password):

        # type checking the parameters
        if((type(enc_string) != str)):
            raise ValueError("enc_string parameter expected to be of str type instead got {} type. If you returned byte type from encrytor for BytesEncryptor , then use decrypt_byte method".format(type(enc_string)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        lenString = len(enc_string)
        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        totalYields = (int(lenString // hashedLength2) * 2 + 1) + int(lenString // 2 // 3)
        
        currentYield = 0

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 
            
            yield currentYield , totalYields

            currentYield = currentYield + 1



        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        genObj_b2s_decode = encoderDecoders.Byte2String_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_b2s_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                result = ex.value
                break

        return result


    @classmethod
    def decrypt_byte(cls , enc_byteObject , password):

        # type checking the parameters
        if((type(enc_byteObject) != bytes) and (type(enc_byteObject) != bytearray)):
            raise ValueError("enc_byteObject parameter expected to be of bytes type or bytearray type instead got {} type".format(type(enc_byteObject)))

        if(type(password) != str):
            raise ValueError("password parameter expected to be of str type instead got {} type".format(type(password)))

        # getting md5 and sha224 hash of the password passed
        md5_hashed_password = hashlib.md5(password.encode("utf-8")).hexdigest()
        sha224_hashed_password = hashlib.sha224(password.encode("utf-8")).hexdigest()

        # shuffling sha224 using md5 as key
        sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password , md5_hashed_password)


        # deviding string into chunks each of the size of sha224_hashed_password_shuffled
        # this time we are not going with half the size because , the encrypted chunk from the encryptor is of sha224_hashed_password_shuffled size
        chunkList = []
        chunkKeys = []

        hashedLength2 = len(sha224_hashed_password_shuffled) * 2

        len_enc_byteObject = len(enc_byteObject)

        totalYields = len_enc_byteObject + (int(len_enc_byteObject // hashedLength2) * 2 + 1) + + int(len_enc_byteObject // 3 // 2)
        currentYield = 0

        genObj_s2b_decode = encoderDecoders.String2Byte_yield.decode(enc_byteObject)

        while(True):
            try:
                _ , _ = next(genObj_s2b_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                enc_string = ex.value
                break

        lenString = len(enc_string)

        for i in range(0 , lenString , hashedLength2):
            if((i+hashedLength2) < lenString):
                chunkList.append(enc_string[i : i + hashedLength2]) 
                chunkKeys.append(sha224_hashed_password_shuffled)
                
            else:
                chunkList.append(enc_string[i : ]) 
                chunkKeys.append(sha224_hashed_password_shuffled[:len(enc_string[i : ])])

            sha224_hashed_password_shuffled = Shuffler.shuffle_string(sha224_hashed_password_shuffled , md5_hashed_password) 
            
            yield currentYield , totalYields

            currentYield = currentYield + 1

        result = ""
        
        # encrypt each chunk using sha224_hashed_password_shuffled as key
        # then shuffle encrypted chunk using md5_hashed_password as key
        # then join and return the result
        for i,j in zip(chunkList , chunkKeys):
            chunk_unShuffled = Shuffler.unShuffle_string(i , md5_hashed_password)
            decryptedChunk = onetimepad.decrypt(chunk_unShuffled , j)

            result = result + decryptedChunk

            yield currentYield , totalYields

            currentYield = currentYield + 1

        genObj_b2s_decode = encoderDecoders.Byte2String_yield.decode(result)

        while(True):
            try:
                _ , _ = next(genObj_b2s_decode)
                yield currentYield , totalYields
                currentYield = currentYield + 1

            except StopIteration as ex:
                result = ex.value
                break

        return result























def __test_stringEncrytor():
    string = "hello world"
    encryptedString = StringEncryptor.encrypt(string , "hello")
    decryptedString = StringEncryptor.decrypt(encryptedString , "hello")

    print(string)
    print(encryptedString)
    print(decryptedString)

    if(string == decryptedString):
        print("ok")
    else:
        print("error")




def __test_stringEncrytor2():
    string = "hello world"
    genObj_encrypt = StringEncryptor_yield.encrypt(string , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = StringEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            decryptedString = ex.value
            break
    print()

    if(string == decryptedString):
        print("\nok")
    else:
        print("\nerror")










def __test_byteEncrytor():
    byteObject = b"hello world"
    encryptedString = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=False)
    decryptedByte = BytesEncryptor.decrypt(encryptedString , "hello")

    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")

    print("\n\ntest 2\n\n")


    byteObject = b"hello world"
    
    # we will get bytes object from the encryptor function , say you are storing this on a blob storage
    encryptedByte = BytesEncryptor.encrypt(byteObject , "hello" , returnByteObject=True)
    decryptedByte = BytesEncryptor.decrypt_byte(encryptedByte , "hello")


    if(byteObject == decryptedByte):
        print("ok")
    else:
        print("error")



def __test_byteEncrytor2():
    byteObject = b"hello world"

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=False)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            encryptedString = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt(encryptedString , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")




    print("\n\ntest 2\n\n")


    byteObject = b"hello world"

    genObj_encrypt = BytesEncryptor_yield.encrypt(byteObject , "hello" , returnByteObject=True)

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_encrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            encryptedByte = ex.value
            break
    print()

    genObj_decrypt = BytesEncryptor_yield.decrypt_byte(encryptedByte , "hello")

    print()
    while(True):
        try:
            onCount , totalCount = next(genObj_decrypt)
            print("on {} out of {}   ".format(onCount , totalCount))
        except StopIteration as ex:
            decryptedByte = ex.value
            break
    print()

    if(byteObject == decryptedByte):
        print("\nok")
    else:
        print("\nerror")


if __name__ == "__main__":
    __test_byteEncrytor2()
    # __test_stringEncrytor2()