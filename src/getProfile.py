import robloxapi
rbx = robloxapi.client()

userId = input("Enter in a userId: ") # Enter in a userId
print(rbx.User.getProfile(userId)) # Returns a dictionary