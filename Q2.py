#!/usr/bin/env python3
# CMT309 Coursework 1
# student number: C1950696

import sys

def is_number(x):  
   '''A function which tells if the string x can be converted to a numerical value or not
      
      Parameters:
      x(str) An element from the input text
      
      Returns:
      True(bool): if the element can be converted to float
      False(bool): if the element cannot be converted to float  ''' 
   
   if x.isdigit()==True:
       return True
   elif x.replace('.','',1).isdigit()==True:
       return True
   else:
       return False

def has_punc(unit_found):
    '''A function which tells if a particular unit x end with a punctuation mark or not
      
       Parameters:
       unit_found(str) A unit from the input text
      
       Returns:
       if punctuation-mark found: unit_found(str) after removing the last char i.e. the punctuation mark, the punctuation mark
       if punctuation-mark NOT found: original unit_found(str), NONE(bool) '''
      
    punc_list=['.', ',' , '!' , ':' , ';','?']
   
    for punc in punc_list:
        
        if unit_found[-1]==punc: #check the last character of word if is a punctuation mark contained in pun_list
            return unit_found[0:len(unit_found)-1],punc
       
    return unit_found,None


def perform_distance_conversion(value, unit_found, convert_to):
    '''This function performs distance/length units conversions
      
       Parameters:
       value(float) A numerical value associated with distance/length unit which is to be changed
       unit_found(str) The initial unit which is found in text
       convert_to(str) New unit which is found in dictionary D
        
       Returns:
       converted_value(float) The converted numerical value '''
       
    distance_conv = [['km',1],['m',1000],['cm',100000],['mm',1000000]] #Distance conversion helper matrix
    
    for distance_units_index in range(len(distance_conv)):
        if convert_to==distance_conv[distance_units_index][0]:
                convert_to_helper=distance_conv[distance_units_index][1]
    
    for distance_units_index in range(len(distance_conv)):
        if distance_conv[distance_units_index][0]==unit_found:
        
                initial_unit_helper=distance_conv[distance_units_index][1]
                converted_value=(value*(float(convert_to_helper))/float(initial_unit_helper))
                
    return converted_value 

def perform_time_conversion(value, unit_found, convert_to):
    '''This function performs time units conversions
      
       Parameters:
       value(float) A numerical value associated with time unit which is to be changed
       unit_found(str) The initial unit which is found in text
       convert_to(str) New unit which is found in dictionary D
        
       Returns:
       converted_value(float) The converted numerical value '''
    
    time_conv = [['sec',3600],['min',60],['h',1]] #Time conversion helper matrix
    
    
    for time_units_index in range(len(time_conv)):
        if convert_to==time_conv[time_units_index][0]:
                convert_to_helper=time_conv[time_units_index][1]
    
    for time_units_index in range(len(time_conv)):
        if time_conv[time_units_index][0]==unit_found:
       
                initial_unit_helper=time_conv[time_units_index][1]
                converted_value=(value*(float(convert_to_helper))/float(initial_unit_helper))
                
    return converted_value

def perform_file_size_conversion(value, unit_found, convert_to):
    '''This function performs filesize units conversions
      
       Parameters:
       value(float) A numerical value associated with filesize unit which is to be changed
       unit_found(str) The initial unit which is found in text
       convert_to(str) New unit which is found in dictionary D
        
       Returns:
       converted_value(float) The converted numerical value '''
    
    file_size_conv=[['B',1000**5],['KB',1000**4],['MB',1000**3],['GB',1000**2],['TB',1000],['PB',1]] #Filesize conversion helper matrix
    
    for file_size_units_index in range(len(file_size_conv)):
        if convert_to==file_size_conv[file_size_units_index][0]:
                convert_to_helper=file_size_conv[file_size_units_index][1]
    
    for file_size_units_index in range(len(file_size_conv)):
        if file_size_conv[file_size_units_index][0]==unit_found:
        
                initial_unit_helper=file_size_conv[file_size_units_index][1]
                converted_value=(value*(float(convert_to_helper))/float(initial_unit_helper))

    return converted_value




