'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    lis3 = dict1+dict2
    dict3 = {}
    for word in lis3:
        if word not in load_stopwords(FILE).keys():
            for i in range(len(word)):
                if word[i] not in '!@#$%^&*()-+=_?1234567890':
                    dict3[word] = (dict1.count(word), dict2.count(word))
    num, sum1, sum2 = 0, 0, 0
    for i in dict3:
        num += dict3[i][0] * dict3[i][1]
        sum1 += dict3[i][0] ** 2
        sum2 += dict3[i][1] ** 2
    den = math.sqrt(sum1) * math.sqrt(sum2)
    return num/den

def load_stopwords(filename):
    '''
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
    input1 = input().lower()
    input2 = input().lower()
    lis1 = input1.split(' ')
    lis2 = input2.split(' ')
    print(similarity(lis1, lis2))

if __name__ == '__main__':
    main()
