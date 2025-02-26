from typing import List, Optional

from base_module import BaseObject


class User(BaseObject):
    list_of_users: List = []

    def __init__(self, email: str, password: str) -> None:
        self.__id = self.generate_id(User.list_of_users)
        self.__email = email
        self.__password = password
        self.__is_logged_in = False
        User.list_of_users.append(self.to_dict())

    @property
    def id(self) -> int:
        return self.__id

    @property
    def email(self) -> str:
        return self.__email

    @property
    def is_logged_in(self) -> bool:
        return self.__is_logged_in

    @is_logged_in.setter  # type: ignore
    def is_logged_in(self, value: bool) -> None:
        self.__is_logged_in = value

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "email": self.email,
            "is_logged_in": self.is_logged_in
        }



class Profile(BaseObject):
    list_of_profiles: List = []

    def __init__(
        self, 
        user: User, 
        first_name: str, 
        last_name: str, 
        sex: str, 
        age: int, 
        bio: Optional[str] = None
    ) -> None:
        self.__id = self.generate_id(Profile.list_of_profiles)
        self.__user = user
        self.__first_name = first_name
        self.__last_name = last_name
        self.__sex = sex
        self.__age = age
        self.__bio = bio
        Profile.list_of_profiles.append(self.to_dict())

    @property
    def id(self) -> int:
        return self.__id

    @property
    def user(self) -> dict:
        return self.__user.to_dict()

    @property
    def first_name(self) -> str:
        return self.__first_name

    @property
    def last_name(self) -> str:
        return self.__last_name

    @property
    def sex(self) -> str:
        return self.__sex

    @property
    def age(self) -> int:
        return self.__age

    @property
    def bio(self) -> Optional[str]:
        return self.__bio

    @first_name.setter  # type: ignore
    def first_name(self, value: str) -> None:
        self.__first_name = value

    @last_name.setter  # type: ignore
    def last_name(self, value: str) -> None:
        self.__last_name = value

    @sex.setter  # type: ignore
    def sex(self, value: str) -> None:
        self.__sex = value

    @age.setter  # type: ignore
    def age(self, value: int) -> None:
        self.__age = value

    @bio.setter  # type: ignore
    def bio(self, value: Optional[str]) -> None:
        self.__bio = value

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "user": self.user,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "sex": self.sex,
            "age": self.age,
            "bio": self.bio
        }
