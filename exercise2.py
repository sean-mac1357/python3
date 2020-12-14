hotel = {
    '1': {
        '101': ['Mando', 'Grogu', 'Cara', 'Greef', 'Kuiil'],
        '102': [],
        '103': [],
        '104': [],
        '105': [],
    },
    '2': {
        '201': [],
        '202': [],
        '203': ['Neo', 'Trinity', 'Morpheus'],
        '204': [],
        '205': [],
    },
    '3': {
        '301': [],
        '302': [],
        '303': [],
        '304': [],
        '305': ['John', 'Winston', 'Charon'],
    }
}

names = []
floor = []
room = []
checked_out = ["Checked Out"]

i = 0



def help_desk():
    print("Hello, how may I help you? ")
    print("A. Checking-in")
    print("B. Checking-out")
    print("C. Exit\n")

    user_input = input("Input here: ")

    inputCheck = False
    while inputCheck == False:
        if user_input.lower() == 'a':
            check_in()
            inputCheck = True
        elif user_input.lower() == 'b': 
            checkout()
            inputCheck = True
        elif user_input.lower() == 'c':
            quit()
        else:
            print("Sorry wrong value! Please try again. ")
            user_input = input("Input here: ")
            inputCheck = False

def check_in():

    global i
    print(" Checking In")
    
    user_name = input("Alrighty then who will the reservation be under? ")
    guest_amt = int(input("And how many guests will be accompanying you today? "))
    # names.append(user_name)

    hm_gstsCheck = False
    while hm_gstsCheck == False:
        if guest_amt <= 5:
            print("And what are the names of the guests that will be staying with you? \n If no more guests just type N/A")
            guest1 = input("Guest1: ")
            # names.append(guest1)
            guest2 = input("Guest2: ")
            # names.append(guest2)
            guest3 = input("Guest3: ")
            # names.append(guest3)
            guest4 = input("Guest4: ")
            # names.append(guest4)
            guest5 = input("Guest5: ")
            # names.append(guest5)
                # if guest1 != "" and guest2 != "" and guest3 != "" and guest4 != "" and guest5 != "":

            hm_gstsCheck = True
        elif guest_amt >= 5:
            print("Sorry but our hotel only allows 6 people per room. \n Please make separate reservations.")
            check_in()
            hm_gstsCheck = True
        else:
            print("Please enter a numerical value. ")
            guest_amt = int(input("And how many guests will be accompanying you today? "))
            hm_gstsCheck = True
    # 

    floor_wanted = str(input("What floor would you like to be on? "))
    floor = hotel.get(floor_wanted)
        
    if floor:
        print(f'{floor_wanted} is {floor}')
        hm_gstsCheck = True
    else:
        print(f'{floor_wanted} is not a floor')
        hm_gstsCheck = True
    #
    room_wanted = str(input("And what room would you like? "))
    room = hotel[floor_wanted].get(room_wanted)
    names = (user_name.capitalize() + ', ' + guest1.capitalize() + ', ' + guest2.capitalize() + ', ' + guest3.capitalize() + ', ' + guest4.capitalize() + ', ' + guest5.capitalize())

    if room:
        print(f'Sorry {room_wanted} is already taken')
        print("Choose another room.")
        room_wanted = str(input("And what room would you like? "))
        print(f'You Will now be assigned to {room_wanted}')
        hotel[floor_wanted][room_wanted] = names
        hm_gstsCheck = True
    else:
        print(f'You will now be assigned to {room_wanted}')
        hotel[floor_wanted][room_wanted] = names
        hm_gstsCheck = True
    print(hotel)


def checkout():
    co_floor = str(input("What floor were you on? "))
    floor_co = hotel.get(co_floor)
    if floor_co:
        print(f'{co_floor} is {floor_co}')
    else:
        print(f'{co_floor} is not a floor')

    co_room = str(input("What room would you like to check out of? "))
    room_co = hotel.get(co_room)
    
    if not room_co:
        ch_o_input = input("Are you %s: " % hotel[co_floor][co_room][0]) 
        if ch_o_input.lower() == 'yes':
            hotel[co_floor][co_room] = checked_out
            print(hotel)
        else:
            print("what do you mean")
    else:
        print("That room doesn't exist")
        hotel[co_room]
    
        
    


help_desk()
