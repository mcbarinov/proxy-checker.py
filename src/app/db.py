from mm_base1.db import BaseDB, DatabaseAny
from mm_mongo import MongoCollection

from app.models import Proxy, Source


class DB(BaseDB):
    def __init__(self, database: DatabaseAny):
        super().__init__(database)
        self.source: MongoCollection[Source] = Source.init_collection(database)
        self.proxy: MongoCollection[Proxy] = Proxy.init_collection(database)
