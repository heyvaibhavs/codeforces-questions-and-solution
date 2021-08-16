info={}
info['name']=input("enter your name")
info['age']=int(input("enter your age"))
info['fav_movie']=input("enter your list of fav movie").split(",")
info['fav_songs']=input("enter your list of fav songs").split(",")
for i,j in info.items():
    print(i," : ",j)