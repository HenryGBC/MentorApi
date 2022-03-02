from fastapi import FastAPI

from .mentors import routers as routers_mentors
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise
from .database import init_db


app = FastAPI()

app.include_router(routers_mentors.router)



@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


@app.on_event("startup")
async def startup_event():
    init_db(app)



# register_tortoise(
#     app,
#     db_url='postgres://devuser:devuser@localhost:5432/mentors_test',
#     modules={"models": ["app.mentors.models"]},
#     generate_schemas=True,
#     add_exception_handlers=True,
# )

# if __name__ == '__main__':
#     print('sda')