A=10;          print(type(A));      print(id(A))
A="Hello";   print(type(A));      print(id(A))
 
A=10;          B=10
print(id(A));  print(id(B));          print(id(10))
 
A=1000
print(id(A)); print(id(1000))
 
lst = [1, 2]        
print(type(lst));   print(id(lst))
lst.append(3)   
print(type(lst));   print(id(lst))
