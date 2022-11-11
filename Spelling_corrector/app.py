import Textlob 
from textlob import Textlob 
def convert(text:str): 
    li=list(text.split())
    return li  # li stands on list : 
n1= str(input('enter your word : '))
word= convert(n1)
op=[]  #op stands for corrected word : 
for i in word :
    op.append(Textlob(i))
print(f'wrong word {word}')
print('correct word are : ')
for  i in op : 
    print(i.correct() , end=' ')
# close : 
