def flatten_varied_int_list(var_list, flat_list=[]):
    # Default cases
    if not var_list:
        return []

    '''
    Below is my first attempt with no research into other tools. My first instinct
    was to use list comprehension, however the individual 'int' elements of the
    list make it uniterable to do: return [j for k in var_list for j in k]
    '''
    for n in var_list:
        if type(n) is list:
            for m in n:
                flat_list.append(m)
        else:
            flat_list.append(n)

    return flat_list

if __name__ == '__main__':
    try:
        varied_int_list    = [[1,2,3,],4,[5,6],7,[8,9,10,11,12],13]
        flattened_int_list = flatten_varied_int_list(varied_int_list)

        print(flattened_int_list)

    except Exception as e:
        print(e)
