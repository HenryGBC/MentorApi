from tortoise import Tortoise

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise


TORTOISE_ORM = {
    "connections": {"default": "postgres://devuser:devuser@localhost:5432/mentors_dev"},
    "apps": {
        "models": {
            "models": [
                "app.mentors.models", "aerich.models"
            ],
            "default_connection": "default",
        },
    },
}


def init_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        db_url="postgres://devuser:devuser@localhost:5432/mentors_dev",
        modules={"models": [
            "app.mentors.models"
        ]},
        generate_schemas=False,
        add_exception_handlers=True,
    )



# async def connectToDatabase():
#     await Tortoise.init(
#         db_url='postgres://devuser:devuser@localhost:5432/mentors_test',
#         modules={'models': ['mentors.models']}
#     )