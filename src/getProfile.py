import robloxapi
import json
rbx = robloxapi.client()

userId = input("Enter in a userId: ") # Enter in a userId
userIdJSON = json.dumps(rbx.User.getProfile(userId)) # Convert this into JSON
print(userIdJSON)
