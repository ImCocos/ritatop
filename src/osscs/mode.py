class BaseMode:
    mode_name: str
    def __str__(self) -> str:
        return f'Mode({self.mode_name})'

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, self.__class__):
            raise NotImplemented
        return self.mode_name == other.mode_name

class SystemMode(BaseMode):
    def __init__(self) -> None:
        self.mode_name = 'system'

class PrivateMode(BaseMode):
    def __init__(self) -> None:
        self.mode_name = 'private'

class PublicMode(BaseMode):
    def __init__(self) -> None:
        self.mode_name = 'public'
