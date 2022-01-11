print(
    '''
                             __
               ---_ ...... _/_ -
              /  .      ./ .'*\ \ 
              : '         /__-'   \.
             /                      )
           _/                  >   .'
         /   .   .       _.-" /  .'
         \           __/"     /.'/|
           \ '--  .-" /     //' |\|
            \|  \ | /     //_ _ |/|
             `.  \:     //|_ _ _|\|
             | \/.    //  | _ _ |/| 
              \_ | \/ /    \ _ _ \\\ 
                  \__/      \ _ _ \|\ 
   '''
)

# Libraries

import os

os.system("pip install GTTs")
os.system("pip install pYfiGlEt")
os.system("cls")
import pyfiglet

sound = pyfiglet.figlet_format("Text --> audio")
print(sound)

from gtts import gTTS

print("read file [1] input text [2]")
ask = input("choose the options: ")

if ask == "1":
    print("""\033[0;31m
             ______________________________________
            | Language abbreviations:              |
            |  Arabic=  ar                         |
            |  English= en                         |
            |  Spanish= es                         |
            |  French=  fr                         |
            |                                      |
            |______________________________________|
            
            """)

    file = open(input("enter the file name :"), "r")
    language = input("enter the language: ")
    read = file.read()
    tts = gTTS(read, lang=language)
    a = "sound"
    tts.save(a + '.mp3')  
    # os.system(a+".mp3")
elif ask == "2":
    print("""\033[0;31m
             ______________________________________
            | Language abbreviations:              |
            |  Arabic=  ar                         |
            |  English= en                         |
            |  Spanish= es                         |
            |  French=  fr                         |
            |                                      |
            |______________________________________|
            
            """)
    tts = gTTS(input("\033[0;34MenTer the text : "), lang=input("enter the LaNguGe --> "))
    a = "sound"
    tts.save(a + '.mp3')  
    # os.system(a+".mp3")
