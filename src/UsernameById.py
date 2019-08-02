import robloxapi
client = robloxapi.client()

userId = input("Enter in a userId (needs to be a number): ")
print(client.User.UsernameById(userId))