import tkinter as tk
import customtkinter as ctk

ctk.set_default_color_theme('blue')
ctk.set_appearance_mode('light')


class App(ctk.CTk):
    def __init__(self, start_size: tuple, title: str):
        super().__init__()

        self.title(title)
        self.geometry(f'{start_size[0]}x{start_size[1]}')

        # Configure the Layout of the App
        self.columnconfigure(1, weight=1)
        self.columnconfigure((2, 3), weight=0)
        self.rowconfigure(0, weight=1)

        # Place the Left Frame
        self.left_frame = left_frame(self, width=140)
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        self.main_frame = main_frame(self)
        self.main_frame.grid(row=0, column=1, sticky='nswe')

        self.mainloop()


class left_frame(ctk.CTkFrame):
    def __init__(self, master, width):
        super().__init__(master, width=width)
        self.configure(corner_radius=0)

        # Row Configure Grid Layout
        self.rowconfigure((0, 1), weight=1)

        # Top Frame
        self.top = ctk.CTkFrame(self, fg_color='transparent', width=140)
        self.top_frame(self.top)
        self.top.grid(row=0, column=0, sticky='nswe')

        # Bottom Frame
        self.bottom = ctk.CTkFrame(self, fg_color='transparent', width=140)
        self.bottom_frame(self.bottom)
        self.bottom.grid(row=1, column=0, sticky='nswe')

    def top_frame(self, frame):
        # Widgets
        self.title_label = ctk.CTkLabel(frame, text='Custom Tkinter')
        self.title_label.pack(padx=20, pady=(20, 10))

        self.button1 = ctk.CTkButton(frame, text='CTk Button', height=30)
        self.button1.pack(padx=20, pady=10)

        self.button2 = ctk.CTkButton(frame, text='CTk Button', height=30)
        self.button2.pack(padx=20, pady=10)

        self.button3 = ctk.CTkButton(frame, text='Disabled CTk Button', state='disabled', height=30)
        self.button3.pack(padx=20, pady=10)

    # Method for the Option Menu

    def print_choice(self):
        print(self.ui_scaling_var)

    def print_appearance(self):
        print(self.appearance_var)

    def bottom_frame(self, frame):
        # Label for Appearance
        self.appearance_title = ctk.CTkLabel(frame, text='Appearance Mode: ')

        # Option Menu for Appearance
        list_appearance = ['Light', 'Dark', 'System']
        self.appearance_var = ctk.StringVar(value='Light')
        self.appearance_menu = ctk.CTkOptionMenu(frame, values=list_appearance,
                                                 variable=self.appearance_var)

        # Label for Scaling
        self.scaling_title = ctk.CTkLabel(frame, text='UI Scaling: ')

        # Option Menu for Scaling
        scaling_list = ['80%', '90%', '100%', '110%', '120%']
        self.ui_scaling_var = ctk.StringVar(value='100%')
        self.ui_scaling_menu = ctk.CTkOptionMenu(frame, values=scaling_list,
                                                 variable=self.ui_scaling_var)

        # Packing the widgets
        self.ui_scaling_menu.pack(side='bottom', padx=20, pady=(5, 20))
        self.scaling_title.pack(side='bottom', padx=20, pady=5)
        self.appearance_menu.pack(side='bottom', padx=20, pady=5)
        self.appearance_title.pack(side='bottom', padx=20, pady=5)


