import json
import urllib3
import websockets

import ubiquity
from ubiquity.ubiquity_openapi_client.model import (block_identifier,tx)


def transform_content_from_type(_type):
    """
    Returns a function that transforms the payload of a
         channel event store in the 'content' key of its
         response according to the type received in the
         '_type' parameter.
    """
    def fn(content):
        # boilerplate API client object
        api_client = ubiquity.ApiClient(ubiquity.Configuration())
        content_as_rest_response = urllib3.response.HTTPResponse(
            json.dumps(content))

        return api_client.deserialize(content_as_rest_response, (_type, ),
                                      True)

    return fn


class WebsocketConnection:
    """
    This class provides methods to connect and subscribe to a websocket channel.

    Its constructor takes a callable '_transform_fn', used to build the 'tranform_fn' property, that's called in the 'subscribe' method.
    If the optional keyword argument 'fn_as_type' is True (the default), '_transform_fn' is used as a type constructor and is passed to the 'transform_content_from_type' function to build the 'transform_fn' property. Otherwise, it's just assigned as is to 'transform_fn'.
    """
    def __init__(self, _transform_fn, fn_as_type=True):
        if fn_as_type:
            self.transform_fn = transform_content_from_type(_transform_fn)
        else:
            self.transform_fn = _transform_fn

    def connect(self, config):
        """
        Creates a connection to the websocket server from a ubiquity.Configuration object

        Parameters:
        ----------
        - config (ubiquity.Configuration) - config object containing url and token to connect to server.
        ----------

        Returns:
        ----------
        - connection (websockets.client.Connect): websockets connection object.---------
        """
        headers = {}
        if config.access_token:
            headers["Authorization"] = "Bearer " + config.access_token

        return websockets.connect(config.host, extra_headers=headers)

    async def _subscribe(self,
                         connection,
                         _id,
                         params,
                         callback,
                         on_connected=None,
                         on_subscribed=None):
        """
        Subscribes to a websocket channel according to 'params' dictionary.
        Executes the 'wrapper_callback' function when an event is received from the server. This function wraps 'callback' for converting the response into the appropriate type indicated by self.transform_fn.
        Parameters:
        ----------
        - connection (websockets.client.Connect): websockets connection object.
        - _id (string): request id.
        - params (dict):
            - channel (string): channel to subscribe to.
            - detail (dict): detail object that can be passed when making the subscription.
        - callback (function): callback function called when an event is received from the server. Takes the JSON response mapped as a dictionary.
        - on_connected (function): callback function called when the connection is actually made (when the connection object is awaited). Takes a websockets.client.WebSocketClientProtocol object as parameter.
        - on_subscribed (function): callback function called when the subscription response is received.
        ----------
        """
        if not callable(callback):
            raise ValueError("Callback argument is not a callable object")
        async with connection as ws:
            if callable(on_connected):
                on_connected(ws)
            subscribe_request = {
                "id": _id,
                "method": "ubiquity.subscribe",
                "params": params,
            }
            await ws.send(json.dumps(subscribe_request))
            while True:
                msg_buf = await ws.recv()
                msg = json.loads(msg_buf)

                method = msg.get("method")

                # Check if this is a subscription response
                if "result" in msg and "subID" in msg["result"]:
                    if callable(on_subscribed):
                        on_subscribed(msg)

                if method is not None and method == "ubiquity.subscription":
                    for event in msg["params"]["items"]:
                        callback(event)

    async def subscribe(self,
                        connection,
                        _id,
                        channel,
                        callback,
                        detail=None,
                        on_connected=None,
                        on_subscribed=None):
        """
        Subscribes to a websocket channel given by 'channel' variable.
        Executes the 'wrapper_callback' function when an event is received from the server. This function wraps 'callback' for converting the response into the appropriate type indicated by self.transform_fn.

=======
                         on_connected=None):
        Parameters:
        ----------
        - connection (websockets.client.Connect): websockets connection object.
        - _id (string): request id.
<<<<<<< HEAD
        - channel (string): channel to subscribe to.
        - callback (function): callback function used by _subscribe and wrapped by wrapper_callback. Takes an event dict.
        - detail (dict): detail object that can be passed when making the subscription.
        - on_connected (function): callback function called when the connection is actually made (when the connection object is awaited). Takes a websockets.client.WebSocketClientProtocol object as parameter.
        - on_subscribed (function): callback function called when the subscription response is received.
        ----------
        """
        def wrapper_callback(event):
            """
            Wraps the deserializing of event's content and calling
                of received callback function into a single function,
                which is then passed to '_subscribe'
            """

            event['content'] = self.transform_fn(event['content'])
            return callback(event)

        params = {
            "channel": channel,
            **({
                "detail": detail
            } if detail != None else {})
        }
        await self._subscribe(connection,
                              _id,
                              params,
                              wrapper_callback,
                              on_connected=on_connected,
                              on_subscribed=on_subscribed)

    async def _unsubscribe(self, connection, _id, channel, subID):
        """
        Unsubscribes to a websocket channel according to 'params' dictionary.
        Parameters:
        ----------
        - connection (websockets.client.Connect): websockets connection object.
        - _id (string): request id.
        - channel (string): channel to subscribe to.
        - subID (int): subscription ID to ask for unsubscription.
        ----------

        Returns:
        ----------
        The unsubscription message received, indicating if it was successful or not
        ----------
        """

        async with connection as ws:
            unsubscribe_request = {
                "id": _id,
                "method": "ubiquity.unsubscribe",
                "params": {
                    "channel": channel,
                    "subID": subID
                },
            }
            await ws.send(json.dumps(unsubscribe_request))
            msg_buf = await ws.recv()
            msg = json.loads(msg_buf)
            return msg


class BlockIdsWebsocketConnection(WebsocketConnection):
    """
    Derives WebsocketConnection to handle the 'ubiquity.block_identifiers' channel
    """
    def __init__(self):
        self.channel = "ubiquity.block_identifiers"
        super().__init__(block_identifier.BlockIdentifier)

    async def subscribe_block_ids(self,
                                  connection,
                                  _id,
                                  callback,
                                  detail=None,
                                  on_connected=None,
                                  on_subscribed=None):
        return await self.subscribe(connection, _id, self.channel, callback,
                                    detail, on_connected, on_subscribed)

    async def unsubscribe_block_ids(self, connection, _id, subID):
        return await self._unsubscribe(connection, _id, self.channel, subID)


class TxsWebsocketConnection(WebsocketConnection):
    """
    Derives WebsocketConnection to handle the 'ubiquity.txs' channel
    """
    def __init__(self):
        self.channel = "ubiquity.txs"
        super().__init__(tx.Tx)

    async def subscribe_txs(self,
                            connection,
                            _id,
                            callback,
                            detail=None,
                            on_connected=None,
                            on_subscribed=None):
        return await self.subscribe(connection, _id, self.channel, callback,
                                    detail, on_connected, on_subscribed)

    async def unsubscribe_txs(self, connection, _id, subID):
        return await self._unsubscribe(connection, _id, self.channel, subID)
