import tkinter as tk


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


class TimeSpanDialog(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.label_from = tk.Label(self, text="Datum von")
        self.label_from.grid(row=0,column=0)
        self.label_til = tk.Label(self, text="Datum bis")
        self.label_til.grid(row=0, column=1)

        self.date_begin = tk.StringVar()
        self.entry_start = tk.Entry(self, width=15)
        self.entry_start['textvariable'] = self.date_begin
        self.entry_start.grid(row=1, column=0)
        self.date_end = tk.StringVar()
        self.entry_end = tk.Entry(self, width=15)
        self.entry_end['textvariable'] = self.date_end
        self.entry_end.grid(row=1, column=1)

        self.grid(row=0, column=0, sticky='NEWS')


def display_report(report):
    root = tk.Tk()
    root.title("Zeitnachweis Bericht")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    report_dialog = ReportDialog(root)

    report_dialog.show_report(report)

    root.mainloop()


def input_timespan():
    root = tk.Tk()
    root.title("Eingabe der Zeitspanne")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    input_dialog = TimeSpanDialog(root)

    root.mainloop()
    from_date = input_dialog.date_begin.get()
    til_date = input_dialog.date_end.get()
    return from_date, til_date
