
# this function is used to calculate the hotel cost
def calculate_hotel_cost(room_type, nights):
    # if the room type is standard and the standard room cost is 150 per night
    if room_type == 'standard':
        return 150 * nights
    # if the room type is deluxe and the deluxe room cost is 180 per night
    elif room_type == 'deluxe':
        return 180 * nights
    # if the room type is suite and the suite room cost is 200 per night
    elif room_type == 'suite':
        return 220 * nights
    # if  no room type is selected then the cost is 0
    else:
        return 0

# this function is used to calculate the car cost
def calculate_car_cost(days):
    # if the car is rented for 1 day then the cost is 100
    if days==1:
        return 100
    # if the car is rented for more than 1 day then the cost is 100 + 60 per day
    elif days>=2:
        return 100+(days-1)*60
    # if the car is not rented then the cost is 0
    else:
        return 0

# this function is used to calculate the theme park cost
def calculate_theme_park_cost(days):
    # if the theme park is visited for 1 day then the cost is 175
    if days==1:
        return 175
    # if the theme park is visited for more than 1 day then the cost is 175 + 50 per day
    elif days>=2:
        return 175+(days-1)*50
    # if the theme park is not visited then the cost is 0
    else:
        return 0

def calculate_total_cost(room_type, nights, rant_car, theme_park_days):
    return calculate_hotel_cost(room_type, nights) + calculate_car_cost(rant_car) + calculate_theme_park_cost(theme_park_days)


# Path: r.py
if __name__ == '__main__':
    # this is the main function
    while True:
        # taking the input from the user for the room type if the user enters the wrong input then the user is asked to enter the input again
        room_type = input('Enter room type: 1 for standard, 2 for deluxe, 3 for suite: ')
        if room_type == '1':
            room_type = 'standard'
        elif room_type == '2':
            room_type = 'deluxe'
        elif room_type == '3':
            room_type = 'suite'
        else:
            print('Invalid room type')
            continue
        # taking the input from the user for the number of nights 
        nights = int(input('Enter number of nights: '))
        break
    
    # taking the input from the user for the number of days the car is rented
    rant_car_days = int(input('Enter number of days to rent a car: '))
    # taking the input from the user for the number of days the theme park is visited
    theme_park_days = int(input('Enter number of days to visit theme park: '))

    total_cost = calculate_total_cost(room_type, nights, rant_car_days, theme_park_days)

    print(f'Total cost: ${total_cost}')
# this function is used to calculate the hotel cost
def calculate_hotel_cost(room_type, nights):
    # if the room type is standard and the standard room cost is 150 per night
    if room_type == 'standard':
        return 150 * nights
    # if the room type is deluxe and the deluxe room cost is 180 per night
    elif room_type == 'deluxe':
        return 180 * nights
    # if the room type is suite and the suite room cost is 200 per night
    elif room_type == 'suite':
        return 220 * nights
    # if  no room type is selected then the cost is 0
    else:
        return 0

# this function is used to calculate the car cost
def calculate_car_cost(days):
    # if the car is rented for 1 day then the cost is 100
    if days==1:
        return 100
    # if the car is rented for more than 1 day then the cost is 100 + 60 per day
    elif days>=2:
        return 100+(days-1)*60
    # if the car is not rented then the cost is 0
    else:
        return 0

# this function is used to calculate the theme park cost
def calculate_theme_park_cost(days):
    # if the theme park is visited for 1 day then the cost is 175
    if days==1:
        return 175
    # if the theme park is visited for more than 1 day then the cost is 175 + 50 per day
    elif days>=2:
        return 175+(days-1)*50
    # if the theme park is not visited then the cost is 0
    else:
        return 0

def calculate_total_cost(room_type, nights, rant_car, theme_park_days):
    return calculate_hotel_cost(room_type, nights) + calculate_car_cost(rant_car) + calculate_theme_park_cost(theme_park_days)


# Path: r.py
if __name__ == '__main__':
    # this is the main function
    while True:
        # taking the input from the user for the room type if the user enters the wrong input then the user is asked to enter the input again
        room_type = input('Enter room type: 1 for standard, 2 for deluxe, 3 for suite: ')
        if room_type == '1':
            room_type = 'standard'
        elif room_type == '2':
            room_type = 'deluxe'
        elif room_type == '3':
            room_type = 'suite'
        else:
            print('Invalid room type')
            continue
        # taking the input from the user for the number of nights 
        nights = int(input('Enter number of nights: '))
        break
    
    # taking the input from the user for the number of days the car is rented
    rant_car_days = int(input('Enter number of days to rent a car: '))
    # taking the input from the user for the number of days the theme park is visited
    theme_park_days = int(input('Enter number of days to visit theme park: '))

    total_cost = calculate_total_cost(room_type, nights, rant_car_days, theme_park_days)

    print(f'Total cost: ${total_cost}')