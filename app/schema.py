# createSchema.py
from tortoise import Tortoise, run_async
# from app.database import connectToDatabase

async def main():
    await Tortoise.init(
        db_url='postgres://devuser:devuser@localhost:5432/mentors_test',
        modules={'models': ['mentors.models']}
    )
    await Tortoise.generate_schemas()
# mentors_test
# devuser

if __name__ == '__main__':
    run_async(main())