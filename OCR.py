import pytesseract as tess
from tkinter import*
import tkinter as tk
from tkinter import filedialog
import cv2

tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
window = tk.Tk()
window.title('Image Recognition')
window.geometry("500x400")
window.configure(bg="Black")
lbl1 = tk.Label(window, text="Image Processing Tool", font=("Garamond Bold Italic", 25), bg="black", fg="white")
lbl1.pack()
lbl2 = tk.Label(window, text ="Click The Below Button:\n\n\n\n\n", font=10, bg="black", fg="white", padx=20)
lbl2.pack()

# Add image file
bg = PhotoImage(file = "simple1.png")
canvas1 = Canvas( window, width = 400,height = 400)
canvas1.pack(fill = "both", expand = True)



def r(): #THIS FUNCTION RETURNS THE OPENED IMAGE FROM ITS PATH 
    file_path = filedialog.askopenfilenames()
    x = str(file_path)
    string = x.replace("'", "")
    string = string.replace(",", "")
    string = string.replace("(", "", 1)
    string = string[:-1]
    img_path = string
    
    image = Image.open(img_path)
    return image
def func8(): #FUNCTION RETURN TEXT FROM IMAGE(OCR)
    img = r()
    window8 = tk.Tk()
    window8.title("Image to Text Converter")
    window8.geometry("500x300")
    window8.configure(bg="black")
    t = tess.image_to_string(img)
    l8 = tk.Text(window8,font=("Arialbold"),  background="pink")
    l8.pack(fill="both", expand=True)
    
    l8.insert(tk.END, t)
  
btn8 = tk.Button(text="Convert the Image to Text", command=func8,font=("Arialbold"), width=25, height=1, background="#3DA8AA")
btn8.pack()
btn8.place(x=130, y=200)
# Button for closing
exit_button = Button(window, text="Exit", command=window.destroy,width=10, height=1, background="red")
exit_button.pack()
exit_button.place(x=210, y=300)


window.mainloop()