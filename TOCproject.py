fp=open("input.txt","r")
str=""
q=""
ch="y"
bool=True
i=0
k=0
D={}
for str in fp:
    if str[0] in "K":
            str=str[3:len(str)-2]
            K=str.split(",");
    if str[0] in "S":
            str=str[3:len(str)-2]
            S=str.split(",");
    if str[0] in "F":
            str=str[3:len(str)-2]
            F=str.split(",");
    if str[0] in "s":
            str=str[2:4]
            s=str.split();
    if str[0]==" ":
        str=str[1:]
        aa=str.split(",")
        D[aa[0]+aa[1]]=aa[2].strip()
while(ch=="y"):
    str=input("Enter the string you want to check:")
    bool=True
    q=s[0];
    for st in str:
        if st not in S:
            print("String contain albhabets which is not in S")
            bool=False
            break;
    if(bool==True):
        while len(str)>0:
            if k!=0:
                print(")");
            print("("+q+","+str+")"+"-|m "+"("+D[q+str[0]],end=",");
            q=D[q+str[0]];
            str=str[1::];
            print(str,end="");
            k=1;
        print("e)")
        if q in F:
            print("DFA accepts your input");
        else:
            print("DFA doesnot accepts your input");
    ch=input("\n\n\nEnter y to continue:");
     


    
    

    
