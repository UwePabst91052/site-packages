"""
#   This file contains methods for writing
#   workpackage content to a data file
"""

indent = 0


def open_tag(file, tag):
    global indent
    file.write("  " * indent)
    file.write("<" + tag + ">\n")
    indent += 1


def close_tag(file, tag):
    global indent
    indent -= 1
    file.write("  " * indent)
    file.write("</" + tag + ">\n")


def write_tag(file, tag, content):
    global indent
    file.write("  " * indent)
    file.write("<{0}>".format(tag))
    file.write(content)
    file.write("</{0}>\n".format(tag))


def write_worktime(file, worktime):
    write_tag(file, "Begin", str(worktime.start_time))
    write_tag(file, "End", str(worktime.end_time))


def write_workday(file, workday):
    write_tag(file, "Date", str(workday.date))
    write_tag(file, "Count", "{0:d}".format(len(workday.worktimes)))
    open_tag(file, "Worktimes")
    for wt in workday.worktimes:
        write_worktime(file, wt)
    close_tag(file, "Worktimes")


def write_workpackage(file, workpackage):
    open_tag(file, "Workpackage")
    write_tag(file, "Name", workpackage.wp_name)
    write_tag(file, "Count", "{0:d}".format(len(workpackage.workdays)))
    open_tag(file, "Workdays")
    for wd in workpackage.workdays:
        write_workday(file, wd)
    close_tag(file, "Workdays")
    close_tag(file, "Workpackage")
