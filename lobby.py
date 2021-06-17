from tkinter import *
from PIL import Image, ImageTk

class Lobby(Frame):

	def __init__(self, main):
		self.main =	main

		super().__init__(self.main.container)
		self.configure(bg="blue")
		self.grid(sticky="nsew", row=0, column=0 )
		self.main.container.grid_columnconfigure(0, weight=1)
		self.main.container.grid_rowconfigure(0, weight=1)

		#command
		self.creating_background()
		self.creating_logo()
		self.creating_button_master_barang()
		self.creating_button_transaksi_penjualan()
		self.exit_button()

	def creating_background(self):
		#importing background
		background = Image.open(self.main.settings.background_path)
		background_w, background_h = background.size
		new_size = (self.main.width, self.main.height)
		background = background.resize(new_size)

		self.background = ImageTk.PhotoImage(background)
		self.background_label = Label(self, image=self.background, width=self.main.width, height=self.main.height)
		self.background_label.pack(expand=True, fill="both")

	def creating_logo(self):
		#importing and resizing logo
		logo = Image.open(self.main.settings.logo_path)
		logo_w, logo_h = logo.size
		new_size = (int(logo_w/2), int(logo_h//2))
		logo = logo.resize(new_size)

		self.logo = ImageTk.PhotoImage(logo)
		self.logo_label = Label(self.background_label, image=self.logo, borderwidth=4, relief="raised")
		self.logo_label.grid(pady=150, padx=570)

	def creating_button_master_barang(self):
		self.master_barang = Button(self.background_label, text="Master Barang", borderwidth=4, relief="raised", font=("Century Gothic", 20, "bold"), bg="SlateBlue1", command=lambda:[self.if_master_barang()])
		self.master_barang.place(x=300, y=450)

	def creating_button_transaksi_penjualan(self):
		self.transaksi_penjualan = Button(self.background_label, text="Transaksi Penjualan", borderwidth=4, relief="raised", font=("Century Gothic", 20, "bold"), bg="SlateBlue1", command=lambda:[self.if_transaksi_penjualan()])
		self.transaksi_penjualan.place(x=1020, y=450)

	def exit_button(self):
		self.exit = Button(self.background_label, text="exit", bg="black", font=("Century Gothic", 11, "bold"), fg="white", command=lambda:[self.if_exit_button()])
		self.exit.place(x=615, y=720)

	def if_exit_button(self):
		self.main.destroy()

	def if_master_barang(self):
		self.main.change_page(which="master_barang")

	def if_transaksi_penjualan(self):
		self.main.change_page(which="transaksi_penjualan")
		