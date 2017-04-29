from __future__ import division
from copy import deepcopy
from operator import itemgetter
from nltk import FreqDist, word_tokenize
from pydoc import render_doc
from random import choice
from re import compile
from string import punctuation


def q_one(prop):
    print render_doc(prop, "Help on %s")


def q_two():
    print "Operations for both tuples and lists :"
    print "+", "in", "=="
    print "Operations for only lists :"
    print "del", "+=", "*="
    print """
    List does not support hash() while tuple does.
    Hash function allows convert inputs to hash values.
    Hash was once used as an encryption method for protecting valuable information such as passwords.
    The problem is that hash function will return the same output for the same input.
    Nowadays, hash is completely cracked and no one should use it to encrypt important information.
    Regardless of hash being obsolete, say that we want to keep a series of personal information and encrypt them.
    If we use a list, using hash() on it will raise a Python error.
    """


def q_three():
    print "Put a comma after the first element :"
    print "('doughnuts',)"
    print "Make a list of one element then tuple() it :"
    print "tuple(['muffins'])"


def q_four():
    words = ['is', 'NLP', 'fun', '?']
    print words
    tmp = words[0]
    words[0] = words[1]
    words[1] = tmp
    words[3] = '!'
    print "->", words
    words = ('is', 'NLP', 'fun', '?')
    print words
    (second, first, third, fourth) = words
    (second, first, third, fourth) = (first, second, third, '!')
    words = (second, first, third, fourth)
    print "->", words


def q_five():
    return q_one(cmp)


def q_six():
    print """
    N-gram is a sequence of n items from a source.
    Sliding window is a list of sub-lists of a source list.
    Thus a sliding window of n means sub-lists of n items.
    In the case n=1, the sliding window would be a list of sub-lists containing each elements.
    If the source list is ['ab', 'ra', 'ca', 'da'], the sliding window of 1 would be [['ab'], ['ra'], ['ca'], ['da'].
    In the case n=len(sent), the sliding window would be a list of a sub-list that is the same as the source list.
    [['ab', 'ra', 'ca', 'da']].
    """


def q_seven(args):
    print bool(args)


def q_eight():
    print "'z' < 'a' :", 'z' < 'a'
    print "'Monty' < 'Montague'", 'Monty' < 'Montague'
    print """
    The lexicographical sort states that the latter the letter is in the alphabetical order, the larger the value.
    And when it comes to comparing two strings with different length, it does not compare the length or total value.
    Instead, it compares each letter until it finds that one letter with different value.
    For example, for 'Monty' and 'Montague', it will compare 'M' to 'M', 'o' to 'o', and so forth.
    They are 'y' and 'a' after each 'Mont', where there will be a difference.
    Since 'y' is placed after than 'a' in the alphabetical order, 'y' has a larger value.
    Thus, 'Monty' is greater than 'Montague'.
    In case of, ('Monty', 1) and ('Monty', 2), it will do the same. But this time it will compare each element.
    If the element is a string, it will do as it did between 'Monty' and 'Montague'.
    Hence, ('Monty', 1) is less than ('Monty', 2)
    """
    print "('Monty', 1) < ('Monty', 2) :", ('Monty', 1) < ('Monty', 2)


def q_nine_a():
    sent = " All along the watchtower princess kept the view. "
    sent = sent.split()

    lst = []
    for w in sent:
        if w:
            lst.append(w)

    sent = ' '.join(lst)
    print sent


def q_nine_b():
    sent = " All along the watchtower princess kept the view. "
    pattern = compile('^\s|\s$')
    sent = pattern.sub('', sent)
    print sent


# Question 10
def cmp_len(x, y):
    assert isinstance(x, basestring)
    assert isinstance(y, basestring)
    a = len(x)
    b = len(y)
    return cmp(a, b)


# Question 11
sent1 = 'Well I stand up next to a mountain'.split()
position = choice(range(len(sent1)))


def q_eleven():
    sent2 = sent1
    sent1[position] = "RANDOM"
    print "sent1 :", sent1
    print "sent2 :", sent2


def q_eleven_a():
    sent2 = sent1[:]
    sent1[position] = "RANDOM"
    print "sent1 :", sent1
    print "sent2 :", sent2
    print """
    sent2 is not changed unlike sent2 = sent1 case because sent2 is not using the same memory location as sent1.
    sent1[:] is a new string that has the same output as sent1.
    sent1's id is {id1} while sent2's id is {id2}
    """.format(id1=id(sent1), id2=id(sent2))


