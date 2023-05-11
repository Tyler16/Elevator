def simulate(num_floors, start_floor, floor_map, total_passengers, start_up=True):
    elevator_passengers = {}                            # Passengers in elevator
    up = start_up                                       # Initial elevator direction
    current_floor = start_floor                         # Current floor of elevator
    highest_pickup_floor = max(floor_map.keys())        # Highest floor a passenger is on
    lowest_pickup_floor = min(floor_map.keys())         # Lowest floor a passenger is on
    highest_dropoff_floor = 0                           # Highest floor a passenger will be dropped off at
    lowest_dropoff_floor = start_floor + 1              # Lowest floor a passenger will be dropped off at
    time = 0                                            # Start time of simulation
    total_time = 0                                      # Sum of times spent in elevator by each person
    passengers_left = total_passengers                  # Number of passengers remaining
    while passengers_left > 0:
        print(f"\nCurrent floor: {current_floor}")
        print(f"Current time: {time}")
        # Drop off any passengers on floor
        if current_floor in elevator_passengers:
            while elevator_passengers[current_floor]:
                print(f"Dropping off passenger {elevator_passengers[current_floor].pop()}")
                total_time += time
                passengers_left -= 1

        # Pick up any passengers from floor that are going in same direction as elevator
        i = 0
        if current_floor in floor_map:
            num_passengers = len(floor_map[current_floor])
            while i < num_passengers:
                if (up and floor_map[current_floor][i][1] > current_floor) or \
                    (not up and floor_map[current_floor][i][1] < current_floor):
                    passenger, dest = floor_map[current_floor].pop(i)
                    print(f"Loading passenger {passenger}")
                    if dest > highest_dropoff_floor:
                        highest_dropoff_floor = dest
                    if dest < lowest_dropoff_floor:
                        lowest_dropoff_floor = dest
                    if dest in elevator_passengers:
                        elevator_passengers[dest].append(passenger)
                    else:
                        elevator_passengers[dest] = [passenger]
                else:
                    i += 1
                num_passengers = len(floor_map[current_floor])
            if len(floor_map[current_floor]) == 0:
                floor_map.pop(current_floor)
        
        # Change elevator direction if needed, and pick up all passengers if direction is changed
        if (up and (current_floor == num_floors or (current_floor >= highest_pickup_floor and current_floor >= highest_dropoff_floor))) or \
            (not up and (current_floor == 1 or (current_floor <= lowest_pickup_floor and current_floor <= lowest_dropoff_floor))):
            up = not up
            if current_floor in floor_map:
                for i in range(len(floor_map[current_floor])):
                    passenger, dest = floor_map[current_floor].pop(0)
                    print(f"Loading passenger {passenger}")
                    if dest > highest_dropoff_floor:
                        highest_dropoff_floor = dest
                    if dest < lowest_dropoff_floor:
                        lowest_dropoff_floor = dest
                    if dest in elevator_passengers:
                        elevator_passengers[dest].append(passenger)
                    else:
                        elevator_passengers[dest] = [passenger]
                floor_map.pop(current_floor)
            highest_pickup_floor = max(floor_map.keys())
            lowest_pickup_floor = min(floor_map.keys())
            

        # Move elevator and increase time
        if up:
            current_floor += 1
        else:
            current_floor -= 1
        time += 1
    print("\nSimulation complete")
    print(f"Time spent: {time}")
    print(f"Average time spent per passenger: {total_time / total_passengers}")
        

while True:
    print("\nWelcome to the Python Elevator Simulator")
    print("Choose an option:")
    print("1. Simulate elevator")
    print("2. Quit")
    option = int(input("> "))

    if option == 1:
        print("Enter number of floors:")
        floor_num = int(input("> "))
        while floor_num < 2:
            print("ERROR: Building must have at least 2 floors")
            print("Enter number of floors:")
            floor_num = int(input("> "))
        
        print("What floor should the elevator start on?")
        start_floor = int(input("> "))
        while start_floor < 1 or start_floor > floor_num:
            print("ERROR: Starting floor is out of range")
            print("What floor should the elevator start on?")
            start_floor = int(input("> "))
        
        print("Enter number of passengers:")
        passenger_count = int(input("> "))
        while passenger_count < 1:
            print("ERROR: At least 1 passenger is required")
            print("Enter number of passengers:")
            passenger_count = int(input("> "))
        
        floor_map = {}
        print("For each passenger, input starting and ending floor with a single comma separating them")
        for i in range(1, passenger_count + 1):
            print(f"Passenger {i}:")
            current_passenger = [int(j) for j in input("> ").split(',')]
            format_error = False
            if len(current_passenger) != 2 or current_passenger[0] == current_passenger[1] or current_passenger[0] < 1 or current_passenger[0] > floor_num or current_passenger[1] < 1 or current_passenger[1] > floor_num:
                format_error = True
            while format_error:
                if len(current_passenger) != 2:
                    print("ERROR: Input not in correct format")
                elif current_passenger[0] == current_passenger[1]:
                    print("ERROR: Start and end floor must be different")
                else:
                    print("ERROR: Start or end floor outside of floor range")
                print(f"Passenger {i}:")
                current_passenger = [int(j) for j in input("> ").split(',')]
                format_error = False
                if len(current_passenger) != 2 or current_passenger[0] < 1 or current_passenger[0] > floor_num or current_passenger[1] < 1 or current_passenger[1] > floor_num:
                    format_error = True
            if current_passenger[0] in floor_map:
                floor_map[current_passenger[0]].append((i, current_passenger[1]))
            else:
                floor_map[current_passenger[0]] = [(i, current_passenger[1])]
        
        print("Should the elevator start by going up or down?(U for up D for down)")
        start_dir = input("> ")
        while start_dir != "U" and start_dir != "D":
            print('ERROR: Input must be "up" or "down"')
            print("Should the elevator start by going up or down?")
            start_dir = input("> ")
        
        if start_dir == "U":
            simulate(floor_num, start_floor, floor_map, passenger_count)
        else:
            simulate(floor_num, start_floor, floor_map, passenger_count, False)

    elif option == 2:
        break
    else:
        print("Invalid option")