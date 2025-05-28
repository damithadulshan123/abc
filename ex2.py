total=0
for i in range(1,11):
    sqr=i*i
    if((sqr%4)==0):
        total +=sqr
print ("sum of the odd numbers from 0 to 100:",total)