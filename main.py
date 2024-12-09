import cv2
from simple_facerec import SimpleFacerec
import datetime
import pyttsx3  # pip install pyttsx3
import speech_recognition as sr
import os
import shutil
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import *
import tkinter.messagebox as t
from PIL import Image, ImageTk


def start():
    root = Tk()
    root.withdraw()
    root.update()

    present_date = datetime.datetime.now().strftime("%d%b%y")
    new_date = datetime.datetime.now().strftime("%d:%b:%y")
    print(new_date)
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(strTime)
    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("images/")
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # Load Camera
    cap = cv2.VideoCapture(0)

    i1 = 0
    list2 = ["farhaan", "mushu", "Jeff Bezoz", "Ryan Reynolds", "Elon Musk", "faizan", "junaid", "siddiq", "ali",
             "taheer", "tarun", "tenzing", "nishmitha", "gokul"]
    string_date = str(present_date)
    folder_loc = os.getcwd()
    attendance_data = f"attendance{string_date}.csv"
    directories = os.listdir()
    if attendance_data not in directories:
        f1 = open(attendance_data, "w+")
        st = "name,time1,date1"
        read = f1.readline()
        print(read)
        print("sasa")
        if read != st:
            print("gfg")
            f1.write(f'name,time1,date1')
        f1.close()
    print(folder_loc)



    def attendance(name):

        name_file = name + ".csv"
        folder_loc1 = os.getcwd()
        directories = os.listdir()
        if name_file not in directories:
            f11 = open(name_file, "w+")
            st1 = "name,time1,date1"
            read1 = f11.readline()
            print(read1)
            print("sasa")
            if read1 != st1:
                print("gfg")
                f11.write(f'name,time1,date1')
            f11.close()

        with open(name_file, "r+") as fn:
            data_fn = fn.readlines()
            namelist_fn = []
            datelist_fn = []
            for line1 in data_fn:
                entry = line1.split(",")
                namelist_fn.append(entry[0])
                datelist_fn.append(entry[2])
            if new_date not in datelist_fn:
                fn.write(f'\n{name},{strTime},{new_date}')
                fn.close()

        with open(attendance_data, "r+") as f:
            data = f.readlines()
            namelist = []
            datelist = []
            for line in data:
                entry = line.split(",")
                namelist.append(entry[0])
                datelist.append(entry[2])
            if name not in namelist:
                f.write(f'\n{name},{strTime},{new_date}')
                f.close()

    while True:
        ret, frame = cap.read()
        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)

        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            for li in list2:

                if name == li:
                    with open(attendance_data, "r+") as f:
                        data = f.readlines()
                        namelist = []
                        for line in data:
                            entry = line.split(",")
                            namelist.append(entry[0])
                        if name not in namelist:
                            word = name, "has logged in at", strTime
                            speak(word)
                    attendance(name)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    pass


def new_user_add():
    pass


def delete():

    pass


def get_attendance_bystudent1():
    from PIL import Image, ImageTk

    def get_student1():
        student_search_name = student_name.get()
        student_search_file = f'{student_search_name}.csv'
        print(student_search_file)
        with open(student_search_file, "r+") as new:
            new_readline_list = []
            data1 = new.readlines()
            i = 0
            for dat in data1:
                i += 1
            i =  i
            print(i)
            i1.set(i)
            label5.update()
    root.destroy()
    root_new = Tk()
    fraem1 = Frame(root_new)
    fraem1.pack()
    root_new1 = Frame(root_new)
    root_new1.pack()
    enter_student = Label(fraem1, text="ENTER STUDENT NAME:")
    enter_student.grid(row=0, column=0)
    student_name = StringVar()
    entry_student = Entry(fraem1, textvariable=student_name)
    entry_student.grid(row=0, column=1)
    search_button = Button(fraem1, text="SEARCH", command=get_student1)
    search_button.grid(row=0, column=2)
    adarsh_college11 = Image.open("J.png")
    re111 = adarsh_college11.resize((200, 200))
    ada = ImageTk.PhotoImage(re111)
    picture21 = Label(root_new1, image=ada)
    picture21.grid(row=1, column=1)
    label1 = Label(root_new1, text="Name", borderwidth=6, relief=GROOVE)
    label1.grid(row=1, column=2)
    label2 = Label(root_new1, text="Course", borderwidth=6, relief=GROOVE)
    label2.grid(row=1, column=3)
    label3 = Label(root_new1, text="Sem", borderwidth=6, relief=GROOVE)
    label3.grid(row=1, column=4)
    label4 = Label(root_new1, text="Total days", borderwidth=6, relief=GROOVE)
    label4.grid(row=1, column=5)
    i1 = StringVar()
    i1.set("no")
    label5 = Label(root_new1, textvariable=i1, borderwidth=6, relief=GROOVE)
    label5.grid(row=1, column=6)
    root_new.mainloop()


