def main(list1):
    """
    A list of zeros and ones is given. Find how many ones and how many zeros there are and return to the list form.
    Args:
        list1(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    z = 0
    o = 0
    l = []

    while i < len(list1):
        if list1[i] == 1:
            o +=1
        else:
            z += 1
        i +=1
    l.append(o)
    l.append(z)

    return l
ls = [0,1]
print(main(ls))