from aiomysql import Pool, DictCursor

from utils.db_api.sql import db_pool


class DBCommands:
    pool: Pool = db_pool

    GET_ROWS = "SELECT * FROM test"

    async def get_rows(self):
        async with self.pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(self.GET_ROWS)
                return await cur.fetchall()


commands = DBCommands()
