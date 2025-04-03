# Bits trocados
v = int(input())
i =  1
while(v != 0):
    
    r_50 = int( v / 50)
    v = v % 50
    
    r_10 = int (v / 10)
    v = v % 10
    
    r_5 = int (v / 5)
    v = v % 5
    
    r_1 = v
    
    print("Teste", i)
    print(r_50, r_10, r_5, r_1)
    print("")
    i+=1
    
    v = int(input())