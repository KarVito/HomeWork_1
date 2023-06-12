import sys, os, shutil, re
from pathlib import Path


if len(sys.argv) == 1:
    print("Enter argument!!!")
else:    
    work_path = sys.argv[1]
    p = Path(work_path)
    Prime_list = []
    for i in p.iterdir():
        print(i, i.name)
        Prime_list.append(i.name)
    

    if os.path.exists(work_path + "/archives") == False:
        os.mkdir(work_path + "/archives")
        if os.path.exists(work_path + "/video") == False:     
            os.mkdir(work_path + "/video")
            if os.path.exists(work_path + "/audio") == False:     
                os.mkdir(work_path + "/audio")
                if os.path.exists(work_path + "/documents") == False:     
                    os.mkdir(work_path + "/documents")
                    if os.path.exists(work_path + "/images") == False:     
                        os.mkdir(work_path + "/images")
    
    LIST_images = {"images": ('.jpeg', '.png', '.jpg', '.svg')}
    LIST_video = {"video": ('.avi', '.mp4', '.mov', '.mkv')}
    LIST_documents = {"documents": ('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.xls', '.pptx')}
    LIST_audio = {"audio": ('.avi', '.mp3', '.mov', '.mkv')}
    LIST_archives = {"archives": ('.zip', '.gz', '.tar', '.rar')}
   
    
    def normalize(file_old_name):
        
        CYRILLIC_SYMBOLS = ("а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", 
               "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я", "є", "і", "ї", "ґ")
        TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g")
            
        TRANS = {}
        for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
            TRANS[ord(c)] = l
            TRANS[ord(c.upper())] = l.upper()
        
        file_new_name = file_old_name.translate(TRANS)
        file_new_name = re.sub('[^a-zA-Z0-9]', '_', file_new_name) 
        return file_new_name
    
    for Inf in Prime_list:
        pp = work_path + "/" + Inf
        print(pp)
        if os.path.isfile(pp) == True:
            for i in LIST_images.values():
                print("Testing for 'images'!!!")
                for ii in i:
                    file_name = Path(pp).name.replace(Path(pp).suffix, "")
                    new_file_name = normalize(file_name)
                    if ii == Path(pp).suffix:
                        shutil.move(pp, work_path + "/images/"+ new_file_name+ii)
                        break
            for i in LIST_video.values():
                print("Testing for 'video'!!!")
                for ii in i:
                    file_name = Path(pp).name.replace(Path(pp).suffix, "")
                    new_file_name = normalize(file_name)
                    if ii == Path(pp).suffix:
                        shutil.move(pp, work_path + "/video/"+ new_file_name+ii)
                        break
            for i in LIST_documents.values():
                print("Testing for 'documents'!!!")
                for ii in i:
                    file_name = Path(pp).name.replace(Path(pp).suffix, "")
                    new_file_name = normalize(file_name)
                    if ii == Path(pp).suffix:
                        shutil.move(pp, work_path + "/documents/"+ new_file_name+ii)
                        break
            for i in LIST_audio.values():
                print("Testing for 'audio'!!!")
                for ii in i:
                    file_name = Path(pp).name.replace(Path(pp).suffix, "")
                    new_file_name = normalize(file_name)
                    if ii == Path(pp).suffix:
                        shutil.move(pp, work_path + "/audio/"+ new_file_name+ii)
                        break
            for i in LIST_archives.values():
                print("Testing for 'archives'!!!")
                for ii in i:
                    file_name = Path(pp).name.replace(Path(pp).suffix, "")
                    new_file_name = normalize(file_name)
                    if ii == Path(pp).suffix:
                        shutil.move(pp, work_path + "/archives/" + new_file_name + ii)
                        shutil.unpack_archive(work_path + "/archives/" + new_file_name + ii, work_path + "/archives/" + new_file_name)
                        os.remove(work_path + "/archives/" + new_file_name + ii)
                        break                                                                            
            