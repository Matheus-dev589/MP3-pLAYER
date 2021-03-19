# Importação de bibliotecas
 
from tkinter import*
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
from tkinter import filedialog

# Cores e fontes usadas

# Cores

CORDEFUNDO = "#282828" # Cinza Escuro
CORDAFONTE = "#CECECE" # Branco Escuro
CORDASONGBOX = "#180219" # Roxo Escuro
CORDAMUSICASELECIONADA = "#5E5E5E" # Cinza Clao
CORDABARRADESTATUS = "#181818" # Preto Escuro

# Fontes

FONTE = "Bandar"

# Configurações da janela 

Janela = Tk()
Janela.title ('Player bat')
Janela.geometry ('500x420')
Janela.resizable (width = FALSE, height=FALSE)
Janela.configure (bg = CORDEFUNDO)
Janela.iconbitmap('Python\musica\Img\icone\Bat.ico')

# Pygame mixer  

pygame.mixer.init()

# Barra de duração

def play_time():
   
    if stopped :
        return

    current_time = pygame.mixer.music.get_pos() / 1000
    
    # Exibir duração da música no formato padrão de tempo
    
    converted_current_time = time.strftime('%H:%M:%S', time.gmtime(current_time))
   
    # Exibir tempo decorrido e restante da música

    current_song = song_box.curselection()
   
    song = song_box.get(ACTIVE)

    song = song_box.get(current_song)
   
    song = f'C:/Users/matheus/Music/{song}.mp3'
    song_mut = MP3(song)
    
    global song_lenght

    song_lenght = song_mut.info.length
    converted_song_lenght = time.strftime('%H:%M:%S', time.gmtime(song_lenght))
 
    current_time +=1
    
    if int(SLIDER.get()) == int(song_lenght):
        
        BARRA.config(text = f'{converted_song_lenght}')

    elif paused:
        pass

    elif int(SLIDER.get()) == int(current_time):

        Slider_position = int(song_lenght)
        SLIDER.config(to = Slider_position, value = int(current_time))

    else:

        Slider_position = int(song_lenght)
        SLIDER.config(to = Slider_position, value = int(SLIDER.get()))

            # Exbir duração da musica no formato padrão de tempo
    
        converted_current_time = time.strftime('%H:%M:%S', time.gmtime(int(SLIDER.get())))

        BARRA.config(text = f'{converted_current_time}                                                                                        {converted_song_lenght}')

        next_time = int(SLIDER.get()) +1
        SLIDER.config(value = next_time)
    
    BARRA.after(1000, play_time)

# Configurações do menu de adição de músicas

def add_song():
   
    songs = filedialog.askopenfilenames(initialdir= 'C:/', title = "Escolha uma música bacana", filetypes = (("mp3 Files", "*.mp3"),))
   
    for song in songs: 

        # Ocultar Caminho e extensão do arquivo

        song = song.replace("C:/Users/matheus/Music/", "")
        song = song.replace(".mp3", "")

        song_box.insert(END, song)
 
# Apagar uma ou mais músicas

# Apagar somente uma música

def apagar_musica():
   
    PARAR()

    # Apagar a música selecionada

    song_box.delete(ANCHOR)
    
    # Parar de tocar a música ao apagar

    pygame.mixer.music.stop()

# Apagar todas as músicas

def apagar_todas_musica():
    
    PARAR()

    # Parar de tocar a música ao apagar

    song_box.delete(0, END)

    # Parar de tocar a música ao apagar

    pygame.mixer.music.stop()

# Tocar música

def TOCAR():
    
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'C:/Users/matheus/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)

    # Mostrar a duração da música ao tocar

    play_time()

# Parar música

# Variável global de parada

global stopped
stopped = False

def PARAR():
    
    # Reiniciar a barra de progresso ao apertar o botão parar

    BARRA.config(text = '')
    SLIDER.config(value = 0)

    # Parar a música que esta tocando

    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    # Limpar textos da barra de duração ao apertar botão parar

    BARRA.config(text = '')

    # Variável global de parada para quando clicarem no botão parar

    global stopped
    stopped = True

# Ir para próxima música

def PROXIMO ():
    
    # Reiniciar a barra de progresso ao apertar o botão parar

    BARRA.config(text = '')
    SLIDER.config(value = 0)

    next = song_box.curselection()
    next = next[0]+1
    song = song_box.get(next)
   
    song = f'C:/Users/matheus/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)

    # Fazer com que seja mostrado na tela quando a música for trocada

    song_box.selection_clear(0, END)

    song_box.activate(next)

    song_box.selection_set(next, last = None)
    
