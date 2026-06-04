# SQUARE ROOT APPROXIMATION


x = int(input('Enter The Number : '))
num_guess = 0

epsilon = float(input('Enter The Epsilon : ')) # EPSILON IS A ERROR IN EXACT ANSWER || HM EPSILON SE YAH DECIDE KRTE H KI HMARA GUESS SQUARE
               # EXACT ANS SE KITNA KAM / JYADA  RHEGA TAB BHI ANS CHAL JAYEGA GA ACCEPTABLE HOGA 
               # EX: HME X = 36 CHAHIYE IF EPSILON = 0.01 MATLB IF GUESS SQUARE = 36.009/35.991 ATA H TO BHI ACCEPTABLE H
               # FI WE INC IN EPSILON MEANS WE INC THE ERROR OR RANGE OF ACCEPTABLE ANSWERS 
               

guess = 0.0 # STRATING OF GUESS
increment = float(input('Enter The Increment : '))


# ALGORITHM                            
while abs(guess**2 - x) >= epsilon and guess**2 <= x : 
                    # [guess**2-x] TELLS US . HM APNE EXACT ANS EX: 36/36.009/35.991 (ACEPTABLE ANS RANGE)
                    # SE KITNE DOOR YA PASS H ( ALSO WE CAN CALLED THIS IS A ERROR IN ANS )
    guess+= increment                  # JAB YE DOOR HMARE ACCEPTABALE ANS RANGE SE KAM HO JAYEGI WE EXIT BECOZ WE FOUND IT!!
    num_guess+=1                       # [guess**2 <= x] ALSO IS A STOPING CONDTION SO THAT HM APNE REAL ANS SE KAHI JAYDA DOOR NA CHALE JAYE
                                       # IF X = 36 KE LIYE GUESS 6.05 HO GYA TO YA 6.1 HO GYA SO WE STOP


print('No Of Guess = ' ,num_guess)  
if abs(guess**2-x )>= epsilon : # OVERSHOT THE X
    print('Failed on square root of ',x)  
    print(f'Last guess was {guess}')
    print(f'Last guess square is {guess*guess}')
else:                
    print(guess, 'Is Close To square Root Of',x)               
               
               