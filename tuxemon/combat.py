"""

Combat related code that can be independent of the combat state.

Code here might be shared by states, actions, conditions, etc.

"""


import tuxemon.player

import logging

logger = logging.getLogger()


def check_battle_legal(player):
    """Checks to see if the player has any monsters fit for battle.

    :type player: tuxemon.player.Player

    :rtype: bool
    """

    # Don't start a battle if we don't even have monsters in our party yet.
    if len(player.monsters) < 1:
        logger.info("Cannot start battle, player has no monsters!")
        return False
    else:
        if fainted_party(player.monsters):
            logger.info("Cannot start battle, player's monsters are all DEAD")
            return False
        else:
            return True


def check_status(monster, status_name):
    return any(t for t in monster.status if t.slug == status_name)


def fainted(monster):
    return check_status(monster, "status_faint") or monster.current_hp <= 0


def get_awake_monsters(player: tuxemon.player.Player):
    """Iterate all non-fainted monsters in party"""
    for monster in player.monsters:
        if not fainted(monster):
            yield monster


def fainted_party(party):
    return all(map(fainted, party))


def defeated(player):
    return fainted_party(player.monsters)
