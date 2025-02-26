from typing import List


class BaseObject:
    @staticmethod
    def generate_id(list_of_objects: List) -> int:
        if len(list_of_objects) < 1:
            return 1
        return list_of_objects[-1].id + 1

    def __str__(self) -> str:
        return f"<{self.__class__.__name__}>"

    def __repr__(self) -> str:
        return self.__str__()
