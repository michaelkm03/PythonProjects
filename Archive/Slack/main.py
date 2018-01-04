import slacker as Slacker
import json

slack = Slacker(token)

# Send a message to #general channel
slack.chat.post_message('#michaelmontgomery', 'Hello from Saturn!')

# Get users list
response = slack.users.list()
users = response.body['members']

json_obj = json.dumps(users)
basic_info = [d['profile'] for d in users]

_Base_API = slacker.BaseAPI(token=token, timeout=100)