import json
#Reading json file
readFile = open("C:\Alumni_Hackathon\input_data\level1a.json", "r")
data = json.load(readFile)

#Storing required data
noOfNeighbour = data["n_neighbourhoods"]
noOfRestaurants = data["n_restaurants"]
graph = {}
restaurant_details = data["restaurants"]
graph[list(restaurant_details)[0]] =restaurant_details['r0']['neighbourhood_distance']
vehicle_details = data["vehicles"]
vehicle_no = (list(vehicle_details)[0])
vehicle_capacity = vehicle_details[vehicle_no]['capacity']

for val in data['neighbourhoods']:
    graph[val] = data["neighbourhoods"][val]["distances"]

#Function to find shortest path
def shortestPath(start, curr, minVal, capacity):
    for i in range(noOfNeighbour-1):
        for each in range(len(visited)):
            if visited[each] == 0 and (int(start[1:]) != each):
                minimum = graph[start][each]+minVal
                break
        for each in range(len(graph[start])):
            if visited[each]==0 and graph[start][each]!=0 and graph[start][each]+minVal <= minimum:
                startNeighbour = 'n'+str(each)
                minimum = graph[start][each]+minVal
                index = each
        if data["neighbourhoods"][startNeighbour]["order_quantity"] <= capacity:
            capacity -= data["neighbourhoods"][startNeighbour]["order_quantity"]
            visited[index] = 1
            curr.append(startNeighbour)
            start = startNeighbour
            minVal=minimum

#Starting from the restaurant
startNode = vehicle_details[vehicle_no]['start_point']
capacity = vehicle_capacity
visited = [0]*(noOfNeighbour)

flag = False
count = 1
resDict ={}
pathDict = {}

while not flag:
    flag = all(ele == 1 for ele in visited)
    if flag:
        break
    for each in range(len(visited)):
        if visited[each] == 0 and (int(startNode[1:]) != each):
            minVal = graph[startNode][each]
            break
    for each in range(len(graph[startNode])):
        if graph[startNode][each] < minVal and visited[each]!=1:
            startNeighbour = 'n'+str(each)
            minVal = graph[startNode][each]
            index = each
    visited[index] = 1
    curr = []
    curr.append(startNeighbour)
    capacity = capacity-data["neighbourhoods"][startNeighbour]["order_quantity"]
    shortestPath(startNeighbour, curr, minVal, capacity)
    curr.insert(0, startNode)
    curr.append(startNode)
    pathDict["path"+str(count)] = curr
    count+=1
    resDict[vehicle_no] = pathDict
    
print(resDict)
json_object = json.dumps(resDict)
with open("C:\Alumni_Hackathon\Output_data\level1a_output.json", "w") as outfile:
    outfile.write(json_object)