root = Tk()
# root.configure(bg="#1E130C")
root.configure(bg="black")
root.title("AUTO ATTENDANCE ")
# root.geometry("382x250")
root.minsize(1000, 540)
root.maxsize(1000, 540)
main_frame_top = Frame(root, bg="grey", borderwidth=6)
main_frame_top.pack(fill=X)
adarsh_logo = Image.open("christ_logo.png")
resize_logo = adarsh_logo.resize((300, 100))
adarsh_log = ImageTk.PhotoImage(resize_logo)
picture1 = Label(main_frame_top, image=adarsh_log)
picture1.grid(row=0, column=0)
main_frame_top2 = Frame(main_frame_top, bg="grey")
main_frame_top2.grid(row=0, column=1)
attendance_label = Label(main_frame_top2, text="CHRIST COLLEGE ATTENDANCE MANAGEMENT SYSTEM  ", bg="grey", fg="white",
                         font="comicsansms 17 bold", pady=10, padx=10)

attendance_label.grid(row=0)
import datetime

date = datetime.datetime.now()
date12 = str(date).split(" ")
date2 = date12[0]

test = Label(main_frame_top2, text=date2, font="comicsansms 22 bold", bg="grey")
test.grid(row=1, column=0)
frame_button_top = Frame(root)
frame_button_top.pack()
frame_button_top1 = Frame(root, borderwidth=1, relief='solid', bg="grey", height=5)
frame_button_top1.pack(fill=X)

add_user = Button(frame_button_top, text="        ADD NEW USER  ", command=new_user_add, padx=120)
add_user.grid(row=0, column=1)
delete_button = Button(frame_button_top, text="           DELETE           ", command=delete, padx=120)
delete_button.grid(row=0, column=2)
exit_button = Button(frame_button_top, text="           exit           ", command=quit, padx=120)
exit_button.grid(row=0, column=3)
middle_frame = Frame(root, bg="black")
middle_frame.pack(fill=X)
left_frame = Frame(middle_frame, bg="black")
left_frame.grid(row=0, column=0)
right_frame = Frame(middle_frame)
right_frame.grid(row=0, column=1, padx=10)
start_button = Button(left_frame, text="    START   ", command=start, padx=7, bg="grey", font="bold")
start_button.grid(row=3, column=0)
text = Label(left_frame, text="ATTENDANCE BY FACE DETECTION\n"
                              "MADE EASY FOR JUSt\n"
                              "CLICK ON THE START BUTTON\n "
                              "TO START ATTENDANCE\n ",
             font="comicsansms 22 bold", fg="white", bg="black")
text.grid(row=0, column=0)
adarsh_college = Image.open("collge.jpg")
re = adarsh_college.resize((500, 300))
adarsh_college_image = ImageTk.PhotoImage(re)
picture2 = Label(right_frame, image=adarsh_college_image)

