"""
 This module contains the following classes:

    - Date............represents a date
    - Time............represents a time
    - Worktime........begin, end and duration of a worktime
    - Workday.........represents a workday with a list of worktimes
    - Workpackage.....contains a list of workdays

"""
from datetime import date as dt


class Date:
    """ This class gets a date string as input splits it and
        stores its components as integer values"""

    def __init__(self, str_date):
        self.daysOfMonth = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        self.day = 0
        self.month = 0
        self.year = 2021
        self.days = 0
        self.is_valid = False
        self.weekday = 0
        self.validate(str_date)

    def validate(self, date):
        """splits the incoming string into its components and validates them"""
        splitted = date.split('.')
        count = len(splitted)
        if count >= 2:
            self.day = int(splitted[0])
            if self.day in range(1, 32):
                self.month = int(splitted[1])
                if self.month in range(1, 13):
                    self.is_valid = True
            if count == 3:
                self.year = int(splitted[2])
        self.days = self.year * 365 + self.daysOfMonth[self.month] + self.day
        self.weekday = dt(self.year, self.month, self.day).weekday()

    def __str__(self):
        if self.is_valid:
            str_out = "{0:02d}.{1:02d}.{2:02d}".format(self.day, self.month, self.year)
        else:
            str_out = "Erwartetes Format: dd.mm.yyyy"
        return str_out

    def __eq__(self, other):
        date = Date(other)
        isequal = False
        if self.day == date.day:
            if self.month == date.month:
                if self.year == date.year:
                    isequal = True
        return isequal

    def __ne__(self, other):
        date = Date(other)
        isnotequal = True
        if self.day == date.day:
            if self.month == date.month:
                if self.year == date.year:
                    isnotequal = False
        return isnotequal

    def __le__(self, other):
        date = Date(other)
        return self.days <= date.days

    def __ge__(self, other):
        date = Date(other)
        return self.days >= date.days

    def __lt__(self, other):
        return self.days < other.days

    def __gt__(self, other):
        date = Date(other)
        isgreater = True
        if self.year <= date.year:
            if self.month > date.month:
                if self.day > date.day:
                    isnotequal = False
        return isgreater

class Time:
    """ This class gets a time string splits it to its components
        and stores them as integer values"""
    def __init__(self, str_time):
        self.hour = 0
        self.minute = 0
        self.second = 0
        self.is_valid = False
        self.validate(str_time)

    def validate(self, time):
        """splits the incoming string into its components and validates them"""
        splitted = time.split(':')
        count = len(splitted)
        if count >= 2:
            self.hour = int(splitted[0])
            if self.hour in range(0, 24):
                self.minute = int(splitted[1])
                if self.minute in range(0, 60):
                    if count == 3:
                        self.second = 0
                    self.is_valid = True

    def __str__(self):
        if self.is_valid:
            str_out = "{0:02d}:{1:02d}".format(self.hour, self.minute)
        else:
            str_out = "Erwartetes Format: hh.mm"
        return str_out

    def __ne__(self, other):
        time = Time(other)
        isnequal = True
        if self.hour == time.hour:
            if self.minute == time.minute:
                if self.second == time.second:
                    isnequal = False
        return isnequal

    def __eq__(self, other):
        time = Time(other)
        isequal = False
        if self.hour == time.hour:
            if self.minute == time.minute:
                if self.second == time.second:
                    isequal = True
        return isequal

    @staticmethod
    def convert_seconds_to_time_string(seconds):
        negative = seconds < 0
        if negative:
            seconds *= -1
        seconds //= 60
        minute = seconds % 60
        hour = seconds // 60
        if negative:
            time_str = "-{0:02d}:{1:02d}".format(hour, minute)
        else:
            time_str = "{0:02d}:{1:02d}".format(hour, minute)
        return time_str

    def get_seconds(self):
        """ returns the time converted to seconds"""
        sec = self.hour * 3600
        sec += self.minute * 60
        sec += self.second
        return sec

    def set_seconds(self, seconds):
        """ converts the incoming seconds to a time"""
        self.second = 0
        seconds //= 60
        self.minute = seconds % 60
        self.hour = seconds // 60

    seconds = property(get_seconds, set_seconds)


class Worktime:
    """
    This class describes a timespan that someone worked for

    Members:
        start_time      work for workpackage begins
        end_time        work for workpackage ends
    """
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def set_start_time(self, time):
        self.start_time = Time(time)

    def set_end_time(self, time):
        self.end_time = Time(time)

    def get_duration(self):
        """ returns the difference between start and end time in seconds """
        sec_start = self.start_time.get_seconds()
        sec_end = self.end_time.get_seconds()
        if sec_start <= sec_end:
            return sec_end - sec_start
        else:
            return 0

    def __str__(self):
        str_out = "{1} {0} {2}".format(str(self.end_time), str(self.start_time), self.get_duration_str())
        return str_out

    def get_duration_str(self):
        """ returns the difference between start and end time in time format """
        duration = self.get_duration()
        duration //= 60
        minute = duration % 60
        hour = duration // 60
        str_out = "{0:02d}:{1:02d}".format(hour, minute)
        return str_out


