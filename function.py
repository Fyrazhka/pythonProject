def inp(a,b):
    return a/b

def con(a, b):
    return(a + b)
def found(str,key):
    list=[]
    lowerstr=str.lower()
    splitstr=lowerstr.split()
    for s in splitstr:
        if(s==key):
            list.append(s)
    print(len(list))

if __name__ == '__main__':
    print(inp(4,2))
    found("Mary had a little lamb Little lamb, little lamb Mary had a little lamb.Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go")

