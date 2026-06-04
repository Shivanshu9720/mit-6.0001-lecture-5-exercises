# CONVERTING FLOAT/FRACTIONAL VALUE TO BINARY FORM


# HOW IT WORK💡
# WHEN WE HAVE A FLAOT VALUE WE JUST FIND MULTIPLE OF 2 SUCH THAT ON MULTIPLY WITH FLOAT
# WE GET A INTEGER THAN APPLY NORMAL INTERGER TO BINARY CONVERTION IDEA AND 
# AFTER THAN WE SHIFT THE DECIMAL IN LEFT TIMES WE HAVE POWER OF 2 

x = float(input("Enter The Float Value : "))

# THE % GRABS THE DECIMAL PART ONLY
# HERE WE FIND POWER (P) OF 2 !!
# WHEN REMAINDER IS 0 WE EXIT BECOZ P BECOME WHOLE NUM  ...
p = 0
while ((2**p)*x)%1 != 0 :
    print('Remainder = ' + str(((2**p)*x) - int((2**p)*x))) # NOT NECESSARY
    p+=1                   # HERE WE DOING SUBTRACTION AND GET IN FORM OF STR

num = int((2**p)*x) # HERE WE GET FLOAT TO INTERGER


# INTERGER TO BINARY CONVERTION 
result = ''
if num == 0 :
    result = "o"
    
while num > 0 :
    result = str(num%2) + result
    num = num//2
    
    
    
# TO SHIFT P STEP AND ADD 0 AND INSERT DECIMAL

for i in range(p - len(result)) :
    result = '0'+ result  # MOVE THE DOT(.) BACK POWER (P) STEP
    
    
result = result[0:-p] + '.' + result[-p:]   # SLICING // ADDING DECIMAL
print('The Binary Representation Of The Decimal ' + str (x) + ' Is ' + str(result))
    
    
    
    
    