import json


class User(object):

    def __init__(self, data):
        self._data = data

    def __str__(self):
        return json.dumps(self._data)

    @property
    def id_(self):
        return self._data['id']

    @property
    def first_name(self):
        return self._data['first_name']

    @property
    def last_name(self):
        return self._data.get('last_name', None)

    @property
    def username(self):
        return self._data.get('username', None)


class Message(object):

    def __init__(self, data):
        self._data = data
        self._from = User(data['from'])
        chat = data['chat']
        if 'first_name' in chat:
            self._chat = User(chat)
        if 'forward_from' in data:
            self._forward_from = User(data['forward_from'])
        else:
            self._forward_from = None
        if 'reply_to_message' in data:
            self._reply_to_message = Message(data['reply_to_message'])
        else:
            self._reply_to_message = None

    def __str__(self):
        return json.dumps(self._data)

    @property
    def message_id(self):
        return self._data['message_id']

    @property
    def from_(self):
        return self._from

    @property
    def date(self):
        return self._data['date']

    @property
    def chat(self):
        return self._chat

    @property
    def forward_from(self):
        return self._forward_from

    @property
    def forward_date(self):
        return self._data.get('forward_date', None)

    @property
    def reply_to_message(self):
        return self._reply_to_message

    @property
    def text(self):
        return self._data.get('text', None)


class Update(object):

    def __init__(self, data):
        self._data = data
        self._message = Message(data['message'])

    def __str__(self):
        return json.dumps(self._data)

    @property
    def update_id(self):
        return self._data['update_id']

    @property
    def message(self):
        return self._message


class ForceReply(object):

    def __init__(self, force_reply, selective=None):
        data = {
            'force_reply': force_reply,
        }
        if selective is not None:
            data['selective'] = selective
        self._data = data

    def __str__(self):
        return json.dumps(self._data)
