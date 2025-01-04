"""
This program loads data from a json file and searches for TV shows and the actors that the user inputed, and displays the information in the json file. 
Author: Sami Pokharel
Date: December 1, 2023
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
        if query == "":
            return None
        elif query.lower() in name.lower():
            return name
        
def find_actor(query: str, cast: list[dict]) -> dict:
    """
    Search for an actor in the cast list
    Return the actor's data if found
    If the actor is not found, return None
    """
    for key in cast:
        if query == "":
            return None
        elif query.lower() in key["person"]["name"].lower() or query.lower() in key["character"]["name"].lower():
            return key

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

def format_actor_info(actor_dict: dict) -> str:
    """
    Format the actor's information
    """
    actor_info = ""
    actor_name = actor_dict["person"]["name"]
    actor_gender = actor_dict["person"]["gender"]
    actor_birthday = actor_dict["person"]["birthday"]
    actor_country = actor_dict["person"]["country"]["name"]
    character_name = actor_dict["character"]["name"]
    actor_info += f"{actor_name} ({actor_gender}, born {actor_birthday} in {actor_country}) plays {character_name}"
    return actor_info

def main():
    shows = load_json("tvshows.json")
    query = input("Search for a TV show: ")
    show_name = find_show(query, shows)
    show_data = get_show_data_by_name(show_name, shows)
    if show_name:
        show_id = get_cast_by_id(shows[show_name]['id'])
        print(f"Found: {show_name}, ({format_show_details(show_data)})")
        print(f"Cast: \n{format_cast(show_id)}")
        query = input("Search for an actor or character: ")
        actor_data = find_actor(query, show_id)
        if actor_data:
            print(f"Found: {format_actor_info(actor_data)}")
        else:
            print("Can't find this actor or character in the cast!")
    else:
        print("Can't find this TV show in the Top 100!")
    

if __name__ == '__main__':
    main()

