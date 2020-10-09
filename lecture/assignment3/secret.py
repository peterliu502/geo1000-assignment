# GEO1000 - Assignment 3
# Authors: Zhenyu Liu, Haoyang Dong
# Studentnumbers: 5386586, 5302501


def reverse_part(part):
    """Take as input a list
    Returns a new list with elements in input reversed
    Note: Pure function, so should not modify input!
    
    Example:
    
        >>> reverse_part(['t', 'h', 'i', 's'])
        ['s', 'i', 'h', 't']
    """
    return list(reversed(part))


def part_to_str(part):
    """Take as input a list with letters.
    Returns a new string with letters in the input list

    Example:

        >>> part_to_str(['a', 'b', 'c'])
        'abc'

    """
    return "".join(part)


def split_in_parts(sentence):
    """Split the string into a list of lists (either containing letters, or just
    one character not part of the alphabet).

    Example:

        >>> split_in_parts("this is.")
        [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]

    """
    list_parts = []
    list_isalpha = []
    for i in sentence:
        if i.isalpha():
            list_isalpha.append(i)
        elif len(list_isalpha) != 0:
            list_parts.append(list_isalpha)
            list_isalpha = []
            list_parts.append([i])
        else:
            list_parts.append([i])
    return list_parts


def reverse_relevant_parts(parts):
    """Reverse only those sublists consisting of letters
    
    Input: list of lists, e.g. [['t', 'h', 'i', 's'], [' '], ['i', 's'], ['.']]
    Returns: list with sublists reversed that consist of letters only.
    """
    return [reverse_part(parts[i]) for i in range(len(parts))]


def glue(parts):
    """Transforms the list of sublists back into a new string
    
    Returns: string
    """
    return "".join([part_to_str(parts[i]) for i in range(len(parts))])
    

def encrypt(sentence):
    """Reverses all consecutive letter parts in a string.
    
    Input: a string
    Returns: a string
    """
    return glue(reverse_relevant_parts(split_in_parts(sentence)))


if __name__ == "__main__":

    paragraph = "toN ylno si ti ysae ot eil htiw spam, ti's laitnesse. oT yartrop lufgninaem spihsnoitaler rof a xelpmoc, eerht-lanoisnemid dlrow no a talf teehs fo repap ro a oediv neercs, a pam tsum trotsid ytilaer. sA a elacs ledom, eht pam tsum esu slobmys taht tsomla syawla era yllanoitroporp hcum reggib ro rekciht naht eht serutaef yeht tneserper. oT diova gnidih lacitirc noitamrofni ni a gof fo liated, eht pam tsum reffo a evitceles, etelpmocni weiv fo ytilaer. erehT's on epacse morf eht cihpargotrac xodarap: ot tneserp a lufesu dna lufhturht erutcip, na etarucca pam tsum llet etihw seil. --- woH ot eil htiw spam, kraM reinomnoM, 1996."
    print(encrypt(paragraph))
    assert encrypt(encrypt(paragraph)) == paragraph

