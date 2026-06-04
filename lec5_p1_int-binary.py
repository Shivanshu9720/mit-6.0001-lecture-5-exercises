# CONVERTING DECIMAL INTEGRE TO BINARY
# CODE JUST DOING SUCCESIVE DIVISIONS

num = int(input("Enter Your Number :"))
# IF NUM -VE 
if num <0:
    flag = True
    num = abs(num)
else:
    flag = False


result = ''
if num == 0 :
    result = 0 
    
#HOW IT WORK?
# IF NUM IS ODD WE GET REMAINDER 1 // AND IF EVEN THAN 0
# BY THIS WE GET 0 & 1 BINARY N0:   
    
while num>0: 
    result = str(num%2)+result # STRING ADDITION
    num = num//2   # THIS CODE SHIFT 
    
# IN CASE OF -VE INPUT WE PRINT BOTH PRINT STATEMENT 
# TO SOLVE THIS PROBLEM I USED BOOLEAN FLAG     
           
if not flag :    
    print('Binary form Is = ',result) 

   
if flag :
   result = ('-' + result)
   print('Binary form Is = ',result)          # FOR -VE AND +VE INPUT -> OUTPUT ARE SAME