import os


class PathValidator:
    def validate_directory_path(self, path: str) -> None:
        if not isinstance(path, str):
            raise TypeError('Path must be string!')
        if not os.path.exists(path):
            raise ValueError(f'Unknown path: "{path}"!')
        if not os.path.isdir(path):
            raise ValueError(f'Path must be a directory!')
    
    def validate_file_path(self, path: str) -> None:
        if not isinstance(path, str):
            raise TypeError('Path must be string!')
        if not os.path.exists(path):
            raise ValueError(f'Unknown path: "{path}"!')
        if not os.path.isfile(path):
            raise ValueError(f'Path must be a file!')
