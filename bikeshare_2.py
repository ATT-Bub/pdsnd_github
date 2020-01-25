import time
import pandas as pd
import numpy as np
import datetime as dt
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

# --------------------------------------------------------------------------------------------------------------------------------------

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
    city = ""
    while True:
        city = input("Please enter city among chicago, new york city, washington: ").strip().lower()
        if city in ['chicago','washington','new york city']:
            break
        else:
            print("Invalid input.\n")


    # get user input for how to filter the data
    while True:
        filt = input("Would you like to filter the data by month, day, both, or not at all? Type \"none\" for no time filter\n")

        if filt.lower() == 'month':
            # get user input for month (all, january, february, ... , june)
            day = 'all'
            while True:
                month = input("Which month? January, February, March, April, May, or June?\n").lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                    break
                else:
                    print("Invalid input")
            break
        elif filt.lower() == 'day':
            # get user input for day of week (all, monday, tuesday, ... sunday)
            month = 'all'
            while True:
                day = input("Which day? Sun, Mon, Tues, Wed, Thurs, Fri, Sat?\n").lower()
                if day in ['sun', 'mon', 'tues', 'wed','thurs','fri','sat']:
                    break
                else:
                    print("Invalid input.")
            break
        elif filt.lower() == 'both':
            # get user input for both month and day of week
            while True:
                month = input("Which month? January, February, March, April, May, or June?\n").lower()
                if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                    break
                else:
                    print("Invalid input")

            while True:
                day = input("Which day? Sun, Mon, Tues, Wed, Thurs, Fri, Sat?\n").lower()
                if day in ['sun', 'mon', 'tues', 'wed','thurs','fri','sat']:
                    break
                else:
                    print("Invalid input.")
            break

        elif filt.lower() == 'none':
            # set month and day to 'all'
            month = 'all'
            day = 'all'
            break
        else:
            print("Invalid input")



    print('-'*40)
    return city, month, day

# --------------------------------------------------------------------------------------------------------------------------------------

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

    # read in city's CSV
    df = pd.read_csv(CITY_DATA[city])
    pd.to_datetime(df['Start Time'])

    df['Month'] = pd.to_datetime(df['Start Time']).dt.month
    df['Day'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    # Filter by month
    if month == 'january':
        df = df.loc[df['Month'] == 1]
    elif month == 'february':
        df = df.loc[df['Month'] == 2]
    elif month == 'march':
        df = df.loc[df['Month'] == 3]
    elif month == 'april':
        df = df.loc[df['Month'] == 4]
    elif month == 'may':
        df = df.loc[df['Month'] == 5]
    elif month == 'june':
        df = df.loc[df['Month'] == 6]


    # Filter by day
    if day == 'mon':
        df = df.loc[df['Day'] == 'Monday']
    elif day == 'tues':
        df = df.loc[df['Day'] == 'Tuesday']
    elif day == 'wed':
        df = df.loc[df['Day'] == 'Wednesday']
    elif day == 'thurs':
        df = df.loc[df['Day'] == 'Thursday']
    elif day == 'fri':
        df = df.loc[df['Day'] == 'Friday']
    elif day == 'sat':
        df = df.loc[df['Day'] == 'Saturday']
    elif day == 'sun':
        df = df.loc[df['Day'] == 'Sunday']



    #df.head()

    return df

# --------------------------------------------------------------------------------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    most_month = calendar.month_name[df['Month'].mode()[0]]
    most_month_count = max(df['Month'].value_counts())
    print("{} was the most common month with {} rides.\n".format(most_month, most_month_count))

    # display the most common day of week
    most_day = df['Day'].mode()[0]
    most_day_count = max(df['Day'].value_counts())
    print("{} was the most common day of the week with {} rides.\n".format(most_day, most_day_count))

    # display the most common start hour
    most_hour = df['Hour'].mode()[0]
    if int(most_hour) > 11:
        ampm = 'pm'
    else:
        ampm = 'am'
    most_hour = str(int(most_hour) % 12)
    most_hour_count = max(df['Hour'].value_counts())
    print("{}{} was the most common start hour with {} rides.\n".format(most_hour, ampm, most_hour_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# --------------------------------------------------------------------------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_start = df['Start Station'].mode()[0]
    most_start_count = max(df['Start Station'].value_counts())
    print("{} was the most common Start Station with {} rides.\n".format(most_start, most_start_count))

    # display most commonly used end station
    most_end = df['End Station'].mode()[0]
    most_end_count = max(df['End Station'].value_counts())
    print("{} was the most common End Station with {} rides.\n".format(most_end, most_end_count))


    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + " to " + df['End Station']
    most_combo = df['Trip'].mode()[0]
    most_combo_count = max(df['Trip'].value_counts())
    print("{} was the most common Combination with {} rides.\n".format(most_combo, most_combo_count))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# --------------------------------------------------------------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df['Travel Time'] = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # display total travel time
    total_time = df['Travel Time'].sum()
    print("Total travel time: {}\n".format(total_time))

    # display mean travel time
    mean_time = df['Travel Time'].mean()
    print("Mean travel time: {}\n".format(mean_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# --------------------------------------------------------------------------------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("User Types:\n{}\n".format(user_types))

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print("Gender:\n{}\n".format(gender))
    else:
        print ("Error. No Gender Data")
    


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        earliest = int(df['Birth Year'].min())
        print("Earliest birth year: {}\n".format(earliest))

        recent = int(df['Birth Year'].max())
        print("Most recent birth year: {}\n".format(recent))

        common = int(df['Birth Year'].mode()[0])
        print("Most common birth year: {}\n".format(common))
    else:
        print("Error. No Birth Year Data")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# --------------------------------------------------------------------------------------------------------------------------------------

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        i = 0
        raw_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').strip().lower()
        while True:
            if raw_data != 'yes':
                break
            else:
                print(df[i:i+5])
                i += 5
                raw_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n').strip().lower()


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Thank you, Udacity!!")
            break


if __name__ == "__main__":
    main()
