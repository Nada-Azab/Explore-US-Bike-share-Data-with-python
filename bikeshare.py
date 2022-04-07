import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():  
    print('Hello! Let\'s explore some US bikeshare data!')
  
    v=["chicago","new york city","washington"]

    city=''
    month=''
    day=''
    city=input("choose the city : chicago, new york city, washington :\n").lower()
    while city not in v :
         print("plase,Type valid name of city \n") 
         city=input("Choose the city :chicago, new york city, washington :\n").lower()
  
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    month=input("Type name of month or all :\n").lower()
    while month not in months :
        print("Plase type corrct name of month") 
        month=input("Type name of month :\n").lower()
  
    day=input("Type the day or all :\n").lower()
    while day not in ['monday','tuesday','sunday','saturday','friday',' wednesday','thursday','all']:
        print("Plase , type valid name of day") 
        day=input("Type the day :\n").lower()
         
  
          
    print('-'*40)
    return city,month,day
    

def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != 'all':
    
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        
        month = months.index(month) + 1

        
        df = df[df['month'] == month]
        
        
        if day != 'all':
            df = df[df['day_of_week'] == day.title()]
    return df

def time_stats(df):
 

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    common_month = df['month'].mode()[0]  
    print("The most common month : ",common_month) 
    
    common_day=df['day_of_week'].mode()[0]
    print("The most common day of week : ",common_month)

    
    common_start_time =df['Start Time'].mode()[0]
    print("The most common start hour : ",common_start_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

   
    commonly_start_station=df['Start Station'].mode()[0]
    print("Most commonly used start station : ",commonly_start_station)
   
    commonly_end_station=df['End Station'].mode()[0]
    print("Most commonly used end station :",commonly_end_station)
 
    most_frequent_combination=df.groupby(['Start Station','End Station']).size().idxmax()
    print("Most frequent combination of start station and end station trip : ",most_frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
 
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

 
    total_traveltime=df['Trip Duration'].sum()
    print("Yotal travel time : ",total_traveltime)
    
    mean_traveltime=df['Trip Duration'].mean()
    print("Average travel time : ",mean_traveltime)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    
    counts_usertype=df['User Type'].value_counts()
    print('Counts of user type : \n',counts_usertype)
    if 'Gender' in  df.columns:
    
     counts_gender=df['Gender'].value_counts()
     print('counts of gender : ',counts_gender)
    if 'Birth Year' in  df.columns : 
    
     print("The earliest of users : ",df['Birth Year'].min())
     print("The most recent of users : ",df['Birth Year'].max())
     print("The most common year of birth of users : ",df['Birth Year'].mode()[0])
     print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        i=''
        a=0
       
        while i!=['yes','no'] :
             i=input("DO YOU WANT TO SEE FRIST 5 RAWS (yes/no) : \n").lower()   
             if i=='yes':
               print(df.iloc[a:a+5])
               a +=5
             elif i=="no":
                break
            
        restart = input('\nWould you like to restart? Enter yes or no (if you type any thing except yes it will be break).\n').lower()
        if restart.lower() != 'yes':       
            break


if __name__ == "__main__":
	main()
import matplotlib as mp
