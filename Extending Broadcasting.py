#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#CMT309 Coursework 2
# student number: 1950696




def extend_broadcast(fun,a,b): #extend boradcasting to make the arrays compatible 
    import numpy as np

    a_new=a
    b_new=b
    for each_dim_a in range(len(a.shape)):
        
        if a.shape[each_dim_a]==0 or b.shape[each_dim_a]==0:
            print('extended broadcasting not possible')
            return 
            
            
        if a.shape[each_dim_a] % b.shape[each_dim_a] == 0 or b.shape[each_dim_a] % a.shape[each_dim_a]==0:
              
             
              
              if a.shape[each_dim_a] < b.shape[each_dim_a]:
                  
                  temp=a_new
                 
                  #print('a smaller')
                  
                  while a_new.shape[each_dim_a] != b.shape[each_dim_a]:
                      
                      a_new=np.concatenate((temp,a_new),axis=each_dim_a)
                    
                      #print('contanated anew:',a_new.shape)
                      #print(a_new)
                      
                      
                  
                      
              elif b.shape[each_dim_a] < a.shape[each_dim_a]:
                  #print('a larger')
                 
                  temp=b_new
                  
                  
                  while a.shape[each_dim_a] != b_new.shape[each_dim_a]:
                      
                      b_new=np.concatenate((temp,b_new), axis=each_dim_a)
                      #print('contanated bnew:',b_new.shape)
                      #print(b_new)
                      
                      
              elif b.shape[each_dim_a] == a.shape[each_dim_a]:
                  #same
                  pass
                 
        else:
            print('extended broadcasting not possible')
            return
                
    print('extended broadcasting result:')        
    result=arithmatic_oper(fun,a_new,b_new)
    return result
    
              
def arithmatic_oper(oper,a_for_oper,b_for_oper): #function for performing arithmatic operations on a and b 
     
     import numpy as np

     return oper(a_for_oper,b_for_oper)      
    
    



def broadcast(fun, a, b):
    #print(a)
    #print(b)
    
    import numpy as np
    from numpy import array, newaxis
    
    try:  # function will try doing a simple braodcast 
        result=arithmatic_oper(fun,a,b)  
        print('Simple broadcasting result')
        return result 
        
    except: #if simple broadcast fails
        a_more_dim=a
        b_more_dim=b
        
        if len(a.shape)!=len(b.shape):
            if len(a.shape)<len(b.shape):
                difference=len(b.shape)-len(a.shape)
                
                for n in range(difference):
                    
                    a_more_dim = array(a_more_dim)[newaxis]
                    
            #print(a_more_dim.shape)
            
            if len(a.shape)>len(b.shape):
                difference=len(a.shape)-len(b.shape)
                
                for n in range(difference):
                    
                    b_more_dim = array(b_more_dim)[newaxis]
                    
            #print(b_more_dim.shape)
            
            result=extend_broadcast(fun,a_more_dim,b_more_dim)
        
        else:
            
            result=extend_broadcast(fun,a_more_dim,b_more_dim)
            
            
    print(result)
    return result


import numpy as np 
#a=np.ones((6,9,1))
#b=np.ones((3,2))


#fun=np.subtract
#broadcast(np.subtract, np.ones((6,9,1)), np.ones((3,2)))
#broadcast(np.subtract,np.eye(4),np.ones((3,2,2)))
    

