import random
import copy

# class to shuffle and deshuffle
class Shuffler:
    
    # method to shuffle a passed list using a seed
    @classmethod
    def shuffe_list(cls , ls, seed , copyList = True):
        
        # copy list so that the original list stays the same
        if(copyList):
            ls = copy.deepcopy(ls)
        
        random.seed(seed)
        random.shuffle(ls)
        return ls



    # method to unshuffel a list shuffled using shuffe_list() method of this class
    # seed should be same for both the methods
    @classmethod
    def unShuffle_list(cls , shuffled_ls, seed):
        n = len(shuffled_ls)

        # reference list containing numbers from 0 to n - 1
        perm = [i for i in range(n)]

        # Apply sigma to perm
        # that is shuffle this refrence list using the same seed
        shuffled_perm = cls.shuffe_list(perm, seed)

        # combine the shuffled reference list and shuffled list passed
        # if the seed was same then the shuffled list passed index would be same as shuffled_perm
        zipped_ls = list(zip(shuffled_ls, shuffled_perm))

        # sort the shuffled list according to shuffled perm
        zipped_ls.sort(key=lambda x: x[1])
        
        # get and return the unshuffledList from zipped_ls
        # unshuffled list elements were at index 0 or at a in zipped_ls
        unshuffledList = [a for (a, b) in zipped_ls]

        return unshuffledList


    # method to shuffle a string
    @classmethod
    def shuffle_string(cls , string , seed):
        
        # convert the string to list and pass to main method
        shuffledList =  cls.shuffe_list(list(string) , seed)

        # convert the shuffled list back to string
        stringFromList = "".join(shuffledList)
        return stringFromList
    

    # function to shuffle a string
    @classmethod
    def unShuffle_string(cls , shuffledString , seed):

        # convert the shuffledString to list and pass to main method
        deshuffledList = cls.unShuffle_list(list(shuffledString) , seed)
        
        # convert the deshuffled list back to string
        stringFromList = "".join(deshuffledList)
        return stringFromList