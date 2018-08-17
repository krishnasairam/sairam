import math
FILE = "stopwords.txt"
def similarity(dict1, dict2):
    '''
        Compute the document distance as given in the PDF
    '''
    str1 ,str2 = '' , ''
    for j in dict1:
        for i in j:
            if i not in '!@#$%^&*()-+=_?.,1234567890':
                if i not in "'":
                    str1 = str1 + i
    for j in dict2:
        for i in j:
            if i not in '!@#$%^&*()-+=_?.,1234567890':
                if i not in "'":
                    str2 = str2 + i 
    lis1 = str1.split()
    lis2 = str2.split()
    lis3 = dict1 + dict2
    dict3 = {}
    for word in lis3:
      if word not in load_stopwords(FILE).keys():
        dict3[word] = (lis1.count(word), lis2.count(word))
    num, sum1, sum2 = 0, 0, 0
    for i in dict3:
        num += dict3[i][0] * dict3[i][1]
        sum1 += dict3[i][0] ** 2
        sum2 += dict3[i][1] ** 2
    den = math.sqrt(sum1) * math.sqrt(sum2)
    sim = num/den 
    return sim
    
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
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()

