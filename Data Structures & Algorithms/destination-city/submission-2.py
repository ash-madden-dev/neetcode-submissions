class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starting_cities = []
        ending_cities = []

        for i in range(len(paths)):
            starting_cities.append(paths[i][0])
            if paths[i][1] not in starting_cities:
                ending_cities.append(paths[i][1])
        
        for ending_city in ending_cities:
            if ending_city not in starting_cities:
                return ending_city