def q_eleven_b():
    text1 = [['do', 'deer'], ['re', 'drop'], ['mi', 'name'], ['fa', 'long'], ['sol', 'needle']]
    text2 = text1[:]
    pos1 = choice(range(len(text1)))
    pos2 = choice(range(2))
    text1[pos1][pos2] = 'RANDOM'
    print "text1 :", text1
    print "text2 :", text2
    print """
    text1 is a list of lists.
    Each element in text1 has its own memory location.
    text2, despite being saved in a different memory location, calls elements from their memory locations.
    Hence, a change in text1 element causes a change in text2 element.
    """


def q_eleven_c(args):
    q_one(deepcopy)
    print id(args)
    print id(deepcopy(args))


def q_twelve(n, m):
    word_table = [[''] * n] * m
    print "Before1 :", word_table
    pos1 = choice(range(m))
    pos2 = choice(range(n))
    word_table[pos1][pos2] = "RANDOM"
    print "After1 :", word_table
    print """
    Every element is affected by the change because each element is a mere referenced copy.
    """
    new_word_table = []
    for i in range(m):
        lst = []
        for j in range(n):
            x = ''
            lst.append(x)
        new_word_table.append(lst)
    print "Before2 :", new_word_table
    new_word_table[pos1][pos2] = "RANDOM"
    print "After2 :", new_word_table


def q_thirteen(m, n, words):
    word_vowels = []
    lst = []
    for i in range(m):
        lst.append(i)
    for j in range(n):
        word_vowels.append(lst)
    for k in word_vowels:
        for word in words:
            l = len(word)
            v = 0
            for letter in word:
                if letter in ['a', 'e', 'i', 'o', 'u']:
                    v += 1
            word_vowels[l][v] = word
    print word_vowels


# Question 14
def novel10(text):
    word_tokens = word_tokenize(text)
    cut = int(0.9 * len(word_tokens))
    body = word_tokens[:cut]
    fin = word_tokens[cut:]
    new_body = []
    for w in body:
        new_body.append(w.lower())
    new_fin = []
    for w in fin:
        new_fin.append(w.lower())
    lst = []
    for w in new_fin:
        if w not in new_body:
            lst.append(w)
    new_lst = []
    for w in lst:
        if w not in punctuation:
            new_lst.append(w)
    res = set(new_lst)
    print res


def q_fifteen(sent):
    words = sent.split()
    length = len(words)
    fd = FreqDist(words)
    lst = list(fd)
    res = sorted(lst)
    pass


# Question 16
def gematria(word):
    letter_vals = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 80, 'g': 3, 'h': 8, 'i': 10, 'j': 10, 'k': 20, 'l': 30,
                   'm': 40, 'n': 50, 'o': 70, 'p': 80, 'q': 100, 'r': 200, 's': 300, 't': 400, 'u': 6, 'v': 6, 'w': 800,
                   'x': 60, 'y': 10, 'z': 7}
    word = list(word)
    word_value = 0
    for l in word:
        for key, value in letter_vals.items():
            pattern = compile(key)
            l = pattern.sub(value, l)
        word_value += int(l)
    print "{word} : {value}".format(word=word, value=word_value)


def q_sixteen_b(text):
    word_tokens = word_tokenize(text)
    count = 0
    for token in word_tokens:
        if token.isalpha():
            if gematria(token.lower()) == 666:
                count += 1
    print "666 : {}".format(count)


def decode(text):
    word_tokens = word_tokenize(text)
    for word in word_tokens:
        position = choice(range(len(word_tokens)))
        word_tokens[position] = gematria(word_tokens[position])
    print word_tokens


# Question 17
def shorten(text, n):
    word_tokens = word_tokenize(text)
    fd = FreqDist(word_tokens)
    words = []
    for key in fd:
        if not fd[key] == n:
            words.append(key)
    new_text = ' '.join(words)
    print new_text


def q_eighteen():
    pass


def q_nineteen():
    pass


def q_twenty(lst):
    assert isinstance(lst, list)
    fd = FreqDist(lst)
    lst = list(fd.most_common())
    lst.reverse()
    new_lst = []
    for w in lst:
        new_lst.append(w[0])
    print new_lst


def q_twentyone(text, vocabulary):
    print [item for item in set(word_tokenize(text)).difference(vocabulary)]


def q_twentytwo(words):
    assert isinstance(words, list)
    print sorted(words, key=itemgetter(1))
    print sorted(words, key=itemgetter(-1))
    print """
    itemgetter(1) pretty much means func[1].
    The key parameter is a function that returns a key to use for sorting purposes.
    Thus, key=itemgetter(1) means that key=func[1] and this is somehow affecting sorted().
    Have no idea how this works.
    """


# Question 23
def lookup(trie, key):
    pass
