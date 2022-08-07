#!/usr/bin/env python3
# CMT309 Coursework 1
# student number: 1950696
import sys

def find_return(index_return,return_not_found,line_splited):  #to find keyword 'return' in lines of file and return that line's index number
    while return_not_found:
                   index_return=index_return+1
                   if index_return<len(line_splited):
                    if line_splited[index_return] and line_splited[index_return][0]=='return':
                       return_not_found=False
                   else:
                       index_return=100000
                       return_not_found=False
    return index_return

def found_return(_line,line_splited,index_line):  #after the keyword 'return' is found, this function 'returns' the return body
    final_return_body=''
    return_body=_line[1:]
    for items in return_body:
        final_return_body=final_return_body+items
    
    return final_return_body    

        
def find_if(index_if,if_not_found,line_splited): #to find keyword 'if' in lines of file and return that line's index number
    while if_not_found:
                   index_if=index_if+1
                   if index_if<len(line_splited):
                    if line_splited[index_if] and line_splited[index_if][0]=='if':
                       if_not_found=False
                   else:
                       index_if=100000
                       if_not_found=False
    return index_if


def found_if_elif_else(_line,line_splited,index_line): #after keywords if,else or elif is found, return the body of conditions 
   
   if _line[0]=='else:' or _line[0]=='else :':
        if _line[-1]==':':
            return _line[0]
        else:
            new_else=_line[0][0:len(_line[0])-1]
            return new_else
   else:    
    if_body=''
   
    if_body=_line[1:]
    
    if_body_string =' '
    
    if_condition_processed=if_body_processing(if_body)
  
    if_body_string=if_body_string.join(if_condition_processed)
   
    return if_body_string
   
   
           
def if_body_processing(if_condition_temp): #process conditions which are followed by 'if' keyword 
           
            if if_condition_temp[-1]==':':
                    if_condition_temp.remove(if_condition_temp[-1])
            else:
                    if_condition_temp[-1]=if_condition_temp[-1][0:len(if_condition_temp[-1])-1]
                
            
            return if_condition_temp



