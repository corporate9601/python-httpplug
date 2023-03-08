import asyncio
import aiohttp

class HTTPPlug:
    
    def __init__(self,port) -> None:
        self.port = port 
        
    async def __aenter__(self): 
        return self
    
    async def __aexit__(self, exc_t, exc_v, exc_tb): 
        if exc_t==None and exc_v==None and exc_tb==None :
            pass
        else:
            print(exc_t)
            print(exc_v)
            print(exc_tb)
        
    async def get_stats(self):
        res = await self.do('/stats')
        return(eval(res))
    
    async def get_tiles(self):
        res = await self.do('/tiles')
        return(eval(res))
    
    async def get_inv(self):
        res = await self.do('/inv')
        return(eval(res))
        
    async def get_objects(self):
        res = await self.do('/objects')
        return(eval(res))
        
    async def get_npcs(self):
        res = await self.do('/npcs')
        return(eval(res))
    
    async def get_players(self):
        res = await self.do('/players')
        return(eval(res))
        
    async def get_events(self):
        res = await self.do('/events')
        return(eval(res))
        
    async def get_doors(self):
        res = await self.do('/doors')
        return(eval(res))
    
    async def do(self,uri):
        async with aiohttp.ClientSession() as session:
            async with session.get('http://localhost:'+str(self.port)+uri) as resp:
                return await resp.text()
        