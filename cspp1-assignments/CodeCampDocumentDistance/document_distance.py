'''
    Document Distance - A detailed description is given in the PDF
'''
import math
import re
stopwords = "stopwords.txt"
def cleaning(input1):
    reg = re.compile('[^a-z]')
    input1 = input1.lower()
    input1 = [reg.sub('',w.strip())for w in input1.split(' ')]
    return input1
def remove_stopwords(input1,input2):
    d = {}
    wordlist = cleaning(input1) + cleaning(input2)
    for word in wordlist:
        if word not in load_stopwords(stopwords) and len(word)>0:
            d[word] = (cleaning(input1).count(word),cleaning(input2).count(word))
    return d        

def similarity(dict1,dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    d = {}
    d = remove_stopwords(dict1,dict2)
   # print(d)
    num,sum1,sum2 = 0,0,0  
    for i in d:
        num  += (d[i][0] * d[i][1])
        sum1 += d[i][0] ** 2
        sum2 += d[i][1] ** 2
    return num/((math.sqrt(sum1))*(math.sqrt(sum2)))

def load_stopwords(filename):
    '''
    den = math.sqrt(sum1) * math.sqrt(sum2)
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords
def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input()
    input2 = input()
    print(similarity(input1,input2))
if __name__ == '__main__':
    main()
