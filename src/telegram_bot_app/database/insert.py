from src.database import async_session_maker
from sqlalchemy import insert
from src.models import users, genders, styles, temporary_request_data, temperature_ranges, outfits

# user_data example
# user_data = {
#     "id": user_id,
#     "user_name": user_name,
#     "first_name": first_name,
#     "last_name": last_name
# }

# insert new user to database
async def insert_user(user_data: dict, get_session = async_session_maker):
    statement = insert(users).values(**user_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)


# gender_data example
# gender_data = {
    # "gender_full_name": query_result_data[0][1],
    # "gender_emoji": query_result_data[0][2],
    # "gender_short_name": query_result_data[0][3]
# }

# insert new gender to database
async def insert_gender(gender_data: dict, get_session = async_session_maker):
    statement = insert(genders).values(**gender_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)


# insert new style to database
async def insert_style(style_data: dict, get_session = async_session_maker):
    statement = insert(styles).values(**style_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)

# insert new temporary user info to database
async def insert_temp_info(info_data: dict, get_session = async_session_maker):
    statement = insert(temporary_request_data).values(**info_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)

# temperature_data example
# temperature_data = {
    # "temperature_min": query_result_data[0][1],
    # "temperature_max": query_result_data[0][2],
    # "temperature_text": query_result_data[0][3],
    # "temperature_emoji": query_result_data[0][3]
# }

# insert temperature ranges to database
async def insert_temperature_range(temperature_data: dict, get_session = async_session_maker):
    statement = insert(temperature_ranges).values(**temperature_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)

# insert outfit to database
async def insert_outfit(outfit_data: dict, get_session = async_session_maker):
    statement = insert(outfits).values(**outfit_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)