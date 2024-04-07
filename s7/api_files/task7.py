from pathlib import Path
from os import chdir

"""
Седьмое задание семинара, функция, которая сортирует файлы по директории: видео, изображение, текст и т.п.
Каждая группа включает файлы с несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки
"""


def sort_files(path: str | Path, groups: dict[Path, list[str]] = None) -> None:
    chdir(path)
    if groups is None:
        groups = {Path('video'): ['avi', 'mp4', 'mkv', 'mov'],
                  Path('image'): ['jpg', 'jpeg', 'png', 'bmp', 'gif'],
                  Path('text'): ['txt', 'rtf', 'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx'],
                  Path('audio'): ['mp3', 'wav', 'aac', 'flac', 'wma', 'ogg', 'aac', 'aac']
                  }
    reverse_groups = {}

    for directory, extension_list in groups.items():
        if not directory.is_dir():
            directory.mkdir()
        for extension in extension_list:
            reverse_groups[f'.{extension}'] = directory

    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)


if __name__ == '__main__':
    sort_files(Path().cwd())
