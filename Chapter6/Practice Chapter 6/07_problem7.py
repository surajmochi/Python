# write a programe to find out whether a given post is talking about "Suraj" or not.


Post = input("Enter the post: ")

if("Suraj".lower() in Post.lower()):
    print("This post is talking about Suraj")
else:
    print("This post is not talking about Suraj: ")


