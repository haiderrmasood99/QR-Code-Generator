from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageEnhance, ImageFilter,ImageDraw
from rembg import remove 
from tkinter import filedialog
from amzqr import amzqr
import os
import cv2
import numpy as np
import random
from datetime import datetime
import tkinter
from tkinter import colorchooser
res_h = []
from tkinter import messagebox 
global change_colour
global final_name
global final_name1
global final_name2
global final_name3
change_colour = np.array([0, 100, 0], dtype=np.uint8)




def choose_color():
 
    # variable to store hexadecimal code of color
    global color_code
    color_code = colorchooser.askcolor(title ="Choose color") 

def displayimage(img):

    outputImage = img

    dispimage = ImageTk.PhotoImage(img)

    panel.configure(image=dispimage)

    panel.image = dispimage

def brightness_callback(brightness_pos):

    brightness_pos = float(brightness_pos)

    global outputImage

    enhancer = ImageEnhance.Brightness(img)

    outputImage = enhancer.enhance(brightness_pos)
    outputImage.save('internal/Recent/output1.png')

    displayimage(outputImage)


def contrast_callback(contrast_pos):

    contrast_pos = float(contrast_pos)

    global outputImage

    enhancer = ImageEnhance.Contrast(img)

    outputImage = enhancer.enhance(contrast_pos)
    outputImage.save('internal/Recent/output1.png')

    displayimage(outputImage)

def sharpen_callback(sharpness_pos):

    sharpness_pos = float(sharpness_pos)

    global outputImage

    enhancer = ImageEnhance.Sharpness(img)

    outputImage = enhancer.enhance(sharpness_pos)
    outputImage.save('internal/Recent/output1.png')
    displayimage(outputImage)

def color_callback(Color_pos):

    Color_pos = float(Color_pos)

    global outputImage

    enhancer = ImageEnhance.Color(img)

    outputImage = enhancer.enhance(Color_pos)
    outputImage.save('internal/Recent/output1.png')

    displayimage(outputImage)
def qr_callback(qr_pos):

    qr_pos = float(qr_pos)
    if qr_pos == 0.0:
        image_display_style = Image.open('internal/Recent/1.png')
    elif qr_pos == 1.0:
        image_display_style = Image.open('internal/Recent/2.png')
    elif qr_pos == 2.0:
        image_display_style = Image.open('internal/Recent/3.png')
    displayimage(image_display_style)



def preprocessing():

    global outputImage
    outputImage = Image.open('internal/Recent/output1.png')
    img = outputImage
    img = remove(img)
    name = 'internal/temp/temp.png'
    img.save(name)
    img_np_bg = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img_np_bg)
    cv2.imwrite(name,cl1)
    input = Image.open(name) 
    output = remove(input) 
    output.save(name) 
    messagebox.showinfo("Preprocessing", "Preprocessing Done") 
    displayimage(output)

