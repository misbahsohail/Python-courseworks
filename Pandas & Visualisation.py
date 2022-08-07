#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#CMT309 Coursework 2
# student number: 1950696

# 2.1 Visualisation

def sale_history(df):
    '''Produces a bar plot that shows, for each year, the quantity sold for each
       product i.e. soda, wine and juice
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       Nothing'''
    
    df['year'] = pd.DatetimeIndex(df['order_date']).year #produces a new column year which contains year corrospoding to each order id
    
    columns = ['soda_qty','wine_qty', 'juice_qty']
    years_set=set(df['year'])
    years_set=sorted(years_set) #a set is created which contains 'year' values
  
    
    qty_soda_grp_by_year = df.groupby("year")["soda_qty"].sum()
    qty_wine_grp_by_year = df.groupby("year")["wine_qty"].sum()
    qty_juice_grp_by_year = df.groupby("year")["juice_qty"].sum()
    
    
    df_years_qty = pd.DataFrame(index=years_set, columns=columns) #a new dataframe is created which contains sum of each drink quantity sald for each year
    
    
    df_years_qty['soda_qty']=qty_soda_grp_by_year
    df_years_qty['wine_qty']=qty_wine_grp_by_year
    df_years_qty['juice_qty']=qty_juice_grp_by_year
    
    df_years_qty.plot.bar()
    return 
    


def heatmap(df):
        '''Produce a correlation matrix and heatmap visualization between gbp
       and quantity values for soda, juice and wine
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       Nothing'''
     
        new_df=df[['soda_qty','wine_qty','juice_qty','soda_gbp','wine_gbp','juice_gbp','total_gbp','total']]
        corr = new_df.corr()
        sns.heatmap(corr,cmap=sns.diverging_palette(220, 10, as_cmap=True),vmin=0, vmax=0.3,linewidths=.5)



#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# 2.3: QUESTIONS

# •    How many orders were placed in 2016?
#ANSWER: 2740 orders
def count_orders_2016(df):
     '''Calculates the total number of orders placed in each year
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       int(Number of orders places in 2016)'''
    
     df['year'] = pd.DatetimeIndex(df['order_date']).year
    
     count_years = df.groupby("year")["order_id"].count()
    
     print('count_orders_2016: ',count_years[2016])
    
     numb_orders = count_years[2016]
    # your code here
     return numb_orders
#------------------------------------------------------------------------------#

# •    Which client has purchased the most number of soda bottles overall?
#ANSWER  client id:  4161  with  41617  number of orders
def best_client_soda_bottles(df):
    '''Calculates the total quantity of soda purchased by each distict client
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       int(Cliend_id of the client who purchased the most number of soda bottles) '''
    
    
    client_soda = df.groupby("client_id")["soda_qty"].sum()
    #print(type(client_soda))
    
    max_value=client_soda.max()#takes the value of quantity such that is the maximum value among quantities for each corrospoding client 
    #print(max_value)
    
    client_ids=set([])
    
    for client in df['client_id']:#makes a set of all distict client_ids from df['client_id'] column
        client_ids.add(client)
         
    client_ids=sorted(client_ids)#the set is being sorted in descending order
    #print(client_ids)
    
    for all_clients in client_ids:# finds the client id who had the maximum quantity value
        
        #print(client_soda[all_clients])
        if client_soda[all_clients]==max_value:
            max_client_id=all_clients
            #print(all_clients)
    
    print('client id: ', max_client_id,' with ',max_value,' number of orders')
            
    best_client_id = max_client_id
    # your code here
    return best_client_id
#------------------------------------------------------------------------------#

