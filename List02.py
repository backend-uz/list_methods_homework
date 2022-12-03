def main(fruits,x,i):
    """
    You will be given a list of fruits. Add the x fruit to the i index and return it.
    Args:
        fruits(list): parameter 
        x(str): parameter
        i(int): parameter
    Returns:
        list: return answer
    """
    fruits.insert(i, x)
    return fruits
a = ['asdf', 'fefec', 'vwrvw']
print(main(a, 'wer', 0))