import pymongo
import os
from dotenv import load_dotenv
from classes import DATA, Dataprocess, DbMongo

def main():
    client, db = DbMongo.getDB()

    Dataprocess.delete_all(db)
    Dataprocess.delete_all(db)

    pipeline = Dataprocess(DATA[7][5])
    
    pipeline.create_careers()
    pipeline.create_students()
    pipeline.create_enrollments()

    print(DATA)
    return True

if __name__ == "__main__":
    main()
    load_dotenv()