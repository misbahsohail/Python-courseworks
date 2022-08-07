#!/usr/bin/env python3
# CMT309 Coursework 1

# student number: C1950696

def cycle_convert(x, n):
    # ... YOUR CODE HERE ...
    
    i=1
    list_variables=[int,float,bool,str,complex]
    
    type_of_initial_variable=type(x)
    
    new_type=''
    

    for i in range(len(list_variables)):  
      if list_variables[i]==type_of_initial_variable:  #find the index of item such that the item is equal to the type of inital variable
    
        break #the particilar index value is stored in i and the program goes out of if loop
    
    if n>0:  #if the step-size, n is positive
     
     
     step=i+n  #step is the number total steps to reach to the new position of index
     
     new_index_num=step%(len(list_variables))  #wrap around from the start of list incase the value of 'step'
                                               #exceeds the length of list and the new index value is stored 
                                               #new_index_value
     
     new_variable=list_variables[new_index_num] 
     
     
     if type(x)==complex and (new_variable==int or new_variable==float):
        print("conversion not possible")
     
     
     else: 
            new_type=new_variable
            new_value=new_variable(x) 
            print('Converted from=',type_of_initial_variable, ': ',x)
            print('Converted to =',new_type, ': ' ,new_value)

    
    if n<0:
     
     
     i_neg=i-5
     step=n+i_neg
     
     
     step=step*(-1)
     
     step_size=(step%5)
    
     
     new_index_num=step_size-5
     new_index_num=-(new_index_num)
     
     if (new_index_num==5):
            new_index_num=-5
     
     
     new_variable=list_variables[new_index_num] 

     if type(x)==complex and (new_variable==int or new_variable==float):
        print("conversion not possible")
     
     else:
            new_type=new_variable
            new_value=new_variable(x) 
            print('Converted from=',type_of_initial_variable, ': ',x)
            print('Converted to =',new_type, ': ' ,new_value)
   
    if n==0:
            
            new_type=type_of_initial_variable
            new_value=type_of_initial_variable(x) 
            print('Converted from=',type_of_initial_variable, ': ',x)
            print('Converted to =',new_type, ': ' ,new_value)
    return new_value
    
    return new_value

# cycle_convert(87, 97)

