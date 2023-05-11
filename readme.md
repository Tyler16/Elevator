Assumptions made:
- Building must have at least 2 floors.
- Building has no maximum number of floors.
- Each floor has two buttons that call the elevator. One button can be used in order to go up floors, other will be used to go down floors. This will be denoted as an up and down call respectively.
- If both floor buttons are pressed, elevator will stop twice, once for each call.
- Elevator can go to any floor in building.
- There must be at least one elevator passenger.
- There is no maximum number of elevator passengers.
- Elevator passengers can enter and leave elevator on any floor, as long as destination and starting floor are different.
- Elevator passengers going up will always enter on up calls. Elevator passengers going down will always enter on down calls.
- Up calls are done as the elevator goes up to a floor. Down calls are done as the elevator goes down to a floor.
- Elevator should try to minimize the amount of time people spend waiting, as well as the total amount of time elevator moves. Time is simulated by number of floors passed and visited.

Unimplemented features:
- Simultaneous actions(new button presses cannot occur at same time as elevator movement).
- Passengers taking multiple elevator trips
- Multiple button presses from one passenger during one trip
