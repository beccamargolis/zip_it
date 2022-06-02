    #ZIP IT
    # Create a standalone function that accepts two arrays and combines their values sequentially into a new array.
    # Extra values from either array should be included afterward.
    # Given [4,15,100] and [10,20,30,40], return new array containing [4,10,15,20,30,40,100].

def zip_it(list_1, list_2):
    new_list = []
    if len(list_1) > len(list_2):
        larger_list = list_1
    else:
        larger_list = list_2
    for i in range(len(larger_list)): #cycles through numbers 0 through length of the larger list (non-inclusive)
        if i <= (len(list_1))-1: #if i is <= any index in list 1
            new_list.append(list_1[i]) #append i to new list
        if i <= (len(list_2))-1: #if i is <= any idex in list 2
            new_list.append(list_2[i]) #append i to new list
    print(new_list)
    return new_list

zip_it([-1,58,34,21],[82,-15,25,32,101])