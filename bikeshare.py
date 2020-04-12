import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city_list=['chicago','new york city','washington']
    months_list=['january','february' ,'march','april','may','june','all']
    day_list=['monday','tuesday','wednesday','thursday','friday','saturday','sunday','all']
    print('Do you have a preferred city to look at between Chicago, New York City and Washington ?')
    city=input('Enter the city name ').lower()
    while city not in city_list :
        city=input('Please try again, there might be a mispelling error ').lower()

    # get user input for month (all, january, february, ... , june)

    month=input('Please enter a month between January and June or all if you want to look at all the months available ').lower()
    while month not in months_list:
        month=input('please try again, there might be a mispelling error ').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('please enter a day of the week or all if you want to look at a whole week ').lower()
    while day not in day_list:
        day=input('please try again, there might be a spelling error ').title()
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
    df = pd.read_csv(CITY_DATA[city])

    #Convert start time to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    #Extract month day and hour and create new columnes

    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour']=df['Start Time'].dt.hour

    months = ['january', 'february', 'march', 'april', 'may', 'june']

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month=df['month'].value_counts().idxmax()
    print('The most common month is ',common_month )

    # TO DO: display the most common day of week
    common_day= df['day'].value_counts().idxmax()
    print('The most common day is',common_day)

    # TO DO: display the most common start hour
    common_hour=df['hour'].value_counts().idxmax()
    print('The most common hour is', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()

    print('The Most common start station is ',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()

    print('The Most common end station is ',end_station)


    # TO DO: display most frequent combination of start station and end station trip
    combo=df.groupby(['Start Station'])['End Station'].value_counts().idxmax()
    print('The Most frequent combination of start station and end station is ',combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time=df['Trip Duration'].values.astype('int')
    print('This is the time people have spent on bikeshare',travel_time.sum())

    # TO DO: display mean travel time
    print('This is the average time people have spent on bikeshare',travel_time.mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count=df['User Type'].value_counts()
    print('These are the types of users that we have and their number', user_count)


    # TO DO: Display counts of gender
    gender_count=df['Gender'].value_counts()
    print('These are the gender of the users that we have and their number ',gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    youngest=df['Birth Year'].max()
    print('The youngest customer was born in the year',youngest)

    earliest=df['Birth Year'].min()
    print('The oldest customer was born in the year',earliest)

    common_year=earliest=df['Birth Year'].mode()
    print('Most of our customer were born in the',common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):
    """Ask to the user if they want to see the raw data"""
    answers=['yes','no']
    check=input('Do you want to see 5 lines of raw data? Reply with a yes or no').lower()
    start=0
    end=4
    while check not in answers:
        check=input(' Please Reply with a yes or no').lower()
    while check == answers[0]:
        print(df.iloc[start:end])
        start+=5
        end+=5
        check=input('Do you want to see the next 5 lines of raw data? Reply with a yes or no').lower()
        while check not in answers:
            check=input(' Please Reply with a yes or no').lower()
            if check==answers[1]:
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
