# Q1
# Student number: 1950696

import re

def read_file(filename):
    ''' Reads a text file
        
        Parameters:
        filename  - the name of the file (string)
    
        Returns:
        S - the entire content of file. Type: string '''
    
    f=open(filename,'r')
    s=f.read()
    return s
    

def find_acronyms(s):
    ''' Finds a list of acronmys in a given string
        
        Parameters:
        s - the text as returned from read_file(). Type: string
        
        Returns:
        acronyms- the list of acronyms. Type: list '''
    
    
    s_split=s.split(' ') #spliting sentenses to words on every space
    e1=[]
    for all_words in s_split:
        if all_words.find('-')==-1:  #if hypen not found in a word
            e_temp=re.findall(r"\b([a-z]{,1}[A-Z]{2,})(s){0,1}\b", all_words)  #looking if the word is an Acronym
           
            for items in e_temp:   
            
                    e1.append(items[0])  #the singular form of acronym (without hypen) is being put into list e1
    
    hyphen_search=re.findall(r'\b([a-z]{,1}[A-Z]{2,})-([a-z]{,1}[A-Z]{2,}(s){0,1})\b',s) #checking if the word with hypen is an Acronym
  
    for all_words in hyphen_search:
            
            word_with_hyphen='-'.join(all_words[0:2])   #the singular form of acronym(with hyphen) is being put into list e1
            e1.append(word_with_hyphen)
        
    acronyms=set(e1)
    print(acronyms)    
    
    return acronyms 
  
def find_long_forms(s, acronyms):
    '''Finds long forms of the acronyms with the text
        
       Parameters:
       s - the text as returned from read_file(). Type: string
       acronmys - list of acronyms as returned from function find acronyms. Type: list
       
       Returns:
       d - list of acronyms and their forms. Type: Dictionary (Key: acronyms, Value: Long forms)'''
    
    from nltk import tokenize
    list_sentences=s.split('.')
    
    word_found = { i : 0 for i in acronyms }
    sent_containing_word = { i : '' for i in acronyms }
    
    for sent_index in range(len(list_sentences)):
        for all_acronyms in acronyms:
    
            if word_found[all_acronyms]==0:
                
                result = list_sentences[sent_index].find(all_acronyms)
            
                if result!=-1:
                    word_found[all_acronyms]=1
                    sent_containing_word[all_acronyms]=list_sentences[sent_index]
                    
                    
            else:
                continue
            
            
            
   
    d={}
    for all_acronyms in acronyms:
        
        
        
        
      
        
        sent_temp=sent_containing_word[all_acronyms]
        
        list_words_temp = tokenize.word_tokenize(sent_temp) #a temporary list of words which may contain dashes
        list_words=[]
        for each_word in list_words_temp:
          
                if each_word.find('\'')!=-1:
                    list_words.append(each_word.replace('\'',''))
                
                elif each_word.find('-')!=-1:
                
                   
                    list_word_having_dash=each_word.split('-')
                    
                    for word_dash in list_word_having_dash:
                       
                        list_words.append(word_dash)
                        
                elif each_word.find('–')!=-1:
                   
                    list_word_having_dash=each_word.split('–')
                    
                    for word_dash in list_word_having_dash:
                        list_words.append(word_dash)
                
                elif each_word.find('\'')!=-1:
                    a=each_word.replace('\'','')
                    list_words.append(a)
                    
                
                else:
                    list_words.append(each_word)
            
        #print(list_words)
        loop_limit=len(all_acronyms)
        for word_index in range(len(list_words)):
            n=1
            n2=1
            n3=n-1
            sameword=''
            try:
                    
                if list_words[word_index][0]==all_acronyms[0] or list_words[word_index][0]==all_acronyms[0].lower():
                    
                   while (n<loop_limit):
                    
                        #checking for the next word if it corrosponds to the longer form of acronym                    
                        if list_words[word_index+n][0]==all_acronyms[0+n2] or list_words[word_index+n][0]==all_acronyms[0+n2].lower():
                        
                            final_word=sameword+' '+list_words[word_index+n]
                            
                            d[all_acronyms]=final_word
                            
                            
                            #checking if one of the acronym is itself a longer form for example fMRI
                            if list_words[word_index+n]==all_acronyms[-len(all_acronyms)+n:]:
                                 d[all_acronyms]=list_words[word_index]+' '+all_acronyms[-len(all_acronyms)+n:]
                                
                
                            n=n+1
                            n2=n2+1
                            #checking for words like for and in
                        elif list_words[word_index+n]=='for' or list_words[word_index+n]=='in':
                               
                                n=n+1
                                loop_limit=loop_limit+1
                               
                        
                                
                             #checking if a single word has longer form of more than 1 letter of an acronym, example eigenvalue 
                        elif list_words[word_index+n3].find(all_acronyms[0+n2])!=-1 or list_words[word_index+n3].find(all_acronyms[0+n2].lower())!=-1:
                            
                            
                            sameword=list_words[word_index+n3]
                           
                            n3=n3+1
                            n2=n2+1
                            
                        else:
                            break
                        
                   if n== loop_limit:
                        acronym_found=all_acronyms
                        long_form=''
                        for count in range(n):
                            
                            long_form=long_form +' ' + list_words[word_index+count]
                   d[acronym_found]=long_form
                   
            
            except:
                  pass
                        
    acronym_list=[ i for i in d.keys()]
    
    for each_acronym in acronym_list:
            
            d[each_acronym]=d[each_acronym].strip().replace('.','')
            d[each_acronym]=d[each_acronym].strip().replace(',','')
            
    for a in acronyms:
        if a in d.keys():
            pass
        else:
            d[a]='None'
    print(d)                    
    return d

