import json

#Reading json file
readFile = open("C:\Alumni_Hackathon\input_data\level0.json", "r")
data = json.load(readFile)

#Storing required data
noOfNeighbour = data["n_neighbourhoods"]
noOfRestaurants = data["n_restaurants"]
graph = {}
restaurant_details = data["restaurants"]
graph[list(restaurant_details)[0]] =restaurant_details['r0']['neighbourhood_distance']
vehicle_details = data["vehicles"]
vehicle_no = (list(vehicle_details)[0])

for val in data['neighbourhoods']:
    graph[val] = data["neighbourhoods"][val]["distances"]
#Function to find shortest path
def shortestPath(start, curr, minVal):
    for i in range(noOfNeighbour-1):
        #print("Previous min ", minVal)
        #print("start value ", start)
        for each in range(len(visited)):
            if visited[each] == 0 and (int(start[1:]) != each):
                minimum = graph[start][each]+minVal
                break
        #startNeighbour = 'n'+str(index)
        for each in range(len(graph[start])):
            if visited[each]==0 and graph[start][each]!=0 and graph[start][each]+minVal <= minimum:
                startNeighbour = 'n'+str(each)
                minimum = graph[start][each]+minVal
                index = each
        visited[index] = 1
        curr.append(startNeighbour)
        start = startNeighbour
        minVal=minimum
        #shortestPath(startNeighbour, curr, minimum)

#Starting from the restaurant
startNode = vehicle_details[vehicle_no]['start_point']
visited = [0]*(noOfNeighbour)
minVal = graph[startNode][0]
#index = 0
for each in range(len(graph[startNode])):
    if graph[startNode][each] < minVal:
        startNeighbour = 'n'+str(each)
        minVal = graph[startNode][each]
        index = each
visited[index] = 1
curr = []
curr.append(startNeighbour)
shortestPath(startNeighbour, curr, minVal)
curr.insert(0, startNode)
curr.append(startNode)
 

resDict = {}
pathDict = {}
pathDict["path"] = curr
resDict[vehicle_no] = pathDict
print(resDict)
json_object = json.dumps(resDict)
with open("C:\Alumni_Hackathon\Output_data\level0_output.json", "w") as outfile:
    outfile.write(json_object)