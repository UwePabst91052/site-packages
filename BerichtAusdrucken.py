"""
This file contains functions for printing time statement reports.

There are two types of reports:
     - Summary report on which days work was carried out for which work packages
     - Summary report how much was worked on which days for a work package
"""

# import Workpackage as Wp

frame_seperator = "--------------------------------------------------------------------------------\n"
line_seperator = "|------------------------------------------------------------------------------|\n"
empty_line = "|                                                                              |\n"
table_header = "|   Tag           |  Beginn  |   Ende   |               Gesamt                 |\n"
text_output = ""
line_width = 80
single_col_cfg = (17, 10, 10, 38)
day_col_cfg = (37, 38)
sum_col_cfg = (57, 20)


def create_work_dictionary(workpackages):
    report = {}
    for wp in workpackages:
        for wd in wp.workdays:
            key = str(wd.date)
            value = [wp]
            if key in report:
                report[key] += value
            else:
                report.update({key: value})
    return report


def report_work_summary(employee_name, workpackages):
    """ starts the print process bay calling sub functions """
    global text_output
    # create dictonary
    report = create_work_dictionary(workpackages)

    # print report header
    keylist = list(report.keys())
    from_date = keylist[0]
    until_date = keylist[len(keylist) - 1]
    evaluation_period = "Auswertungszeitraum vom {0} bis {1}".format(from_date, until_date)
    print_report_header(employee_name, evaluation_period)

    # print all worktimes sorted by date and workpackage
    text_output += "\n"
    print_single_worktimes(workpackages)

    # print the summary of all worktimes sorted by workpackages
    text_output += "\n"
    print_worktime_summary(workpackages)

    return text_output


def create_workday_dictionary(date, workpackeges):
    report = {}
    for wp in workpackeges:
        for wd in wp.workdays:
            if date == str(wd.date):
                key = wp.wp_name
                value = (wd.worktimes, wd.get_duration_str())
                report.update({key: value})
    return report


def report_workday_summary(date, workpackages):
    """ starts the print process for displaying all workpackeges for a specific day """
    global text_output
    text_output = ""
    print_report_title("Zeitnachweis Arbeitstag")
    print_report_subject("Berichtsdatum:  {0}".format(date))
    wp_dict = create_workday_dictionary(date, workpackages)
    print_workday_worktimes(date, wp_dict)
    return text_output


def report_workpackage_summary(wp_name, workpackages):
    """ starts the print process for displaying all worktimes for a specific workpackage """
    global text_output
    text_output = ""
    print_report_title("Zeitnachweis Arbeitspaket")
    print_report_subject("Arbeitspaket:  {0}".format(wp_name))
    for wp in workpackages:
        if wp.wp_name == wp_name:
            print_workpackage_worktimes(wp)
            print_workpackage_summary(wp)
    return text_output


def print_report_header(employee_name, evaluation_period):
    print_report_title("Zeitnachweisliste")
    print_report_subject("Mitarbeiter:  {0}".format(employee_name))
    print_report_foot(evaluation_period)


def create_table_row(col_cfg, row, col, text, align):
    col_width = col_cfg[col]
    text_len = len(text)
    if align == 'left':
        row += text
        row += " " * (col_width - text_len - 1)
    else:
        pre_blanks = col_width // 2 - text_len // 2
        after_blanks = col_width - text_len - pre_blanks
        row += " " * pre_blanks + text + " " * after_blanks
    return row


def print_single_worktimes(workpackages):
    global text_output
    print_report_title("Einzelergebnisse")
    row = ""
    for wp in workpackages:
        print_report_subject("Arbeitspaket:  {0}".format(wp.wp_name))
        text_output += table_header + frame_seperator
        for wd in wp.workdays:
            text = str(wd.date)
            row = create_table_row(single_col_cfg, row, 0, text, 'left')
            row += "|"
            count_wt = len(wd.worktimes)
            if count_wt == 0:
                continue
            for wt in wd.worktimes:
                if count_wt > 1 and len(row) == 0:
                    row = create_table_row(single_col_cfg, row, 0, "", 'left')
                    row += "|"
                wt_strings = str(wt).split(" ", 3)
                row = create_table_row(single_col_cfg, row, 1, wt_strings[0], 'center')
                row += "|"
                row = create_table_row(single_col_cfg, row, 2, wt_strings[1], 'center')
                row += "|"
                row = create_table_row(single_col_cfg, row, 3, wt_strings[2], 'center')
                text_output += print_layout_justify(row, 'left')
                row = ""
            row = create_table_row(day_col_cfg, row, 0, "Tages-Summation:", 'center')
            row += " "
            row = create_table_row(day_col_cfg, row, 1, wd.get_duration_str(), 'center')
            text_output += print_layout_justify(row, 'center')
            row = ""
        text_output += frame_seperator


