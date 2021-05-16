from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os

#setup tkinter
root = Tk()
root.geometry("1280x720") 

#tkinter GUI
#Search options frame and buttons
search_options_frame = Frame(root)
search_options_frame.grid(row=0,column=0,sticky="W")

folder_search_button = Button(search_options_frame,text="Folder search")
folder_search_button.grid(row=0,column=0)

tag_search_button = Button(search_options_frame,text="Tag search")
tag_search_button.grid(row=0,column=1)

refresh_button = Button(search_options_frame,text="Refresh")
refresh_button.grid(row=0,column=2)

#Search query and resaults frame
search_resaults_frame = Frame(root)
search_resaults_frame.grid(row=1,column=0,sticky="NW")

#Current search query label
search_query_label = Label(search_resaults_frame,text="/")
search_query_label.grid(row=0,column=0)

#Search resaults treeview
search_tree = ttk.Treeview(search_resaults_frame,columns=("N","T"),show="headings",height=6)

search_tree.column("N",width=360,minwidth=360,stretch=NO)
search_tree.column("T",width=64,minwidth=64,stretch=NO)

search_tree.heading("N",text="Name")
search_tree.heading("T",text="Type")

search_tree.insert("",END,values=("sdfsd","dsf"))
search_tree.insert("",END,values=("sdfsd","dsf"))
search_tree.insert("",END,values=("sdfsd","dsf"))
search_tree.insert("",END,values=("sdfsd","dsf"))
search_tree.insert("",END,values=("sdfsd","dsf"))
search_tree.insert("",END,values=("sdfsd","dsf"))

search_tree.grid(row=1,column=0)

separator = ttk.Separator(search_resaults_frame, orient='vertical')
separator.grid(row=1,column=1)

#Currently selected data's name
data_name_label = Label(root,text="/testfolder/testy2/sfsdf.png")
data_name_label.grid(row=0,column=1,sticky="NESW")

#Data viewing/tagging frame
data_view_frame = Frame(root)
data_view_frame.grid(row=1,column=1)

#Currently selected data's tags
current_tags_listbox = Listbox(data_view_frame,width=16,height=6)
current_tags_listbox.insert(0,"Python")
current_tags_listbox.insert(1,"Perl")
current_tags_listbox.insert(2,"C")
current_tags_listbox.insert(3,"PHP")
current_tags_listbox.insert(4,"JSP")
current_tags_listbox.insert(5,"Ruby")
current_tags_listbox.grid(row=0,column=0,sticky="N")

#Data preview
data_image_src = Image.open("testimage.png")
resize_image = data_image_src.resize((640,640))
data_image = ImageTk.PhotoImage(resize_image)

data_preview_label = Label(data_view_frame,image=data_image)
data_preview_label.grid(row=0,column=1,sticky="N")

#Tagging input and buttons frame
tag_input_frame = Frame(data_view_frame)
tag_input_frame.grid(row=1,column=1,sticky="E")

#Tag entry field and buttons
tag_entry = Entry(tag_input_frame,width=48)
tag_entry.grid(row=0,column=0,sticky="NESW")

add_tag_button = Button(tag_input_frame,text="Add")
add_tag_button.grid(row=0,column=1)

delete_tag_button = Button(tag_input_frame,text="Delete")
delete_tag_button.grid(row=0,column=2)

#configuration to make sure the data search and the data preview equally take up 50% of the horizontal real-estate of the current resolution
root.grid_columnconfigure(0,weight=1,uniform="root_uniform")
root.grid_columnconfigure(1,weight=2,uniform="root_uniform")

#draw window
root.title("Gorge - 'Datbase name' - /home/zdog/Projects/_GIT/Gorge/testhord")
root.resizable(False,False) 
root.mainloop()