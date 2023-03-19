from imdb import ImDb

db = ImDb()
db.fill_ratings_with_random(100)

order_by_title = db.execute_sql('SELECT * FROM ratings ORDER BY title')
rating_more_than_eight_point_seven = db.execute_sql('SELECT * FROM ratings WHERE rating > 8.70')

for rating in order_by_title:
    print(rating)

print('----------------------------------------')
for rating in rating_more_than_eight_point_seven:
    print(rating)
