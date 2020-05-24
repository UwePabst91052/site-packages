import tkinter as tk
from tkinter.simpledialog import *

class ReportDialog(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.yscroll = tk.Scrollbar(self, orient=tk.VERTICAL)
        self.yscroll.grid(row=0, column=1, sticky='NS')
        self.report_list = tk.Listbox(self, width=80, height=40)
        self.report_list['font'] = ('Courier', 10)
        self.report_list['yscrollcommand'] = self.yscroll.set
        self.report_list.grid(row=0, column=0, sticky='NSEW')
        self.yscroll['command'] = self.report_list.yview

        self.grid(row=0, column=0, sticky='NEWS')

    def show_report(self, report_text):
        self.report_list.delete(0, tk.END)
        report_lines = report_text.split('\n')
        for line in report_lines:
            self.report_list.insert(tk.END, line)


class TimeSpanDialog(Dialog):
    def body(self, parent):
        self.frame1 = tk.Frame(parent)
        self.label_from = tk.Label(self.frame1, text="Datum von")
        self.label_from.pack(anchor='nw')

        self.date_begin = tk.StringVar()
        self.entry_start = tk.Entry(self.frame1, width=10)
        self.entry_start['textvariable'] = self.date_begin
        self.entry_start.pack()

        self.frame2 = tk.Frame(parent)
        self.label_til = tk.Label(self.frame2, text="Datum bis")
        self.label_til.pack(anchor='nw')

        self.date_end = tk.StringVar()
        self.entry_end = tk.Entry(self.frame2, width=10)
        self.entry_end['textvariable'] = self.date_end
        self.entry_end.pack()

        self.frame1.pack(side='left', padx=10, pady=20)
        self.frame2.pack(side='left', padx=10, pady=20)

        return self.entry_start

    def apply(self):
        self.from_date = self.date_begin.get()
        self.until_date = self.date_end.get()
        self.result = 1


def display_report(report):
    root = tk.Tk()
    root.title("Zeitnachweis Bericht")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    report_dialog = ReportDialog(root)

    report_dialog.show_report(report)

    root.mainloop()


def input_timespan(root):

    input_dialog = TimeSpanDialog(root,
                                  title="Zeitspanne eingeben")
    if input_dialog.result is not None:
        from_date = input_dialog.from_date
        til_date = input_dialog.until_date
        return from_date, til_date
    else:
        return "xx.xx.yyyy", "aa.bb.cccc"
