class ArrayContainsDuplicate:
    def array_contains_duplicate(self,list):
        if not list:
            return False
        elif len(list) == 1:
            return False
        else:
            dupl_dict = {}
            for item in list:
                if item in dupl_dict:
                    return True
                else :
                    dupl_dict[item] = 1
            return False

test = ArrayContainsDuplicate()
list = [2,3,5,2,4,5]
list1 = [5,9,8,7,6]
print(test.array_contains_duplicate(list))
print(test.array_contains_duplicate(list1))
