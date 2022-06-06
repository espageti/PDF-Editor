#Import the required Libraries
import PyPDF2
from pdf2image import convert_from_path
import tkinter as tk
from tkinter import filedialog, Text
from PIL import ImageTk, Image
import shutil
import os
from tkinter import messagebox
#Create an instance of tkinter frame
win= tk.Tk()
#Set the Geometry
width = win.winfo_screenwidth()
height = win.winfo_screenheight()
win.geometry(str(width) + "x" + str(height))




currentImage = 0
images = [] 
#Define a function to open the pdf file
def open_pdf():
   file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*"))) 
   if file:
      #Open the PDF File
      
      if(os.path.exists('images')):
         shutil.rmtree('images', ignore_errors=False, onerror=None)
      os.mkdir('images')
      imageNum = 0
      try:
         global images
         images = convert_from_path(file)
         for img in images:
            img.save('images/' + str(id(img)) + '.jpg', 'JPEG')
            
            
            images[imageNum] = 'images/' + str(id(img)) + '.jpg'
            print(images[imageNum])
            imageNum += 1
         

      except  :
         Result = "Error" 
         messagebox.showinfo("Result", Result)
      
      else:
         Result = "success"
         messagebox.showinfo("Result", Result)
         updateUI()
         display()


def next_button():
   global currentImage
   currentImage += 1
   updateUI()
   display()

def prev_button():
   global currentImage
   currentImage -= 1
   updateUI()
   display()

def updateUI():
   global currentImage
   if(currentImage + 1 >= len(images)):
      
      print(currentImage, len(images))
      nextButton.place_forget()
   else:
      nextButton.place(x = 50, y = 100)
   if(currentImage <= 0):
      
      print(currentImage, len(images))
      prevButton.place_forget()
   else:
      prevButton.place(x = 25, y = 100)





img = ImageTk.PhotoImage(Image.open("random.jpg"))
panel = tk.Label(win, image  = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "bottom", fill = "both", expand = "yes", ipadx=10)
def display():
   global currentImage
   global img
   raw = Image.open(images[currentImage])
   scale = min(width/raw.width, height/raw.height)

   print(scale, scale)
   raw = raw.resize(((int)(raw.width * scale), (int)( raw.height*scale)), Image.ANTIALIAS)
   img =  ImageTk.PhotoImage(raw)
   
   print(images[currentImage])
   #The Label widget is a standard Tkinter widget used to display a text or image on the screen.
   global panel
   panel.configure(image = img)
   panel.image = img
   
   
   text = Text(win, height=8)
   text.pack()

   text.insert('1.0', 'This is a Text widget demo')


def export():
   global images
   imagePDFs = []
   image1 = Image.open(images[0])
   for i in range(1, len(images)):
      imagePDFs.append(Image.open(images[i]).convert('RGB'))
   image1.save('my_images.pdf', save_all=True, append_images=imagePDFs)


#Define function to Quit the window
def quit_app():
   win.destroy()


#Create a Menu
my_menu= tk.Menu(win)
win.config(menu=my_menu)

#Menu dropdowns
file_menu=tk.Menu(my_menu,tearoff=False)
#File Menu
my_menu.add_cascade(label="File",menu= file_menu)
file_menu.add_command(label="Open",command=open_pdf)
file_menu.add_command(label="Export",command=export)
file_menu.add_command(label="Quit",command=quit_app)

def duplicate():
   
   if(len(images) == 0):
      print("nothing")
   newImg = Image.open(images[currentImage])
   newImg.save('images/' + str(id(newImg)) + '.jpg', 'JPEG')

   updateUI()
   
            
   
   images.insert(currentImage + 1, 'images/' + str(id(newImg)) + '.jpg')
   print(images[currentImage + 1])


#Page Menu
page_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Page", menu = page_menu)
page_menu.add_command(label="Duplicate", command = duplicate)



#next button
nextButton = tk.Button(win,text = ">" , command = next_button)
nextButton.place_forget()
#prev button
prevButton = tk.Button(win, text = '<', command = prev_button)
prevButton.place_forget()

win.mainloop()