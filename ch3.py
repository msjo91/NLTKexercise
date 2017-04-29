from __future__ import division
from bs4 import BeautifulSoup
from random import choice
from urllib import urlopen
from ch3test import monty
import re
import nltk


def q_one():
    s = 'colorless'
    return s[:4] + 'u' + s[4:]


def q_two():
    print 'dishes'[:-2]
    print 'running'[:-4]
    print 'nationality'[:-5]
    print 'undo'[2:]
    print 'preheat'[3:]


def q_three(n, sent):
    if n < 0:
        if abs(n) > len(sent):
            try:
                sent[n]
            except Exception, e:
                print "Error Message : " + str(e)
                print "I guess it doesn't work this way."
        else:
            print "{n} should have an absolute value greater than {len}. Try again.".format(n=n, len=len(sent))
    else:
        print "{} should be a negative number. Try again.".format(n)


def q_four(x, y, z):
    monty = 'Monty Python'
    print "monty[6:11:2] = %s" % monty[6:11:2]
    print "monty[10:5:-2] = %s" % monty[10:5:-2]
    print "monty[{x}:{y}:{z}] = {sent}".format(x=x, y=y, z=z, sent=monty[x:y:z])


def q_five():
    monty = 'Monty Python'
    print "monty='{}'".format(monty)
    print "monty[::-1]='{}'".format(monty[::-1])
    print """
    'Monty Python' is arranged backwards.
    monty[::-1] calls every element one by one, just like monty[::1].
    However, unlike those two, monty[::-1] calls the elements backwards, from monty[{}] to monty[0].
    Hence, the outcome is a reversed monty.
    """.format(len(monty) - 1)


def q_seven():
    return nltk.re_show(r'(\ba\b|\ban\b|\bthe\b|\+|-|\*|/)',
                        '"2 + 1" says the deer. Now this does not make a single sense.')


def q_eight(url):
    raw_contents = urlopen(url).read()
    soup = BeautifulSoup(raw_contents, 'html.parser')
    return soup.get_text()


# Question 9
def load(f):
    raw = open(f).read()
    return raw


def q_nine_a():
    pnct_pattern = r'''(?x)
        \.
        |\?
        |!
        |,
        |'
        |"
    '''
    text = load('ch3corpus.txt')
    return nltk.regexp_tokenize(text, pnct_pattern)


def q_nine_b():
    mny_pattern = r'^[A-Z]{3}(\d{3},)*\d{3}(.\d{2})?$'
    date_pattern = r'^\d{4}.\d{2}.\d{2}'
    ppl_pattern = r'[A-Z][a-z]+\s[A-Z][a-z]+'
    org_pattern = r'[A-Z]+(\s[A-Z]+)?'
    text = load('ch3corpus.txt')
    print "Monatery amounts :\n", nltk.regexp_tokenize(text, mny_pattern)
    print "Dates :\n", nltk.regexp_tokenize(text, date_pattern)
    print "People :\n", nltk.regexp_tokenize(text, ppl_pattern)
    print "Organizations :\n", nltk.regexp_tokenize(text, org_pattern)


def q_ten():
    sent = ['The', 'dog', 'gave', 'John', 'the', 'newspaper']
    result = [(word, len(word)) for word in sent]
    return result


def q_eleven(char):
    raw = "Iknowthespadesaretheswordsofasoldier"
    return raw.split(char)


def q_twelve(sent):
    for char in sent:
        print char


def q_thirteen():
    sent = "Yo, I  love   Lasagna    so     much."
    print sent.split()
    print sent.split(' ')
    print """
    sent.split() detects and removes all spaces.
    sent.split(' ') removes only the first space if there are multiple consecutive spaces.
    """


def q_fourteen():
    words = ['pikachu', 'raichu', 'pairi', 'kkobooggi', 'butterful', 'yadoran', 'pigeontwo', 'ttogas']
    words_cp = ['pikachu', 'raichu', 'pairi', 'kkobooggi', 'butterful', 'yadoran', 'pigeontwo', 'ttogas']
    print words.sort()
    print words
    print sorted(words_cp)
    print words_cp
    print """
    words.sort() sorts the elements of words permanently.
    It does not require an extra step for saving the rearrangement.
    Also, it can only be used for a list.
    sorted(words), on the other hand, is temporary and requires a variable to be saved.
    Also, the output is always a list.
    """


def q_fifteen():
    print "3" * 7
    print 3 * 7
    print int("3") * 7
    print str(3) * 7
    print """
    Multiplying a string will only return the string again and again by the number it was multiplied.
    Multiplying an integer will return the calculated result of the multiplication.
    """


def q_sixteen():
    return monty


def q_seventeen():
    print "It just prints the whole string."