def lambda_machine(filename):
  
    filename_temp=filename.split('.')
    
    filename_lambda='lambda_'+str(filename_temp[0])+'.py'
    
    
    
    f=open(filename,'r')
    lines=f.readlines()
    
    f2=open(filename_lambda,'w+')
    line_splited=[]
    
    
    
    #append all lines in a list, with each line having its own list
    for each_line in lines:
        if each_line.strip():
         line_splited.append(each_line.split())
        
    #check on which lines, function is defined    
    for index_line in range(len(line_splited)):
       #print(line_splited[index_line])
       final_func_body=''
       for index_words in range(len(line_splited[index_line])):
           if  line_splited[index_line][0]=='def':
               
               func_name_args=line_splited[index_line][1]
               #print(func_name_args)
               func_name_arg_list1=func_name_args.split('(') #split at ( to get name
               #print(func_name_arg_list1)
               func_name=func_name_arg_list1[0]
               func_name_arg_list2= func_name_arg_list1[1].split(')')
               #print(func_name_arg_list2)
               func_arg=func_name_arg_list2[0]
               f2.write(func_name)
               f2.write('=')
               
               f2.write('lambda ')
               f2.write(func_arg)
               f2.write(':')
               
               index_return=index_line
               index_if=index_line
              
               return_not_found=True
               
               index_return=find_return(index_return,return_not_found,line_splited)
               
               if_not_found=True
               index_if=find_if(index_if,if_not_found,line_splited)
              
              
                    
               if index_return<index_if: #return 'return' without if statmement
                
                   if line_splited[index_return][0]=='return':
                       
                       final_func_body=found_return(line_splited[index_return],line_splited,index_return)
                       f2.write(final_func_body)
               else:
                   if line_splited[index_if][0]=='if': #first if found
                      
                
                       if_body=found_if_elif_else(line_splited[index_if],line_splited,index_if)
                      
                      
                       return_not_found=True
                       index_return=find_return(index_if,return_not_found,line_splited)
                       final_return_body=found_return(line_splited[index_return],line_splited,index_return)
                       
                       first_if_statement=''
                       first_if_statement=str(final_return_body) + ' if '+ if_body
                       f2.write(first_if_statement)
                       index_for_new_if=index_return
                       
                      
                       while line_splited[index_for_new_if][0]!='def' and index_for_new_if<len(line_splited)-1: #repeating the loop until the new function def is found
                           index_for_elif=10000
                           index_for_else=10000   
                           index_for_new_if=index_for_new_if+1
                           if line_splited[index_for_new_if][0]=='if':
                               if_body=found_if_elif_else(line_splited[index_for_new_if],line_splited,index_for_new_if)
                      
                               return_not_found=True
                               index_return=find_return(index_for_new_if,return_not_found,line_splited)
                               final_return_body=found_return(line_splited[index_return],line_splited,index_return)
                               
                               first_if_statement=''
                               first_if_statement=str(final_return_body) + ' if '+ if_body
                               f2.write(' ')
                               f2.write(first_if_statement)
                               
                               index_for_new_if=index_return
                               
                               
                           if line_splited[index_for_new_if][0]=='elif': #elif found

                                
                                if_body=found_if_elif_else(line_splited[index_for_new_if],line_splited,index_for_new_if)
                      
                                return_not_found=True
                                index_return=find_return(index_for_new_if,return_not_found,line_splited)
                                final_return_body=found_return(line_splited[index_return],line_splited,index_return)
                                
                                _elif_statement=''
                                _elif_statement=str(final_return_body) + ' if '+ if_body
                               
                                index_else=index_return+1
                                else_body=found_if_elif_else(line_splited[index_else],line_splited,index_else)
                                index_return=find_return(index_else,return_not_found,line_splited)
                               
                                final_return_body=found_return(line_splited[index_return],line_splited,index_return)
                                
                               
                                f2.write(' ')
                                elif_else_statement=' else ' + '( ' +  _elif_statement + ' else '+ str(final_return_body)+' )'
                                
                                f2.write(elif_else_statement)
                                index_for_new_if=index_return
                                index_for_elif=index_return

                           index_for_elif=index_for_elif+1
                           
                           if line_splited[index_for_new_if][0]=='else' or line_splited[index_for_new_if][0]=='else:' : # else found
                                
                                
                                else_body=found_if_elif_else(line_splited[index_else],line_splited,index_else)
                                #index_return=find_return(index_else,return_not_found,line_splited)
                               
                                final_return_body=found_return(line_splited[index_for_new_if + 1],line_splited,index_return)
                               
                                else_statement=''
                                else_statement=' else '+ final_return_body
                                f2.write(else_statement)
                            
                                index_for_new_if=index_return 
                                index_for_else=index_return 
                           index_for_else=index_for_else+1
                           if index_for_elif<len(line_splited) :     
                                if line_splited[index_for_elif][0]=='if' or line_splited[index_for_elif][0]=='def':
                                     break
                                break
                           if index_for_else<len(line_splited):     
                                if  line_splited[index_for_else][0]=='if' or  line_splited[index_for_else][0]=='def':
                                     break
                                break
                            
                            
               f2.write('\n')
               break

    for index_line_lambda in range(len(line_splited)):  
          
     for index_words_lambda in range(len(line_splited[index_line_lambda])):
        if  line_splited[index_line_lambda][index_words_lambda]=='lambda' or line_splited[index_line_lambda][index_words_lambda]=='lambda:' :
             
             loc_of_lambda=index_words_lambda
             
             if len(line_splited[index_line_lambda][0:loc_of_lambda])==2 or len(line_splited[index_line_lambda][0:loc_of_lambda])==1:
                 f2.write('\n')
                 
                 
                 lambda_string=' '
                 lambda_string=lambda_string.join(line_splited[index_line_lambda])
                 f2.write(lambda_string)
                 
    # YOUR CODE HERE
    # YOUR CODE HERE
    return
#filename='mytest.py'
#lambda_machine(filename)
# ---- DO NOT CHANGE THE CODE BELOW ----
if __name__ == "__main__":
    if len(sys.argv)<2: raise ValueError('Provide filename as input argument')
    filename = sys.argv[1]
    print('filename is "{}"'.format(filename))
    lambda_machine(filename)