class Workday:
    """
    This class collects all worktimes for a workday and provides the summarized worktime

    Members:
        date            workdays date
        cur_worktime    current worktime object
        sum_duration    summarization of all worktimes for this day
        worktimes       list of worktime objects
        is_running      start time is entered but end time is still missing
    """
    daily_sum_str = "|               Tages-Summation                    {0}                    |"

    def __init__(self, date_str):
        self.date = Date(date_str)
        self.cur_worktime = None
        self.sum_duration = 0
        self.worktimes = []
        self.is_running = False

    def begin_working(self, time_str):
        self.cur_worktime = None
        self.cur_worktime = Worktime()
        self.cur_worktime.set_start_time(time_str)
        self.is_running = True

    def finish_worktime(self, time_str):
        if self.cur_worktime is not None:
            self.cur_worktime.set_end_time(time_str)
            self.is_running = False
            self.worktimes.append(self.cur_worktime)
        else:
            print("Sie haben noch keinen Beginn eingeben")

    def add_worktime(self, new_worktime):
        """ This method allows to add a worktime without using the begin.. and finish.. methods """
        self.worktimes.append(new_worktime)
        self.correct_list()

    def delete_worktime(self, index):
        """ This method deletes the worktime addressed by the given index from list """
        del self.worktimes[index]

    def change_cur_worktime(self, with_worktime):
        """ This method allows to change the current worktime"""
        self.cur_worktime = with_worktime

    def correct_list(self):
        """ This method sorts the worktime list in ascending order and corrects time conflicts """
        if len(self.worktimes) == 0:
            return
        # first sort list ascendent
        self.worktimes.sort(key=lambda wt: wt.start_time.seconds)

        # then check consistency
        count = len(self.worktimes)
        for ix in range(0, count - 1):
            end_time_cur = self.worktimes[ix].end_time.seconds
            start_time_next = self.worktimes[ix + 1].start_time.seconds
            if end_time_cur > start_time_next:
                self.worktimes[ix].end_time.seconds = start_time_next

        # then update current worktime with last worktime from list
        self.cur_worktime = self.worktimes[count - 1]

    def get_duration(self):
        """ returns the summarized worktime of the workday in seconds """
        self.sum_duration = 0
        for wt in self.worktimes:
            self.sum_duration += wt.get_duration()
        return self.sum_duration

    def get_workday_balance(self):
        self.sum_duration = self.get_duration()
        if (self.date > "28.02.2021"):
            daily_hours = 8 * 3600
        else:
            daily_hours = 7 * 3600
        if self.date.weekday == 5:
            return self.sum_duration
        else:
            if self.sum_duration >= daily_hours:
                return self.sum_duration - daily_hours
            else:
                return 0 - daily_hours + self.sum_duration

    def get_duration_str(self):
        """ returns the summarized worktime of the workday in time format """
        duration = self.get_duration()
        str_out = Time.convert_seconds_to_time_string(duration)
        return str_out

    def __str__(self):
        self.correct_list()
        str_out = "| {0}      ".format(str(self.date))
        first_line = True
        for wt in self.worktimes:
            if not first_line:
                str_out += "|                 "
            else:
                first_line = False
            str_out += "| {0} | {1} |          {2}                    |\n".format(
                wt.start_time, wt.end_time, wt.get_duration_str())
        str_out += self.daily_sum_str.format(self.get_duration_str()) + "\n"
        return str_out


class Workpackage:
    """
    This class collects the workdays for one workpackage
    Members
        wp_name         workpackage name
        cur_workday     current workday
        workdays        list of workday
    """
    def __init__(self, wp_name):
        self.wp_name = wp_name
        self.cur_workday = None
        self.workdays = []

    def add_workday(self, date_str):
        """ adds a new workday if it not yet exists, and sets the current workday to the passed date"""
        self.cur_workday = None
        for wd in self.workdays:
            if wd.date == date_str:
                self.cur_workday = wd
        if self.cur_workday is None:
            self.cur_workday = Workday(date_str)
            self.workdays.append(self.cur_workday)

    def begin_working(self, time_str):
        if self.cur_workday is not None:
            try:
                self.cur_workday.begin_working(time_str)
            except ValueError:
                print("ValueError on date {0} and time {1}".format(self.cur_workday.date, time_str))
        else:
            print("You have to enter a workday, first!")

    def finish_working(self, time_str):
        if self.cur_workday is not None:
            self.cur_workday.finish_worktime(time_str)
        else:
            print("You have to enter a workday, first!")

    def sort_workdays(self):
        self.workdays.sort(key=lambda wd: wd.date)

    def __str__(self):
        wp_duration = 0
        for wd in self.workdays:
            wp_duration += wd.get_duration()
        str_out = Time.convert_seconds_to_time_string(wp_duration)
        return str_out

    def __eq__(self, other):
        return other == self.wp_name

    def get_wpckg_duration_str(self, from_date, until_date):
        wp_duration = 0
        for wd in self.workdays:
            if from_date <= wd.date <= until_date:
                wp_duration += wd.get_duration()
        str_out = Time.convert_seconds_to_time_string(wp_duration)
        return self.wp_name, str_out

    def get_wpckg_duration_for_date(self, date_str):
        wd_duration = 0
        for wd in self.workdays:
            if wd.date == date_str:
                wd_duration += wd.get_duration()
        return wd_duration

    def duration_for_date(self, date_str):
        print("Für \"{0}\" haben Sie ".format(self.wp_name, date_str), end="")
        wd_duration = 0
        for wd in self.workdays:
            if wd.date == date_str:
                wd_duration += wd.get_duration()
        print("{0} gearbeitet".format(Time.convert_seconds_to_time_string(wd_duration)))

    def get_workpackage_balance(self, from_date, til_date):
        wp_balance = 0
        for wd in self.workdays:
            if from_date <= wd.date <= til_date:
                wp_balance += wd.get_workday_balance()
        return wp_balance

    def delete_workdays_wo_worktimes(self):
        for wd in self.workdays:
            if len(wd.worktimes) == 0:
                self.workdays.remove(wd)
