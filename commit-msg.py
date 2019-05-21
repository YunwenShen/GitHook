#! /usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import re

pattern = re.compile("^(feat|fix|polish|docs|style|refactor|perf|test|workflow|ci|chore|types)(\(.+\))?: .{1,50}")


def validate_commit_msg(msg: str):
    """
    校验git commit 内容格式是否满足要求
    :param msg:
    :return: void
    """

    if msg.startswith("Revert"):
        sys.exit(0)
    elif msg.startswith("Merge"):
        sys.exit(0)
    elif re.match(pattern, msg):
        sys.exit(0)
    else:
        print("invalid commit format")
        sys.exit(1)


if __name__ == "__main__":
    file_name = sys.argv[1]
    print(file_name)
    commit_msg = ""
    with open(file_name, encoding="utf-8") as file:
        for line in file.readlines():
            commit_msg += line
    validate_commit_msg(commit_msg)
