def display_friends(friends_dict):
    for username, followers in friends_dict.items():
        print(f"{username}: {followers} followers")

friends = {"raj_07": "2.3K", "ananya_xo": "1.8K", "dev_coder": "3K"}
display_friends(friends)
