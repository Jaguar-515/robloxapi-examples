# non-async version
import robloxapi
client = robloxapi.client()

username =  input("Please enter in a username: ")
print(client.User.IdByUsername(username))