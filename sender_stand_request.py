import configuration
import requests
import data


def post_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)

response_track = post_new_order()
order_track = response_track.json()["track"]

def post_new_order():
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + '?t=' + str(order_track))