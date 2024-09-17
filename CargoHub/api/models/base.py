from datetime import datetime

class Base:
    def __init__():
        pass

    # This function returns now in the ISO 8601 format
    def get_timestamp(self):
        return datetime.utcnow().isoformat() + "Z"