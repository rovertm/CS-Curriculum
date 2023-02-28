# Problem Set 4A
# Name: Trevor KM
# Collaborators: NONE
# Time Spent: 1:00

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    # to return 
    perm_list = []
    
    # base case
    if len(sequence)==1:
        perm_list.append(sequence)
        return perm_list # singleton list
    
    for i, char in enumerate(sequence):
        # current leading character in recursion
        current_char = sequence[:i]
        # remaining characters
        remain_chars = sequence[i + 1:]
        # loop through recursive permutation outputs
        for perm in get_permutations(current_char + remain_chars):
            # add leading char to remaining permutation
            new_perm = char + perm
            # append to resulting perm_list if not a dupe
            if new_perm not in perm_list:
                perm_list.append(char+perm)
    return perm_list


if __name__ == '__main__':
    
    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    # Put three example test cases here (for your sanity, limit your inputs
    # to be three characters or fewer as you will have n! permutations for a 
    # sequence of length n)
    
    # MY TEST CASES
    example_ii = '_3'
    print('Input:', example_ii)
    print('Expected Output:', ['_3', '3_'])
    print('Actual Output:', get_permutations(example_input))
    
    example_iii = '%3%'
    print('Input:', example_iii)
    print('Expected Output:', ['%3%', '%%3', 
                               '3%%'])
    print('Actual Output:', get_permutations(example_input))
    