def get_bound(x,y):
    list_bound = [(x-5,y-5),(x-4,y-5),(x-3,y-5),(x-2,y-5),(x-1,y-5),(x,y-5),(x+1,y-5),(x+2,y-5),(x+3,y-5),(x+4,y-5),
                  (x+5,y-5),(x-5,y+5),(x-4,y+5),(x-3,y+5),(x-2,y+5),(x-1,y+5),(x,y+5),(x+1,y+5),(x+2,y+5),(x+3,y+5),
                  (x+4,y+5),(x+5,y+5),

                  (x-5,y-4),(x-5,y-3),(x-5,y-2),(x-5,y-1),(x-5,y),(x-5,y+1),(x-5,y+2),(x-5,y+3),(x-5,y+4),
                  (x+5,y-4),(x+5,y-3),(x+5,y-2),(x+5,y-1),(x+5,y),(x+5,y+1),(x+5,y+2),(x+5,y+3),(x+5,y+4),
                  
                  (x-7,y-7),(x-7,y-6),(x-7,y-5),(x-7,y-4),(x-7,y-3),(x-7,y-2),(x-7,y-1),(x-7,y),(x-7,y+1),
                  (x-7,y+2),(x-7,y+3),(x-7,y+4),(x-7,y+5),(x-7,y+6),(x-7,y+7),
                  (x+7,y-7),(x+7,y-6),(x+7,y-5),(x+7,y-4),(x+7,y-3),(x+7,y-2),(x+7,y-1),(x+7,y),(x+7,y+1),
                  (x+7,y+2),(x+7,y+3),(x+7,y+4),(x+7,y+5),(x+7,y+6),(x+7,y+7),
                  
                  (x-6,y-7),(x-5,y-7),(x-4,y-7),(x-3,y-7),(x-2,y-7),(x-1,y-7),(x,y-7),(x+1,y-7),
                  (x+2,y-7),(x+3,y-7),(x+4,y-7),(x+5,y-7),(x+6,y-7),
                  (x-6,y+7),(x-5,y+7),(x-4,y+7),(x-3,y+7),(x-2,y+7),(x-1,y+7),(x,y+7),(x+1,y+7),
                  (x+2,y+7),(x+3,y+7),(x+4,y+7),(x+5,y+7),(x+6,y+7),

                  (x-6,y-6),(x-6,y-5),(x-6,y-4),(x-6,y-3),(x-6,y-2),(x-6,y-1),(x-6,y),(x-6,y+1),
                  (x-6,y+2),(x-6,y+3),(x+7,y+4),(x+7,y+5),(x-6,y+6),

                  (x+6,y-6),(x+6,y-5),(x+6,y-4),(x+6,y-3),(x+6,y-2),(x+6,y-1),(x+6,y),(x+6,y+1),
                  (x+6,y+2),(x+6,y+3),(x+6,y+4),(x+6,y+5),(x+6,y+6),

                  (x-5,y-6),(x-4,y-6),(x-3,y-6),(x-2,y-6),(x-1,y-6),(x,y-6),(x+1,y-6),
                  (x+2,y-6),(x+3,y-6),(x+4,y-6),(x+5,y-6),
                  (x-5,y+6),(x-4,y+6),(x-3,y+6),(x-2,y+6),(x-1,y+6),(x,y+6),(x+1,y+6),
                  (x+2,y+6),(x+3,y+6),(x+4,y+6),(x+5,y+6)
                  ]
    return list_bound
def get_boundry_pixels_colour(list_new,image_pil):
    boundry_pixels =[]
    for i in list_new:
        value_grey_white = image_pil.getpixel(i)
        boundry_pixels.append(value_grey_white)
        boundry_pixels.append(0)
        boundry_pixels.append(255)
    boundry_pixels = np.array(boundry_pixels)
    return boundry_pixels

def first_pass(value_1,value_2,image_np_arg,image_pil_arg):
    image = image_np_arg
    for i in range(27):
        valuess = (value_2,value_1)
        center_x = value_2
        center_y = value_1
        pixel = image_pil_arg.getpixel(valuess)
        list_bound_1 = get_bound(value_2,value_1)
        boundry_pixels_colour = []
        boundry_pixels_colour = get_boundry_pixels_colour(list_bound_1,image_pil_arg)
        value_2 = value_2 + 9
        count = np.unique(boundry_pixels_colour, return_counts=True)
        if count[1][0] == count[1][1]:
            main_pixel = 255
            background_pixels = 0
        elif count[1][0] > count[1][1]:
            main_pixel = 0
            background_pixels = 0
        else:
            main_pixel = 255
            background_pixels = 255
        count = tuple()
        image[center_x-4:center_x+5,center_y-4:center_y+5]=main_pixel
        image[center_x-4:center_x+1,center_y-4:center_y+1]=main_pixel
        image[center_x:center_x+5,center_y:center_y+5]=main_pixel
    return image
      
def second_pass(value_1,value_2,image_np_arg,image_pil_arg):
    image = image_np_arg
    for i in range(27):
        valuess = (value_1,value_2)
        center_x = value_1
        center_y = value_2
        pixel = image_pil_arg.getpixel(valuess)
        list_bound_1 = get_bound(value_1,value_2)
        boundry_pixels_colour = []
        boundry_pixels_colour = get_boundry_pixels_colour(list_bound_1,image_pil_arg)
        value_2 = value_2 + 9
        count = np.unique(boundry_pixels_colour, return_counts=True)
        
        if count[1][0] == count[1][1]:
            main_pixel = 0
            background_pixels = 255
        elif count[1][0] > count[1][1]:
            main_pixel = 0
            background_pixels = 255
        else:
            main_pixel = 255
            background_pixels = 0
        count = tuple()
        image[center_x-4:center_x+5,center_y-4:center_y+5]=main_pixel
        image[center_x-4:center_x+1,center_y-4:center_y+1]=main_pixel #main_pixel
        image[center_x:center_x+5,center_y:center_y+5]=main_pixel #main_pixel
    return image

