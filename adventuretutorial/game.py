import world
import tiles
from player import Player

def play():
    world.load_tiles()
    character = Player()
    room = world.tile_exists(character.location_x, character.location_y)
    #print(room.intro_text())
    print character.location_x, character.location_y
    print room

    while character.is_alive() and not character.victory:
        room = world.tile_exists(character.location_x, character.location_y)
        room.modify_player(character)
        # Check again since the room could have changed the player's state
        if character.is_alive() and not character.victory():
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    character.do_action(action, **action.kwargs)
                    break     

if __name__ == "__main__":
    play()
        