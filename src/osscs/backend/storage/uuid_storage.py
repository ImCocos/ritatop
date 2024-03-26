class UUIDStorage:
    def __init__(self, max_size: int) -> None:
        self.max_size = max_size
        self.uuids: list[str] = []
        self.uuids_count = 0
    
    def have(self, uuid: str) -> bool:
        return uuid in self.uuids
    
    def add(self, uuid: str) -> None:
        if uuid not in self.uuids:
            self.uuids.append(uuid)
            self.uuids_count += 1

        if self.uuids_count > self.max_size:
            del self.uuids[0]
            self.uuids_count -= 1