picture2.grid(row=0, column=4)
frame_button_dowm1 = Frame(root, borderwidth=1, relief='solid', bg="grey", height=5)
frame_button_dowm1.pack(fill=X)
frame_button_dowm = Frame(root, borderwidth=1, relief='solid', bg="black")
frame_button_dowm.pack(fill=X)
get_attedance = Button(frame_button_dowm, text="       GET ATTENDANCE       ", command=quit, padx=180)
get_attedance.grid(row=0, column=0)
getstudentattandance = Button(frame_button_dowm, text="           GET ATTENDANCE OF STUDENT           ",
                              command=get_attendance_bystudent1, padx=220)
getstudentattandance.grid(row=0, column=2)
frame_dowm1 = Frame(root, borderwidth=1, relief='solid', bg="grey")
frame_dowm1.pack(fill=X)
label1 = Label(frame_dowm1, text="For any help- \n"
                                 "\tgmail:mushuu123456@gmail.com\n"
                                 "contact:8888888888888"
               , bg="grey")
label1.grid(row=0, column=0)
root.mainloop()


#
#
#
#
#
# import cv2
# from simple_facerec import     SimpleFacerec
# import datetime
# import pyttsx3  # pip install pyttsx3
# import speech_recognition as sr
# import os
# import shutil
# from tkinter import Tk
# from tkinter.filedialog import askopenfilename
# from tkinter import *
# import tkinter.messagebox as t
# from PIL import Image, ImageTk
#
#
# def start():
#     root = Tk()
#     root.withdraw()
#     root.update()
#
#     present_date = datetime.datetime.now().strftime("%d%b%y")
#     new_date = datetime.datetime.now().strftime("%d:%b:%y")
#     print(new_date)
#     strTime = datetime.datetime.now().strftime("%H:%M:%S")
#     print(strTime)
#     # Encode faces from a folder
#     sfr = SimpleFacerec()
#     sfr.load_encoding_images("images/")
#     engine = pyttsx3.init('sapi5')
#     voices = engine.getProperty('voices')
#     engine.setProperty('voice', voices[1].id)
#
#     def speak(audio):
#         engine.say(audio)
#         engine.runAndWait()
#
#     # Load Camera
#     cap = cv2.VideoCapture(0)
#
#     i1 = 0
#     list2 = ["farhaan", "mushu", "Jeff Bezoz", "Ryan Reynolds", "Elon Musk", "faizan", "junaid", "siddiq", "ali",
#              "taheer", "tarun", "tenzing", "nishmitha", "gokul"]
#     string_date = str(present_date)
#     folder_loc = os.getcwd()
#     attendance_data = f"attendance{string_date}.csv"
#     directories = os.listdir()
#     if attendance_data not in directories:
#         f1 = open(attendance_data, "w+")
#         st = "name,time1,date1"
#         read = f1.readline()
#         print(read)
#         print("sasa")
#         if read != st:
#             print("gfg")
#             f1.write(f'name,time1,date1')
#         f1.close()
#     print(folder_loc)
#
#     # global name
#     # person_attendance = name+".csv"
#     # per = open(person_attendance, "w+")
#     # st = "name,time1,date1"
#     # if per.readline() != st:
#     #     per.write("assa")
#     #     per.write("name,time1,date1")
#     # per.close()
#
#     def attendance(name):
#         # with open(person_attendance, "r+") as per1:
#         #     data1 = per1.readlines()
#         #     namelist1 = []
#         #     datelist1 = []
#         #     for line in data1:
#         #         entry1 = line.split(",")
#         #         namelist1.append(entry1[0])
#         #         datelist1.append(entry1[2])
#         #     if datelist1!=new_date:
#         #         per1.write(f'\n{name},{strTime},{new_date}')
#         # per1.close()
#         name_file = name + ".csv"
#         folder_loc1 = os.getcwd()
#         directories = os.listdir()
#         if name_file not in directories:
#             f11 = open(name_file, "w+")
#             st1 = "name,time1,date1"
#             read1 = f11.readline()
#             print(read1)
#             print("sasa")
#             if read1 != st1:
#                 print("gfg")
#                 f11.write(f'name,time1,date1')
#             f11.close()
#
#         with open(name_file, "r+") as fn:
#             data_fn = fn.readlines()
#             namelist_fn = []
#             datelist_fn = []
#             for line1 in data_fn:
#                 entry = line1.split(",")
#                 namelist_fn.append(entry[0])
#                 datelist_fn.append(entry[2])
#             if new_date not in datelist_fn:
#                 fn.write(f'\n{name},{strTime},{new_date}')
#                 fn.close()
#
#         with open(attendance_data, "r+") as f:
#             data = f.readlines()
#             namelist = []
#             datelist = []
#             for line in data:
#                 entry = line.split(",")
#                 namelist.append(entry[0])
#                 datelist.append(entry[2])
#             if name not in namelist:
#                 f.write(f'\n{name},{strTime},{new_date}')
#                 f.close()
#
#     while True:
#         ret, frame = cap.read()
#         # Detect Faces
#         face_locations, face_names = sfr.detect_known_faces(frame)
#
#         for face_loc, name in zip(face_locations, face_names):
#             y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
#
#             cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
#             cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
#
#             for li in list2:
#
#                 if name == li:
#                     with open(attendance_data, "r+") as f:
#                         data = f.readlines()
#                         namelist = []
#                         for line in data:
#                             entry = line.split(",")
#                             namelist.append(entry[0])
#                         if name not in namelist:
#                             word = name, "has logged in at", strTime
#                             speak(word)
#                     attendance(name)
#
#         cv2.imshow("Frame", frame)
#
#         key = cv2.waitKey(1)
#         if key == 27:
#             break
#
#     cap.release()
#     cv2.destroyAllWindows()
#
#     pass
#
#
# def new_user_add():
#     # import subprocess
#     # t.showinfo("info","Please note that while uploading image please upload it with student name also")
#     # filename = askopenfilename()
#     # print(filename)
#     # filename1 = r'{}'.format(filename)
#     # subprocess.run(["powershell", "-command", filename1], shell=True)
#     # ima = r'C:\Users\mubashir ahmed\PycharmProjects\source code\images'
#     # dir = (os.listdir(r'C:\Users\mubashir ahmed\PycharmProjects\source code\images'))
#     # str1 = os.path.split(filename1)[1]
#     #
#     # for i in dir:
#     #     if str1 == i:
#     #         t.showwarning("user name already exists","name and picture already exists please select other name")
#     #     else:
#     #         shutil.copy(filename1, ima)
#     pass
#
#
# def delete():
#     # import subprocess
#     # root.destroy()
#     # def user_delte():
#     #     dir = (os.listdir(r'C:\Users\mubashir ahmed\PycharmProjects\source code\images'))
#     #     # str1 = os.path.split(filename1)[1]
#     #     print(user_value.get())
#     #     for i in dir:
#     #         dir1=i.split(".")[0]
#     #         print(dir1)
#     #         if user_value.get() == dir1:
#     #             user_pic_delete = r'C:\Users\mubashir ahmed\PycharmProjects\source code\images\{}'.format(i)
#     #             subprocess.run(["powershell", "-command", user_pic_delete], shell=True)
#     #
#     #             os.remove(user_pic_delete)
#     #     else:
#     #             t.showwarning("error","Name doesnt exists" )
#     #
#     #
#     #     # user_pic_delete = r'C:\Users\mubashir ahmed\PycharmProjects\source code\images\{}'.format(
#     #     #     user_value.get()
#     #     #     + ".jpg")
#     #     # subprocess.run(["powershell", "-command", user_pic_delete], shell=True)
#     #     # os.remove(user_pic_delete)
#     #
#     #     # try:
#     #     #     os.remove(user_pic_delete)
#     #     # else:
#     #     #     user_pic_delete = r'C:\Users\mubashir ahmed\PycharmProjects\source code\images\{}'.format( user_value.get()+".jpeg")
#     #     #     subprocess.run(["powershell", "-command", user_pic_delete], shell=True)
#     #     #     os.remove(user_pic_delete)
#     #
#     # del_root=Tk()
#     # Label(text="DELETE USER").grid(row=0,column=1)
#     # user_delte_name=Label(text="USERNAME")
#     # user_delte_name.grid(row=1,column=1)
#     # user_value=StringVar()
#     # user_delte_name_value=Entry(textvariable=user_value)
#     # user_delte_name_value.grid(row=1,column=2)
#     # user_delte_name_button=Button(text="DELETE USER",command=user_delte)
#     # user_delte_name_button.grid(row=2,column=2)
#     # del_root.mainloop()
#     pass
#
#
# # def get_attendance_bystudent:
# # def get_student1:
# #     student_search_name=student_name.get()
# #     student_search_file=f'{student_search_name}.csv'
# #     print(student_search_file)
# #     with open(student_search_file,"r+") as new:
# #         new_readline_list=[]
# #
# # root_new=Tk()
# # enter_student=Label(root_new,text="ENTER STUDENT NAME:")
# # enter_student.grid(row=0,column=0)
# # student_name=StringVar()
# # entry_student=Entry(root_new,textvariable=student_name)
# # entry_student.grid(row=0,column=1)
# # search_button=Button(root_new,text="SEARCH",command=get_student1)
# # root_new.mainloop()
# def get_attendance_bystudent1():
#     from PIL import Image, ImageTk
#
#     def get_student1():
#         student_search_name = student_name.get()
#         student_search_file = f'{student_search_name}.csv'
#         print(student_search_file)
#         with open(student_search_file, "r+") as new:
#             new_readline_list = []
#             data1 = new.readlines()
#             i = 0
#             for dat in data1:
#                 i += 1
#             i =  i
#             print(i)
#             i1.set(i)
#             label5.update()
#     root.destroy()
#     root_new = Tk()
#     fraem1 = Frame(root_new)
#     fraem1.pack()
#     root_new1 = Frame(root_new)
#     root_new1.pack()
#     enter_student = Label(fraem1, text="ENTER STUDENT NAME:")
#     enter_student.grid(row=0, column=0)
#     student_name = StringVar()
#     entry_student = Entry(fraem1, textvariable=student_name)
#     entry_student.grid(row=0, column=1)
#     search_button = Button(fraem1, text="SEARCH", command=get_student1)
#     search_button.grid(row=0, column=2)
#     adarsh_college11 = Image.open("J.png")
#     re111 = adarsh_college11.resize((200, 200), Image.ANTIALIAS)
#     ada = ImageTk.PhotoImage(re111)
#     picture21 = Label(root_new1, image=ada)
#     picture21.grid(row=1, column=1)
#     label1 = Label(root_new1, text="Name", borderwidth=6, relief=GROOVE)
#     label1.grid(row=1, column=2)
#     label2 = Label(root_new1, text="Course", borderwidth=6, relief=GROOVE)
#     label2.grid(row=1, column=3)
#     label3 = Label(root_new1, text="Sem", borderwidth=6, relief=GROOVE)
#     label3.grid(row=1, column=4)
#     label4 = Label(root_new1, text="Total days", borderwidth=6, relief=GROOVE)
#     label4.grid(row=1, column=5)
#     i1 = StringVar()
#     i1.set("no")
#     label5 = Label(root_new1, textvariable=i1, borderwidth=6, relief=GROOVE)
#     label5.grid(row=1, column=6)
#     root_new.mainloop()
#
#
# root = Tk()
# # root.configure(bg="#1E130C")
# root.configure(bg="black")
# root.title("AUTO ATTENDANCE ")
# # root.geometry("382x250")
# root.minsize(1000, 540)
# root.maxsize(1000, 540)
# main_frame_top = Frame(root, bg="grey", borderwidth=6)
# main_frame_top.pack(fill=X)
# adarsh_logo = Image.open("adarshlogoo.png")
# resize_logo = adarsh_logo.resize((300, 100), Image.ANTIALIAS)
# adarsh_log = ImageTk.PhotoImage(resize_logo)
# picture1 = Label(main_frame_top, image=adarsh_log)
# picture1.grid(row=0, column=0)
# main_frame_top2 = Frame(main_frame_top, bg="grey")
# main_frame_top2.grid(row=0, column=1)
# attendance_label = Label(main_frame_top2, text="ADARSH COLLEGE ATTENDANCE MANAGEMENT SYSTEM  ", bg="grey", fg="white",
#                          font="comicsansms 17 bold", pady=10, padx=10)
#
# attendance_label.grid(row=0)
# import datetime
#
# date = datetime.datetime.now()
# date12 = str(date).split(" ")
# date2 = date12[0]
#
# test = Label(main_frame_top2, text=date2, font="comicsansms 22 bold", bg="grey")
# test.grid(row=1, column=0)
# frame_button_top = Frame(root)
# frame_button_top.pack()
# frame_button_top1 = Frame(root, borderwidth=1, relief='solid', bg="grey", height=5)
# frame_button_top1.pack(fill=X)
#
# add_user = Button(frame_button_top, text="        ADD NEW USER  ", command=new_user_add, padx=120)
# add_user.grid(row=0, column=1)
# delete_button = Button(frame_button_top, text="           DELETE           ", command=delete, padx=120)
# delete_button.grid(row=0, column=2)
# exit_button = Button(frame_button_top, text="           exit           ", command=quit, padx=120)
# exit_button.grid(row=0, column=3)
# middle_frame = Frame(root, bg="black")
# middle_frame.pack(fill=X)
# left_frame = Frame(middle_frame, bg="black")
# left_frame.grid(row=0, column=0)
# right_frame = Frame(middle_frame)
# right_frame.grid(row=0, column=1, padx=10)
# start_button = Button(left_frame, text="    START   ", command=start, padx=7, bg="grey", font="bold")
# start_button.grid(row=3, column=0)
# text = Label(left_frame, text="ATTENDANCE BY FACE DETECTION\n"
#                               "MADE EASY FOR JUSt\n"
#                               "CLICK ON THE START BUTTON\n "
#                               "TO START ATTENDANCE\n ",
#              font="comicsansms 22 bold", fg="white", bg="black")
# text.grid(row=0, column=0)
# adarsh_college = Image.open("adarshcollege.jpg")
# re = adarsh_college.resize((500, 300), Image.ANTIALIAS)
# adarsh_college_image = ImageTk.PhotoImage(re)
# picture2 = Label(right_frame, image=adarsh_college_image)
#
# picture2.grid(row=0, column=4)
# frame_button_dowm1 = Frame(root, borderwidth=1, relief='solid', bg="grey", height=5)
# frame_button_dowm1.pack(fill=X)
# frame_button_dowm = Frame(root, borderwidth=1, relief='solid', bg="black")
# frame_button_dowm.pack(fill=X)
# get_attedance = Button(frame_button_dowm, text="       GET ATTENDANCE       ", command=quit, padx=180)
# get_attedance.grid(row=0, column=0)
# getstudentattandance = Button(frame_button_dowm, text="           GET ATTENDANCE OF STUDENT           ",
#                               command=get_attendance_bystudent1, padx=220)
# getstudentattandance.grid(row=0, column=2)
# frame_dowm1 = Frame(root, borderwidth=1, relief='solid', bg="grey")
# frame_dowm1.pack(fill=X)
# label1 = Label(frame_dowm1, text="For any help- \n"
#                                  "\tgmail:mushuu123456@gmail.com\n"
#                                  "contact:8888888888888"
#                , bg="grey")
# label1.grid(row=0, column=0)
# root.mainloop()
