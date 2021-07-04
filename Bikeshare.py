import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    print("Hello! Let\'s explore some US bikeshare data!")
    
    us_city = input("choose from three cities: chicago, new york, washington?")
    while us_city not in CITY_DATA.keys():
        print("you put invalid item")
        us_city = input("choose from three cities: chicago, new york, washington?").lower()
    
    us_filter = input("choose filtering data: month - day - together - none?").lower()
    months_6 = ['january', 'february', 'march', 'april','may', 'june']
    while us_filter not in ['month', 'day', 'together', 'none']:
        print("you put invalid item")
        us_filter = input("choose filtering data: month - day - together - none?").lower()
    
    if us_filter == 'month' or us_filter == 'both':
        month_6 = input('choose month: january, february, march, april, may, june?').lower()
        while month_6 not in months_6:
            print('you put invalid item')
            month_6 = input('choose month: january, february, march, april, may, june?').lower()
        
    else:
        month_6 = 'first six months'
    
    us_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    if us_filter == 'day' or us_filter == 'together':
        day_7 = input("choose day: monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        while day_7 not in us_days:
            print("you put invalid item")
            day_7 = input("choose day: monday, tuesday, wednesday, thursday, friday, saturday, sunday")
        
    else:
        day_7 = "all days"
    
    print('-'*40)
    return us_city, month_6, day_7
        
def load_data( us_city, month_6, day_7 ):
    
    df= pd.read_csv(CITY_DATA[us_city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month_6'] = df['Start Time'].dt.month
    df['day_of_week_7'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    
    if month_6 != 'first six months':
       months_6 = ['january', 'february', 'march', 'april', 'may', 'june']
       month_6 = months_6.index(month_6) +1 
        
       df = df[df['month_6'] == month_6]
        
    if day_7 != "all days":
       df = df[df['day_of_week_7'] == day_7.title()]
        
    return df

def time_stats(df):
    print("\nCalculating the most frequent times of travel...\n")
    start_time = time.time()
    
    most_month = df['month_6'].mode()[0]
    print(" most month : ", most_month)
    
    most_day_of_week = df['day_of_week_7'].mode()[0]
    print("most day :", most_day_of_week)
    
    most_common_start_time = df['hour'].mode()[0]
    print("Most Start Time: ", most_common_start_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def station_stats(df):
    print("\nCalculating the most popular station and trip....\n")
    start_time = time.time()
    
    most_common_start_station= df['Start Station'].mode()[0]
    print("most common start station:", most_common_start_station)
    
    most_common_end_station = df['End Station'].mode()[0]
    print("most common end station:",  most_common_end_station)
    
    start_end_grouped = df.groupby(['Start Station','End Station'])
    most_trip = start_end_grouped.size().sort_values(ascending= False).head(1)
    print("most frequent combination of start station trip:\n", most_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
def trip_duration_stats(df):
    print("\nCalculating trip duration...\n")
    start_time = time.time()
    
    total_trip_time = df['Trip Duration'].sum()
    print("Total trip time:", total_trip_time)
    
    mean_trip_time = df['Trip Duration'].mean()
    print("Mean trip time:", mean_trip_time)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def user_stats(df, us_city):
    print("\nCalculating user stats...\n")
    start_time = time.time()
    
    print("conts user\n",df['User Type'].value_counts())
    
    if us_city != 'washington':
        
        print("gender stats:\n",df['Gender'].value_counts)
        
        print("most birth year\n", df['Birth Year'].mode()[0])
        
        print("most recent birth year\n", df['Birth Year'].max())
        
        print("earliest birth year\n", df['Birth Year'].min())
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    show_raw = input('\nDo you want to show some raws?\n')
    if show_raw.lower() == 'yes':
        count =0
        while True:
            print(df.iloc[count: count+5])
            count+=5
            next_raws = input('show more?')
            if next_raws.lower() != 'yes':
                break
    

def main():
    while True:
        us_city, month_6, day_7 = get_filters()
        df = load_data(us_city, month_6, day_7) 
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, us_city)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            
if __name__ == "__main__":
        main()