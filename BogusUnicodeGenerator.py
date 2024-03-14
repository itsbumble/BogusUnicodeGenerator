import random
import tkinter as tk

# Constants
BG_COLOR = "#263238"
FG_COLOR = "#FFFFFF"
BUTTON_BG_COLOR = "#37474F"

def generate_random_unicode(length):
    bogus_unicode = "".join(chr(random.randint(0x0000, 0x10FFFF)) for _ in range(length))
    return bogus_unicode

def generate_and_display():
    try:
        length = int(length_entry.get())
        bogus_unicode = generate_random_unicode(length)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, bogus_unicode)
    except ValueError:
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, "Please enter a valid integer for length.")

# TKINTER SETUP
root = tk.Tk()
root.geometry("1000x500")
root.title("Bogus Unicode Generator")
root.config(bg=BG_COLOR)

input_frame = tk.Frame(root, bg=BG_COLOR)
input_frame.pack(pady=20)

length_label = tk.Label(input_frame, text="Enter Length:", font=("Helvetica", 14), bg=BG_COLOR, fg=FG_COLOR)
length_label.pack(side=tk.LEFT, padx=10)

length_entry = tk.Entry(input_frame, font=("Helvetica", 14), width=10)
length_entry.pack(side=tk.LEFT, padx=10)

generate_button = tk.Button(input_frame, text="Generate", font=("Helvetica", 14),
                             bg=BUTTON_BG_COLOR, fg=FG_COLOR, command=generate_and_display)
generate_button.pack(side=tk.LEFT, padx=10)

output_box = tk.Frame(root, bg=BG_COLOR)
output_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

output_text = tk.Text(output_box, wrap=tk.WORD, font=("Arial Unicode MS", 12), bg=BUTTON_BG_COLOR, fg=FG_COLOR)
output_text.pack(fill=tk.BOTH, expand=True)

root.mainloop()
