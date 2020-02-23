f=input('Enter a file: ')
file=open(f,'r')
text=file.read()
file.close()
words=text.split()
w=len(words)
for i in range (w):
    if (len(words[i])>3):
        p=list(words[i])
        d=p[0]
        m='a'
        r='y'
        p.remove(p[0])
        p.append(d)
        p.append(m)
        p.append(r)
        print(p)
