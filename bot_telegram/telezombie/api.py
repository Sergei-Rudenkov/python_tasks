import json
from tornado import gen, httpclient, web, httputil
from . import types

_API_TEMPLATE = 'https://api.telegram.org/bot{api_token}/{api_method}'


class TeleZombie(object):

    def __init__(self, api_token):
        self._api_token = api_token
        if not self._api_token:
            raise TeleError('invalid API token')

    @gen.coroutine
    def get_updates(self, offset=0, limit=100, timeout=0):
        args = {
            'offset': offset,
            'limit': limit,
            'timeout': timeout,
        }
        data = yield self._get('getUpdates', args)
        return [types.Update(u) for u in data]

    @gen.coroutine
    def set_webhook(self, url=None):
        if url is None:
            args = None
        else:
            args = {
                'url': url
            }

        # TODO undocumented return type
        data = yield self._get('setWebhook', args)
        return None

    @gen.coroutine
    def get_me(self):
        data = yield self._get('getMe')
        return types.User(data)

    @gen.coroutine
    def send_message(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None):
        args = {
            'chat_id': chat_id,
            'text': text,
        }
        if disable_web_page_preview is not None:
            args['disable_web_page_preview'] = disable_web_page_preview
        if reply_to_message_id is not None:
            args['reply_to_message_id'] = reply_to_message_id
        if reply_markup is not None:
            args['reply_markup'] = str(reply_markup)

        data = yield self._get('sendMessage', args)
        return types.Message(data)

    @gen.coroutine
    def forward_message(self, chat_id, from_chat_id, message_id):
        args = {
            'chat_id': chat_id,
            'from_chat_id': from_chat_id,
            'message_id': message_id,
        }

        data = yield self._get('forwardMessage', args)
        return types.Message(data)

    def _get_api_url(self, api_method):
        return _API_TEMPLATE.format(api_token=self._api_token, api_method=api_method)

    def _parse_response(self, response):
        data = response.body.decode('utf-8')
        data = json.loads(data)
        if not data['ok']:
            raise TeleError(data['description'])
        return data['result']

    @gen.coroutine
    def _get(self, api_method, args=None):
        url = self._get_api_url(api_method)
        if args is not None:
            url = httputil.url_concat(url, args)

        link = httpclient.AsyncHTTPClient()
        request = httpclient.HTTPRequest(url)
        response = yield link.fetch(request)
        return self._parse_response(response)


class _DispatcherMixin(object):

    def __init__(self, *args, **kwargs):
        super(_DispatcherMixin, self).__init__()

    @gen.coroutine
    def on_text(self, message):
        pass

    @gen.coroutine
    def _receive_message(self, message):
        if message.text is not None:
            yield self.on_text(message)
        else:
            raise TeleError('unknown message type')


class TeleLich(_DispatcherMixin):

    def __init__(self, api_token):
        self._api = TeleZombie(api_token)

    @property
    def zombie(self):
        return self._api

    @gen.coroutine
    def get_updates(self, timeout=0):
        offset = 0
        updates = []
        while True:
            us = yield self._api.get_updates(offset, timeout=timeout)
            updates.extend(us)
            if not us:
                break
            offset = us[-1].update_id + 1
        return updates

    @gen.coroutine
    def get_me(self):
        return self._api.get_me()

    @gen.coroutine
    def send_message(self, chat_id, text, disable_web_page_preview=None, reply_to_message_id=None, reply_markup=None):
        return self._api.send_message(chat_id, text, disable_web_page_preview, reply_to_message_id, reply_markup)

    @gen.coroutine
    def forward_message(self, chat_id, from_chat_id, message_id):
        return self._api.forward_message(chat_id, from_chat_id, message_id)

    @gen.coroutine
    def poll(self, timeout=1):
        # remove previous webhook first
        yield self._api.set_webhook()
        # forever
        while True:
            try:
                updates = yield self.get_updates(timeout)
                for u in updates:
                    yield self._receive_message(u.message)
            except httpclient.HTTPError as e:
                if e.code != 599:
                    raise

    @gen.coroutine
    def listen(self, hook_url):
        yield self._api.set_webhook(url=hook_url)

    @gen.coroutine
    def close(self):
        # remove webhook
        yield self._api.set_webhook()


class TeleHookHandler(web.RequestHandler, _DispatcherMixin):

    @gen.coroutine
    def post(self):
        data = self.request.body
        data = data.decode('utf-8')
        data = json.loads(data)
        update = types.Update(data)
        yield self._receive_message(update.message)


class TeleError(Exception):

    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description
