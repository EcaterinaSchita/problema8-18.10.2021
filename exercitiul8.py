s='A B C D E F G H I J K L M N O P R S T U V W X Y Z'
s1=''
s2=''
s3=''
for i in s:
    x=chr(ord(i)+1)
    s1+=x
    a=s1.replace('!', '')
    b=a.replace('[', 'A')
print('Sirul 1 este:', b) 

s2=b
for i in s:
    c=s2.replace(("Z"), ("A"))
    d=c.replace('!', '')
    e=d.replace('[', 'A')
print('Sirul 2 este:', e)   

s3=e
for i in s:
    f=s3.replace('.', '-')
print('Sirul 3 este:',e)    