# •    In which weekday is wine sold the most on average (across the whole sales history)?
#ANSWER  MONDAY
def best_weekday_for_wine(df):
    '''Calculates the average of total quantity of wine sold in each week day
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       str(weekday in the most wine was sold out on average) '''
       
    df['Day of Week'] = pd.to_datetime(df['order_date']).dt.day_name() #creates a column of week-day associated with with each order time i.e. each row
   
    #print(df['Day of Week'])
    count_wine_sold_weekdays = df.groupby("Day of Week")["wine_qty"].mean()
    
    weekdays_name=set([])
    
    for each_day in df['Day of Week']: #makes a set of days of each week, i.e. Monday, Tuesday,......
        weekdays_name.add(each_day)
    
   
    max_value=count_wine_sold_weekdays.max() #finds the max value of wine among all the values
    
    
    for each_day in weekdays_name:#finds a particular week day which had the wine quanity average equal to the max value found above
        
        if count_wine_sold_weekdays[each_day]==max_value:
           best_weekday=each_day
           

    print("best_weekday_for_wine: ",best_weekday)
    #best_weekday = ''
    # your code here
    return best_weekday
#------------------------------------------------------------------------------#
    
# •    Which drink was the most popular (in GBP) in winter
#    (from Dec 21st to March 21st)? Break your answer down for each year.
#ANSWER {2013: 'wine', 2014: 'soda', 2015: 'soda', 2016: 'soda', 2017: 'wine'}
def most_popular_drink(df):
    '''Calculates which drink was popular in DBP in a particular time period (Dec 21st to March 21st) for each distinct year
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       dictionary(year being the key and its corrospoding popular drink type ) '''
    d = {}
    df['date_and_time']=pd.to_datetime(df['order_date'])
    
    #gives for 4 different sets of rows each within a particular time period allocated with the conditions
    mask1 = (df['date_and_time'] >= '2013-12-21') & (df['date_and_time'] <= '2014-3-21') #between 21 Dec 2013 to 21 March 2014
    mask2 = (df['date_and_time'] >= '2014-12-21') & (df['date_and_time'] <= '2015-3-21') #between 21 Dec 2014 to 21 March 2015
    mask3 = (df['date_and_time'] >= '2015-12-21') & (df['date_and_time'] <= '2016-3-21') #between 21 Dec 2015 to 21 March 2016
    mask4 = (df['date_and_time'] >= '2016-12-21') & (df['date_and_time'] <= '2017-3-21') #between 21 Dec 2016 to 21 March 2017
     
    
    column_names = df.head() 
    
    df_masked = pd.DataFrame(columns=column_names) #creates a new dataframe to save the filtered values
    
    #Appends the values to the new data_frame created
    df_masked=df.loc[mask1]
    df_masked=df_masked.append(df.loc[mask2])
    df_masked=df_masked.append(df.loc[mask3])
    df_masked=df_masked.append(df.loc[mask4])
    
    
    df_masked['year'] = pd.DatetimeIndex(df_masked['date_and_time']).year #extracts year to create a new column 'year'
    
    columns = ['soda_gbp','wine_gbp', 'juice_gbp']
    years_set=set(df_masked['year'])
    years_set=sorted(years_set)
    
    #calculates sum of each drink sold in each year
    soda_gbp_year = df_masked.groupby("year")["soda_gbp"].sum()
    wine_gbp_year = df_masked.groupby("year")["wine_gbp"].sum()
    juice_gbp_year = df_masked.groupby("year")["juice_gbp"].sum()
    
    #creates a data_frame with 4 columns
    #Year(index)  soda_gbp wine_gbp  juice_gbp
    df_years_gbp = pd.DataFrame(index=years_set, columns=columns)
    
    df_years_gbp['soda_gbp']=soda_gbp_year
    df_years_gbp['wine_gbp']=wine_gbp_year
    df_years_gbp['juice_gbp']=juice_gbp_year
    

    
    df_years_gbp["max_gbp"] = df_years_gbp[["soda_gbp", "wine_gbp","juice_gbp"]].max(axis=1) #created a new column max_gbp which contains the maximnum value among the 3 drinks gbp, 
    #i.e. gives a row wise max value
 
    for index,each_row in df_years_gbp.iterrows(): #finds which drink's gbp matchs the max value of gbp obtained for each year and saves them into a dictionary 
        
        max_value=each_row['max_gbp']
        
        for drink_types in df_years_gbp:
                if df_years_gbp.loc[index,drink_types]==max_value:
                    drink_name_for_dictionary=drink_types.replace('_gbp','')
                    d.update({index:drink_name_for_dictionary})
                    
                    break
        
    print ("most_popular_drink: ",d)
    #d = {} # d could be {2009:'wine',2010:'soda',2011:'soda' ... }
    
    return d
