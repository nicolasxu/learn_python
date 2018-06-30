# 03. check param must be a container.py




# Example 12
def normalize_defensive(numbers):
    if iter(numbers) is iter(numbers):  # An iterator -- bad!
        raise TypeError('Must supply a container')
    total = sum(numbers)
    result = []
    for value in numbers:
        percent = 100 * value / total
        result.append(percent)
    return result


'''

The protocol
states that when an iterator is passed to the iter built-in function, iter will
return the iterator itself. In contrast, when a container type is passed to iter,
a new iterator object will be returned each time.

'''

visits = [15, 35, 80]
normalize_defensive(visits) # No error
visits = ReadVisits(path)
normalize_defensive(visits) # No error


it = iter(visits)
normalize_defensive(it)
>>>
TypeError: Must supply a container