def q_eighteen():
    text = nltk.corpus.gutenberg.raw('melville-moby_dick.txt')
    words = nltk.word_tokenize(text)
    lst = []
    for w in words:
        if re.search(r'^wh', w.lower()):
            lst.append(w)
    lst = sorted(set(lst))
    print lst
    print "Yes."


def q_nineteen():
    lst = open('ch3q19.txt').readlines()
    new_lst = []
    res_lst = []
    for i in lst:
        ele = re.split(r' ', i)
        new_lst.append(ele)
    for i in new_lst:
        i[1] = int(i[1])
    return res_lst


def q_twenty(url, word, n):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    raw = soup.get_text()
    idx = raw.index(word)
    return raw[idx:idx + n]


# Question 21
def unknown(url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    raw = soup.get_text()
    words = re.findall(r'[a-z]+', raw)
    lst = []
    res_lst = []
    for w in words:
        if w.isalpha():
            lst.append(w)
    new_lst = sorted(set(lst))
    for w in new_lst:
        if not w in nltk.corpus.words.words():
            res_lst.append(w)
    print "Warning : This takes forever."
    return res_lst


def q_twentytwo():
    raw = unknown('http://news.bbc.co.uk/')
    nonwords = re.findall(r'[a-z]{,4}', raw)
    lst = []
    for w in raw:
        if not w in nonwords:
            lst.append(w)
    return lst


def q_twentythree():
    pattern = r"n't|(\w+)?"
    sent = "I really don't know."
    res = nltk.re_show(pattern, sent)
    print 'When used r"n\'t|(\w+)?" : ', res
    print """
    r"n't|\w+" means "n't" or any letters. So, by r'\w+', "don't" is separated to "don" and "t" without "'".
    Bascially "\w+" was greedy.
    """


def q_twentyfour():
    pass


def q_twentyfive():
    pass


def q_twentyseven():
    lst = []
    for w in range(500):
        w = choice("aehh ")
        lst.append(w)
    jlst = ''.join(lst)
    slst = jlst.split()
    res_lst = ''.join(slst)
    return res_lst


def q_twentynine(category):
    words = nltk.corpus.brown.words(categories=category)
    sents = nltk.corpus.brown.sents(categories=category)
    all_words = ''.join(words)
    avg_word_per_sent = len(words) / len(sents)
    avg_letter_per_word = len(all_words) / len(words)
    ARI = 4.71 * avg_word_per_sent + 0.5 * avg_letter_per_word - 21.43
    return ARI


def q_thirty():
    raw = "For god's sake, this is way too difficult. I need hints many, many hints. Argh!"
    tokens = nltk.word_tokenize(raw)
    porter = nltk.PorterStemmer()
    lancaster = nltk.LancasterStemmer()

    print "PorterStemmer :"
    for t in tokens:
        print porter.stem(t),
    print "\nLancasterStemmer :"
    for t in tokens:
        print lancaster.stem(t),
    print """
    \nBoth seems to remove suffix for singular-plural change.
    One differences is that Lancaster does not allow any capitalized letter while Porter allows it for 'I'.
    Also Lancaster removes suffix for tense change as well.
    Porter changes 'y' to 'i' when it is positioned right after a consonant.
    It is possible that it reflects noun and verb change of 'y' (although 'many' is neither).
    """


def q_thirtyone():
    saying = ['After', 'all', 'is', 'said', 'and', 'done', ',', 'more', 'is', 'said', 'than', 'done', '.']
    lengths = []
    for w in saying:
        lengths.append(len(w))


def q_thirtytwo():
    silly = 'newly formed bland ideas are inexpressible in an infuriating way'
    bland = silly.split()
    print bland
    lst = []
    for w in bland:
        lst.append(w[1])
    print ''.join(lst)
    print ' '.join(bland)
    for w in sorted(bland):
        print w


def q_thirtythree():
    print """
    It gives the same answer as 'inexpressible'.index('r').
    """
    words = ['Hello', 'world', 'Michael', 'Jackson', 'Shamona']
    print words.index(choice(words))
    silly = 'newly formed bland ideas are inexpressible in an infuriating way'
    bland = silly.split()
    phrase = bland[:bland.index('in')]
    print phrase


def q_thirtyseven(url):
    raw_contents = urlopen(url).read()
    regexp = r'\<.*\>\n'
    re.sub(regexp, '', raw_contents)
    print "Couldn't go further from this."


def q_thirtyeight(word):
    regexp = r'\n'
    print regexp
    new_word = re.sub(regexp, '', word)
    print new_word
    print "Couldn't solve the third subquestion."


def q_fourty():
    pass


def q_fourtyone():
    words = ['attribution', 'confabulation', 'elocution', 'sequoia', 'tenacious', 'unidirectional']
    sorted_vsequences = sorted(set([''.join([char for char in word if char in 'aeiou']) for word in words]))
    return sorted_vsequences


def q_fourtytwo():
    pass


def q_foutythree():
    pass


def q_fourtyfour():
    pass