class main_frame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master)

        self.configure(fg_color='transparent')

        self.columnconfigure(0, weight=1)
        self.columnconfigure((1, 2), weight=0)
        self.rowconfigure((0, 1), weight=1)
        self.rowconfigure(2, weight=0)

        # Text Box
        self.text_box = ctk.CTkTextbox(self)
        self.text_box.grid(row=0, column=0, sticky='nsew', padx=(20, 0), pady=(20, 10))
        self.text_box.insert('0.0', 'Hello World\n\n' * 100)

        # Tab View
        self.tab_view = ctk.CTkTabview(self, width=250)
        self.tab_view.grid(row=0, column=1, sticky='nswe', padx=20, pady=(20, 10))

        tab1 = self.tab_view.add('CTkTabview')
        self.option_menus(tab1)

        tab2 = self.tab_view.add('Tab 2')
        self.label_tab2 = ctk.CTkLabel(tab2, text='CTkLabel on Tab 2')
        self.label_tab2.pack()

        tab3 = self.tab_view.add('Tab 3')

        # Radio Button Frame
        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.grid(row=0, column=2, sticky='nswe', padx=(0, 20), pady=(20, 10))

        self.radio_title = ctk.CTkLabel(self.radio_frame, text='CTkRadioButton Group: ')
        self.radio_title.pack(padx=10, pady=(10, 0))

        self.radio_buttons(self.radio_frame)

        # Frame for Sliders, Segmented Button
        self.lower_frame = ctk.CTkFrame(self, fg_color='transparent')
        self.lower_frame.grid(row=1, column=0, sticky='nswe', padx=(20, 0), pady=10)

        self.lower_frame.columnconfigure(0, weight=1)
        self.lower_frame.columnconfigure(1, weight=0)
        self.lower_frame.rowconfigure(0, weight=1)

        # Left Lower Frame
        self.left_frame = ctk.CTkFrame(self.lower_frame, fg_color='transparent')
        self.left_frame.grid(row=0, column=0, sticky='nswe')

        self.left_frame.columnconfigure(0, weight=1)

        # Segmented Buttons
        self.segmented_var = ctk.StringVar(value='CTkSegmentedButton')
        list_segmented = ['CTkSegmentedButton', 'Value 2', 'Value 3']
        self.segemented_button = ctk.CTkSegmentedButton(self.left_frame, values=list_segmented,
                                                        variable=self.segmented_var)
        self.segemented_button.grid(row=0, column=0, sticky='nswe', padx=10, pady=(10))

        # Progress Bar
        self.progressbar1 = ctk.CTkProgressBar(self.left_frame, mode='indeterminate')
        self.progressbar1.grid(row=1, column=0, sticky='nswe', padx=10, pady=10)
        self.progressbar1.start()

        self.progress_var = ctk.DoubleVar(value=0.5)
        self.progressbar2 = ctk.CTkProgressBar(self.left_frame, variable=self.progress_var)
        self.progressbar2.grid(row=2, column=0, sticky='nswe', padx=10, pady=10)

        self.slider1 = ctk.CTkSlider(self.left_frame, from_=0, to=1, variable=self.progress_var, number_of_steps=4)
        self.slider1.grid(row=3, column=0, sticky='nswe', padx=10, pady=10)

        # Right Lower Frame
        self.right_frame = ctk.CTkFrame(self.lower_frame, fg_color='transparent')
        self.right_frame.grid(row=0, column=1, sticky='nswe')

        self.right_frame.rowconfigure(0, weight=1)

        self.progress_var2 = ctk.DoubleVar(value=0.5)
        self.slider2 = ctk.CTkSlider(self.right_frame, from_=0, to=1, number_of_steps=100, variable=self.progress_var2,
                                     orientation='vertical')
        self.slider2.grid(row=0, column=0, sticky='nswe', padx=10, pady=10)

        self.progressbar3 = ctk.CTkProgressBar(self.right_frame, variable=self.progress_var2, orientation='vertical')
        self.progressbar3.grid(row=0, column=1, sticky='nswe', padx=10, pady=10)

        # Scrollable Frame
        self.scroll_frame = ctk.CTkScrollableFrame(self, label_text='CTkScrollableFrame')
        self.scroll_frame.grid(row=1, column=1, sticky='nswe', padx=20, pady=10)

        # self.scroll_frame.grid_columnconfigure(0, weight= 1)

        for i in range(100):
            switch = ctk.CTkSwitch(self.scroll_frame, text=f'CTkSwitch {i}')
            switch.pack(padx=20, pady=10)

        # Checkbox Frame
        self.checkbox_frame = ctk.CTkFrame(self)
        self.checkbox_frame.grid(row=1, column=2, sticky='nswe', padx=(0, 20), pady=10)

        check_var = ctk.IntVar(value=1)
        self.check1 = ctk.CTkCheckBox(self.checkbox_frame, text='CTkCheckBox', onvalue=1, offvalue=0,
                                      variable=check_var)
        self.check1.pack(padx=20, pady=10)

        self.check2 = ctk.CTkCheckBox(self.checkbox_frame, text='CTkCheckBox')
        self.check2.pack(padx=20, pady=10)
        self.check3 = ctk.CTkCheckBox(self.checkbox_frame, text='CTkCheckBox', state='disabled')
        self.check3.pack(padx=20, pady=10)

        # Entry
        self.entry = ctk.CTkEntry(self, placeholder_text='CTkEntry')
        self.entry.grid(row=2, column=0, columnspan=2, sticky='nswe', padx=20, pady=(10, 20))

        # Button
        self.button = ctk.CTkButton(self, text='CTkButton', fg_color='transparent', border_width=2)
        self.button.grid(row=2, column=2, sticky='nswe', padx=(0, 20), pady=(10, 20))

    def radio_buttons(self, master):
        radio_var = ctk.IntVar(value=1)

        radio1 = ctk.CTkRadioButton(master, text='CTkRadioButton', variable=radio_var, value=1)
        radio1.pack(padx=10, pady=10)
        radio2 = ctk.CTkRadioButton(master, text='CTkRadioButton', variable=radio_var, value=2)
        radio2.pack(padx=10, pady=10)
        radio3 = ctk.CTkRadioButton(master, text='CTkRadioButton', variable=radio_var, value=3, state='disabled')
        radio3.pack(padx=10, pady=10)

    def option_menus(self, master):
        list_option = ['Value 1', 'Value 2', 'Value Long Long Long']
        option_menu = ctk.CTkOptionMenu(master, values=list_option)
        option_menu.pack(pady=10)

        list_combo = ['Value 1', 'Value 2', 'Value Long.....']
        combo_box = ctk.CTkComboBox(master, values=list_combo)
        combo_box.pack(pady=10)

        dialog_button = ctk.CTkButton(master, text='OpenCTkInputDialog', command=self.input_dialog)
        dialog_button.pack(pady=10)

    def input_dialog(self):
        dialog_box = ctk.CTkInputDialog(text='Type in a Number', title='Clone')


if __name__ == '__main__':
    App((1100, 580), 'Custom Tkinter')
