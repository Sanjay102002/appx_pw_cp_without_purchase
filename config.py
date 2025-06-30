from decouple import config

api_id = config('API_ID')
api_hash = config('API_HASH')
bot_token = config('BOT_TOKEN')
auth_users = config('AUTH_USERS', cast=lambda v: [int(x) for x in v.strip('[]').split(',')])
