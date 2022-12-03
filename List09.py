def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    b =0
    answer=[]

    while i < len(fruits):
        if fruits[i] == 'apple':
            b+=1
            answer.append(i)
        i += 1
    answer.insert(0, b)
    return answer
mevalar = ["apple", "banana", "apple", "pear", "apple"]
print(main(mevalar))