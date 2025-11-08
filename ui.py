"""
ui.py
-----
Modern UI for the Temperature Converter application using CustomTkinter.
"""

import customtkinter as ctk
from tkinter import messagebox
from converter import convert_temperature

def launch_app():
    # App appearance settings
    ctk.set_appearance_mode("System")  # Can be "Dark" or "Light"
    ctk.set_default_color_theme("blue")

    # Main window
    app = ctk.CTk()
    app.title("🌡️ Temperature Converter - Bhumika Macharla")
    app.geometry("800x500")
    app.resizable(False, False)

    # Header
    title_label = ctk.CTkLabel(
        app,
        text="🌡️ Temperature Converter",
        font=("Poppins", 28, "bold"),
        text_color="#000000"
    )
    title_label.pack(pady=25)

    # Frame for inputs
    frame = ctk.CTkFrame(app, corner_radius=20)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Input label and entry
    temp_label = ctk.CTkLabel(frame, text="Enter Temperature:", font=("Poppins", 18))
    temp_label.grid(row=0, column=0, padx=20, pady=25, sticky="e")

    temp_entry = ctk.CTkEntry(frame, width=120, height=40, font=("Poppins", 18))
    temp_entry.grid(row=0, column=1, padx=10, pady=25)

    # Dropdowns
    units = ["C", "F", "K"]

    from_unit = ctk.CTkOptionMenu(frame, values=units, font=("Poppins", 16))
    from_unit.set("C")
    from_unit.grid(row=0, column=2, padx=10, pady=25)

    to_label = ctk.CTkLabel(frame, text="to", font=("Poppins", 18))
    to_label.grid(row=0, column=3, padx=10)

    to_unit = ctk.CTkOptionMenu(frame, values=units, font=("Poppins", 16))
    to_unit.set("F")
    to_unit.grid(row=0, column=4, padx=10, pady=25)

    # Conversion logic
    def on_convert():
        try:
            value = float(temp_entry.get())
            result = convert_temperature(value, from_unit.get(), to_unit.get())
            result_label.configure(
                text=f"{value:.2f}°{from_unit.get()} = {result:.2f}°{to_unit.get()}"
            )
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")

    # Convert button
    convert_btn = ctk.CTkButton(
        frame,
        text="Convert",
        command=on_convert,
        font=("Poppins", 18, "bold"),
        width=160,
        height=50,
        corner_radius=12,
        fg_color="#0078D7",
        hover_color="#005A9E"
    )
    convert_btn.grid(row=1, column=0, columnspan=5, pady=30)

    # Result label
    result_label = ctk.CTkLabel(
        app,
        text="",
        font=("Poppins", 22, "bold"),
        text_color="#000000"
    )
    result_label.pack(pady=20)

    # Footer
    footer = ctk.CTkLabel(
        app,
        text="Developed by Bhumika Macharla | Software Development Internship Project",
        font=("Poppins", 12),
        text_color="#000000"
    )
    footer.pack(side="bottom", pady=10)

    # Run
    app.mainloop()