def replace_acronyms(s, d):
    '''Replaces acronyms with the long forms in the given text
        
       Parameters:
       s - the text as returned from read_file(). Type: string
       d - list of acronyms and their forms. Type: Dictionary (Key: acronyms, Value: Long forms)
           returned from function find_long_forms()
       
       Returns:
       new_s - text, with the acronyms replaced with their corrospoding longer forms. Type: String'''
    
    acronym_list=[ i for i in d.keys()]
    #print(acronym_list)
    words_list=s.split(' ')
    possible=1
    
    for each_acronym in acronym_list:
        
        count=0
        for word_index in range(len(words_list)):
            
            if words_list[word_index].find(each_acronym)!=-1:
                if words_list[word_index].find('-')!=-1:  #finding words with dash
                    #print('found',words_list[word_index])
                    res=[words_list[word_index]]
                    #print(res)
                else:
                    reg= r"(?<!\-|\w|\/)" + each_acronym + r"(?!\w|\-|\/)|" + each_acronym + r"(?=s)" #finding acronmys in words
                    res = re.findall(reg, words_list[word_index])
                #print(res, 'out res' )
                try:
                    if res[0] in acronym_list:  #if the word is list of acronyms
                        
                        if d[res[0]]=='None':  #and the long form is not available
                           
                            possible=0  #putting possible to 0
                        else:
                            possible=1  #putting possible to 1
                except:
                    pass
                    
              
                if count>=1 and possible!=0:
                    #print(each_acronym, 'at', count)
                    
                    if words_list[word_index-1][-1]=='.' or  ("\n" in words_list[word_index]):  #checking if the word is the first word of a sentence or a paragraph
                        temp=d[each_acronym].capitalize()
                        temp5=''
                        if temp.find(' ')!=-1:
                            temp4=temp.split(' ')  
                        
                            for items in temp4:
                                if items.upper() in d.keys():
                                    items=items.upper()
                                temp5=temp5+' '+items
                        words_list[word_index]=words_list[word_index].replace(each_acronym,temp5) 
                    
                    else:
                        temp = d[each_acronym][0].lower() + d[each_acronym][1:]
                        
                        temp3=''
                        if temp.find(' ')!=-1:
                            temp2=temp.split(' ')
                            for items in temp2:
                                if items.upper() in d.keys():
                                    items=items.upper()
                                    temp3=temp3+' '+items
                                else: 
                                    items = items[0].lower() + items[1:]
                                    temp3=temp3+' '+items
                        temp=temp3
                        

                        words_list[word_index]=words_list[word_index].replace(each_acronym,temp)
                        count=count+1
                else:
                    count=count+1
                    
            else:
                pass
    
    final_para_string=''    
    for words in words_list:
        final_para_string=final_para_string+' '+words    
 
    print(final_para_string)
    new_s=final_para_string
    return new_s       

#filename='acronym_example4.txt'       
#text=read_file(filename)
#acronyms=find_acronyms(text)
#dictionary=find_long_forms(text,acronyms)
#replace_acronyms(text,dictionary)

