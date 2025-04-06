def calculator(a,b,o):
    li=["+","-","*","/","%"]
    try:
        for i in li:
            if o not in li:
                raise ValueError("Unsupported Operator")
        if(type(a)==int or float and type(b)==int or float):
            if(o=="/"):
                print(a/b)
            if(o=="+"):
                print(a+b)
            if(o=="-"):
                print(a-b)
            if(o=="*"):
                print(a*b)
            if(0=="%"):
                print(a*b)
        else:
            raise ValueError("Invalid Input Type")
    except (ZeroDivisionError, ValueError, TypeError) as x:
        print(x)
    except Exception as e:
        print(e)

calculator(3,5,"+")
        
