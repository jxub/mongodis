import pymongo


def collections_with(field)
    db = pymongo.MongoConn()
    colls = db.collections()

    for coll in colls:
        cnt = db[coll].find({field: {'$exists': True}).count()
        if cnt:
            print(coll)
