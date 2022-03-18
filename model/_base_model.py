class BaseModel:

    def to_dict(self) -> dict:
        dict = self.__dict__.copy()
        return dict