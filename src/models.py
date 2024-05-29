from sqlalchemy import Table, Column, BigInteger, String, ForeignKey, TIMESTAMP, BOOLEAN, FLOAT, MetaData, VARCHAR, Integer

metadata = MetaData()

genders = Table(
    "genders",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("gender_full_name", String, nullable=False),
    Column("gender_emoji", String),
    Column("gender_short_name", VARCHAR(1), nullable=False)
)

users = Table(
    "users",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_name", String, nullable=False),
    Column("first_name", String),
    Column("last_name", String),
    Column("is_premium", BOOLEAN, default=False)
)

styles = Table(
    "styles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("gender_id", Integer, ForeignKey("genders.id"))
)

temperature_ranges = Table(
    "temperature_ranges",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("temperature_min", FLOAT, nullable=False),
    Column("temperature_max", FLOAT, nullable=False),
    Column("temperature_text", String,nullable=False),
    Column("temperature_emoji", String)
)

outfits = Table(
    "outfits",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("outfit_name", String),
    Column("outfit_description", String),
    Column("outfit_photo_url", String, nullable=False),
    Column("outfit_gender_id", Integer, ForeignKey("genders.id")),
    Column("outfit_style_id", Integer, ForeignKey("styles.id"))
)

outfit_rating = Table(
    "outfit_rating",
    metadata,
    Column("outfit_id", BigInteger, ForeignKey("outfits.id")),
    Column("outfit_rated_qty", BigInteger, default=0),
    Column("outfit_rating_value", FLOAT, default=0)
)

outfit_rating_log = Table(
    "outfit_rating_log",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("outfit_id", BigInteger, ForeignKey("outfits.id")),
    Column("rating_value", Integer, nullable=False),
    Column("rating_time", TIMESTAMP, nullable=False)
)

tg_bot_rating = Table(
    "tg_bot_rating",
    metadata,
    Column("tg_bot_rated_qty", BigInteger, default=0),
    Column("tg_bot_rating_value", FLOAT, default=0)
)

tg_bot_rating_log = Table(
    "tg_bot_rating_log",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("rating_value", Integer, nullable=False),
    Column("rating_time", TIMESTAMP, nullable=False)
)

tg_bot_comments_log = Table(
    "tg_bot_comments_log",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("comment_text", String, nullable=False),
    Column("comment_time", TIMESTAMP, nullable=False)
)

payment_log = Table(
    "payment_log",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("payment_amount", FLOAT),
    Column("payment_description", String),
    Column("payment_time", TIMESTAMP, nullable=False)
)

activity_log = Table(
    "activity_log",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("activity_type", String, nullable=False),
    Column("activity_parameters", String),
    Column("activity_time", TIMESTAMP, nullable=False)
)

temporary_request_data = Table(
    "temporary_request_data",
    metadata,
    Column("user_id", BigInteger, ForeignKey("users.id")),
    Column("is_premium", BOOLEAN),
    Column("gender", String),
    Column("style_id", BigInteger, ForeignKey("styles.id")),
    Column("temperature_range_id", Integer, ForeignKey("temperature_ranges.id"))
)
