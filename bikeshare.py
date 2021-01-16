import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

# # adding line for github modification

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.


    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cities = ['chicago', 'new york city', 'washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nPlease enter the city name: \n')
        city = city.lower()
        if city in cities:
            break
        else:
            print("Please enter 3 of these cities  new york city - chicago - washington")

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nPlease enter the month name: \n')
        if month in months:
            break
        else:
            print("It's not right month")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nPlease enter the day name: \n')
        if days:
            break
        else:
            print("It's not right day")
    print('-' * 40)
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
    df['start'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['start'].dt.month
    df['day'] = df['start'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_month = df['month'].mode()[0]
    print('Most Popular Month:', most_month)

    # TO DO: display the most common day of week
    most_day_of_week = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', most_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start_station = df['Start Station'].mode()[0]
    print('most commonly used start station:', most_start_station)
    # TO DO: display most commonly used end station
    most_end_station = df['End Station'].mode()[0]
    print('most commonly used end  station:', most_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    df['Start_Stop'] = df['Start Station'] + " - " + df['End Station']
    most__station = df['Start_Stop'].mode()[0]
    print('most frequent station trip:', most_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_dur = df['Trip Duration'].sum()
    print('total travel time is :', total_dur)

    # TO DO: display mean travel time
    avg_dur = df['Trip Duration'].mean()
    print('Avg travel time is :', avg_dur)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users = df['User Type'].nunique()
    print('Number of user types are : ', users)

    # TO DO: Display counts of gender
    try:
        genders = df['Gender'].nunique()
        print('Number of gender types are : ', genders)
    except KeyError:
        print("Error")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        d_min = df['Birth Year'].min()
        d_max = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]
        print('Earliest Year of Birth is : ', d_min)
        print('Most Year of Birth is : ', d_max)
        print('Most Common Year of Birth is : ', common_year)
    except KeyError:
        print("Error")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
