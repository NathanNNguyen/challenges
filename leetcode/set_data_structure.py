# Design a data structure that supports all following operations in average O(1) time.


# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


# Example:

# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();

# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);

# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);

# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);

# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();

# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);

# // 2 was already in the set, so return false.
# randomSet.insert(2);

# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

import random


class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            self.data.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        if len(self.data) >= 1:
            return random.sample(self.data, 1)[0]

        return


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.remove(1)
param_1 = obj.insert(2)
param_3 = obj.getRandom()
