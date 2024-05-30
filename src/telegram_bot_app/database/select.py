from src.database import async_session_maker
from sqlalchemy import select
from src.models import users, genders, styles, temporary_request_data, temperature_ranges, outfits


# Select user info
async def select_user(user_id: int, get_session = async_session_maker) -> dict | None:
    async with get_session() as session:        
        query = select(users.c.id, users.c.user_name, users.c.first_name, users.c.last_name, users.c.is_premium).where(users.c.id == user_id)
        query_result = await session.execute(query)
        query_result_data = query_result.all()
    
    if query_result_data:
        return {
            "id": query_result_data[0][0],
            "user_name": query_result_data[0][1],
            "first_name": query_result_data[0][2],
            "last_name": query_result_data[0][3],
            "is_premium": query_result_data[0][4]
        }
    else:
        return None
    
    
# Select all genders info
async def select_all_genders_info(get_session = async_session_maker) -> dict | None:
    query = select(genders)
    async with get_session() as session:
        query_result = await session.execute(query)
        query_result_data = query_result.all()

    if query_result_data:
        result_dict = {}

        for gender in query_result_data:
            result_dict.setdefault(gender[3], {
                "id": gender[0],
                "gender_full_name": gender[1],
                "gender_emoji": gender[2]
            })
            
        return result_dict
    else:
        return None
    

# Select all styles info
async def select_all_style_info(gender_data: dict, get_session = async_session_maker) -> dict | None:
    query = select(styles)
    async with get_session() as session:
        query_result = await session.execute(query)
        query_result_data = query_result.all()

    if query_result_data:
        result_dict = {}

        for style in query_result_data:
            for item in gender_data:
                if item[0] == style[2]:
                    if item[3] in result_dict.keys():
                        result_dict[item[3]].append(
                            {"name": style[1], "id": style[0]}
                        )
                    else:
                        result_dict.setdefault(item[3], [
                            {"name": style[1], "id": style[0]}
                        ])          
        return result_dict
    else:
        return None
    
# Select temporary info user entered
async def select_temp_info(user_id: int, get_session = async_session_maker) -> dict | None:
    async with get_session() as session:        
        query = select(temporary_request_data).where(temporary_request_data.c.user_id == user_id)
        query_result = await session.execute(query)
        query_result_data = query_result.all()
    
    if query_result_data:
        return {
            "user_id": query_result_data[0][0],
            "is_premium": query_result_data[0][1],
            "gender": query_result_data[0][2],
            "style_id": query_result_data[0][3]
        }
    else:
        return None
    

# Select temperature range
async def select_temperature_range(temperature: float, get_session = async_session_maker) -> dict | None:
    async with get_session() as session:        
        query = select(temperature_ranges).where((temperature_ranges.c.temperature_min <= temperature) & (temperature_ranges.c.temperature_max >= temperature))
        query_result = await session.execute(query)
        query_result_data = query_result.all()
    
    if query_result_data:
        return {
            "id": query_result_data[0][0],
            "temperature_min": query_result_data[0][1],
            "temperature_max": query_result_data[0][2],
            "temperature_text": query_result_data[0][3],
            "temperature_emoji": query_result_data[0][4]
        }
    else:
        return None
    
# Select outfit
async def select_outfit(style_id: int, temperature_id: int, get_session = async_session_maker) -> list | None:
    async with get_session() as session:        
        query = select(outfits.c.outfit_photo_url).where((outfits.c.outfit_style_id == style_id) & (outfits.c.outfit_temperature_range_id == temperature_id))
        query_result = await session.execute(query)
        query_result_data = query_result.all()
    
    if query_result_data:
        result = []
        for item in query_result_data:
            result.append(item[0])
        return result
    else:
        return None