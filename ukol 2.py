cisla = [3, 5, 8, 1, 2, 4, 6, 7]

temp = 0;    
    
    
     
for i in range(0, len(cisla)):    
    for j in range(i+1, len(cisla)):    
        if(cisla[i] > cisla[j]):    
            temp = cisla[i];    
            cisla[i] = cisla[j];    
            cisla[j] = temp;               
    
   
for i in range(0, len(cisla)):    
    print(cisla[i], end=" ");    

print()

for i in range(0, len(cisla)):    
    for j in range(i+1, len(cisla)):    
        if(cisla[i] < cisla[j]):    
            temp = cisla[i];    
            cisla[i] = cisla[j];    
            cisla[j] = temp;    
     
print();    
         
for i in range(0, len(cisla)):     
    print(cisla[i], end=" ");  

print()

def Average(x): 
    return sum(cisla) / len(cisla) 

average = Average(cisla) 

# Printing average of the list 
print("Average of the list =", round(average, 2))