# Ir para a musica anterior

def RETORNAR():

    # Reiniciar a barra de progresso ao apertar o botao parar

    BARRA.config(text = '')
    SLIDER.config(value = 0)

    next = song_box.curselection()
    next = next[0]-1
    song = song_box.get(next)
   
    song = f'C:/Users/matheus/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0)

    # Fazer com que seja mostrado na tela quando a música for trocada

    song_box.selection_clear(0, END)

    song_box.activate(next)

    song_box.selection_set(next, last = None)

# Definindo variável global de pause, para usar em outras partes do código além da parte dedicado ha pausar os áudios

global paused
paused = False

# Pausar e despausar a musica

def PAUSAR(is_paused):

    global paused

    paused = is_paused

    if paused:

        # Despausar musica

        pygame.mixer.music.unpause()
        paused = False

    else:

        # Pausar musica

        pygame.mixer.music.pause()
        paused = True

# Controle deslizante

def ROLAR(x):

    # O código vai permitir que o usuário controle em qual parte da música ele quer estar, com a ajuda do controle deslizante

    song = song_box.get(ACTIVE)
    song = f'C:/Users/matheus/Music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops = 0, start = int(SLIDER.get()))


# Lista de reprodução

song_box = Listbox(Janela, bg = CORDASONGBOX, fg = CORDAFONTE, font = FONTE, width = 50, bd = 0, selectbackground="#5E5E5E")
song_box.pack(pady = 20)

# Definindo ícone dos botoes

VOLTAR = PhotoImage(file = 'Python\musica\Img\Botoes\Back.png')
AVANCAR = PhotoImage(file = 'Python\musica\Img\Botoes\AVANCAR.png')
PLAY = PhotoImage(file = 'Python\musica\Img\Botoes\PLAY.png')
STOP = PhotoImage(file = 'Python\musica\Img\Botoes\STOP.png')
PAUSE = PhotoImage(file = 'Python\musica\Img\Botoes\PAUSE.png')

# Painel de controle

PAINEL = Frame(Janela)
PAINEL.pack()

# Inserindo botes na interface

BTN_VOLTAR = Button(PAINEL, image=VOLTAR, borderwidth=0, bg=CORDEFUNDO, command = RETORNAR)
BTN_PARAR = Button(PAINEL, image=STOP, borderwidth=0, bg=CORDEFUNDO, command = PARAR)
BTN_PAUSE = Button(PAINEL, image=PAUSE, borderwidth=0, bg=CORDEFUNDO, command = lambda: PAUSAR(paused))
BTN_PLAY = Button(PAINEL, image=PLAY, borderwidth=0, bg=CORDEFUNDO, command = TOCAR)
BTN_AVANCAR = Button(PAINEL, image=AVANCAR, borderwidth=0, bg=CORDEFUNDO, command = PROXIMO)

# Definindo a posição dos botoes na tela

BTN_VOLTAR.grid(row=0, column=0) 
BTN_PARAR.grid(row=0, column=1)
BTN_PAUSE.grid(row=0, column=2)
BTN_PLAY.grid(row=0, column=3)
BTN_AVANCAR.grid(row=0, column=4)

# Criando menu

MENU = Menu(Janela)
Janela.config(menu = MENU)

# Menu de adição de músicas

ADD_MUSICA = Menu(MENU)
MENU.add_cascade(label = "Adicionar musicas", menu = ADD_MUSICA)
ADD_MUSICA.add_command(label = "Adicionar uma ou mais musicas a playlist", command = add_song)

# Menu de remoção de músicas
 
remover_musica = Menu(MENU)
MENU.add_cascade(label="Remover Musica", menu=remover_musica)
remover_musica.add_command(label="Excluir uma musica da playlist", command = apagar_musica)
remover_musica.add_command(label="Excluir todas as musicas da playlist", command = apagar_todas_musica)

# Controle deslizante de tempo

SLIDER = ttk.Scale(Janela, from_= 0 , to = 100, orient = HORIZONTAL, value =0, command = ROLAR, length = 5)
SLIDER.pack(fill = X,side = BOTTOM, pady = 5 )

# Barra de duração

BARRA = Label(Janela, font="Bandar 13", text='', bd=0, relief=GROOVE, anchor= CENTER, bg="#181818", width = 17, fg = "#D7DBDD")
BARRA.pack(fill=X, side=BOTTOM, ipady= 17)
 
# Fim do programa

Janela.mainloop()