def unit_translator(filename, D):
  
    
    if 'length' in D:     
        convert_dist_to=D['length']
    if 'time' in D:
        convert_time_to=D['time']   
    if 'filesize' in D:
        convert_file_size_to=D['filesize']
    
    #Initialize helper lists 
    distance_units=['km','m','cm','mm']
    file_size_units = ['B','KB','MB','GB','TB','PB']
    time_units = ['sec','min','h']

    
    # read file
    f=open(filename,'r')
    content=f.readlines()
    filename_temp=filename.split('.')
    
    newfile=str(filename_temp[0])+'_translated.txt'
    
    
    f2=open(newfile,'w+')
    
    
    #print(content)

    para_index=0
    words_in_para_list=[]
    
    #Making a list of words in each paragraph i.e. seperated by new line
    for paragraphs in content:
      words_in_para_list.append([])
      words_in_para_list[para_index] = paragraphs.split()
      para_index+=1
    
    output = ''
    for words_in_para in words_in_para_list:
        
        for index in range(len(words_in_para)): #for each word in paragraph
            
            current_word = words_in_para[index]
            current_word_without_punc, punc = has_punc(current_word)
        
        
            if is_number(current_word):   #True if the current word can be converted to a numerical value
                numeric_value = float(current_word)
                unit_found = words_in_para[index + 1]
                
                unit_found, punc = has_punc(unit_found)
                
                if unit_found in distance_units:
                    if unit_found != convert_dist_to: #If the initial is not the same as the final unit
                        converted_value = perform_distance_conversion(numeric_value, unit_found, convert_dist_to)
                        if punc!=None:
                            output += str(converted_value) + ' ' + convert_dist_to + str(punc) + ' '
                        else:
                            output += str(converted_value) + ' ' + convert_dist_to + ' '
                    else:
                        if punc!=None:
                            output += str(numeric_value) + ' ' + convert_dist_to + str(punc) + ' ' 
                        else:
                            output += str(numeric_value) + ' ' + convert_dist_to + ' ' 
                    
        
                elif unit_found in time_units:
                    if unit_found != convert_time_to:
                        converted_value = perform_time_conversion(numeric_value, unit_found, convert_time_to)
                        if punc!=None:
                            output += str(converted_value) + ' ' + convert_time_to + str(punc) + ' '
                        else:
                            output += str(converted_value) + ' ' + convert_time_to + ' '  
                    else:
                        if punc!=None:
                            output += str(numeric_value) + ' ' + convert_time_to + str(punc) + ' ' 
                        else:
                            output += str(numeric_value) + ' ' + convert_time_to + ' ' 
        
                elif unit_found in file_size_units:
                    if unit_found != convert_file_size_to:
                        converted_value = perform_file_size_conversion(numeric_value, unit_found, convert_file_size_to)
                        if punc!=None:
                            output += str(converted_value) + ' ' + convert_file_size_to + str(punc) + ' '
                        else:
                            output += str(converted_value) + ' ' + convert_file_size_to + ' '
                    else:
                        if punc!=None:
                            output += str(numeric_value) + ' ' + convert_file_size_to + str(punc) + ' ' 
                        else:
                            output += str(numeric_value) + ' ' + convert_file_size_to + ' ' 
        
            else:
                #If the current word(punctuation removed) is not the list of distance, time or filesize parameter, write the current_word as it is
                #as the units in distance, time and filesize lists doesn't have punctuation marks
                if (current_word_without_punc in distance_units or current_word_without_punc in time_units or current_word_without_punc in file_size_units) is False :
                    output +=  current_word + ' '
                #If the current word(punctuation removed) is part of distance, time or filesize list, but the preceding word is not a numerical value,
                #write the current word as it is
                if (current_word_without_punc in distance_units or current_word_without_punc in time_units or current_word_without_punc in file_size_units) is True and (is_number(words_in_para[index - 1])) is False:
                    output +=  current_word + ' '    
        output=output+'\n'     #write line new after each paragraph                 
    f2.write(output)
    print(output)
    

    return


# define dictionary here
D= {'length' : 'm', 'filesize' : 'B' , 'time' : 'h'}
#unit_translator('example.txt', D)
# ---- DO NOT CHANGE THE CODE BELOW ----
if __name__ == "__main__":
    if len(sys.argv)<2: raise ValueError('Provide filename as input argument')
    filename = sys.argv[1]
    print('filename is "{}"'.format(filename))
    unit_translator(filename, D)
