from module import Screenshot
import customtkinter as tk
from Module.Modulev2 import HandTracking

class GUI:
    def __init__(self):
        tk.set_appearance_mode("dark")
        tk.set_default_color_theme("green")

        self.root = tk.CTk()
        self.root.geometry("400x500")

        self.label = tk.CTkLabel(
            master=self.root, text="Handtracking", font=('Arial', 25))
        self.label.place(relx=0.06, rely=0.05)

        self.switch_var = tk.StringVar(value="off")
        self.switch = tk.CTkSwitch(master=self.root, command=self.switch_event, text="",
                                   variable=self.switch_var, onvalue="on", offvalue="off")
        self.switch.place(relx=0.8, rely=0.057)

        self.check_var = tk.StringVar(value="off")
        self.checkbox = tk.CTkCheckBox(master=self.root, text="Screenshot", command=self.checkbox_event,
                                       variable=self.check_var, onvalue="on", offvalue="off", font=('Arial', 17))
        self.checkbox.place(relx=0.06, rely=0.2)

        self.handtracker = HandTracking()
        self.screenshot = Screenshot(self.handtracker)

        self.root.mainloop()

    def switch_event(self):
        if self.switch_var.get() == 'on':
            self.handtracker.start()
        else:
            self.handtracker.stop()

    def checkbox_event(self):
        if self.check_var.get() == 'on':
            self.screenshot.start()
        else:
            self.screenshot.stop()


if __name__ == '__main__':
    GUI()
