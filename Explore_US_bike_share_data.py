import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city would you like to analyze?\n(New York City, Chicago or Washington)\n').title()
        if city not in CITY_DATA.keys() :     
            print('\nInvalid input!') 
            continue
        else:
            break          

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while True:
        month = input('\nPlease select a month from the list [all, january, february, march, april, may, june]\n').lower()
        if month not in months :
             print('\nInvalid input!')
             continue
        else:
             break
    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all', 'monday','tuesday','wednessday','thursday','friday','saturday','sunday']
    while True :
        day = input('\nPlease enter a day from the list[all, monday, tuesday, wednessday, thursday, friday, saturday, sunday]\n').lower()
        if day not in days:
            print('\nInvalid input!')
            continue
        else:
            break
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()  
    
    # filter by month if applicable
    if month != 'all' :
    # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nThe most common month : ',df['month'].mode()[0])

    # display the most common day of week
    print('\nThe most common day : ',df['day_of_week'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('\nThe most common Start hour : ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most common used start station : ',df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nThe most common used end station : ',df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    most_fequent_combination = df['Start Station'] + df['End Station']
    print('\nThe most frequent combination of start station and end station trip :',most_fequent_combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time : ',df['Trip Duration'].sum())

    # display mean travel time
    print('\nMean travel time (avg) : ',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Count of user types :',df['User Type'].value_counts())

    # Display counts of gender
    try :
        print('\nGender Types: ',df['Gender'].value_counts())
    except KeyError :
        print('\nNo data available')
    
    # Display earliest, most recent, and most common year of birth
    try :
        print('\nThe earlies year of birth :',df['Birth Year'].min())
        print('The most recent year of birth :',df['Birth Year'].max())
        print('The most common year of birth :',df['Birth year'].mode()[0])
    except KeyError :
        print('No data available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_row(df) :
    #will ask the customer if he\she would like to display the first 5 row of data
    Client_input = input('\nWould you like to preview first five row of data ?(yes \ no)').lower()
    if Client_input == 'yes' :
        row = 0
        while True :
            print(df.iloc[row:row+5])
            row+=5  
            display_more = input('\nWould you like to display more five data ?(yes \ no)')
            if display_more != 'yes' :
                break
          
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_row(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()