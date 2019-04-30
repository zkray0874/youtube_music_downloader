
import youtube_dl
import ffmpeg
import re
import os
import shutil
from youtube_dl_Gui import*


def opts_path(path):
    option = {
        'format': 'bestaudio/best',
        'username': 'toby.olime@gmail.com',
        'password': '08740608',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'noplaylist': True
    }
    option['outtmpl'] = path

    return option


L_path = r'D:\Song for kids\Leona\%(title)s.%(etx)s'
E_path = r'D:\Song for kids\Eliana\%(title)s.%(etx)s'
C_path = r'D:\Song for kids\Cedrik\%(title)s.%(etx)s'
my_path = r'D:\Music\%(title)s.%(etx)s'

ydl_opts_L = opts_path(L_path)
ydl_opts_E = opts_path(E_path)
ydl_opts_C = opts_path(C_path)
ydl_opts_my = opts_path(my_path)


path_dict = {
    'L': r'D:\Song for kids\Leona', 'l': r'D:\Song for kids\Leona',
    'E': r'D:\Song for kids\Eliana', 'e': r'D:\Song for kids\Eliana',
    'C': r'D:\Song for kids\Cedrik', 'c': r'D:\Song for kids\Cedrik',
    'T': r'D:\Music', 't': r'D:\Music',

}

user = input("""

This is a music download program for my baby kids
===================================================
        Enter L to get music for Leona
        Enter E to get music for Eliana
        Enter C to get music for Cedrik
        Enter A to get music for everybody
===================================================

Enter here:"""
             )

pat = re.compile(r'^[LlEeCcAaTt]?[LlEeCcAaTt][LlEeCcAaTt]?$')

while re.match(pat, user) == None:
    print("""    Entered wrong letter, do it again!!!""")
    user = input(
        """===================================================
    Enter \u261bL \u261a to get music for Leona
    Enter \u261bE \u261a to get music for Eliana
    Enter \u261bC \u261a to get music for Cedrik
    Enter \u261bA \u261a to get music for everybody
===================================================

Enter here:""")


url = input("Then enter the music URL:")
while not url:
    print("""
    =====================================================
         \u2620\u2620\u2620  You enter nothing!!!!  \u2620\u2620\u2620
    =====================================================
            """)
    url = input("Enter a valid music URL:")

url_list = url.split(' ')
cwd = os.getcwd()
path_t = os.path.join(cwd, 'e04su3su;6')
T_path = r'{}\%(title)s.%(etx)s'.format(path_t)
ydl_opts_T = opts_path(T_path)
while True:
    try:
        if len(user) == 1:
            if re.match(r'[Ll]', user):
                for i in url_list:
                    with youtube_dl.YoutubeDL(ydl_opts_L) as ydl:
                        ydl.download([i])
                break

            elif re.match(r'[Ee]', user):
                for i in url_list:
                    with youtube_dl.YoutubeDL(ydl_opts_E) as ydl:
                        ydl.download([i])
                break

            elif re.match(r'[Tt]', user):
                for i in url_list:
                    with youtube_dl.YoutubeDL(ydl_opts_my) as ydl:
                        ydl.download([i])
                break

            elif re.match(r'[Cc]', user):
                for i in url_list:
                    with youtube_dl.YoutubeDL(ydl_opts_C) as ydl:
                        ydl.download([i])
                break

            elif re.match(r'[Aa]', user):
                os.mkdir(path_t)
                for i in url_list:
                    with youtube_dl.YoutubeDL(ydl_opts_T) as ydl:
                        ydl.download([i])
                    for source_name in os.listdir(path_t):
                        for name in 'LEC':
                            source_file_path = os.path.join(path_t, source_name)
                            shutil.copy(source_file_path, path_dict[name])
                shutil.rmtree(path_t)
                break

        elif len(user) > 1:
            os.mkdir(path_t)
            for i in url_list:
                with youtube_dl.YoutubeDL(ydl_opts_T) as ydl:
                    ydl.download([i])
                for source_name in os.listdir(path_t):
                    for name in user:
                        source_file_path = os.path.join(path_t, source_name)
                        shutil.copy(source_file_path, path_dict[name])
            shutil.rmtree(path_t)
            break

    except:
        if len(user) > 1:
            shutil.rmtree(path_t)
        print("""
    =====================================================
         \u2620\u2620\u2620  Invalid URL!!!!  \u2620\u2620\u2620
    =====================================================
            """)
        url = input("Enter a valid music URL:")
        url_list = url.split(' ')


print("""
=====================================================
              Download complete!!!!
=====================================================
            """)

app = QApplication(sys.argv)
ex = youtube_dl_Gui()
sys.exit(app.exec_())
