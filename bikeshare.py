import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



MONTHS_TO_INDEX = {'JAN': '1',
          "FEB": "2",
          'MAR': '3',
          'APR': '4',
          'MAY': '5',
          'JUN': '6',
          'JUL': '7',
          'AUG': '8',
          'SEP': '9',
          'OCT': '10',
          'NOV': '11',
          'DEC': '12',
          'ALL': 'ALL'}

INDEX_TO_MONTH = {1: 'January',
                  2: 'February',
                  3: 'March',
                  4: 'April',
                  5: 'May',
                  6: 'June',
                  7: 'July',
                  8: 'August',
                  9: 'September',
                  10: 'October',
                  11: 'November',
                  12: 'December'}

DAY_T0_INDEX = {'MON': 0,
       'TUE': 1,
       'WED': 2,
       'THU': 3,
       'FRI': 4,
       'SAT': 5,
       'SUN': 6,
       'ALL': "ALL"}

INDEX_TO_DAY = {0: 'Monday',
                1: 'Tuesday',
                2: 'Wednesday',
                3: 'Thursday',
                4: 'Friday',
                5: 'Saturday',
                6: 'Sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
	
	"""  Suggestion apporté dans le code  """  
	
	
	"""while True:
        city = input("Select a city from {}, {} or {}:".format(*CITY_DATA.keys())).strip().lower()
        if city in CITY_DATA.keys():
            break"""
	"""  FIN """
		
    print('Hello! Let\'s explore some US bikeshare data for chicago new_york_city washington!')
    city_found, month_found, day_found = False, False, False
	
    while True:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if not city_found:
            city = input("We have 3 cities available to explore : Chicago, Washington, New York City. Please choose "
                         "one : ")
            city = city.lower()
            if city not in CITY_DATA:
                print("Invalid city or data not available, please choose one of the 3 : Chicago, Washington, "
                      "New York City")
                continue
            else:
                city_found = True
        print('\n')

    # TO DO: get user input for month (all, january, february, ... , june)
        if not month_found:
            month = input("Enter month you want to explore. Choose one of : "
                          "JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, ALL. ALL denotes data for all months : ")
            month = month.upper()
            if month not in MONTHS_TO_INDEX:
                print("Invalid month entered!!! Enter a valid month!!!!")
                continue
            else:
                month_found = True

        print('\n')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Enter day you want to explore. Choose one of : MON, TUE, WED, THU, FRI, SAT, SUN, ALL. ALL denotes data for all days :")
        day = day.upper()
        if day not in DAY_T0_INDEX:
            print("Invalid day entered!!! Enter a valid day!!!!")
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
    start_time = time.time()
    df = pd.read_csv(CITY_DATA.get(city))
    
    # extract start month from the Start time column to create Start Month column
    df['Start Month'] = pd.DatetimeIndex(df['Start Time']).month

    # extract start day from the Start time column to create Start Day column
    df['Start Day'] = pd.to_datetime(df['Start Time'], format='%Y-%m-%d %H:%M:%S').dt.dayofweek

    # extract start hour from the Start Time column to create an Start Hour column
    df['Start Hour'] = pd.DatetimeIndex(df['Start Time']).hour

    # filter on month, if month is specified
    if month != MONTHS_TO_INDEX.get('ALL'):
        df = df[df['Start Month'] == int(MONTHS_TO_INDEX.get(month))]

    # filter on day, if day is specified
    if day != DAY_T0_INDEX.get('ALL'):
        df = df[df['Start Day'] == int(DAY_T0_INDEX.get(day))]

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    if month == MONTHS_TO_INDEX.get('ALL'):
        popular_month = df['Start Month'].dropna()
        if popular_month.empty:
            print("No popular month found for the filter specified!! Please adjust your filter!!")
        else:
            popular_month = popular_month.mode()[0]
            print('Most popular month for renting is : {}'.format(INDEX_TO_MONTH.get(popular_month)))
    else:
        print('As you have chosen month : {} as filter, most popular month for renting won\'t be calculated'.format(month))


    # TO DO: display the most common day of week
    if day == DAY_T0_INDEX.get('ALL'):
        popular_day = df['Start Day'].dropna()  #.mode()[0]
        if popular_day.empty:
            print('No popular day found for the filters specified!! Please adjust your filter!!!')
        else:
            popular_day = popular_day.mode()[0]
            print('Most popular day for renting is : {}'.format(INDEX_TO_DAY.get(popular_day)))
    else:
        print('As you have chosen "{}day" as filter, most popular day for renting won\'t be calculated'.format(day.title()))


    # TO DO: display the most common start hour
    popular_start_hour = df['Start Hour'].dropna()
    if popular_start_hour.empty:
        print('No popular start hour found for the filter specified!! Please adjust your filter !!!')
    else:
        popular_start_hour = popular_start_hour.mode()[0]
        print('Most popular renting start hour is : {}:00 hrs'.format(popular_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    
    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', Start_Station)


    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print('\nMost Commonly used end station:', End_Station)


    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print('\nMost Commonly used combination of start station and end station trip:', Start_Station, " & ", End_Station)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    valid_time = df['Trip Duration'].dropna()
    if valid_time.empty:
        print('No record found!! Please adjust your filter')
    else:
        total_time = valid_time.sum()
        print('Total travel time in seconds is : {}'.format(total_time))


    # TO DO: display mean travel time
    mean_travel_time = valid_time.mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].dropna()

    if user_type.empty:
        print('No data available for specified filter, please adjust your filter!!')
    else:
        user_type = user_type.value_counts()
        print('User type details for the filter specified : {}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df:
            user_gender = df['Gender'].dropna()
            if user_gender.empty:
                print('No data available for specified filter, please adjust your filter!!')
            else:
                user_gender = user_gender.value_counts()
                print('User gender count : {}'.format(user_gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_years = df['Birth Year'].dropna()
        if birth_years.empty:
            print('No data available for specified filter, please adjust your filter!!')
        else:
            user_birth_year = df['Birth Year'].dropna()
            if user_birth_year.empty:
                print('No data available for your filter, please adjust your filter!!!')
            else:
                oldest_user = user_birth_year.min()
                print('Earliest year of birth for the selected filter : {}'.format(int(oldest_user)))

                youngest_user = user_birth_year.max()
                print('Most recent year of birth for the selected filter : {}'.format(int(youngest_user)))

                most_common_year_of_birth = user_birth_year.mode()[0]
                print('Most common year of birth for the selected filter : {}'.format(int(most_common_year_of_birth)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    choice = input("Would you like to see raw data or no?[Y/n] : ")
    choice = choice.upper()

    count = 0
    if choice == 'Y':
        for row in df.iterrows():
            print(row)
            count += 1
            if count != 0 and count % 5 == 0:
                choice = input("Would you like to see raw data? [Y/n] : ")
                if choice.upper() != 'Y':
                    break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()