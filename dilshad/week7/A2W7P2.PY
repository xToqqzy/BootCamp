import os
import sys
import csv


def load_csv_file(file_name):
    file_content = []

    with open(os.path.join(sys.path[0], file_name), newline='', encoding="utf8") as csv_file:
        file_content = list(csv.reader(csv_file, delimiter=","))

    return file_content


def print_all_tv_shows(file_content):
    show_type_tv_show = 'TV Show'
    tv_show_count = 0

    for item in file_content:
        if item[1] == show_type_tv_show:
            tv_show_count += 1
            print(f"{tv_show_count}: {item[1]}")

    print(f"\nTotal TV Shows: {tv_show_count}")


def print_all_movies(file_content):
    movie_type = 'Movie'
    movie_count = 0

    for item in file_content:
        if item[1] == movie_type:
            movie_count += 1
            print(f"{movie_count}: {item[1]}")

    print(f"\nTotal Movies: {movie_count}")


def search_by_type(file_content, show_type):

    return


def search_by_director(file_content, director):
    director = 'Director'
    for item in file_content:
        if item[3] == director:

    return


def menu(file_content):
    while True:
        print("\nMenu:")
        print("[1] Print all TV Shows")
        print("[2] Print all Movies")
        print("[0] Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            print_all_tv_shows(file_content)
        elif choice == '2':
            print_all_movies(file_content)
        elif choice == '0':
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    file_name = 'netflix_titles.csv'
    file_content = load_csv_file(file_name)
    menu(file_content)
