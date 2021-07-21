import socket
import tkinter as tk
from tkinter import font
from tkinter import ttk
from tkinter import filedialog
import time
import threading
import os


class GUI:

    def __init__(self, ip_address, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect((ip_address, port))

        self.Window = tk.Tk()
        self.Window.withdraw()

        self.login = tk.Toplevel()

        self.login.title("Welcome Page")
        self.login.resizable(width=False, height=False)
        self.login.configure(width=400, height=350)

        self.pls = tk.Label(self.login,
                            text="Selamat Datang di Chat Room! \n Silakan Login.",
                            justify=tk.CENTER,
                            font="Arial 14 bold")

        self.pls.place(relheight=0.15, relx=0.2, rely=0.07)

        self.userLabel = tk.Label(self.login, text="Nama : ", font="Arial 12")
        self.userLabel.place(relheight=0.2, relx=0.1, rely=0.25)

        self.userEntry = tk.Entry(self.login, font="Arial 12")
        self.userEntry.place(relwidth=0.4, relheight=0.1, relx=0.35, rely=0.30)
        self.userEntry.focus()

        self.roomLabel = tk.Label(self.login, text="Nomor Ruangan : ", font="Arial 12")
        self.roomLabel.place(relheight=0.2, relx=0.1, rely=0.40)

        self.roomEntry = tk.Entry(self.login, font="Arial 11", show="*")
        self.roomEntry.place(relwidth=0.4, relheight=0.1, relx=0.35, rely=0.45)

        self.go = tk.Button(self.login,
                            text="Masuk",
                            font="Arial 12 bold",
                            command=lambda: self.goAhead(self.userEntry.get(), self.roomEntry.get()))

        self.go.place(relx=0.35, rely=0.62)

        self.Window.mainloop()

    def goAhead(self, nama, room_id=0):
        self.name = nama
        self.server.send(str.encode(nama))
        time.sleep(0.1)
        self.server.send(str.encode(room_id))

        self.login.destroy()
        self.layout()

        rcv = threading.Thread(target=self.receive)
        rcv.start()

    def layout(self):
        self.Window.deiconify()
        self.Window.title("Chat Room Page")
        self.Window.resizable(width=False, height=False)
        self.Window.configure(width=470, height=550, bg="#332b22")
        self.chatBoxHead = tk.Label(self.Window,
                                    bg="#281d10",
                                    fg="#ab9072",
                                    text=self.name,
                                    font="Arial 14 bold",
                                    pady=5)

        self.chatBoxHead.place(relwidth=1)

        self.line = tk.Label(self.Window, width=450, bg="#7e776f")

        self.line.place(relwidth=1, rely=0.07, relheight=0.012)

        self.textCons = tk.Text(self.Window,
                                width=20,
                                height=2,
                                bg="#ffffff",
                                fg="#000000",
                                font="Arial 12",
                                padx=5,
                                pady=5)

        self.textCons.place(relheight=0.745, relwidth=1, rely=0.08)

        self.labelBottom = tk.Label(self.Window, bg="#3d3327", height=80)

        self.labelBottom.place(relwidth=1,
                               rely=0.8)

        self.entryMsg = tk.Entry(self.labelBottom,
                                 bg="#ffffff",
                                 fg="#000000",
                                 font="Arial 12")

        self.entryMsg.place(relwidth=0.74,
                            relheight=0.03,
                            rely=0.008,
                            relx=0.011)
        self.entryMsg.focus()

        self.buttonMsg = tk.Button(self.labelBottom,
                                   text="Kirim",
                                   font="Arial 11 bold",
                                   width=20,
                                   bg="#bba68e",
                                   command=lambda: self.sendButton(self.entryMsg.get()))

        self.buttonMsg.place(relx=0.77,
                             rely=0.008,
                             relheight=0.03,
                             relwidth=0.22)

        self.labelFile = tk.Label(self.Window, bg="#2a231b", height=70)

        self.labelFile.place(relwidth=1,
                             rely=0.9)

        self.fileLocation = tk.Label(self.labelFile,
                                     text="Pilih File",
                                     bg="#FFFFFF",
                                     fg="#545455",
                                     font="Arial 12")
        self.fileLocation.place(relwidth=0.65,
                                relheight=0.03,
                                rely=0.008,
                                relx=0.011)

        self.browse = tk.Button(self.labelFile,
                                text="Cari",
                                font="Arial 11 bold",
                                width=13,
                                bg="#bba68e",
                                command=self.browseFile)
        self.browse.place(relx=0.67,
                          rely=0.008,
                          relheight=0.03,
                          relwidth=0.15)

        self.kirimfileBtn = tk.Button(self.labelFile,
                                      text="Kirim",
                                      font="Arial 11 bold",
                                      width=13,
                                      bg="#bba68e",
                                      command=self.sendFile)

        self.kirimfileBtn.place(relx=0.84,
                                rely=0.008,
                                relheight=0.03,
                                relwidth=0.15)

        self.textCons.config(cursor="arrow")
        scrollbar = tk.Scrollbar(self.textCons)
        scrollbar.place(relheight=1,
                        relx=0.974)

        scrollbar.config(command=self.textCons.yview)
        self.textCons.config(state=tk.DISABLED)

    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/",
                                                   title="Pilih file",
                                                   filetypes=(("Text files",
                                                               "*.txt"),
                                                              ("image files",
                                                               "*.jpg"),
                                                              ("all files",
                                                               "*.*")))
        self.fileLocation.configure(text="File Dibuka: " + self.filename)

    def sendFile(self):
        self.server.send("FILE".encode())
        time.sleep(0.1)
        self.server.send(str("File " + os.path.basename(self.filename)).encode())
        time.sleep(0.1)
        self.server.send(str(os.path.getsize(self.filename)).encode())
        time.sleep(0.1)

        file = open(self.filename, "rb")
        data = file.read(1024)
        while data:
            self.server.send(data)
            data = file.read(1024)
        self.textCons.config(state=tk.DISABLED)
        self.textCons.config(state=tk.NORMAL)
        self.textCons.insert(tk.END, "[ Anda ] "
                             + str(os.path.basename(self.filename))
                             + " Terkirim\n\n")
        self.textCons.config(state=tk.DISABLED)
        self.textCons.see(tk.END)

    def sendButton(self, msg):
        self.textCons.config(state=tk.DISABLED)
        self.msg = msg
        self.entryMsg.delete(0, tk.END)
        snd = threading.Thread(target=self.sendMessage)
        snd.start()

    def receive(self):
        while True:
            try:
                message = self.server.recv(1024).decode()

                if str(message) == "FILE":
                    file_name = self.server.recv(1024).decode()
                    lenOfFile = self.server.recv(1024).decode()
                    send_user = self.server.recv(1024).decode()

                    if os.path.exists(file_name):
                        os.remove(file_name)

                    total = 0
                    with open(file_name, 'wb') as file:
                        while str(total) != lenOfFile:
                            data = self.server.recv(1024)
                            total = total + len(data)
                            file.write(data)

                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state=tk.NORMAL)
                    self.textCons.insert(tk.END, "[ " + str(send_user) + " ] " + file_name + " Diterima\n\n")
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.see(tk.END)

                else:
                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.config(state=tk.NORMAL)
                    self.textCons.insert(tk.END,
                                         message + "\n\n")

                    self.textCons.config(state=tk.DISABLED)
                    self.textCons.see(tk.END)

            except:
                print("Terdapat error!")
                self.server.close()
                break

    def sendMessage(self):
        self.textCons.config(state=tk.DISABLED)
        while True:
            self.server.send(self.msg.encode())
            self.textCons.config(state=tk.NORMAL)
            self.textCons.insert(tk.END,
                                 "[ Anda ] " + self.msg + "\n\n")

            self.textCons.config(state=tk.DISABLED)
            self.textCons.see(tk.END)
            break


if __name__ == "__main__":
    ip_address = "127.0.0.1"
    port = 12345
    g = GUI(ip_address, port)