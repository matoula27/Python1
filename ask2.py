f=input('Enter a file: ')
file=open(f,'r')
text=file.read()
file.close()
list_text=list(text)
l=len(list_text)
a1=0
a2=0
for i in range (l):
    if (list_text[i]!=' ' and list_text[i]!='\n'):
        if (list_text[i]=='f' or list_text[i]=='c' or list_text[i]=='k' or list_text[i]=='r'):
            a1+=1
        else:
            if (list_text[i]=='b' or list_text[i]=='d' or list_text[i]=='g' or list_text[i]=='h' or list_text[i]=='j' or list_text[i]=='l' or list_text[i]=='m' or list_text[i]=='n' or list_text[i]=='p' or list_text[i]=='q' or list_text[i]=='s' or list_text[i]=='t' or list_text[i]=='v' or list_text[i]=='w' or list_text[i]=='x' or list_text[i]=='z'):
                a2+=1
    else:
        if (a1>=a2 and (a2!=0 or a1!=0)):
            print('Bad word')
        else:
            print('Good word')
        a1=0
        a2=0
