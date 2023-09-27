import instaloader

# Get instance
ig=instaloader.Instaloader()

# Get username from user
username=input("Enter username: ")

# Fetch profile details
profile=instaloader.Profile.from_username(ig.context,username)

# Print profile details
print("Username: ",profile.username)
print("User ID: ",profile.userid)
print("Number of Posts: ",profile.mediacount)
print("Followers: ",profile.followers)
print("Following: ",profile.followees)
print("Bio: ",profile.biography,sep="\n")

# Download profile picture
download=input("Do you want to download profile picture? (y/n): ")
if download=='y':
    ig.download_profile(username,profile_pic_only=True)
    print("Profile picture downloaded successfully!")
else:
    print("Thank you!")