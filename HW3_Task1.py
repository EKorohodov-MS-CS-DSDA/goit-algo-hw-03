# Recursion. Homework 3. Task 1.
from pathlib import Path
import shutil
import sys

DEFAULT_TARGET_FOLDER = Path("dist")

def copy_file(source: Path, destination: Path) -> None:
    if source.is_file():
        destination_path = destination / source.suffix[1:]
        if not destination_path.exists():
            destination_path.mkdir(parents=True, exist_ok=True)

        destination_file = destination_path / source.name
        copy_counter = 1
        while destination_file.exists():
            destination_file = destination_path / f"{source.stem}_{copy_counter}{source.suffix}"
            copy_counter += 1

        shutil.copy2(source, destination_file)


def copy_source(source: Path, destination: Path) -> None:
    if source.is_dir():
        children = sorted(source.iterdir(), key=lambda x: (x.is_file(), x.name))

        for child in children:
            copy_source(child, destination)
    else:
        copy_file(source, destination)


def validate_paths(source: Path, destination: Path) -> None:
    if not source.is_dir():
        raise ValueError(f"The source path {source} is not a directory")
    if not destination.is_dir():
        destination.mkdir(parents=True, exist_ok=True)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 HW3_Task1.py <source directory> <destination directory>")
        sys.exit(1)

    source_dir = Path(sys.argv[1])
    destination_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_TARGET_FOLDER
    validate_paths(source_dir, destination_dir)
    copy_source(source_dir, destination_dir)

if __name__ == '__main__':
    main()
