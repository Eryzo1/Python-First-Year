"""
New features in this version:
* Showing all actors in the show and their roles

"""

import json

def load_json(filename) -> dict:
    """
    Load JSON from a file
    """
    file = open(filename, "r")
    data = json.load(file)
    file.close()
    return data

def find_show(query: str, shows: dict) -> str:
    """
    Search for TV shows in the shows dictionary
    Return the name of the first (only one) result based on the query
    If the show is not found, return None
    """
    for name in shows:
        if query.lower() in name.lower():
            return name

def get_show_data_by_name(show_name: str, shows: dict) -> dict:
    """
    Return the data for a show based on its name
    """
    for name, info in shows.items():
        if show_name == name:
            return info
    

def format_show_details(show: dict) -> str:
    """
    Format the show details
    """
    premiered = show["premiered"][:4]
    ended = show["ended"]
    genres = ', '.join(show["genres"]).lower()
    if ended == None:
        ended = "?"
    else:
        ended = ended[:4]
    return f"{premiered} - {ended}, {genres}"
    

def get_cast_by_id(show_id: int) -> list[dict]:
    """
    Get the cast for a show
    """
    file = open(f"Lab 9 Demo/cast/{show_id}_cast.json", "r")
    data = json.load(file)
    file.close()
    return data


def format_cast(cast: list[dict]) -> str:
    """
    Format the cast
    """
    cast_names = ""
    for i in range(len(cast)):
        Actor_name = cast[i]['person']['name']
        Character_name = cast[i]['character']['name']
        cast_names += f"{Actor_name} as {Character_name}\n"
    return cast_names

def main():
    shows = load_json("tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    show_data = get_show_data_by_name(show_name, shows)
    print(show_data)
    if show_name:
        show_id = get_cast_by_id(shows[show_name]['id'])
        print(f"Found: {show_name}, ({format_show_details(show_data)})")
        print(f"Cast: \n{format_cast(show_id)}")
    else:
        print("Can't find this TV show in the Top 100!")

if __name__ == '__main__':
    main()