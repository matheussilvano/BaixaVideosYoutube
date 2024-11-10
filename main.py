import pytubefix
import ffmpeg
import tkinter as tk
from tkinter import messagebox

def baixar_video():
    url = entrada_link.get("1.0", "end-1c")
    formato = formato_var.get()

    if not url:
        messagebox.showerror("Erro", "Nenhum Link foi inserido.")
        return
    
    try:
        yt = pytubefix.YouTube(url)
        if formato == "wav":
            filename = "audio.wav"
            stream = yt.streams.filter(only_audio=True).first().url
            ffmpeg.input(stream).output(filename, format='wav', loglevel="error").run()
            messagebox.showinfo("Sucesso", "Áudio baixado com sucesso em formato WAV!")

        elif formato == "mp3":
            filename = "audio.mp3"
            stream = yt.streams.filter(only_audio=True).first().url
            ffmpeg.input(stream).output(filename, format='mp3', loglevel="error").run()
            messagebox.showinfo("Sucesso", "Áudio baixado com sucesso em formato MP3!")

        elif formato == "mp4":
            filename = "video.mp4"
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first().url
            ffmpeg.input(stream).output(filename, format='mp4', loglevel="error").run()
            messagebox.showinfo("Sucesso", "Vídeo baixado com sucesso em formato MP4!")
        
        else:
            messagebox.showerror("Erro", "Formato inválido selecionado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    

root = tk.Tk()

root.geometry("800x500") 
root.title("Baixar vídeos do Youtube")

fonte_principal = 'Arial'
tamanho_fonte_botoes = 12
width_botoes = 25
height_botoes = 3

titulo = tk.Label(root, text="Baixar vídeos do Youtube", font=(fonte_principal, 20))
titulo.pack(pady=15)

titulo_inserir_link = tk.Label(root, text="Insira o Link do vídeo:", font=(fonte_principal, 12))
titulo_inserir_link.pack(padx=10, pady=10)

entrada_link = tk.Text(root, width=width_botoes, height=1, font=(fonte_principal, tamanho_fonte_botoes))
entrada_link.pack(padx=10)

titulo_selecionar_formato = tk.Label(root, text="Selecione o formato:", font=(fonte_principal, 12))
titulo_selecionar_formato.pack(padx=10, pady=10)

formato_var = tk.StringVar()

botao_wav = tk.Radiobutton(root, text='Wav (Áudio)', variable=formato_var, value='wav', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes))
botao_wav.pack(padx=10, pady=5)

botao_mp3 = tk.Radiobutton(root, text='MP3 (Áudio)', variable=formato_var, value='mp3', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes))
botao_mp3.pack(padx=10, pady=5)

botao_mp4 = tk.Radiobutton(root, text='MP4 (Vídeo)', variable=formato_var, value='mp4', width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes))
botao_mp4.pack(padx=10, pady=5)

botao_baixar = tk.Button(root, text="Baixar", command=baixar_video, width=width_botoes, height=height_botoes, font=(fonte_principal, tamanho_fonte_botoes))
botao_baixar.pack(pady=20)


root.mainloop()
