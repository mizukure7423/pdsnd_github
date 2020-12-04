+import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
#dictionaryの型
DAY_DATA = ['all', 'monday', 'tuesday', 'wednesday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of thevailed_cities day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    city_name = ''
    while city_name.lower() not in CITY_DATA:
        #whileでもifでも　while　関数()　＝＝　['abc']はできない。この場合、while　関数()　in　['abc']とするのが正解。
        #なお、while　関数()　＝＝　'abc'なら可能。
        city_name = input("\nWhat is the name of the city to analyze data? (E.g. Input either chicago, new york city, washington)\n")
        if city_name.lower() in CITY_DATA:
        #We were able to get the name of the city to analyze data.
            city = CITY_DATA[city_name.lower()]
        else:
        #We were not able to get the name of the city to analyze data so we continue the loop.
            print("Sorry we were not able to get the name of the city to analyze data, Please input either chicago, new york city or washington.\n")

    # get user input for month (all, january, february, ... , june)
    month_name = ''
    while month_name.lower() not in MONTH_DATA:
        month_name = input("\nWhat is the name of the month to filter data?(E.g. Input either all, january, february, ... , june)\n")
        if month_name.lower() in MONTH_DATA:
             month = month_name.lower()
        else:
            print("Sorry we were not able to get the name of the month to filter data, Please input either 'all' to apply no month filter or january, february, ... , june.\n")

    # get user input for day of week (all, monday, tuesday,.. sunday)
    day_name = ''
    while day_name.lower() not in DAY_DATA:
        day_name = input("\nWhat is the name of the day to filter data? (E.g. Input either 'all' to apply no day filter or monday, tuesday, ... sunday)\n")
        if day_name.lower() in DAY_DATA:
            day = day_name.lower()
        else:
            print("Sorry we were not able to get the name of the day to filter data, Please input either 'all' to apply no day filter or monday, tuesday, ... sunday.\n")

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
    df = pd.read_csv(city)
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour


    # filter by month if applicable
    if month != 'all':
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
    common_month = df['month'].mode()[0]
    print("The most common month is: {}" .format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day is: " + common_day)

    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common hour is: " + str(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("The total travel time is: " + str(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("The mean travel time is: " + str(mean_time))


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is: " + popular_start_station)

    # display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is: " + popular_end_station)

    # display most frequent combination of start station and end station trip
    frequent_es_combination = (df['Start Station'] + "||" + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station trip is: "+ str(frequent_es_combination.split("||")))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    user_type = df['User Type'].value_counts()
    print("The count of user types is: \n" + str(user_type))

    if city == 'chicago.csv' or city == 'new_york_city.csv':

        # Display counts of gender
        gender = df['Gender'].value_counts()
        print("The count of gender is: \n" + str(gender))

        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        most_recent_birth = df['Birth Year'].max()
        most_common_birth = df['Birth Year'].mode()[0]
        print('Earliest birth : {}\n'.format(earliest_birth))
        print('Most recent birth : {}\n'.format(most_recent_birth))
        print('Most common birth : {}\n'.format(most_common_birth))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def data(df):
    """Asking 5 lines of the raw data and more, if they want"""
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0
    while True:
        if view_data not in ['yes', 'no']:
            view_data = input("You wrote the wrong word. Please type yes or no.").lower()
        elif view_data == 'yes':
            print(df.iloc[ start_loc: start_loc+5])
            start_loc += 5
        elif view_data == 'no':
            break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
