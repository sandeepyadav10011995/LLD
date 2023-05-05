"""
Elevator System:
Expectation -:
    A building -> Multiple Elevator
    Passenger -: Min Wait Time
                 Maintenance
                 Min Running Cost


    Approach -: Components
                - Button
                - Door
                - Panel
                - Elevator Car
                - Building

    Patterns -: Strategy Design Pattern
                State Design Pattern


    Requirements
        1. Multiple elevator cars and floors are in building
        2. Max Floors and max Elevators
        3. Can have states
            - Move Up
            - Move Down
            - Idle
        4. Doors of the elevator can be opened only in Idle State
        5. Floors through which elevator passes
        6. Panel should be outside and shuld have buttons (State)
        7. Panel inside Elevator Car
        8. Capacity of Elevator
        9. Multiple floors
        10. Interconnected
        11. Service
                - Downtime



    Actors :
            Primary Actors -: Pasengers
                - Press Elevevator Panel Button
                - Emerncgy Button
            Secondary Actor -: Admin/System
                - Move?Stop Elevator
                - Algorithm -: Dispatcher Algorithm
                - Display outside/inside
                - Open/Close Door

            Algorithm -: Dispatcher Algorithm



    enum ElevatorState
        - IDLE
        - UP
        - DOWN

    enum Direction
        - UP
        -DOWN

    enum DoorState
        - OPEN
        - CLOSE

    Button(ABC)
        - status
        + pressDown()
        @abstractMethod
        + isPressed()

    ElevatorButton(Button)
        - destinatorFloor
        + isPressed()

    HallButton(Button)
        - buttonSign
        + isPressed()


    ElevatorSystem -: Singleton
        + monitoring()
        + dispatcher()

    Request
        - target
        - requestType
        - origin
        - direction


    class Elevator:
        - direction
        - currentFloor
        - upStops: []
        - downStops: []

        def sendUpRequest(upRequest: Request):
            if upRequest.requestType == external
                heappush(upStops, (up)









"""
from enum import Enum
from heapq import heappush, heappop
from dataclasses import dataclass

class Direction(Enum):
    up = "UP"
    down = "DOWN"
    idle = "IDLE"


class RequestType(Enum):
    external = "EXTERNAL"
    internal = "INTERNAL"


@dataclass
class Request:
    origin: int = None
    target: int = None
    requestType: RequestType = None
    direction: Direction = None


@dataclass
class Button:
    floor: int = None


class Elevator:
    def __init__(self, currentFloor: int) -> None:
        self.direction = Direction.idle
        self.currentFloor = currentFloor
        self.upStops = []
        self.downStops = []

    def sendUpRequest(self, upRequest: Request) -> None:
        if upRequest.requestType == RequestType.external:
            heappush(self.upStops, (upRequest.origin, upRequest.origin))
        heappush(self.upStops, (upRequest.target, upRequest.origin))


    def sendDownRequest(self, downRequest: Request) -> None:
        if downRequest.requestType == RequestType.external:
            heappush(self.downStops, (-downRequest.origin, downRequest.origin))
        heappush(self.downStops, (-downRequest.target, downRequest.origin))

    def run(self):
        while self.upStops or self.downStops:
            self.processRequests()

    def processRequests(self):
        if self.direction in [Direction.up, Direction.idle]:
            self.processUpRequests()
            self.processDownRequests()
        else:
            self.processDownRequests()
            self.processUpRequests()


    def processUpRequests(self):  # sourcery skip: assign-if-exp
        while self.upStops:
            target, origin = heappop(self.upStops)
            self.currentFloor = target
            if target == origin:
                print(f"Stopping at floor {target} to pick up people")
            else:
                print(f"Stopping at floor {target} to let people out")

        if self.downStops:
            self.direction = Direction.down
        else:
            self.direction = Direction.idle

    def processDownRequests(self):  # sourcery skip: assign-if-exp
        while self.downStops:
            target, origin = heappop(self.downStops)
            self.currentFloor = -target
            if -target == origin:
                print(f"Stopping at floor {-target} to pick up people")
            else:
                print(f"Stopping at floor {-target} to let people out")

        if self.upStops:
            self.direction = Direction.up
        else:
            self.direction = Direction.idle


elevator = Elevator(currentFloor=0)
# Up Request
upRequest1 = Request(origin=elevator.currentFloor, target=5, requestType=RequestType.internal, direction=Direction.up)
upRequest2 = Request(origin=elevator.currentFloor, target=3, requestType=RequestType.internal, direction=Direction.up)
# Register these requests
elevator.sendUpRequest(upRequest=upRequest1)
elevator.sendUpRequest(upRequest=upRequest2)

# Down Request
downRequest1 = Request(origin=elevator.currentFloor, target=1, requestType=RequestType.internal, direction=Direction.down)
downRequest2 = Request(origin=elevator.currentFloor, target=2, requestType=RequestType.internal, direction=Direction.down)
# Register these requests
elevator.sendDownRequest(downRequest=downRequest1)
elevator.sendDownRequest(downRequest=downRequest2)

# External Request
upRequest3 = Request(origin=4, target=8, requestType=RequestType.external, direction=Direction.up)
downRequest3 = Request(origin=6, target=3, requestType=RequestType.external, direction=Direction.down)
# Register these requests
elevator.sendUpRequest(upRequest=upRequest3)
elevator.sendDownRequest(downRequest=downRequest3)

elevator.run()