#------------------------------------------------------------------------------#
    
# •    In which year-month (e.g. January 2015) was there the
#   highest number of orders in which the quantity of wine bottles
#   was higher than the average for that year?
#ANSWER Year:2016 Month: December
def best_yearmonth_aboveavg_wine(df):
    '''Finds total count of orders of wine qty for each month such that the value of these wine orders are greater than the average of total for that particular year  
      
       Parameters:
       df(dataframe) Dataframe of the orignal csv file
       
       Returns:
       string( year and month such that the count is highest ) '''
    
    #extracts each date into year, month and day and puts them into new columns
    df['year'] = pd.DatetimeIndex(df['order_date']).year
    df['month'] = pd.DatetimeIndex(df['order_date']).month
    df['day'] = pd.DatetimeIndex(df['order_date']).day
    
    
    avg_wine_qty_year = df.groupby("year")["total"].mean() #finds the average of all totals for each year
    year_month_order_count=df.groupby(["year","month","day"])["wine_qty"].sum() #sum of wine qty for each day of all months of all years and creates a panda series
    
    years_set=set(df['year'])
    years_set=sorted(years_set)
    
    index_col=list(range(1, 1000))
    columns = ['year','month','day','orders']
    
    
    #for each value of wine count in series called 'year_month_order_count', 
    #the code below checks if the value is greater than the average of total for that year
    #if yes, it gets saved into a new dataframe called df_2 with 5 columns
    #index_col(index) year month day orders
    df_2 = pd.DataFrame(index=index_col,columns=columns)
    count=1
    for year in years_set: #for all years
        for month in range(1,13): #for all months in a year
            for day in range(1,32):#for all days in a month
                try: #for all possible comninations.. like year=2017,month=3, day=4 is not possible since we dont have the values for that comnination
                    a=year_month_order_count[year][month][day]
                    if a>avg_wine_qty_year[year]:
                        # Add a new row at index position count with values provided in list
                        df_2.iloc[count] = [year, month, day, a]
                        count=count+1
                        
                        
                except: #the loop just ignores and pass if an error for bad combination arrises 
                    pass
                    
                    
   
    df_2=df_2.dropna() #removes the reduntant rows
    
    count_wine_order_per_month=df_2.groupby(["year","month"])["orders"].count() #counts the new number of days which satisfies the condition for each month of each year
    #print(count_wine_order_per_month)
    
    max_value=count_wine_order_per_month.max() #finds the max value of all the counts for all the months in all years
    
   
    
    for year in years_set:
        for month in range(1,13): #for all months a in year
            
            try: #try if the value is availabe is for that particular index
                if count_wine_order_per_month[year][month]==max_value: #gives that particular month of the year which has the highest number of order satisfing the condiion
         
                    #print(year,' ',month)
                    a=year
                    b=month
            except: #or else pass
                pass
    
    
    number_month={1:'January',2:'Feburary',3:'March',4:'April',5:'May',6:'June',7:'July',8:'August',9:'September',10:'October',11:'November',12:'December'}
    best_ym = 'Year:'+str(a)+' Month: '+number_month[b]
    print("best_yearmonth_aboveavg_wine: ",best_ym)
    return best_ym


#------------------------------------------------------------------------------------------------#  


import pandas as pd
import seaborn as sns

#data_frame = pd.read_csv("/home/c1950696/Desktop/DataScienceComputation/coursework2/orders_cardiff_drinks.csv")


#######ANSWERS#######
#QUESTION 2.3
#1... 3740
#2... client id:  4161  with  41617  number of orders
#3...'Monday'
#4...{2013: 'wine', 2014: 'soda', 2015: 'soda', 2016: 'soda', 2017: 'wine'}
#5...Year:2016 Month: December
