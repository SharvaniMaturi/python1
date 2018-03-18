import math
for i in range(1,1000):
    for j in range(i+1,1000):
       for k in range(j+1,1000):
         if(i+j+k==1000 & math.pow(i,2)+math.pow(j,2)==math.pow(k,2)):
            print(i);print(j);print(k);
            print(i*j*k);
            
              


