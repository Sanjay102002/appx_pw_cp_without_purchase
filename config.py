from decouple import config

api_id = config('11734178')
api_hash = config('11e86105f12d9121b04afe06adf4d35f')
bot_token = config('8052463036:AAFwBwCa9Pfmh6WFZRmEr4SlxZtIqJjSZhU')
auth_users = config('7575753569', cast=lambda v: [int(x) for x in v.strip('[]').split(',')])
