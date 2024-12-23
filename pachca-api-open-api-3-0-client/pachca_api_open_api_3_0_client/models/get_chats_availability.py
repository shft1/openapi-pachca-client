from enum import Enum


class GetChatsAvailability(str, Enum):
    IS_MEMBER = "is_member"
    PUBLIC = "public"

    def __str__(self) -> str:
        return str(self.value)
