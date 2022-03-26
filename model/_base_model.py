import json


class BaseModel:

    def to_dict(self) -> dict:
        dict = self.__dict__.copy()
        return dict

    def to_json(self) -> str:
        return json.dumps(self.__dict__.copy())
