import os
import sys
import json


movie_list = []


def load_movies():
    global movie_list
    try:
        with open('movies.json', 'r') as file:
            movie_list = json.load(file)
    except FileNotFoundError:
        print("movies.json file not found.")
        sys.exit(1)


def save_movies():
    with open('movies.json', 'w') as file:
        json.dump(movie_list, file, indent=4)


def movie_info():
    movies_2004 = []
    genre_fiction = []
    keanu_reeves = []
    stallone_1995_2005 = []

    for movie in movie_list:
        if movie['year'] == 2004:
            movies_2004.append(movie)
        if 'Science Fiction' in movie['genres']:
            genre_fiction.append(movie)
        if 'Keanu Reeves' in movie['cast']:
            keanu_reeves.append(movie)
        if 'Sylvester Stallone' in movie['cast'] and 1995 < movie['year'] < 2010:
            stallone_1995_2005.append(movie)

    oldest_movie = movie_list[0]
    for movie in movie_list:
        if movie['year'] < oldest_movie['year']:
            oldest_movie = movie

    print(f"Movies released in 2004: {len(movies_2004)}")
    print(f"Movies in Science Fiction genre: {len(genre_fiction)}")
    print("Movies with Keanu Reeves:")
    for movie in keanu_reeves:
        print(movie)
    print("Movies with Sylvester Stallone between 1995 and 2005:")
    for movie in stallone_1995_2005:
        print(movie)
    print(f"The oldest movie is: {oldest_movie}")


def veranderingen():
    for movie in movie_list:
        if movie['title'] == 'Gladiator' and movie['year'] == 2000:
            movie['year'] = 2001

    oldest_movie = movie_list[0]
    for movie in movie_list:
        if movie['year'] < oldest_movie['year']:
            oldest_movie = movie
    oldest_movie['year'] -= 1

    for movie in movie_list:
        if 'Natalie Portman' in movie['cast']:
            movie['cast'] = ['Nat Portman' if actor ==
                             'Natalie Portman' else actor for actor in movie['cast']]
        if 'Kevin Spacey' in movie['cast']:
            movie['cast'] = [actor for actor in movie['cast']
                             if actor != 'Kevin Spacey']

    save_movies()
    print("Modifications saved successfully.")


def search_movie():
    title = input("Enter movie title: ")
    for movie in movie_list:
        if movie['title'].lower() == title.lower():
            print(movie)
            return
    print("Movie not found.")


def change_movie():
    title = input("Enter movie title: ")
    for movie in movie_list:
        if movie['title'].lower() == title.lower():
            new_title = input("Enter new title: ")
            new_year = int(input("Enter new year: "))
            movie['title'] = new_title
            movie['year'] = new_year
            save_movies()
            print("Movie updated successfully.")
            return
    print("Movie not found.")


def main() -> None:
    load_movies()

    while True:
        print("[I] Movie information overview")
        print("[M] Make modification based on assignment")
        print("[S] Search a movie title ")
        print("[C] Change title and/or release year by search on title")
        print("[Q] Quit program")

        choice = input("choose between [I] [M] [S] [C] [Q]").upper()

        if choice == 'I':
            movie_info()
        elif choice == 'M':
            veranderingen()
        elif choice == 'S':
            search_movie()
        elif choice == 'C':
            change_movie()
        elif choice == 'Q':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
