import aiomysql
from data import config


async def create_pool(lp):
    return await aiomysql.create_pool(
        host=config.DB_HOST,
        port=3306,
        user=config.DB_USER,
        password=config.DB_PASS,
        db=config.DB_NAME,
        loop=lp,
        autocommit=True,
    )

db_pool = config.loop.run_until_complete(create_pool(config.loop))
