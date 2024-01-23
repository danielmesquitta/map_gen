import os

cwd = os.getcwd()

tmp_dir = os.path.join(cwd, 'tmp')


def delete_file(file_path: str):
  if os.path.exists(file_path):
    os.remove(file_path)
