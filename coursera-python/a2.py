def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """
    return dna2 in dna1

def is_valid_sequence(dna1):
    """
     (str) -> bool
    >>> is_valid_sequence('ATCGATGCCC')
    True
    >>> is_valid_sequence('pATSDsd')
    False
    """
    return len(dna1) == dna1.count('A') + dna1.count('T') + dna1.count('C') + dna1.count('G')

def insert_sequence(dna1, dna2, num):
    """
    (str, str, int) -> str
    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    """
    return dna1[:num] + dna2 + dna1[num:]
    
def get_complement(dna1):
    """
    (str) -> str
    >>> get_complement('A')
    'T'
    >>> get_complement('T')
    'A'
    >>> get_complement('C')
    'G'
    >>> get_complement('G')
    'C'
    """
    mapping = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return mapping[dna1]

def get_complementary_sequence(dna1):
    """
    (str) -> str
    >>> get_complementary_sequence('ATATCGGC')
    'TATAGCCG'
    """
    complement = ''
    for ele in dna1:
        complement += get_complement(ele)
    return complement
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
