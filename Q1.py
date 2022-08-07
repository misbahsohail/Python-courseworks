#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# CMT309 Coursework 2
# student number: 1950696


def wikipage2file(wikipedia_pagetitle, output_filepath):
    
    import wikipedia 
    first_result= wikipedia.search(wikipedia_pagetitle, results=1)
    
    #print(first_result)
    
    content=wikipedia.page(first_result).content
    
    title=wikipedia.page(first_result).title
    
    title_without_spaces=title.replace(' ','_')
    #print(title_without_spaces)
    
    filename='/'+title_without_spaces+'.txt'
    
    f2=open(output_filepath + filename,'w+')
    
    f2.write(title)
    f2.write('\n')
    f2.write('\n')
    f2.write('\n')
    f2.write(content)
    
    f2.close()
    
    
    
    # ... YOUR CODE HERE ...


def similar(x,y):
    import wikipedia 
    result = ''
    x=wikipedia.page(x).content
    y=wikipedia.page(y).content
    
    
    
    x_set=set([])
    y_set=set([])
    
    
    x_in_list=x.split(' ')
    y_in_list=y.split(' ')
    
    
    for each_word in x_in_list:
       
        each_word=each_word.lower()
        x_set.add(each_word)
    
    for each_word in y_in_list:
        
        
        each_word=each_word.lower()
        y_set.add(each_word)
        
    
    intersection_x_y=x_set.intersection(y_set)
    union_x_y=x_set.union(y_set)
    
    
    similarity=len(intersection_x_y)/len(union_x_y)
    print(similarity)
    
    
    result=similarity
    # ... YOUR CODE HERE ...
    return result


import wikipedia
#wikipedia_pagetitle='Jennifer Aniston'
#output_filepath='/home/c1950696/Desktop/DataScienceComputation/coursework2'
#wikipage2file(wikipedia_pagetitle,output_filepath)
#x=wikipedia.page('python').content
#y=wikipedia.page('java').content
#similar('java','python')