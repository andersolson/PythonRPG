import items, enemies, actions, world, player

class MapTile(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def intro_text(self):
        raise NotImplementedError()
    
    def modify_player(self, player):
        raise NotImplementedError()
    
    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_exists(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_exists(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_exists(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_exists(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves
    
    def available_actions(self):
        """Returns all of the available actions in the room"""
        moves = self.adjacent_moves()
        moves.append(actions.ViewInventory())
        return moves
    
class StartingRoom(MapTile):
    def intro_text(self):
        return """
        You find yourself in a cave with a flickering torch on the wall.
        You can make out four paths, each equally as dark and foreboding.
        """
    
    def modify_player(self, player):
        #Room has no action on player, but the player is now in game and
        #the NotImplementedError will not be raised
        pass

class LeaveCaveRoom(MapTile):
    def intro_text(self):
        return """
        You see a bright light in the distance...
        ... it grows brighter as you get closer!
        It's sunlight!
        
        Victory is yours! You escaped the cave.
        """
    
    def modify_player(self, player):
        player.victory = True
    
class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super(MapTile, self).__init__(x, y)
    
    def add_loot(self, player):
        player.inventory.append(self.item)
        
    def modify_player(self, player):
        self.add_loot(player)
    
class EnemyRoom(MapTile):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super(EnemyRoom, self).__init__(x, y)
        
    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print ("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage,
                                                                            the_player.hp))
    def available_actions(self):
        if self.enemy.is_alive():
            return [actions.Flee(tile=self), actions.Attack(enemy=self.enemy)]
        else:
            return self.adjacent_moves()
    
class EmptyCavePath(MapTile):
    def intro_text(self):
        return """
        Another dank featureless part of the cave. You must march onwards."""
    
    def modify_player(self, player):
        #Room has no action on player
        pass
    
class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y, enemy):
        super(EnemyRoom,self).__init__(x, y, enemies.GiantSpider())
    
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A giant spider looms in a web above you.
            The spider descends from it's nook and drops infront of you!
            """
        else:
            return """
            The giant corpse of a dead spider lays rotting on the ground.
            Tiny baby spiders have begun the work of devouring their mother.
            """
        
class OgreRoom(EnemyRoom):
    def __init__(self, x, y):
        super(OgreRoom, self).__init__(x, y, enemies.Ogre())
    
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            An Ogre is sitting by a fire while gnawing on a deer leg.
            He hears your approaching foots steps and turns with his club 
            raised ready to confront you!
            """
        
        else:
            return """
            The body of a dead Ogre is spread out on the floor.
            A half eaten deer clings to life while it nibbles 
            at the dead Ogre's flesh.
            """
        
class LettuceRoom(EnemyRoom):
    def __init__(self, x, y):
        super(LettuceRoom, self).__init__(x, y, enemies.lettuce())
    
    def intro_text(self):
        if self.enemy.is_alive():
            return """
            A wet, wedge of lettuce sits motionless on the floor before you.
            It doesn't like the way you walk. Prepare for battle!
            """
        
        else:
            return """
            A mutilated pile of lettuce is oozing green juice across the floor.
            """

class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super(FindDaggerRoom, self).__init__(x, y, items.Dagger())
    
    def intro_text(self):
        return """
        You notice something shine in the corner.
        It's a dagger! You pick it up.
        """

class Find5GoldRoom(LootRoom):
    def __init__(self, x, y):
        super(Find5GoldRoom,self).__init__(x, y, items.Gold(5))
    
    def intro_text(self):
        return """
        You find 5 gold in this chamber!
        """

class FindSuperRockRoom(LootRoom):
    def __init__(self, x, y):
        super(FindSuperRockRoom, self).__init__(x, y, items.superChargedRock())
    
    def intro_text(self):
        return """
        You notice a large file cabinet sized rock in the middle of the room.
        Something seems strange about it... 
        It's a Super Charged Rock! You pick it up. Elemental magic flows through you.
        """