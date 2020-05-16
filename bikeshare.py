import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
SIX_MONTH = ['january', 'february', 'march', 'april', 'may', 'june']
DAY_IN_WEEK = {'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}

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
    while True:
        city = input('\nEnter city. \nChoose either Chicago, New York City or Washington?:\n').lower()
        if city not in CITY_DATA:
            print("\nInvalid answer. Please choose either Chicago, New York City or Washington\n")
            continue
        else:
            break
        return city

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ""
    day = ""

    while True:
        time = input("\nDo you want to filter as month, day, all or none?\n").lower()
        if time != 'month' and time != 'day' and time != 'all' and time != 'none':
            print("\nInvalid answer. Please choose either month, day, all or none.\n")
            continue
        elif time == 'month':
            while True:
                month = input("\nWhich month? January, February, March, April, May or June.\n").lower()
                if month not in SIX_MONTH:
                    print("\nInvalid answer. Please choose either January, February, March, April, May or June.\n")
                    continue
                else:
                    break
            break
        elif time == 'day':
            while True:
                day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n").lower()
                if day not in DAY_IN_WEEK:
                    print("\nInvalid answer. Please choose either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n")
                    continue
                else:
                    break
            break
        elif time == 'all':
            while True:
                month = input("\nWhich month? January, February, March, April, May or June.\n").lower()
                if month not in SIX_MONTH:
                    print("\nInvalid answer. Please choose either January, February, March, April, May or June.\n")
                    continue
                else:
                    break
            while True:
                day = input("\nWhich day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n").lower()
                if day not in DAY_IN_WEEK:
                    print("\nInvalid answer. Please choose either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or Sunday.\n")
                    continue
                else:
                    break
            break
        elif time == 'none':
            break
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
    # loads data file into dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracts month, day of week and hour from Start Time to create new column
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    while True:
        if month == '' and day == '':
            break
        elif day == '' and month != 'all':
            # uses the index of the months list to get corresponding int
            month = SIX_MONTH.index(month)+1

            # filter by month to create the new dataframe
            df = df[df['month'] == month]
            break
        elif month == '' and day != 'all':
            # filter by day of week to create the new dataframe
            df = df[df['day'] == day.title()]
            break
        else:
            break
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month          :', common_month)

    # TO DO: display the most common day of week
    common_day_of_week = df['day'].mode()[0]
    print('Most Common Day of the Week:', common_day_of_week)

    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour     :', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is:', common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is  :', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end_station_combo = df.groupby(['Start Station','End Station']).size().sort_values(ascending=False).nlargest(1)
    print('{} are the most commonly used start and end stations.\n'.format(start_end_station_combo))

    print('\nThis took %s seconds.' % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is:', total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time is :', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The number of users by type is:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nThe count by Gender is:\n', gender)
    else:
        print('Gender info is not available in this data')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        mode_year = df['Birth Year'].mode()[0]
        print('\nThe earliest birth year is {}, the most recent birth year is {}, and the most common birth year is {}.\n'.format(min_year, max_year, mode_year))

    else:
        print('Birth Year info is not availbale in this data.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    """Prompt user if they would like to see lines of raw data"""

    raw_data = 0
    while True:
        answer = input("\nDo you want to see 5 lines of raw data? Yes or No.\n").lower()
        if answer not in ['yes','no']:
            print("\nInvalid input. Please enter Yes or No.\n")
            continue
        if answer == 'yes':
            while True:
                raw_data += 5
                print(df.iloc[raw_data : raw_data +5])
                display_more = input("Do you want to see 5 more lines of data? Yes or No.\n").lower()
                if display_more == 'no':
                    answer = "no"
                    break
        if answer == 'no':
            break
    return



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
