import asyncio
import json
import time
import unittest

import test.mock
import test.utils
import test.serve_websockets

import httpretty
import pytest
import websockets

import ubiquity.websockets as ws
from ubiquity import Configuration
from ubiquity.api import ApiClient
from ubiquity.ubiquity_openapi_client.model import (block, block_identifier,
                                                    tx)


async def setup_client_server(_class):
    port = test.utils.get_open_port()
    start_server = websockets.serve(test.serve_websockets.run_server,
                                    "127.0.0.1", port)
    server_conn = await start_server

    obj = _class()

    return obj, obj.connect(
        Configuration(f"ws://127.0.0.1:{port}")), server_conn


async def _test_websocket_subscription(_class,
                                       method,
                                       _type,
                                       request_detail=None):
    def assert_type(res):
        assert isinstance(res['content'], _type)

    connection = None

    def on_connected(_connection):
        nonlocal connection
        connection = _connection

    obj, client_connection, server_connection = await setup_client_server(
        _class)
    try:
        await asyncio.wait_for(
            obj.__getattribute__(method)(client_connection,
                                         1,
                                         assert_type,
                                         detail=request_detail,
                                         on_connected=on_connected), 0.01)
    except asyncio.TimeoutError:
        pass
    await connection.close()
    server_connection.close()
    await server_connection.wait_closed()


@pytest.mark.asyncio
async def test_websocket_subscription_block_ids():
    return await _test_websocket_subscription(ws.BlockIdsWebsocketConnection,
                                              "subscribe_block_ids",
                                              block_identifier.BlockIdentifier)



@pytest.mark.asyncio
async def test_websocket_subscription_txs():
    return await _test_websocket_subscription(
        ws.TxsWebsocketConnection,
        "subscribe_txs",
        tx.Tx,
        request_detail={"addresses": ["0x123"]})


@pytest.mark.asyncio
async def test_websocket_unsubscribe():
    _class = ws.BlockIdsWebsocketConnection
    subscribe_method = "subscribe_block_ids"
    unsubscribe_method = "un" + subscribe_method

    ws_client_connection = None
    subscription = None
    received_events = []

    def on_subscribed(_subscription):
        nonlocal subscription
        subscription = _subscription

    def on_connected(_connection):
        nonlocal ws_client_connection
        ws_client_connection = _connection

    obj, client_connection, server_connection = await setup_client_server(
        _class)

    async def wait_then_unsubscribe():
        await asyncio.sleep(0.1)
        return await obj.__get_attribute__(unsubscribe_method)(
            client_connection, 2, 'ubiquity.block_identifiers',
            subscription['result']['subID'])

    t, pending = await asyncio.wait([
        obj.__getattribute__(subscribe_method)(
            client_connection,
            1,
            lambda ev: received_events.append(ev),
            on_subscribed=on_subscribed,
            on_connected=on_connected),
        wait_then_unsubscribe()
    ],
                                    return_when=asyncio.FIRST_COMPLETED)

    await ws_client_connection.close()
    server_connection.close()
    await server_connection.wait_closed()


if __name__ == '__main__':
    unittest.main()
