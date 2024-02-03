import sender_stand_request
import data

def test_create_order():
    response_order = sender_stand_request.post_new_order()
    assert response_order.status_code == 200