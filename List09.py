def main(fruits):
    """
    A list called “fruits” is given and is five in length and contains at least one “apple”. Calculate how many “apple” were involved and return the indexes in a list view.
    Args:
        fruits(list): parameter
    Returns:
        list: return answer
    """
    i = 0
    b = []
    while i < len(fruits):
        b.append(i)
        i += 1
    return b
    
mevalar = ['apple','apple','olma']
print(main(mevalar))