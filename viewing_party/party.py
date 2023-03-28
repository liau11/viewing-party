# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}

    if not title or not genre or not rating:
        return None
    
    movie["title"], movie["genre"], movie["rating"] = title, genre, rating
    
    return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if title not in movie['title']:
            return user_data
        user_data['watched'].append(movie)
        user_data['watchlist'].remove(movie)

    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
