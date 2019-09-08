import robloxapi, json

client = robloxapi.client()

groupId = input("Please enter a valid groupId")
wallJSON = json.dumps(client.Group.getWall(groupId))
jsonFile = open("groupWall.json", "w")
jsonFile.write(wallJSON)