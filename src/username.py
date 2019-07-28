import robloxapi
rbx = robloxapi.client() 

username = input("Enter in a username: ") # Enter in a username 
rbx.Auth.IsUsernameTaken(username) # Checks if username is taken or not
if (rbx.Auth.IsUsernameTaken(username)): # If username is taken, do this
    print("Username is taken")
else: # If username is not taken, do this
    print("Username is not taken")
