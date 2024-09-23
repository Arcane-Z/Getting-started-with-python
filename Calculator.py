num1=input("Enter the first no: ")
       num2=input("Enter the second no: ")
       calc=input("Enter the operation  ")
       import operator

       ops = {
           '+' : operator.add,
           '-' : operator.sub,
           '*' : operator.mul,
           '/' : operator.truediv, 
           '%' : operator.mod,
           '^' : operator.xor,
       }
       print(ops[calc](float(num1),float(num2)))
