import robloxapi
rbx = robloxapi.client()

keyword = input("Please enter in a keyword to search users: ") # Enter in a keyword
print(rbx.User.searchUsers(keyword)) # Returns a dictionary