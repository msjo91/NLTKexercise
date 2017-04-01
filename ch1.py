from nltk.book import *


def q_one():
    print 12 / (4 + 1)


def q_two():
    print 26 ** 100


def q_three():
    print "List * integer creates a list of elements repeated by the number multiplied."


def q_four():
    print len(text2)
    print len(set(text2))


def q_five():
    print "romance"


def q_six():
    print """
    Elinor and Marianne are mentioned more often.
    Unless 'Sense and Sensibility' is written in first person, the females are the main leads.
    'Elinor' appears nearly everywhere, thus, Elinor is the main character.
    Marianne is probably in the position of Elinor's best friend.
    Since Willoughby appears whenever Marianne does, it is assumable that Willoughby and Marianne are together.
    """
    return text2.dispersion_plot(["Elinor", "Marianne", "Edward", "Willoughby"])


def q_seven():
    return text5.collocations()


def q_eight():
    print """
    len(set(text4)) returns the number of words used in text4.
    set(text4) changes text4 into a set.
    It splits the text into words.
    Each word becomes an element of the set.
    In a set, there cannot be any repetition.
    Repeated elements are deleted, leaving only one of its kind.
    len() is the length. It counts the number of elements.
    """


def q_nine():
    my_str = "I'll be better at this one day."
    print my_str
    print my_str + my_str
    print my_str * 5
    new_str = my_str.split(' ')
    new_str = new_str * 3
    print ' '.join(new_str)


def q_ten():
    my_sent = ["I'll", "be", "better", "at", "this", "one", "day."]
    join_sent = ' '.join(my_sent)
    print ' '.join(my_sent)
    print join_sent.split(' ')


def q_eleven():
    phrase1 = ["I", "had", "the", "same", "thought."]
    phrase2 = ["Make", "the", "hosts", "more", "manageable."]
    phrase3 = ["No", "one", "respects", "him", "more", "than", "I."]
    phrase4 = ["Get", "some", "sleep,", "Mr.Sizemore."]
    print phrase2 + phrase1 + phrase4 + phrase3
    print phrase1 + phrase2 + phrase3 + phrase4
    print phrase4 + phrase3 + phrase2 + phrase1
    print """
    len(phrase1 + phrase2) returns the number of elements in one combined list consisted of phrase1 and phrase2.
    len(phrase1) + len(phrase2) returns the addition of the length of phrase1 and the length of phrase2.
    In the end, the returned results are the same. Still, the process and implication are different.
    """


def q_twelve():
    print """
    ["Monty", "Python"][1] is more relevant in NLP because the result is tokenized.
    """


def q_thirteen():
    print sent1[2][2]
    print """
    sent1[2] returns the third index of sent1.
    Since sent1 is a list, sent1[2] is the third element in the list.
    sent1[2][2] returns the third index of sent1[2].
    sent1[2] is a string.
    sent1[2][2] returns the third character.
    """


def q_fourteen():
    for i, x in enumerate(sent3):
        if x == "the":
            print i


def q_fifteen():
    lst = []
    for i, x in enumerate(text5):
        if x.startswith('b'):
            lst.append(x)
    print sorted(lst)


def q_sixteen():
    print range(10)
    print range(10, 20)
    print range(10, 20, 2)
    print range(20, 10, -2)


def q_seventeen():
    print text9.index('sunset')
    print text9[621:644]


def q_eighteen():
    print sorted(set(sent1 + sent2 + sent3 + sent4 + sent5 + sent6 + sent7 + sent8))


def q_nineteen():
    lst1 = sorted(set([w.lower() for w in text1]))
    lst2 = sorted([w.lower() for w in set(text1)])

    print """
    The first line changes string elements in a list into lowercase.
    Then, it makes a set from the list getting rid of redundancies.
    By sorted(), a list in order is made.
    The second line makes a set out of text1.
    It rids redundancies.
    A set distinguishes lowercase and uppercase.
    For example, if there are 'what' and 'What', the set will recognize them as two different string elements.
    Then, a list is made which every element in the set is included in a lowercase form.
    If there were 'what' and 'What' in the set, the list will have two 'what's.
    In the end, regardless of which text is called, both lines return lists.
    However, the lengths are likely be different, the second line having more elements.
    """

    if len(lst1) > len(lst2):
        print "sorted(set[w.lower() for w in text1])) is larger."
    elif len(lst1) < len(lst2):
        print "sorted([w.lower() for w in set(text1)]) is larger."
    else:
        print "They have the same length."


def q_twenty():
    w1 = "TEST STRING"
    w2 = "test string"
    isup1 = w1.isupper()
    isup2 = w2.isupper()
    notlow1 = not w1.islower()
    notlow2 = not w2.islower()
    if isup1 == notlow1 and isup2 == notlow2:
        print """
        They return the same result.
        However, '.isupper()' returns a boolean value asking if the string is in uppercase.
        On the other hand, 'not .islower()' returns a boolean value that is the opposite of the boolean value from '.islower()'.
        """
    else:
        print "Obviously, they are different."


def q_twentyone():
    print text2[-2:]


def q_twentytwo():
    lst = []
    fdist5 = FreqDist(text5)
    for i in fdist5:
        if len(i) == 4:
            lst.append(i)


def q_twentythree():
    lst = []
    for i in text6:
        if i.isupper():
            lst.append(i)
    print set(lst)


def q_twentyfour():
    lst = []
    for i in text6:
        if i.endswith('ize'):
            lst.append(i)
        if 'z' in i:
            lst.append(i)
        if 'pt' in i:
            lst.append(i)
        if i.istitle():
            lst.append(i)
    print set(lst)


def q_twentyfive():
    sent = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']
    lst1 = []
    lst2 = []
    for i in sent:
        if i.startswith('sh'):
            lst1.append(i)
        if len(i) > 4:
            lst2.append(i)
    print "Starts with 'sh' :"
    print lst1
    print "Longer than 4 characters :"
    print lst2


def q_twentysix():
    print "It returns the total sum of the length of each word in text1."
    print "Average word length :"
    print sum([len(w) for w in text1]) / len(text1)


# Question 27
def vocab_size(text):
    lst = []
    for i in text:
        if i.isalpha():
            lst.append(i.lower())
    return len(set(lst))


# Question 28
def percent(word, text):
    freq = float(100 * text.count(word) / len(text))
    print str(freq) + "%"


def q_twentynine():
    print set(sent3) < set(text1)
    print """
    Operators return boolean value.
    They can be used to compare or set a condition.
    The former tells whether the left value is as the operator says to the right value.
    In the case that both are iterations like above, the operator compares the lengths of each.
    The latter can be used in if and while functions.
    """
