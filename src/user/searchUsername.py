import robloxapi, json
rbx = robloxapi.client()

keyword = input("Please enter in a keyword to search users: ") # Enter in a keyword
keywordJSON = json.dumps(rbx.User.searchUsers(keyword)) # Convert this into JSON
jsonFile = open("searchResults.json", "w")
jsonFile.write(keywordJSON)
