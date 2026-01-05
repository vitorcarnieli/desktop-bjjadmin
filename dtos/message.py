from enums.message_type import MessageType


class Message:

    def __init__(self, type=None, payload=None):
        self.type: MessageType = type
        self.payload: str = payload
