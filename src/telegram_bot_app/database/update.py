from src.database import async_session_maker
from sqlalchemy import select,update
from src.models import users, genders, styles, temporary_request_data

# update temporary user info to database
async def update_temp_info(info_data: dict, get_session = async_session_maker):
    statement = update(temporary_request_data).where(temporary_request_data.c.user_id == info_data["user_id"]).values(**info_data)
    try:
        async with get_session() as session:
            await session.execute(statement)
            await session.commit()
    except Exception as e:
        print(e.__context__)