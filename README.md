# python-httpplug
An Async context manager for HTTPPlug runelite plugin written in Python

Example use:
```
from httpplug import HTTPPlug

async def main():
  async with HTTPPlug(8080) as plug:
    events = await plug.get_events()
    #stats = await plug.get_stats()
    #players = await plug.get_players()
    #walking_tiles = await plug.get_tiles() #use this to make a walker script
    #objects = await plug.get_objects()
    #npcs = await plug.get_npcs()
    #inv = await plug.get_inv()
    #equip = await plug.get_equip()
    #doors = await plug.get_doors()
    
    print(events)
```
