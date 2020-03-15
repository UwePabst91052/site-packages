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


def display_report(report):
    root = tk.Tk()
    root.title("Zeitnachweis Bericht")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    report_dialog = ReportDialog(root)

    report_dialog.show_report(report)

    root.mainloop()
