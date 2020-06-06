import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'C:\\Users\\ps063n\\Desktop\\AT&T\\ND - Programming for Data Science\\Python\\bikeshare-2\\chicago.csv',
              'New York': 'C:\\Users\\ps063n\\Desktop\\AT&T\\ND - Programming for Data Science\\Python\\bikeshare-2\\new_york_city.csv',
              'Washington': 'C:\\Users\\ps063n\\Desktop\\AT&T\\ND - Programming for Data Science\\Python\\bikeshare-2\\washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    print('\nWhich city you want to explore: Chicago, New York, or  Washington? Enter only one')
    
    city = ''
    
    while city not in ('Chicago', 'New York', 'Washington'):
        
        city_name = input().title()
        
        print('\nCity Selected: {}'.format(city_name))
        
        if city_name not in ('Chicago', 'New York', 'Washington'):
            print('\nWrong Selection! Please enter only 1 value from these 3 options: Chicago, New York, or  Washington')
            continue
        else:
            city = city_name

    # TO DO: get user input for month (all, january, february, ... , june)

    print('\nEnter a month to explore: all, january, february, march, april, may, or june? Enter only one')
    
    month = ''
    
    while month not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
        
        month_name = input().title() 
        
        print('\nMonth Selected: {}'.format(month_name))
        
        if month_name not in ('All', 'January', 'February', 'March', 'April', 'May', 'June'):
            print('\nWrong Selection! Please enter only 1 value from these 7 options: all, january, february, march, april, may, or june')
            continue
        else:
            month = month_name

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('\Enter a day of week to explore: all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday? Enter only one')

    day = ''
    
    while day not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
        
        day_name = input().title() 
        
        print('\nDay Selected: {}'.format(day_name))
        
        if day_name not in ('All', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            print('\nWrong Selection! Please enter only 1 value from these 8 options: all, monday, tuesday, wednesday, thursday, friday, saturday, or sunday')
            continue
        else:
            day = day_name

    print('-'*40)
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
    print('\nPlease wait, the data is loading ...\n')
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'All':
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+1
        df = df[df['month']==month]
    
    if day != 'All':
        df = df[df['day_of_week']==day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('\nThe most common month is {}'.format(df['Start Time'].dt.month.mode()[0]))

    # TO DO: display the most common day of week
    print('\nThe most common day of week is {}'.format(df['Start Time'].dt.weekday_name.mode()[0]))

    # TO DO: display the most common start hour
    print('\nThe most common start hour is {}'.format(df['Start Time'].dt.hour.mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station is:\n {}'.format(pd.DataFrame(df['Start Station'].value_counts()).reset_index()['index'][0]))

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is:\n {}'.format(pd.DataFrame(df['End Station'].value_counts()).reset_index()['index'][0]))

    # TO DO: display most frequent combination of start station and end station trip
    start = df.groupby(['Start Station','End Station']).size().nlargest(1).reset_index()[['Start Station','End Station']].iloc[0][0]
    end = df.groupby(['Start Station','End Station']).size().nlargest(1).reset_index()[['Start Station','End Station']].iloc[0][1]
    
    print('\nThe most frequent combination of start station and end station trip is:\n{}\nTO\n{}'.format(start,end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time: {}'.format(df['Trip Duration'].sum()))

    # TO DO: display mean travel time
    print('\nAverage travel time: {}'.format(df['Trip Duration'].mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    print('\nThere are total {} user types.'.format(df['User Type'].value_counts().count()))

    if 'Gender' in list(df.columns):
        # TO DO: Display counts of gender
        print('\nThere are total {} genders.'.format(df['Gender'].value_counts().count()))
    
    else:
        print('\nGender data not available for this city.')
    
    if 'Birth Year' in list(df.columns):
        # TO DO: Display earliest, most recent, and most common year of birth
        print('\nEarliest birth year: {}'.format(df['Birth Year'].min()))
        print('\nMost Recent birth year: {}'.format(df['Birth Year'].max()))
        print('\nMost Common birth year: {}'.format(df['Birth Year'].mode()[0]))
    
    else:
        print('\nBirth Year data not available for this city.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? Enter Yes or No.').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? Enter Yes or No.').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
