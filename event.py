from datetime import datetime
from flask import abort, make_response


def get_timestamp():
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')


EVENT = {
    "5000": {
        'event_id': '5000',
        'event_title': 'MPS',
        'event_description': 'descricao',
        'event_date': '9/10/2023 18:00:00',
        'user_id': '1000',
        'timestamp': get_timestamp()
    }
}


def read_all():
    return list(EVENT.values())


def create(event):
    event_id = event.get('event_id')
    event_title = event.get('event_title', '')
    event_description = event.get('event_description')
    event_date = event.get('event_date')
    user_id = event.get('user_id')

    if event_id and event_id not in EVENT:
        EVENT[event_id] = {
            'event_id': event_id,
            'event_title': event_title,
            'event_description': event_description,
            'event_date': event_date,
            'user_id': user_id,
            'timestamp': get_timestamp()
        }
        return EVENT[event_id], 201
    else:
        abort(
            406,
            f'user with last name {event_id} already exists',
        )


def read_one(event_id):
    if event_id in EVENT:
        return EVENT[event_id]
    else:
        abort(404, f'Event not found')


def update(event_id, event):
    if event_id in EVENT:
        EVENT[event_id]["event_title"] = event.get("event_title", EVENT[event_id]["event_title"])
        EVENT[event_id]["event_description"] = event.get("event_description", EVENT[event_id]["event_description"])
        EVENT[event_id]["timestamp"] = get_timestamp()
        return EVENT[event_id]
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )


def delete(event_id):
    if event_id in EVENT:
        del EVENT[event_id]
        return make_response(
            f"{event_id} successfully deleted", 200
        )
    else:
        abort(
            404,
            f"Event with ID {event_id} not found"
        )
