import os, glob
File_exist = os.path.isfile("C:/Users/Vitaliy/Desktop/Study/lesson_6/Хлам/")
print(File_exist)


for root, dirs, files in os.walk("C:/Users/Vitaliy/Desktop/Study/lesson_6/Хлам"):  
    #for filename in files:
    #    print(filename)
    for rootnames in root:   
        print(root)