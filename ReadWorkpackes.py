"""
#   This file contains methods for reading
#   workpackage content from a data file
"""

import Workpackage as Wp


def read_workpackages(file):
    workpackages = []
    cur_wp = None
    check_worktimes = False
    for line in file:
        line = line.strip()
        if line == "</Workpackage>":
            cur_wp.sort_workdays()
            workpackages.append(cur_wp)
        elif "<Name>" in line:
            name = get_tag_content(line)
            cur_wp = Wp.Workpackage(name)
        elif "<Date>" in line:
            date = get_tag_content(line)
            check_worktimes = True
        elif ("<Count>" in line) and check_worktimes:
            count = int(get_tag_content(line))
            if count > 0:
                cur_wp.add_workday(date)
            check_worktimes = False
        elif "<Begin>" in line:
            time = get_tag_content(line)
            cur_wp.begin_working(time)
        elif "<End>" in line:
            time = get_tag_content(line)
            cur_wp.finish_working(time)
    return workpackages


def get_tag_content(line):
    line = line.strip('<>')
    line = line.replace('>', ';')
    line = line.replace('</', ';')
    splitted = line.split(';')
    return splitted[1]
