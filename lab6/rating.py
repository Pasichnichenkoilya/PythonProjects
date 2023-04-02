class Rating:
    def __init__(self, rating_id, title, year, rating):
        self.rating_id = rating_id
        self.title = title
        self.year = year
        self.rating = rating

    def __repr__(self):
        return f"Rating(id={self.rating_id}, title={self.title}," \
               f"year={self.year}, rating={self.rating})"