def anchor_shape(option,image):
    if option == 'square':
        return image
    elif option == 'circle':
        image[0:99,0:99] = 255
        image[342:405,36:99]=255
        image[36:99,342:405]=255
        image[336:356,336:356]
        center_coordinates1s = (346, 346) 
        center_coordinates2 = (67,67)
        center_coordinates3 = (67,373)
        center_coordinates4 = (373,67)
        radius_s = 5
        radius_s_outer = 18
        radius_l = 14
        radius_l_outer = 28
        color = (0, 0, 0) 
        thickness = -1
        image = cv2.circle(image, center_coordinates1s, radius_s, color, thickness) 
        image = cv2.circle(image, center_coordinates2, radius_l_outer, color, 8) 
        image = cv2.circle(image, center_coordinates2, radius_l, color, thickness)  
        image = cv2.circle(image, center_coordinates3, radius_l, color, thickness) 
        image = cv2.circle(image, center_coordinates3, radius_l_outer, color, 8) 
        image = cv2.circle(image, center_coordinates4, radius_l_outer, color, 8)  
        image = cv2.circle(image, center_coordinates4, radius_l, color, thickness)  
        return image
    elif option == 'blank':
        image[0:99,0:99] = 255
        image[342:405,36:99]=255
        image[36:99,342:405]=255
        image[336:356,336:356] 
        return image
    
def anchor_shape_rounded_square(image):
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((36, 36, 98, 98), fill="black",
                           width=3, radius=7)
    draw.rounded_rectangle((45, 45, 89, 89), fill="white",
                           width=3, radius=7)
    draw.rounded_rectangle((54, 54, 80, 80), fill="black",
                           width=3, radius=7)
    

    draw.rounded_rectangle((342, 36, 404, 98), fill="black",
                           width=3, radius=7)
    draw.rounded_rectangle((351, 45, 395, 89), fill="white",
                           width=3, radius=7)
    draw.rounded_rectangle((360, 54, 386, 80), fill="black",
                           width=3, radius=7)
    


    draw.rounded_rectangle((36, 342, 98, 404), fill="black",
                           width=3, radius=7)
    draw.rounded_rectangle((45, 351, 89, 395), fill="white",
                           width=3, radius=7)
    draw.rounded_rectangle((54, 360, 80, 386), fill="black",
                           width=3, radius=7)
    


    draw.rounded_rectangle((342, 342, 350, 350), fill="black",
                           width=3, radius=7)





    return image
