number = int(input ("Enter the table you want to print"))      
      
print ("The Multiplication Table of: ", number)    
for count in range(1, 11):      
   print (number, 'x', count, '=', number * count)   