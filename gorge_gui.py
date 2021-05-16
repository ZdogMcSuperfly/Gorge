from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import glob
import os


def main():
    root = Tk()
    root.geometry("1280x720")
    root.title("Gorge - 'Datbase name' - "+os.path.dirname(os.path.abspath(__file__))+"/data/")
    draw_buttons(root)
    draw_search_frame(root)
    draw_contents(root)
    root.resizable(False, False)
    root.mainloop()


def draw_buttons(root):
    search_options_frame = Frame(root)
    search_options_frame.grid(row=0, column=0)

    folder_search_button = Button(search_options_frame, text="Folder search")
    folder_search_button.grid(row=0, column=0)

    tag_search_button = Button(search_options_frame, text="Tag search")
    tag_search_button.grid(row=0, column=1)

    refresh_button = Button(search_options_frame, text="Refresh")
    refresh_button.grid(row=0, column=2)

    #Why worry about multiple database files when we dont even have one working :P
    #open_database_button = Button(search_options_frame, text="Open DB")
    #open_database_button.grid(row=0, column=3)

    #new_database_button = Button(search_options_frame, text="New DB", width=5)
    #new_database_button.grid(row=0, column=4)


def draw_search_frame(root):
    # Search query and results frame
    search_results_frame = Frame(root)
    search_results_frame.grid(row=1, column=0, sticky="NW")

    # Current search query label
    search_query_label = Label(search_results_frame, text="/")
    search_query_label.grid(row=0, column=0)

    # Search results treeview
    search_tree = ttk.Treeview(search_results_frame, columns=("N", "T"), show="headings", height=len(glob.glob("data/*")))

    search_tree.column("N", width=360, minwidth=360, stretch=NO)
    search_tree.column("T", width=64, minwidth=64, stretch=NO)

    search_tree.heading("N", text="Name")
    search_tree.heading("T", text="Type")

    files_in_dir = glob.glob("data/*")
    for file in files_in_dir:
        filename = file.split("/")[-1]
        #fills the type column with weather its a file or folder
        if os.path.isdir(file) == True:
            extension = "Folder" 
        else:
            extension = "File"
        search_tree.insert("", END, values=(filename, extension))

    search_tree.grid(row=1, column=0)


def draw_contents(root):
    # Currently selected data's name
    data_name_label = Label(root, text="/testfolder/testy2/sfsdf.png")
    data_name_label.grid(row=0, column=1, sticky="NESW")

    # Data viewing/tagging frame
    data_view_frame = Frame(root)
    data_view_frame.grid(row=1, column=1)

    # Currently selected data's tags
    current_tags_listbox = Listbox(data_view_frame, width=16, height=6)
    current_tags_listbox.insert(0, "Python")
    current_tags_listbox.insert(1, "Perl")
    current_tags_listbox.insert(2, "C")
    current_tags_listbox.insert(3, "PHP")
    current_tags_listbox.insert(4, "JSP")
    current_tags_listbox.insert(5, "Ruby")
    current_tags_listbox.grid(row=0, column=0, sticky="N")

    # Data preview
    data_image_src = Image.open("no_preview.png")
    resize_image = data_image_src.resize((640, 640))
    data_image = ImageTk.PhotoImage(resize_image)

    data_preview_label = Label(data_view_frame, image=data_image)
    data_preview_label.grid(row=0, column=1, sticky="N")

    # Tagging input and buttons frame
    tag_input_frame = Frame(data_view_frame)
    tag_input_frame.grid(row=1, column=1, sticky="E")

    # Tag entry field and buttons
    tag_entry = Entry(tag_input_frame, width=48)
    tag_entry.grid(row=0, column=0, sticky="NESW")

    add_tag_button = Button(tag_input_frame, text="Add")
    add_tag_button.grid(row=0, column=1)

    delete_tag_button = Button(tag_input_frame, text="Delete")
    delete_tag_button.grid(row=0, column=2)

    # configuration to make sure the data search and the data preview equally take up 50% of the horizontal real-estate of the current resolution
    root.grid_columnconfigure(0, weight=1, uniform="root_uniform")
    root.grid_columnconfigure(1, weight=2, uniform="root_uniform")


main()