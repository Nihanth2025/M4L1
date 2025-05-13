def m(w):
    c=0
    l=[]
    for x in w:
        if x[0]==x[-1] and len(x)>1:
            c=c+1
            l.append(x)
    
    print("Words mathching are: ",l)
    return c

count=m(["524","Mam","lal"])
print("No.of Words mathching are: ",count)