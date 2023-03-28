import pandas as pd
import nltk
from nltk.tokenize import TreebankWordTokenizer
from nltk.metrics.distance  import edit_distance


def writer(sentence):

    df = pd.read_excel("ResultsDS.xlsx")
    # sentence = "Write a query to join teaspaceregisterkeyresultsqlds and teamspaceregisterthemsqldds."
    # sentence = input()
    tokenizer = TreebankWordTokenizer()
    tokens = tokenizer.tokenize(sentence)


    correct_spellings = df['Name']

    entries = tokens

    lst = []

    for entry in entries:
        temp = [w for w in correct_spellings if edit_distance(entry.lower(), w.lower())<4]
        if temp != []:
            # print(temp)
            lst.append(temp)

    print('### My SQL tables, with their properties:\n#')

    for wrd in lst:
        count = 0
        for name in df['Name']:
            if wrd[0] == name:
                # print(token)
                print(df['TableDef'][count])
            count+=1
        # print(tokn)

    print('#\n### %s;\nSELECT' % sentence)

# writer('Write a query to join teaspaceregisterkeyresultsqlds and teamspaceregisterthemsqldds.')
