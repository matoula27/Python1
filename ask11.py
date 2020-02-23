file=open('numbers.txt','r')
for line in file:
    j=list(line)
    j.remove('\n')
    for i in range (100000,1000000):
        f=str(i)
        l=list(f)
        k=list(l)
        if (((j[0]==k[0]) and (j[1]==k[1]) and (j[2]==k[2]) and (j[3]==k[3])) or ((j[0]==k[1]) and (j[1]==k[2]) and (j[2]==k[3]) and (j[3]==k[4])) or ((j[0]==k[1]) and (j[1]==k[3]) and (j[2]==k[4]) and (j[3]==k[5])) or ((j[0]==k[1]) and (j[1]==k[2]) and (j[2]==k[3]) and (j[3]==k[4])) or ((j[0]==k[1]) and (j[1]==k[4]) and (j[2]==k[3]) and (j[3]==k[5])) or ((j[0]==k[1]) and (j[1]==k[4]) and (j[2]==k[5]) and (j[3]==k[2])) or ((j[0]==k[0]) and (j[1]==k[1]) and (j[2]==k[2]) and (j[3]==k[4])) or ((j[0]==k[0]) and (j[1]==k[1]) and (j[2]==k[2]) and (j[3]==k[5])) or ((j[0]==k[0]) and (j[1]==k[2]) and (j[2]==k[3]) and (j[3]==k[4])) or ((j[0]==k[0]) and (j[1]==k[2]) and (j[2]==k[3]) and (j[3]==k[5])) or((j[0]==k[3]) and (j[1]==k[2]) and (j[2]==k[1]) and (j[3]==k[0])) or ((j[0]==k[3]) and (j[1]==k[4]) and (j[2]==k[5]) and (j[3]==k[1])) or ((j[0]==k[3]) and (j[1]==k[1]) and (j[2]==k[0]) and (j[3]==k[5])) or((j[0]==k[4]) and (j[1]==k[3]) and (j[2]==k[5]) and (j[3]==k[0])) or ((j[0]==k[4]) and (j[1]==k[2]) and (j[2]==k[5]) and (j[3]==k[1])) or ((j[0]==k[4]) and (j[1]==k[1]) and (j[2]==k[2]) and (j[3]==k[3])) or ((j[0]==k[5]) and (j[1]==k[4]) and (j[2]==k[3]) and (j[3]==k[2])) or ((j[0]==k[5]) and (j[1]==k[3]) and (j[2]==k[4]) and (j[3]==k[0])) or ((j[0]==k[5]) and (j[1]==k[2]) and (j[2]==k[0]) and (j[3]==k[4]))):
            print ('We can do it')
file.close()
