# Coding
#write a  function to remove a given word and strip it



def Sentence(word1,word2):
    line = word1.replace(word2,'')
    return line.strip()
WORD ='     Python is very easy to understand, Python is easy to handle  '
x = Sentence(WORD,'Python')
print(x)
# output:is very easy to understand,  is easy to handle
