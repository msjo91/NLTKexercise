from __future__ import division

from nltk import *
from nltk.book import *
from nltk.corpus import *
from nltk.corpus import wordnet as wn


def q_one():
    sent = "Mathilda, I'm glad you don't have a stomach ache any more."
    phrase = sent.split()
    phrase.append("Leon")
    for i in phrase:
        print phrase.index(i)
    print phrase * 2
    print phrase[-2:]
    print phrase[1:6]
    print sorted(phrase)


def q_two():
    print len(gutenberg.words('austen-persuasion.txt'))
    print len(set(gutenberg.words('austen-persuasion.txt')))


def q_three():
    br = brown.words()
    wt = webtext.words()
    lstbr = []
    lstwt = []
    for i in br:
        lstbr.append(i.lower())
    for i in wt:
        lstwt.append(i.lower())
    fdistbr = FreqDist(lstbr)
    fdistwt = FreqDist(lstwt)
    modals = ['cookie', 'monster', 'sesame', 'street']
    for i in modals:
        print i + ":", fdistbr[i]
        print i + ":", fdistwt[i]


def q_four():
    cfd = ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in state_union.fileids()
        for i in state_union.words(fileid)
        for target in ['men', 'women', 'people']
        if i.lower() == target
    )
    cfd.tabulate()
    print """
    There is a great spike in uses of the word 'people' in the mid 90s.
    The word 'men' was more often used than 'women' until the 60s.
    However, since the 70s, the patterns shown by 'men' and 'women' are quite similar.
    """
    cfd.plot()


def q_five():
    """
    I gave five words a try and got nothing. So, I decided to use the one given by the book.
    """
    tree = wn.synset('tree.n.01')
    print "Member meronyms : ", tree.member_meronyms()
    print "Part meronyms : ", tree.part_meronyms()
    print "Substance meronyms : ", tree.substance_meronyms()
    print "Member holonyms : ", tree.member_holonyms()
    print "Part holonyms : ", tree.part_holonyms()
    print "Substance holonyms : ", tree.substance_holonyms()


def q_six():
    print """
    If there is any word that is spelled the same but has different meaning in English there could be confusion.
    Either there should be a separate dictionary for such word (but must be able to distinguish) or the program should allow other language letters.
    Also, a word has more than one meaning in many cases. There should be a way to access other meanings in translation.
    """


def q_seven():
    print Text(gutenberg.words('austen-emma.txt')).concordance('however')
    print Text(gutenberg.words('austen-persuasion.txt')).concordance('however')
    print Text(state_union.words(state_union.fileids())).concordance('however')
    print """
    It seems that the word 'however' is barely used at the beginning of a sentence.
    Yet, even when it is used, it is immediately followed by a comma(,).
    And it seems the meaning is often 'but' or 'even though'.
    """


def q_eight():
    cfd = ConditionalFreqDist(
        (fileid, name[0])
        for fileid in names.fileids()
        for name in names.words(fileid)
    )
    print """
    All letters are more often used as an initial letter of a female name except 'H' and 'W'.
    There are some others, however, the difference is so little it seems meaningless.
    """
    cfd.plot()


# Question 9
def lexical_diversity(self):
    word_count = len(self)
    vocab_size = len(set(self))
    diversity_score = float(word_count / vocab_size)
    return diversity_score


def compare_texts(t1, t2):
    if lexical_diversity(t1) > lexical_diversity(t2):
        print "{} is more diverse.".format(t1)
    elif lexical_diversity(t1) < lexical_diversity(t2):
        print "{} is more diverse.".format(t2)
    else:
        if len(set(t1)) > len(set(t2)):
            print "{} has richer vocabulary.".format(t1)
        elif len(set(t1)) > len(set(t2)):
            print "{} has richer vocabulary.".format(t2)
        else:
            "No point comparing anymore."


def find_shared_word(t1, t2, n):
    set1 = set(FreqDist(t1).keys())
    set2 = set(FreqDist(t2).keys())
    lst = []
    for i in set1:
        for j in set2:
            if i == j:
                lst.append(i)
    return lst[n]


def concord(t1, t2, n):
    w = find_shared_word(t1, t2, n)
    print t1.concordance(w)
    print t2.concordance(w)
    print """
    I chose the word 'leaves' (41st word in the list created by find_shared_word() function).
    In text3, it appears only once and as a noun.
    In text4, it appears 5 times as verb and noun.
    """


def q_ten():
    """
    I don't understand the question.
    """
    pass


def q_eleven():
    """
    I don't understand the question.
    """
    pass


def q_twelve():
    entry_dict = cmudict.entries()
    lst = []
    for i, x in entry_dict:
        lst.append(i)
    total_words = len(lst)
    distinct_words = len(set(lst))
    res = float((1 - (distinct_words / total_words)) * 100)
    print "Distinct words : ", distinct_words
    print "More than one pronunciation : ", res, "%"


def q_thirteen():
    all_syn = list(wn.all_synsets('n'))
    x = 0
    for i in all_syn:
        if not i.hyponyms():
            x += 1
    res = float((x / len(all_syn)) * 100)
    print res, "%"


# Question 14
def supergloss(s):
    print "Definition :\n", s, wn.synset(s).definition
    print "Hypernyms :"
    for i in set(wn.synset(s).hypernyms()):
        print i, ":", i.definition
    print "Hyponyms :"
    for i in set(wn.synset(s).hyponyms()):
        print i, ":", i.definition


def q_fifteen():
    fdist = FreqDist(brown.words())
    lst = []
    for i in set(fdist):
        if fdist[i] >= 3:
            lst.append(i)
    print lst


def q_sixteen():
    for i in brown.categories():
        w = brown.words(categories=i)
        type = len(w)
        token = len(set(w))
        diversity_score = token / type
        print i, type, token, diversity_score
        print "Genre 'humor' has the lowest diversity score."


def q_seventeen(brown_word):
    stopword = stopwords.words('english')
    lst = []
    for i in brown_word:
        if i not in stopword:
            lst.append(i)
    fdist = FreqDist(lst)
    print fdist.items()[:50]


def q_eighteen(category):
    bigram = bigrams(brown.words(categories=category))
    stopword = stopwords.words('english')
    lst = []
    for i in bigram:
        if i[0] and i[1] not in stopword:
            lst.append(i)
    fdist = FreqDist(lst)
    print fdist.itmes()[:50]


def q_nineteen():
    genre_word = [
        (genre, word)
        for genre in brown.categories()
        for word in brown.words(categories=genre)
    ]
    cfd = ConditionalFreqDist(genre_word)
    modals = ['healthy', 'quick', 'road', 'create']
    cfd.tabulate(conditions=genre, samples=modals)


# Question 20
def word_freq(word, section):
    lst = []
    for i in brown.words(categories=section)
        lst.append(i)
    fdist = FreqDist(lst)
    print fdist.__getitem__(word)


def q_twentyone(text):
    lst = []
    for i, x in enumerate(cmudict.entries()):
        if x[0] in text:
            lst.append(x)
    complete_lst = []
    x = 0
    for i in lst:
        if i[0] not in complete_lst:
            x += len(i[1])
            complete_lst.append(i[0])
    print x


# Question 22
def hedge(text):
    lst = []
    x = 0
    for i in text:
        lst.append(i)
        if x % 3 == 0:
            lst.append('like')
        x += 1
    print lst


# Below questions are beyond my level of comprehension.
# I messed up big time.
def q_twentythree():
    pass


def q_twentyfour():
    pass


def q_twentyfive():
    pass


def q_twentysix():
    pass


def q_twentyseven():
    pass


def q_twentyeight():
    pass
