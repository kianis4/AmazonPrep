# LeetCode 1603: Design Parking System
# Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.
# 
# Implement the ParkingSystem class:
# 1. ParkingSystem(int big, int medium, int small): Initializes the ParkingSystem class with the number of slots for each type.
# 2. bool addCar(int carType): Adds a car of the given type (1 = big, 2 = medium, 3 = small) to the parking system. 
#    - Return true if there is available space for this carType.
#    - Return false if no such space is available.
#
# Constraints:
# - 0 <= big, medium, small <= 1000
# - carType is 1, 2, or 3
# - At most 1000 calls will be made to addCar.
#
# Example:
# Input:
#   ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
#   [[1, 1, 0], [1], [2], [3], [1]]
# Output:
#   [null, true, true, false, false]
# Explanation:
#   ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
#   parkingSystem.addCar(1); // returns true because there is 1 big parking spot available
#   parkingSystem.addCar(2); // returns true because there is 1 medium parking spot available
#   parkingSystem.addCar(3); // returns false because there are no small parking spots
#   parkingSystem.addCar(1); // returns false because the big parking spot is already occupied
#
# Runtime Complexity: O(1) for each addCar call.
# Space Complexity: O(1) for maintaining the counts of parking spaces.

class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # Initialize the available parking spots for each type
        self.bigSpots = big
        self.mediumSpots = medium
        self.smallSpots = small

    def addCar(self, carType: int) -> bool:
        # Check carType and adjust parking spot availability
        if carType == 1:  # Big car
            if self.bigSpots > 0:
                self.bigSpots -= 1
                return True
            return False
        elif carType == 2:  # Medium car
            if self.mediumSpots > 0:
                self.mediumSpots -= 1
                return True
            return False
        elif carType == 3:  # Small car
            if self.smallSpots > 0:
                self.smallSpots -= 1
                return True
            return False

# Example usage:
# parkingSystem = ParkingSystem(1, 1, 0)
# parkingSystem.addCar(1) # True
# parkingSystem.addCar(3) # False