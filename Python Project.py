# Successfully completed all of Part 1 - Luke

def main():
    print('Project 3 by Luke Buckner')
    analyze_temp_data()


def check_highest_temp(data):
    """ Finds the highest temperature """

    highest = -273
    highest_date = ""
    for day in data:
        day_data = day.split(',')
        if int(day_data[1]) > highest:
            highest = int(day_data[1])
            highest_date = day_data[0]
        
    print('The highest temperature of the year was ' + str(highest) + ', and it occured on ' + highest_date)
    

def check_lowest_temp(data):
    """ Finds the lowest temperature """

    lowest = 273
    lowest_date = ""
    for day in data:
        day_data = day.split(',')
        if int(day_data[2]) < lowest:
            lowest = int(day_data[2])
            lowest_date = day_data[0]
        
    print('The lowest temperature of the year was ' + str(lowest) + ', and it occured on ' + lowest_date)
    

def check_lowest_high_temp(data):
    """ Finds the lowest high temperature """

    lowest_high = 273
    lowest_high_date = ""
    for day in data:
        day_data = day.split(',')
        if int(day_data[1]) < lowest_high:
            lowest_high = int(day_data[1])
            lowest_high_date = day_data[0]
        
    print('The lowest high temperature of the year was ' + str(lowest_high) + ', and it occured on ' + lowest_high_date)
    

def check_highest_low_temp(data):
    """ Finds the highest low temperature """

    highest_low = -273
    highest_low_date = ""
    for day in data:
        day_data = day.split(',')
        if int(day_data[2]) > highest_low:
            highest_low = int(day_data[2])
            highest_low_date = day_data[0]
        
    print('The highest low temperature of the year was ' + str(highest_low) + ', and it occured on ' + highest_low_date)
    

def check_average_high_temp(data):
    """ Finds the average high temperature """

    high_temp_sum = 0
    for day in data:
        day_data = day.split(',')
        high_temp_sum = high_temp_sum + int(day_data[1])
    
    average_high_temp = high_temp_sum / len(data)
    print('The average high temperature of the year 2017 was ' + str(average_high_temp))
    

def check_average_low_temp(data):
    """ Finds the average low temperature """

    low_temp_sum = 0
    for day in data:
        day_data = day.split(',')
        low_temp_sum = low_temp_sum + int(day_data[2])
    
    average_low_temp = low_temp_sum / len(data)
    print('The average low temperature of the year 2017 was '+ str(average_low_temp))
    


def check_low_temp_below_threshold(data):
    """ Finds the number of days in a year where the temp was lower than the entered threshold """

    print('Enter a threshold value to check the number of days where the temperature was lower than the entered threshold: ')
    threshold = float(input())
    day_count = 0
    for day in data:
        day_data = day.split(',')
        if int(day_data[2]) < threshold:
            day_count = day_count + 1
    print('There were ' + str(day_count) + ' days when the temperature was lower than the threshold')
    

def check_high_temp_below_threshold(data):
    """ Finds the number of days in a year where the temp was higher than the entered threshold """
    
    print('Enter a threshold value to check the number of days where the temperature was higher than the entered threshold: ')
    threshold = float(input())
    day_count = 0
    for day in data:
        day_data = day.split(',')
        if int(day_data[1]) > threshold:
            day_count = day_count + 1
    print('There were ' + str(day_count) + ' days when the temperature was higher than the threshold')


def analyze_temp_data():
    """ Opens and analyzes the AtlantaTemps2017.csv and reads it to return information about its data"""
    
    temp_file = 'AtlantaTemps2017.csv'

    temp_file = open(temp_file,'r')

    data = temp_file.readlines()
    
    check_highest_temp(data)
    check_lowest_temp(data)
    check_lowest_high_temp(data)
    check_highest_low_temp(data)
    check_average_high_temp(data)
    check_average_low_temp(data)
    check_low_temp_below_threshold(data)
    check_high_temp_below_threshold(data)

    temp_file.close()


main()
