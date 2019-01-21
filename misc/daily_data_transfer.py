# -*- coding:utf-8 -*-
# @Author: Niccolò Bonacchi
# @Date: Wednesday, January 16th 2019, 2:03:59 pm
# @Last Modified by: Niccolò Bonacchi
# @Last Modified time: 16-01-2019 02:04:01.011
import datetime
import shutil
import sys
from pathlib import Path
from folders import find_subjects_folder
from ibllib.io.raw_data_loaders import read_flag_file


def main(local_folder: str, remote_folder: str, day: str = None) -> None:
    if day is None:
        day = datetime.datetime.now().date().isoformat()

    local_folder = find_subjects_folder(local_folder)
    remote_folder = find_subjects_folder(remote_folder)

    src_session_paths = [x.parent for x in local_folder.rglob("transfer_me.flag")]

    # Create all dst paths
    dst_session_paths = []
    for s in src_session_paths:
        mouse = s.parts[-3]
        date = s.parts[-2]
        sess = s.parts[-1]
        d = remote_folder / mouse / date / sess
        dst_session_paths.append(d)

    for src, dst in zip(src_session_paths, dst_session_paths):
        flag = read_flag_file(src / "transfer_me.flag")
        if isinstance(flag, list):
            raise NotImplementedError
        else:
            shutil.copytree(src, dst)


if __name__ == "__main__":
    # local_folder = "/home/nico/Projects/IBL/IBL-github/iblrig/scratch/test_iblrig_data"
    # remote_folder = "/home/nico/Projects/IBL/IBL-github/iblrig/scratch/test_iblrig_data_on_server"
    if len(sys.argv == 3):
        main(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