def generateQR():
    text = frame_text.get()
    image = 'internal/temp/temp.png'
    #print(text)
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    name = str(current_time) + "_output_qr.png"
    name1 = str(current_time) + "_output_qr1.png"
    name2 = str(current_time) + "_output_qr2.png"
    name3 = str(current_time) + "_output_qr3.png"
    final_name = 'Output/'+name
    final_name1 = 'Output/'+name1
    final_name2 = 'Output/'+name2
    final_name3 = 'Output/'+name3

    final_namer1 = 'internal/Recent/1.png'
    final_namer2 = 'internal/Recent/2.png'
    final_namer3 = 'internal/Recent/3.png'
    version, level, qr_name = amzqr.run(
    words = text,
    version=6,
    level='H',
    picture= image,
    colorized=False,
    contrast=2.0,
    brightness=1.0,
    save_name=final_name,
    save_dir=os.getcwd()
    )
    image_numpy_qr_gen = cv2.imread(final_name,0)
    image_pil_qr_gen = Image.open(final_name)
    image_temp_qr_gen = first_pass(94,103,image_numpy_qr_gen,image_pil_qr_gen)
    image_temp_qr_gen1 = second_pass(94,103,image_temp_qr_gen,image_pil_qr_gen)
    cv2.imwrite(final_name,image_temp_qr_gen1)
    image_temp_qr_gen2 = anchor_shape('circle',image_temp_qr_gen1)
    cv2.imwrite(final_name1,image_temp_qr_gen2)
    image_final_blank = image_temp_qr_gen2
    image_final_blank = anchor_shape('blank',image_final_blank)
    cv2.imwrite(final_name2,image_final_blank)
    image_pil_1 = Image.open(final_name2)
    image_square = anchor_shape_rounded_square(image_pil_1)
    image_square = np.array(image_square)
    cv2.imwrite(final_name2,image_square)

    imagec0 = cv2.imread(final_name,cv2.IMREAD_COLOR)
    imagec1 = cv2.imread(final_name1,cv2.IMREAD_COLOR)
    imagec2 = cv2.imread(final_name2,cv2.IMREAD_COLOR)
    black = np.array([0, 0, 0], dtype=np.uint8)
    mask = np.all(imagec0 == black, axis=-1)
    mask1 = np.all(imagec1 == black, axis=-1)
    mask2 = np.all(imagec2 == black, axis=-1)
    #print("new")
    color_code = colorchooser.askcolor(title ="Choose color") 
    #print(change_colour[0]) # 64 128 0 RGB
    # print("Old")
    # print(change_colour)
    change_colour[0]= color_code[0][2]
    change_colour[1]= color_code[0][1]
    change_colour[2]= color_code[0][0]
    # print("New")
    # print(change_colour)
    imagec0[mask] = change_colour
    imagec1[mask1] = change_colour
    imagec2[mask2] = change_colour
    cv2.imwrite(final_name, imagec0)
    blurred = cv2.blur(imagec0, (2, 2))
    cv2.imwrite(final_name, blurred)
    cv2.imwrite(final_namer1, blurred)
    blurred1 = cv2.blur(imagec1, (2, 2))
    cv2.imwrite(final_name1, imagec1)
    cv2.imwrite(final_name1, blurred1)
    cv2.imwrite(final_namer2, blurred1)
    blurred2 = cv2.blur(imagec2, (2, 2))
    cv2.imwrite(final_name2, imagec2)
    cv2.imwrite(final_name2, blurred2)
    cv2.imwrite(final_namer3, blurred2)
    image_display = Image.open(final_name2)
    displayimage(image_display)
    

def edgeEnhance():

    global img

    img = img.filter(ImageFilter.FIND_EDGES)

    displayimage(img)

def resize():

    global img

    img = img.resize((200, 300))

    displayimage(img)

def mouse_crop(event, x, y, flags, param):

    global x_start, y_start, x_end, y_end, cropping


    if event == cv2.EVENT_LBUTTONDOWN:
        x_start, y_start, x_end, y_end = x, y, x, y
        cropping = True


    elif event == cv2.EVENT_MOUSEMOVE:
        if cropping == True:
            x_end, y_end = x, y


    elif event == cv2.EVENT_LBUTTONUP:

        x_end, y_end = x, y
        cropping = False 

        refPoint = [(x_start, y_start), (x_end, y_end)]

        if len(refPoint) == 2:
            roi = oriImage[refPoint[0][1]:refPoint[1][0], refPoint[0][0]:refPoint[1][0]]
            cv2.imshow("Cropped", roi)
            cv2.imwrite("cropped.png",roi)
            a = 0
def crop():

    global img
    global a
    a = 1
    #print("new")
    image_np  = np.array(img)
    image_np = image_np[:, :, ::-1] 
    global cropping
    cropping = False
    x_start, y_start, x_end, y_end = 0, 0, 0, 0
    global oriImage
    oriImage = image_np.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", mouse_crop)
    
    print(cropping)
    i = image_np.copy()
    if not cropping:
        #print("hello")
        cv2.imshow("image", image_np)

    elif cropping:
        i = cv2.rectangle(i, (x_start, y_start), (x_end, x_end), (0, 0, 0), 10)
        cv2.imshow("image", i)
    cv2.waitKey(0)
        # if key == ord('c'):  # stop the loop if 'c' key is pressed
        #     break
    
    cv2.destroyAllWindows()
    displayimage(img)

def ChangeImg():

    global img

    imgname = filedialog.askopenfilename(title="Change Image")

    if imgname:
        img = Image.open(imgname).convert('RGB')
        img.save('internal/Recent/output1.png')
        img = img.resize((600, 600))

        displayimage(img)
def clear_all():
    frame_text.delete(0,END)
def save():

    global outputImage
    now = datetime.now()
    current_time = now.strftime("%H_%M_%S")
    name = str(current_time) + "_output_qr.png"
    outputImage.save(name)

