class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # The final city will be the city that is not a starting destination, or connecting
        # city anywhere else. So basically it's just one City that appears at index 1 in one
        # of the lists, without appearing anywhere else.

        # How can we determine what that city is, in the fewest possible steps?
        # The best time complexity would have to be O(n) because we need to go through all of the
        # cities to accurately know the final city for certain

        # It will be the only ending city that is never a starting city
        
        starting_cities = []
        ending_cities = []

        for i in range(len(paths)):
            starting_cities.append(paths[i][0])
            ending_cities.append(paths[i][1])
        
        for ending_city in ending_cities:
            if ending_city not in starting_cities:
                return ending_city
