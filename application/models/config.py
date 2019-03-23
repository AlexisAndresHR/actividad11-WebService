import web

db_host = 'localhost'
db_name = 'act11_webservice_aahr'
db_user = 'aahr'
db_pw = 'aahr.2019'

db = web.database(
    dbn='mysql',
    host=db_host,
    db=db_name,
    user=db_user,
    pw=db_pw
    )