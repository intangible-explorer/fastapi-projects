class CustomAPIException(Exception):
    def __init__(self, name: str, status_code: int):
        self.status_code = status_code
        self.name = name