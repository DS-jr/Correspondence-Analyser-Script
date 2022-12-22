import json, psycopg2
import hidden_3

with open("export_result_TG_account_N4.json") as json_export_file:
    dict_3 = json.load(json_export_file)
    # print(type(dict_3))
    # a_1 = json_export.read()
    # print(type(a_1))

# for k in dict_3["chats"]["list"]:
#     print(k["id"])

connection_3 = psycopg2.connect(
    host=hidden_3.secrets_3()["host"],
    port=hidden_3.secrets_3()["port"],
    database=hidden_3.secrets_3()["database"],
    user=hidden_3.secrets_3()["user"]
)

cur_3 = connection_3.cursor()

#  (w/ Python) Create a new table in Postgres w/ three columns about "chats"
var_2 = "CREATE TABLE if not exists chats (id SERIAL, name VARCHAR(128), type VARCHAR(32), tgchatid INTEGER, UNIQUE(tgchatid), PRIMARY KEY(id) );"
cur_3.execute(var_2)
connection_3.commit()


# (w/ Python) Insert all the selected CHAT IDs to this table

# Var 1:
for k in dict_3["chats"]["list"]:  # (CDL) Adding "if True" condition below is important, as it's better to check if every key exists in every dict
    if k['']:  # (?) How to bypass the error here?  ***"Saved messages" chat's dictionary has NO key "name"
        print('yes')
    else:
        pass
    #print(type(k))
    # var_3 = "INSERT INTO v1_tg_data_export(name, type, tgchatid) VALUES(%s, %s, %s)"
    # cur_3.execute()
# if k['type'] in dict_3["chats"]["list"]:

# Var 2:
# (!) Proceed from here:
for k in range():  #  Try a temporary solution: exclude "Saved messages" chat
    ...

#a_1 = dict_3["chats"]["list"][1]["id"]
#print(a_1)













# var_1 = "INSERT INTO contacts_users (tg_ids) VALUES (78901);"
# cur_3.execute(var_1)
# connection_3.commit()

# (via Python) Add manually a new row to an existing table in the DB


