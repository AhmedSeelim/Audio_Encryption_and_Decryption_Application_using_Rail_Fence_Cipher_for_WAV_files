import tkinter as tk
from tkinter import messagebox , filedialog
import voice as vc
import rail_fence as rs

# def record_audio(file_name):
#     audio_data=vc.record_audio()
#     vc.write_audio_file(audio_data, file_name+".wav")
#     messagebox.showinfo("Save audio", f"Audio saved to file: {file_name}.wav")


def encrypt_audio_from_record( key,file_name):
    audio_data=vc.record_audio()
    encry_matrix=rs.encrypt_rail_fence(audio_data,int(key))
    vc.write_audio_file(encry_matrix,file_name+".wav")
    messagebox.showinfo("Audio Encryption", "Encrypted audio display")
    vc.play_audio_file(file_name + ".wav")



def encrypt_audio_from_pc( key,file_name):
    audio_file = filedialog.askopenfilename()

    file_matrix=vc.wave_to_matrix(audio_file)
    encry_matrix=rs.encrypt_rail_fence(file_matrix,int(key))
    vc.write_audio_file(encry_matrix,file_name+".wav")
    messagebox.showinfo("Audio Encryption", "Encrypted audio display")
    vc.play_audio_file(file_name + ".wav")




def decrypt_audio_from_pc( key,file_name):
    audio_file = filedialog.askopenfilename(filetypes=[(" WAV", "*.wav")])
    file_matrix=vc.wave_to_matrix(audio_file)
    encry_matrix=rs.decrypt_rail_fence(file_matrix,int(key))
    vc.write_audio_file(encry_matrix,file_name+".wav")
    messagebox.showinfo("Audio Decryption", "Decrypted audio display")
    vc.play_audio_file(file_name + ".wav")

window = tk.Tk()
window.title(" Audio Encryption App")


window.geometry("700x500")

bg_image = tk.PhotoImage(file="IMG_20230511_155203_448.png")
bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)



audio_file_label = tk.Label(window, text="Enter the name of the encrypted audio file :",fg="blue")
audio_file_label.pack(pady=(60,0),anchor="w")
audio_file_entry = tk.Entry(window)
audio_file_entry.pack(anchor="w")

key_label = tk.Label(window, text="enter Encryption key :",fg="blue")
key_label.pack(anchor="w")
key_entry = tk.Entry(window)
key_entry.pack(anchor="w")


rec_and_encrypt_button = tk.Button(window, text="Audio recording and encryption", command=lambda: [encrypt_audio_from_record(key_entry.get() ,audio_file_entry.get())])
rec_and_encrypt_button.pack(pady=(0,20),anchor="w")




audio_file_label2 = tk.Label(window, text="Enter the name of the encrypted audio file :",fg="blue")
audio_file_label2.pack(anchor="w")
audio_file_entry2 = tk.Entry(window)
audio_file_entry2.pack(anchor="w")

key_label2 = tk.Label(window, text="enter Encryption key :",fg="blue")
key_label2.pack(anchor="w")
key_entry2 = tk.Entry(window)
key_entry2.pack(anchor="w")

load_and_encrypt_button = tk.Button(window, text="Upload and encrypt the audio file", command=lambda: [encrypt_audio_from_pc(key_entry2.get() ,audio_file_entry2.get())])
load_and_encrypt_button.pack(pady=(0,20),anchor="w")




audio_file_label3 = tk.Label(window, text="Enter the name of the decrypted audio file :",fg="blue")
audio_file_label3.pack(anchor="w")
audio_file_entry3 = tk.Entry(window)
audio_file_entry3.pack(anchor="w")

key_label2 = tk.Label(window, text="enter Decryption key :",fg="blue")
key_label2.pack(anchor="w")
key_entry3 = tk.Entry(window)
key_entry3.pack(anchor="w")

load_and_decrypt_button = tk.Button(window, text="Upload and decrypt the audio file", command=lambda: [decrypt_audio_from_pc(key_entry3.get() ,audio_file_entry3.get())])
load_and_decrypt_button.pack(pady=(0,20),anchor="w")

# window.update()
# bg_label.configure(width=window.winfo_width(), height=window.winfo_height())

window.mainloop()




#cipher_text = [char for rail in fence for char in rail if char != 'c']