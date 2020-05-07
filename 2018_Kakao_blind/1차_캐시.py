def solution(cacheSize, cities):
    if cacheSize == 0:
        return 5*len(cities)
    else:
        cities = list(map(lambda x: x.lower(), cities))
        cache = []
        time = 0
        for i in range(len(cities)):
            if cities[i] in cache:
                time += 1
                cities.pop(cities.index(cities[i]))
                cities.append(cities[i])
            else:
                time += 5
                cache.append(cities[i])
                if len(cache) > cacheSize:
                    cache = cache[-cacheSize:]
        return time

cacheSize = [5]
cities = [["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]]

for i in range(len(cacheSize)):
    print(solution(cacheSize[i], cities[i]))