def print_workday_worktimes(date, wp_dict):
    global text_output
    row = ""
    for item in wp_dict.items():
        wp_name, wt_item = item
        wt_list, duration = wt_item
        print_report_subject("Arbeitspaket:  {0}".format(wp_name))
        text_output += table_header + line_seperator
        row = create_table_row(single_col_cfg, row, 0, date, 'left')
        row += "|"
        count_wt = len(wt_list)
        if count_wt == 0:
            continue
        for wt in wt_list:
            if count_wt > 1 and len(row) == 0:
                row = create_table_row(single_col_cfg, row, 0, "", 'left')
                row += "|"
            wt_strings = str(wt).split(" ", 3)
            row = create_table_row(single_col_cfg, row, 1, wt_strings[0], 'center')
            row += "|"
            row = create_table_row(single_col_cfg, row, 2, wt_strings[1], 'center')
            row += "|"
            row = create_table_row(single_col_cfg, row, 3, wt_strings[2], 'center')
            text_output += print_layout_justify(row, 'left')
            row = ""
        row = create_table_row(day_col_cfg, row, 0, "Tages-Summation:", 'center')
        row += " "
        row = create_table_row(day_col_cfg, row, 1, duration, 'center')
        text_output += print_layout_justify(row, 'center')
        text_output += line_seperator
        row = ""
        
        
def print_workpackage_worktimes(wp):
    global text_output
    row = ""
    for wd in wp.workdays:
        text = str(wd.date)
        row = create_table_row(single_col_cfg, row, 0, text, 'left')
        row += "|"
        count_wt = len(wd.worktimes)
        if count_wt == 0:
            continue
        for wt in wd.worktimes:
            if count_wt > 1 and len(row) == 0:
                row = create_table_row(single_col_cfg, row, 0, "", 'left')
                row += "|"
            wt_strings = str(wt).split(" ", 3)
            row = create_table_row(single_col_cfg, row, 1, wt_strings[0], 'center')
            row += "|"
            row = create_table_row(single_col_cfg, row, 2, wt_strings[1], 'center')
            row += "|"
            row = create_table_row(single_col_cfg, row, 3, wt_strings[2], 'center')
            text_output += print_layout_justify(row, 'left')
            row = ""
        row = create_table_row(day_col_cfg, row, 0, "Tages-Summation:", 'center')
        row += " "
        row = create_table_row(day_col_cfg, row, 1, wd.get_duration_str(), 'center')
        text_output += print_layout_justify(row, 'center')
        row = ""
    text_output += frame_seperator


def print_worktime_summary(workpackages):
    global text_output
    print_report_title("Summenübersicht")
    row = ""
    row = create_table_row(sum_col_cfg, row, 0, "Arbeitspaket", 'left')
    row += "| "
    row = create_table_row(sum_col_cfg, row, 1, "Summe", 'left')
    text_output += print_layout_justify(row, 'center')
    text_output += frame_seperator
    for wp in workpackages:
        name, duration = wp.get_wpckg_duration_str()
        row = ""
        row = create_table_row(sum_col_cfg, row, 0, name, 'left')
        row += "| "
        row = create_table_row(sum_col_cfg, row, 1, duration, 'left')
        text_output += print_layout_justify(row, 'center')
    text_output += frame_seperator


def print_workpackage_summary(workpackage):
    global text_output
    print_report_title("Summe Arbeitspaket")
    row = ""
    # text_output += frame_seperator
    name, duration = workpackage.get_wpckg_duration_str()
    row = ""
    row = create_table_row(sum_col_cfg, row, 0, name, 'left')
    row += "| "
    row = create_table_row(sum_col_cfg, row, 1, duration, 'left')
    text_output += print_layout_justify(row, 'center')
    text_output += frame_seperator


def print_layout_justify(text, align):
    line = empty_line[:]
    text_len = len(text)
    if align == 'left':
        start_pos = 2
    else:
        start_pos = line_width // 2 - text_len // 2
    end_pos = start_pos + text_len
    line_parts = list(line[:start_pos])
    line_parts.append(text)
    line_parts.append(line[end_pos:])
    return "".join(line_parts)


def print_report_title(title):
    global text_output
    text_output += frame_seperator
    text_output += print_layout_justify(title, 'center')
    text_output += line_seperator


def print_report_subject(subject):
    global text_output
    text_output += print_layout_justify(subject, 'left')
    text_output += line_seperator


def print_report_foot(text):
    global text_output
    text_output += print_layout_justify(text, align='center')
    text_output += frame_seperator
