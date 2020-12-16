from instaloader import instaloader

insta = instaloader.Instaloader()
username = input(">>>Username:")
password = input(">>>Password:")
print("[+] Logging in...")
insta.login(username, password)
print("[+] Loggin Successful!")
target = input(">>>Target username(Must be public or you follow them):")
try:
    insta.check_profile_id(target)
    profile = instaloader.Profile.from_username(insta.context, username=target)
    print("[+]Getting List of followers...")
    followers = set(profile.get_followers())
    print("[+]Getting List of followings...")
    print("Got the List!")
    following = set(profile.get_followees())
    """Property of set
    if a={1,2,3,4,5,6} and b={1,2,6,7,3}
    a-b={4,5} and b-a={7}"""
    limit = input(">>>Limit of followers of target(none for no limit):")
    unfollowers = following - followers
    count = 0
    print(">>>List of Non-followers")
    for users in unfollowers:
        if limit == "none":
            print(users.username)
            count += 1
        elif users.followers < int(limit):
            print(users.username)
            count += 1
    print(">>>Total Non-followers you wanted", count)
    print(">>>Total Non-followers:", len(unfollowers))
    print("[+] Mission Accomplished!")
except instaloader.ProfileNotExistsException:#if The profile doesnt exist!
    print("[-]Target does not exists!")