import json, config
from sqlalchemy import create_engine
from sqlalchemy.sql import text

with open("export_result_TG_account_N4.json") as json_file:
    exported_data_dict = json.load(json_file)
    # print(type(exported_data_dict))

engine = create_engine(config.DATABASE_STRING, future=True)  # Engine is a factory that can create new database connections

# insert chat data (telegram_id, name, type) into SQLite:
with engine.connect() as con_5:
    for chat in exported_data_dict["chats"]["list"]:
        var_1 = text()  # (?) Is 'text' module vital here?
        """
        INSERT INTO telegram_chats (name, type, telegram_id,) 
        VALUES(:name, :type, :id) 
        ON CONFLICT (telegram_id) DO NOTHING
        """
        )
        # con_5.execute(var_1, {..??..})   # Proceed from here!

        # print(chat["type"])





    # print(type(exported_data_dict["chats"]["list"]))
    # ...??...
