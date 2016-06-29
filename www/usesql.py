import orm, asyncio
from models import User, Blog, Comment

async def test():
    await orm.create_pool(loop,user='root', password='password', database='awesome')

    u=User(name='Test', email = 'test@example.com', passwd='12344567890',image='about:blank')

    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
