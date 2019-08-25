import robloxapi
import json
client = robloxapi.client()

groupId = input("Please enter in a valid group id: ") # Enter in a groupId
groupJSON = json.dumps(client.Group.getGroup(groupId)) # Convert into a JSON file
jsonFile = open("group.json", "w")
jsonFile.write(groupJSON)
