'''
Write a function to print a dictionary with the keys in sorted order along with the
frequency of each word. Display the frequency values using “#” as a text based graph
'''

def frequency_graph(dictionary):
	"""frequency_graph"""
    lis = sorted(dictionary.keys())
    for i in lis:
        print(str(i)+' - '+int(dictionary[i])*'#')

def main():
	"""enter input"""
    dictionary = eval(input())
    frequency_graph(dictionary)

if __name__ == '__main__':
    main()
