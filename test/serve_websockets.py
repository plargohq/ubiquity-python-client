#!/usr/bin/env python

# WS server example

import json
import websockets

from test import mock

BLOCKS_REQUEST = json.dumps(
    {
        "id": 1,
        "method": "ubiquity.subscribe",
        "params": {
            "channel": "ubiquity.blocks"
        }
    },
    sort_keys=True)

BLOCK_IDS_REQUEST = json.dumps(
    {
        "id": 1,
        "method": "ubiquity.subscribe",
        "params": {
            "channel": "ubiquity.block_identifiers"
        }
    },
    sort_keys=True)

BLOCK_IDS_UNSUBSCRIBE_REQUEST = json.dumps(
    {
        "id": 2,
        "method": "ubiquity.unsubscribe",
        "params": {
            "channel": "ubiquity.block_identifiers",
            "subID": 1
        }
    },
    sort_keys=True)

TX_REQUEST = json.dumps(
    {
        "id": 1,
        "method": "ubiquity.subscribe",
        "params": {
            "channel": "ubiquity.txs",
            "detail": {
                "addresses": ["0x123"]
            }
        }
    },
    sort_keys=True)

MOCK_RESPONSES = {
    TX_REQUEST: mock.get_mock_file_content('websocket_api/txs.json'),
    BLOCKS_REQUEST: mock.get_mock_file_content('websocket_api/blocks.json'),
    BLOCK_IDS_REQUEST:
    mock.get_mock_file_content('websocket_api/block_ids.json'),
    BLOCK_IDS_UNSUBSCRIBE_REQUEST: mock.get_mock_file_content('websocket_api/unsubscribe_block_ids.json')
}


def get_mock_response(request_dict):
    dict_key = json.dumps(request_dict, sort_keys=True)
    if not dict_key in MOCK_RESPONSES:
        raise NotImplementedError(
            f"Mock response not found for request {dict_key}")
    return MOCK_RESPONSES[dict_key]


async def run_server(websocket, path):
    try:
        while True:
            request = await websocket.recv()
            parsed_request = json.loads(request)
            mock_responses = json.loads(get_mock_response(parsed_request))

            # iterate through list in mock response list and send each item
            for res in mock_responses:
                await websocket.send(json.dumps(res))
    except json.decoder.JSONDecodeError:
        print("Malformed JSON request!")
    except websockets.exceptions.ConnectionClosedOK:
        print("Connection closed!")
    except websockets.exceptions.ConnectionClosedError as e:
        print(
            f"Error when closing connection. code = {e.code}, reason = {e.reason}"
        )


if __name__ == "__main__":
    import asyncio
    start_server = websockets.serve(run_server, "localhost", 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
