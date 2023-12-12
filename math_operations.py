def basic_operations(a,b):
    try:
        ans={}
        ans["divide"]=a/b 
        ans["add"]=a+b
        ans["subtract"]=a-b
        ans["multiply"]=a*b  
    except TypeError:
        print("invalid type")
    except ZeroDivisionError:
        print("Invalid division")        
    else:
        return ans
def power_operation(base,exponent,**kwargs):
    try:
        result=base**exponent
    except TypeError:
        print("Invalid exponent value")
    else:
        if kwargs:
            return result%kwargs["modulo"]
        return result
def apply_operations(operation_list):
    def which(tuple1):
        fun=tuple1[0]
        return fun(tuple1[1][0],tuple1[1][1])
    return list(map(which,operation_list))





