while True:
    n=list(input())
    if(n[0]=='0'):
        break
    left=0
    right=len(n)-1
    a=True
    for i in range(len(n)):
        if n[left]!=n[right]:
            a=False
        left+=1
        right-=1
    
    if a==True:
        print("yes")
    else:
        print("no")
        
    
        
    
    