mains = Tk()

space=(" ")*215

screen_width=mains.winfo_screenwidth()

screen_height = mains.winfo_screenheight()

mains.geometry(f"{screen_width}x{screen_height}")

mains.title(f"{space}Image Editor")

mains.configure(bg='#323946')

img = Image.open("internal/Resource/main.jpg").convert('RGB')
img = img.resize((441, 441))

panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=150, pady=50)
displayimage(img)


 

brightnessSlider = Scale(mains, label="Brightness", from_=0, to=10, orient=HORIZONTAL, length=400,

                         resolution=1.0, command=brightness_callback, bg="#1f242d")

brightnessSlider.set(1)

brightnessSlider.configure(font=('poppins',11,'bold'),foreground='white')

brightnessSlider.place(x=1070,y=255)

contrastSlider = Scale(mains, label="Contrast", from_=0, to=10, orient=HORIZONTAL, length=400,

                       command=contrast_callback, resolution=1.0, bg="#1f242d")

contrastSlider.set(1)

contrastSlider.configure(font=('poppins',11,'bold'),foreground='white')

contrastSlider.place(x=1070,y=330)

sharpnessSlider = Scale(mains, label="Sharpness", from_=0, to=2, orient=HORIZONTAL, length=400,

                        command=sharpen_callback, resolution=0.1, bg="#1f242d")

sharpnessSlider.set(1)

sharpnessSlider.configure(font=('poppins',11,'bold'),foreground='white')

sharpnessSlider.place(x=1070,y=405)

colorSlider = Scale(mains, label="Colors", from_=0, to=2, orient=HORIZONTAL, length=400,

                    command=color_callback, resolution=0.1, bg="#1f242d")
colorSlider.set(1)
colorSlider.configure(font=('poppins',11,'bold'),foreground='white')
colorSlider.place(x=1070,y=480)


# NEW
# colorSlider1 = Scale(mains, label="BGR VALUE", from_=0, to=2, orient=HORIZONTAL, length=400,
qrSlider = Scale(mains, label="QR CODE STYLES TO PREVIEW", from_=0, to=2, orient=HORIZONTAL, length=400,

                    command=qr_callback, resolution=1, bg="#1f242d")
qrSlider.set(1)
qrSlider.configure(font=('poppins',11,'bold'),foreground='white')
qrSlider.place(x=1070,y=570)
#                     command=color_callback, resolution=0.1, bg="#1f242d")
# colorSlider1.set(1)
# colorSlider1.configure(font=('poppins',11,'bold'),foreground='white')
# colorSlider1.place(x=1070,y=480)
# NEW


btnChaImg = Button(mains, text='Change Image', width=25,command=ChangeImg,bg="#1f242d",activebackground="ORANGE")

btnChaImg.configure(font=('poppins',11,'bold'),foreground='white')

btnChaImg.place(x=805,y=155)

btnCrop = Button(mains, text='Crop', width=25, command=crop, bg="#1f242d")

btnCrop.configure(font=('poppins',11,'bold'),foreground='white')

btnCrop.place(x=805,y=240)


btnpreprocessing = Button(mains, text='Preprocess Image', width=25, command=preprocessing, bg="#1f242d")

btnpreprocessing.configure(font=('poppins',11,'bold'),foreground='white')

btnpreprocessing.place(x=805,y=325)
 

# button = Button(mains, text = "Select color",width=25, command = choose_color, bg="#1f242d")
# button.configure(font=('poppins',11,'bold'),foreground='white')
# button.place(x=805,y=510)


btnQR = Button(mains, text='Generate QR', width=25, command=generateQR, bg="#1f242d")

btnQR.configure(font=('poppins',11,'bold'),foreground='white')

btnQR.place(x=805,y=390)
 

btnSave = Button(mains, text='Save', width=25, command=save, bg="black")

btnSave.configure(font=('poppins',11,'bold'),foreground='white')

btnSave.place(x=805,y=455)

frame_text = Entry(mains,font=("Helvetica",18))
frame_text.place(x=800,y=520)

btnClear = Button(mains, text='Clear QR Text', width=15, command=clear_all, bg="black")

btnClear.configure(font=('poppins',11,'bold'),foreground='white')

btnClear.place(x=805,y=600)
 
mains.mainloop()