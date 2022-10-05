from pymongo import MongoClient
client = MongoClient('mongodb+srv://test_user:rhaehfdl@cluster0.u1zjohc.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

# 영화제목 '가버나움'의 평점 가져오기
movie = db.movies.find_one({'title':'가버나움'})
star = movie['star']
print(star)


# '가버나움'의 평점과 같은 평점의 영화 제목들 가져오기
all_movies = list(db.movies.find({'star':star},{'_id':False}))
for movie in all_movies:
    print(movie['title'])


# '가버나움'영화의 평점을 0으로 만들기
db.movies.update_one({'title':'가버나움'},{'$set':{'star':'0'}})