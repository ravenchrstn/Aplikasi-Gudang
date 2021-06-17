from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Master(Frame):

	def __init__(self, main):
		self.main = main
		self.settings = self.main.settings
		self.data = self.main.data
		self.dictionary_data_label = self.data.copy()
		
		super().__init__(self.main.container)
		self.configure(bg="green")
		self.grid(row=0, column=0, sticky="nsew")
		self.main.container.grid_rowconfigure(0, weight=1)
		self.main.container.grid_columnconfigure(0, weight=1)

		#list and dictionary
		self.detecting_right_frame = {}
		self.cntr_right_side = []
		self.cntr_right_side_tambah = []
		self.data_structure = ["kode barang", "nama barang", "satuan", "stok", "harga satuan", "delete", "edit"]

		#command
		self.title()
		self.left_frame()

	def title(self):
		self.title = Frame(self, bg="black", width=self.main.width)
		self.title.pack(fill="both")

		self.title_text()
		self.lobby_button()

	def title_text(self):
		self.text = Label(self.title, fg="white", text="Master Barang", font=("Century Gothic", 30, "bold"), bg="black")
		self.text.grid()

	def lobby_button(self):
		self.lobby_button = Button(self.title, fg="white", text="Lobby", font=("Century Gothic", 19, "bold"), bg="black", command=lambda:[self.main.change_page("lobby_page")])
		self.lobby_button.place(x=1430, y=2)

	def left_frame(self):
		self.left_frame = Frame(self, bg="white", width=self.main.width/5, height=self.main.height)
		self.left_frame.pack(side="left")

		self.left_content()

	def left_content(self):
		self.list_box = Listbox(self.left_frame, bg="yellow", font=("Century Gothic", 16), height=self.main.height)
		self.list_box.pack(side="left", expand=True, fill="both")
		feature = ["Stok", "Tambah Item"]
		self.list_box.bind("<<ListboxSelect>>", self.pressed_left_content)

		for i in feature:
			self.list_box.insert("end", i)

	def stock_frame(self):
		self.stock_right_frame = Frame(self, width=6*self.main.width/7, height=self.main.height)
		self.stock_right_frame.pack(side="left", expand=True, fill="both")

		#adding item to detect
		self.detecting_right_frame["stok"] = "ada"

		#commands
		self.stok_frame()

	def blank_right_side(self):
		self.addition_right_frame = Frame(self, width=6*self.main.width/7, height=self.main.height)
		self.addition_right_frame.pack(side="left", expand=True, fill="both")

		#adding item to detect
		self.detecting_right_frame["tambah item"] = "ada"

	def pressed_left_content(self, event):
		selection = event.widget.curselection()
		try :
			self.index = selection[0]
			self.last_index = self.index
		except IndexError:
			self.index = self.last_index

		if self.index == 0:
			if "tambah item" in self.detecting_right_frame:
				self.detecting_right_frame.pop("tambah item")
				self.addition_right_frame.destroy()

			if len(self.cntr_right_side) == 0:
				self.stock_frame()

			#adding item to detect double clicks
			self.cntr_right_side.append("aku")

			#making list none
			self.cntr_right_side_tambah = []

		elif self.index == 1:
			if "stok" in self.detecting_right_frame:
				self.detecting_right_frame.pop("stok")
				self.stock_right_frame.destroy()

			if len(self.cntr_right_side_tambah) == 0:
				self.blank_right_side()

			#adding item to detect double clicks
			self.cntr_right_side_tambah.append("aku")

			#making list none
			self.cntr_right_side = []

	def stok_frame(self):
		self.top_right_frame = Frame(self.stock_right_frame, bg="green", width=6*self.main.width/7, height=100)
		self.top_right_frame.pack(side="top", fill="both")

		self.bottom_right_frame = Frame(self.stock_right_frame, bg="red", width=6*self.main.width/7, height=700)
		self.bottom_right_frame.pack(side="top", fill="both", expand=True)

		self.top_content_right_frame()
		self.bottom_content_right_frame()

	def top_content_right_frame(self):
		self.add_items = Button(self.top_right_frame, bg="gray", width=20, height=1, font=("Century Gothic", 16, "bold"), text="Tambah Item", command=lambda:[self.if_adding_items_pressed()])
		self.add_items.place(x=0, y=28)

		self.show_all = Button(self.top_right_frame, bg="black", width=4, font=("Century Gothic", 13), text="all", fg="white", command=lambda:[self.if_all()])
		self.show_all.place(x=1235, y=40)

		self.searching_box()

		self.search = Button(self.top_right_frame, bg="black", width=4, font=("Century Gothic", 13), text="enter", fg="white", command=lambda:[self.if_search_button_pressed(berdasarkan=self.combobox.get())])
		self.search.place(x=1184, y=40)
		
	def bottom_content_right_frame(self):
		self.frame_title_for_items = Frame(self.bottom_right_frame, bg="pink", width=2*self.main.width/10, height=self.main.height/7)
		self.frame_title_for_items.pack(side="top", fill="both")

		self.frame_content_for_items =  Frame(self.bottom_right_frame, bg="aqua", width=2*self.main.width/10, height=self.main.height)
		self.frame_content_for_items.pack(side="top", fill="both")
		
		self.showing_title_for_items()
		self.showing_items_content()

	def showing_title_for_items(self):
		self.label_code_items = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Kode Barang", width=12, height=2, relief="raised", borderwidth=1)
		self.label_code_items.pack(side="left", fill="x", expand=True)

		self.label_items_name = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Nama Barang", width=12, height=2, relief="raised", borderwidth=1)
		self.label_items_name.pack(side="left", fill="x", expand=True)

		self.label_unit = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Satuan", width=12, height=2, relief="raised", borderwidth=1)
		self.label_unit.pack(side="left", fill="x", expand=True)

		self.label_stock = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Stok", width=6, height=2, relief="raised", borderwidth=1)
		self.label_stock.pack(side="left", fill="x", expand=True)

		self.label_each_price = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Harga Satuan", width=12, height=2, relief="raised", borderwidth=1)
		self.label_each_price.pack(side="left", fill="x", expand=True)

		self.label_action = Label(self.frame_title_for_items, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Aksi", width=6, height=2, relief="raised", borderwidth=1)
		self.label_action.pack(side="left", fill="x", expand=True)

	def showing_items_content(self):
		canvas = Canvas(self.frame_content_for_items, width=500, height=700, bg="gray45")
		scrollbar = ttk.Scrollbar(self.frame_content_for_items, orient="vertical", command=canvas.yview)
		self.scrollable_frame = ttk.Frame(canvas)

		self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
		canvas.create_window((0,0), window=self.scrollable_frame, anchor="nw")
		canvas.configure(yscrollcommand=scrollbar.set)

		canvas.pack(side="left", expand=True, fill="both")
		scrollbar.pack(side="right", fill="y")

		#put all items
		self.put_items_code()
		self.put_items_name()
		self.put_unit()
		self.put_stock()
		self.put_each_price()
		self.put_action()

		self.settings.save_master_barang()

	def put_items_code(self):
		i = 0
		for x in self.data:
			self.dictionary_data_label[x] = {}
			self.kode_barang = Label(self.scrollable_frame, text=self.data[x]["kode barang"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.kode_barang.grid(row=i, column=0)
			self.dictionary_data_label[x][self.data_structure[0]] = self.kode_barang
			i += 1

	def put_items_name(self):
		i = 0
		for x in self.data:
			self.nama_barang = Label(self.scrollable_frame, text=x, width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.nama_barang.grid(row=i, column=1)
			self.dictionary_data_label[x][self.data_structure[1]] = self.nama_barang
			i += 1

	def put_unit(self):
		i = 0
		for x in self.data:
			self.satuan = Label(self.scrollable_frame, text=self.data[x]["satuan"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.satuan.grid(row=i, column=2)
			self.dictionary_data_label[x][self.data_structure[2]] = self.satuan
			i += 1

	def put_stock(self):
		i = 0
		for x in self.data:
			self.stok = Label(self.scrollable_frame, text=self.data[x]["stok"], width=15, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.stok.grid(row=i, column=3)
			self.dictionary_data_label[x][self.data_structure[3]] = self.stok
			i += 1

	def put_each_price(self):
		i = 0
		for x in self.data:
			self.harga_satuan = Label(self.scrollable_frame, text=f"Rp.{self.data[x]['harga satuan']},00", width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.harga_satuan.grid(row=i, column=4)
			self.dictionary_data_label[x][self.data_structure[4]] = self.harga_satuan
			i += 1

	def put_action(self):
		self.doesitever = False
		tell = True
		i = 0
		for x in self.data:
			self.delete = Button(self.scrollable_frame, width=9, text="delete", relief="raised", borderwidth=3, bg="red", command=lambda y=x:[self.if_delete_button_pressed(apa=y)])
			self.delete.grid(row=i, column=5)
			self.dictionary_data_label[x][self.data_structure[5]] = self.delete

			self.edit = Button(self.scrollable_frame, width=9, text="edit", relief="raised", borderwidth=3, bg="gray", command=lambda y=x, b=tell:[self.edit_tabel(apa=y, itu=b)])
			self.edit.grid(row=i, column=6)
			self.dictionary_data_label[x][self.data_structure[6]] = self.edit
			i += 1
		#for multiple clicks in self.edit
		self.multiple_clicks = 0
		self.counter_untuk_replacement = True
		self.counterlagisih = False

	def edit_tabel(self, apa, itu):
		#reset or change to entry
		# print(self.dictionary_data_label)
		if self.doesitever == True:	
			if self.entry_items_code.get() == "" or self.entry_items_name.get() == "" or self.entry_unit.get() == "" or self.entry_stock.get() == "" or self.entry_each_price == "":
				messagebox.showerror("Value Error", "Don't let the data empty")
				itu = False
			elif self.entry_each_price.get().replace(".", "").isnumeric() == False:
				messagebox.showerror("Value Error", "The each price has to be integer only!")
				itu = False
			elif self.entry_stock.get().isnumeric() == False:
				messagebox.showerror("Value Error", "The stock has to be integer only!")
				itu = False
			elif self.entry_unit.get().isalpha() == False:
				messagebox.showerror("Value Error", "The satuan has to be alphabet only and without any spacings!")
				itu = False
			else:
				itu = True

			if self.entry_each_price.get().isnumeric() == True:
				new_total = self.main.pages["transaksi_penjualan"].turning_into_three_points(value=self.entry_each_price.get())
			else:
				new_total = self.entry_each_price.get()

			if itu == True:
				name_answer = self.entry_items_name.get()
				code_answer = self.entry_items_code.get()
				unit_answer = self.entry_unit.get()
				stock_answer = self.entry_stock.get()
				harga_satuan = new_total

				for name, info in self.dictionary_data_label.items():
					info["edit"]["state"] = "normal"
					info["delete"]["state"] = "normal"

				if self.entry_items_name.get() in self.data:
					if apa.upper() == self.entry_items_name.get().upper():
						self.dictionary_data_label[apa]["kode barang"].configure(text=self.entry_items_code.get())
						self.dictionary_data_label[apa]["nama barang"].configure(text=self.entry_items_name.get())
						self.dictionary_data_label[apa]["satuan"].configure(text=self.entry_unit.get())
						self.dictionary_data_label[apa]["stok"].configure(text=self.entry_stock.get())
						self.dictionary_data_label[apa]["harga satuan"].configure(text=f"Rp.{new_total},00")

						self.data[apa] = {}
						self.data[apa]["kode barang"] = self.entry_items_code.get()
						self.data[apa]["satuan"] = self.entry_unit.get()
						self.data[apa]["stok"] = self.entry_stock.get()
						self.data[apa]["harga satuan"] = self.entry_each_price.get()

					else:
						tanya = messagebox.askyesnocancel("Replacement", "Do you want to replace the edited data with the original one?")
						if tanya == True:
							for x in self.data_structure:
								self.dictionary_data_label[apa][x].destroy()
							self.dictionary_data_label.pop(apa)
							self.data.pop(name_answer)
							self.data.pop(apa)

							self.dictionary_data_label[name_answer]["kode barang"].configure(text=code_answer)
							self.dictionary_data_label[name_answer]["nama barang"].configure(text=name_answer)
							self.dictionary_data_label[name_answer]["satuan"].configure(text=unit_answer)
							self.dictionary_data_label[name_answer]["stok"].configure(text=stock_answer)
							self.dictionary_data_label[name_answer]["harga satuan"].configure(text=f"Rp.{new_total},00")

							self.data[name_answer] = {}
							self.data[name_answer]["kode barang"] = code_answer
							self.data[name_answer]["satuan"] = unit_answer
							self.data[name_answer]["stok"] = stock_answer
							self.data[name_answer]["harga satuan"] = new_total

							self.counterlagisih = True
						else:
							print("false")
							self.counter_untuk_replacement = False
							self.doesitever = True
				else:
					self.data[self.entry_items_name.get()] = {}
					self.data[self.entry_items_name.get()]["kode barang"] = self.entry_items_code.get()
					self.data[self.entry_items_name.get()]["satuan"] = self.entry_unit.get()
					self.data[self.entry_items_name.get()]["stok"] = self.entry_stock.get()
					self.data[self.entry_items_name.get()]["harga satuan"] = new_total

				if self.counter_untuk_replacement == True:
					self.entry_items_code.destroy()
					self.entry_items_name.destroy()
					self.entry_unit.destroy()
					self.entry_stock.destroy()
					self.entry_each_price.destroy()

					self.doesitever = False
					self.settings.save_master_barang()
			else:
				self.doesitever = True

		else:
			if self.doesitever == False:
				for name, info in self.dictionary_data_label.items():
					if name == apa:
						for x in self.data_structure:
							if x == "edit" or x == "delete":
								pass
							else:
								info[x].configure(text="")

				self.entry_items_code = Entry(self.dictionary_data_label[apa]["kode barang"], width=18, font=("Century Gothic", 13), bg="gray")
				self.entry_items_code.place(x=20, y=45)
				self.entry_items_code.insert(0, self.data[apa]["kode barang"])

				self.entry_items_name = Entry(self.dictionary_data_label[apa]["nama barang"], width=18, font=("Century Gothic", 13), bg="gray")
				self.entry_items_name.place(x=20, y=45)
				self.entry_items_name.insert(0, apa)

				self.entry_unit = Entry(self.dictionary_data_label[apa]["satuan"], width=18, font=("Century Gothic", 13), bg="gray")
				self.entry_unit.place(x=20, y=45)
				self.entry_unit.insert(0, self.data[apa]["satuan"])

				self.entry_stock = Entry(self.dictionary_data_label[apa]["stok"], width=9, font=("Century Gothic", 13), bg="gray")
				self.entry_stock.place(x=15, y=45)
				self.entry_stock.insert(0, self.data[apa]["stok"])

				self.entry_each_price = Entry(self.dictionary_data_label[apa]["harga satuan"], width=18, font=("Century Gothic", 13), bg="gray")
				self.entry_each_price.place(x=20, y=45)
				self.entry_each_price.insert(0, self.data[apa]["harga satuan"])

				for name, info in self.dictionary_data_label.items():
					info["edit"]["state"] = "disabled"
					info["delete"]["state"] = "disabled"
				self.dictionary_data_label[apa]["edit"]["state"] = "normal"
				print(self.dictionary_data_label)
				self.doesitever = True
				# print(self.dictionary_data_label)
	
	def if_adding_items_pressed(self):
		#making a new tkinter for adding new items
		self.newtk_for_adding_items = Tk()
		ti_w = 600
		ti_h = 300
		size = f"{ti_w}x{ti_h}"

		self.newtk_for_adding_items.geometry(size)
		self.newtk_for_adding_items.title("Penambahan Item")

		self.header_frame = Frame(self.newtk_for_adding_items, bg="red", width=ti_w, height=ti_h/3)
		self.header_frame.pack(fill="both", side="top")

		self.footer_frame = Frame(self.newtk_for_adding_items, bg="dark blue", width=ti_w)
		self.footer_frame.pack(fill="both", expand=True, side="top")

		self.header_title = Label(self.header_frame,  font=("Century Gothic", 22, "bold"), text="Penambahan Item", fg="white", bg="red")
		self.header_title.pack(pady=20)

		self.code_label = Label(self.footer_frame, text="Kode Barang", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
		self.code_label.place(x=0, y=5)

		self.name_label = Label(self.footer_frame, text="Nama Barang", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
		self.name_label.place(x=0, y=40)

		self.unit_label = Label(self.footer_frame, text="Satuan", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
		self.unit_label.place(x=0, y=75)

		self.stock_label = Label(self.footer_frame, text="Stok", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
		self.stock_label.place(x=0, y=110)
		
		self.each_price_label = Label(self.footer_frame, text="Harga Satuan", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
		self.each_price_label.place(x=0, y=145)

		#making the content
		i = 5
		for x in range(5):
			self.samadengan = Label(self.footer_frame, text=":", font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue")
			self.samadengan.place(x=120, y=i)
			i += 35

		self.kode_entry = Entry(self.footer_frame, width=30, font=("Century Gothic", 12, "bold"), fg="white", bg="red")
		self.kode_entry.place(x=150, y=5)

		self.name_entry = Entry(self.footer_frame, width=30, font=("Century Gothic", 12, "bold"), fg="white", bg="red")
		self.name_entry.place(x=150, y=40)

		self.stok_entry = Entry(self.footer_frame, width=30, font=("Century Gothic", 12, "bold"), fg="white", bg="red")
		self.stok_entry.place(x=150, y=110)

		self.satuan_entry = Entry(self.footer_frame, width=30, font=("Century Gothic", 12, "bold"), fg="white", bg="red")
		self.satuan_entry.place(x=150, y=75)

		self.harga_satuan_entry = Entry(self.footer_frame, width=30, font=("Century Gothic", 12, "bold"), fg="white", bg="red")
		self.harga_satuan_entry.place(x=150, y=145)

		self.enter_button = Button(self.footer_frame, width=10, font=("Century Gothic", 12, "bold"), fg="white", bg="red", text="Enter", command=lambda:self.are_you_sure())
		self.enter_button.place(x=467, y=5)
	
	def if_yes(self):
		if self.name_entry.get() in self.data:
			really = messagebox.askyesnocancel("Replacement", "Are you sure to replace this data with the original one?")
			if really == False:
				self.test = False
				self.test2 = False
			else:
				self.test = True
				self.test2 = False

		if self.test == True:
			money = self.main.pages["transaksi_penjualan"].turning_into_three_points(value=self.harga_satuan_entry.get())
			self.data[self.name_entry.get()]["kode barang"] = self.kode_entry.get()
			self.data[self.name_entry.get()]["satuan"] = self.satuan_entry.get()
			self.data[self.name_entry.get()]["stok"] = self.stok_entry.get()
			self.data[self.name_entry.get()]["harga satuan"] = money

			self.dictionary_data_label[self.name_entry.get()]["kode barang"].configure(text=self.kode_entry.get())
			self.dictionary_data_label[self.name_entry.get()]["satuan"].configure(text=self.satuan_entry.get())
			self.dictionary_data_label[self.name_entry.get()]["stok"].configure(text=self.stok_entry.get())
			self.dictionary_data_label[self.name_entry.get()]["harga satuan"].configure(text=money)

			self.settings.save_master_barang()

		if self.test2 == True:
			self.answer_kode = self.kode_entry.get()
			self.answer_name = self.name_entry.get()
			self.answer_satuan = self.satuan_entry.get()
			self.answer_stok = self.stok_entry.get()
			self.answer_harga_satuan = self.harga_satuan_entry.get()

			self.newtk_for_adding_items.destroy()

			self.data[self.answer_name] = {}
			self.data[self.answer_name]["kode barang"] = self.answer_kode
			self.data[self.answer_name]["satuan"] = self.answer_satuan
			self.data[self.answer_name]["stok"] = self.answer_stok
			self.data[self.answer_name]["harga satuan"] = self.main.pages["transaksi_penjualan"].turning_into_three_points(value=self.answer_harga_satuan)
			self.settings.save_master_barang()

			self.adding_new_items_to_table()
			self.putting_new_items_to_dic_data_label()

	def adding_new_items_to_table(self):
		self.items_code_addition = Label(self.scrollable_frame, text=self.data[self.answer_name]["kode barang"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
		self.items_code_addition.grid(row=len(self.data), column=0)

		self.items_name_addition = Label(self.scrollable_frame, text=self.answer_name, width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
		self.items_name_addition.grid(row=len(self.data), column=1)

		self.unit_addition = Label(self.scrollable_frame, text=self.data[self.answer_name]["satuan"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
		self.unit_addition.grid(row=len(self.data), column=2)

		self.stock_addition = Label(self.scrollable_frame, text=self.data[self.answer_name]["stok"], width=15, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
		self.stock_addition.grid(row=len(self.data), column=3)

		self.each_price_addition = Label(self.scrollable_frame, text=f"Rp.{self.data[self.answer_name]['harga satuan']},00", width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
		self.each_price_addition.grid(row=len(self.data), column=4)

		self.delete_addition = Button(self.scrollable_frame, width=9, text="delete", relief="raised", borderwidth=3, bg="red", command=lambda y=self.answer_name:[self.if_delete_button_pressed(apa=y)])
		self.delete_addition.grid(row=len(self.data), column=5)

		self.edit_addition = Button(self.scrollable_frame, width=9, text="edit", relief="raised", borderwidth=3, bg="gray", command=lambda y=self.answer_name, b=True:[self.edit_tabel(apa=y, itu=b)])
		self.edit_addition.grid(row=len(self.data), column=6)

	def putting_new_items_to_dic_data_label(self):
		self.dictionary_data_label[self.answer_name] = {}
		self.dictionary_data_label[self.answer_name]["kode barang"] = self.items_code_addition
		self.dictionary_data_label[self.answer_name]["nama barang"] = self.items_name_addition
		self.dictionary_data_label[self.answer_name]["satuan"] = self.unit_addition
		self.dictionary_data_label[self.answer_name]["stok"] = self.stock_addition
		self.dictionary_data_label[self.answer_name]["harga satuan"] = self.each_price_addition
		self.dictionary_data_label[self.answer_name]["delete"] = self.delete_addition
		self.dictionary_data_label[self.answer_name]["edit"] = self.edit_addition
		self.main.dic_price_int[self.answer_name] = int(self.settings.data[self.answer_name]["harga satuan"].replace(".", ""))

	def are_you_sure(self):
		self.test = False
		self.test2 = True
		if self.stok_entry.get().isnumeric() == False or self.satuan_entry.get().isalpha() == False or self.harga_satuan_entry.get().isnumeric() == False:
			self.error_stok = messagebox.showerror("Value Error", "Restrictions :\n1. The stok and the harga satuan have to be positive integers only without any points and commas!\n2. The satuan has to be string only!\n3. Don't let the data empty!")
			a = False
		else:
			a = True

		if a == True:
			self.are_you_sure_label = Label(self.footer_frame, font=("Century Gothic", 12, "bold"), fg="white", bg="dark blue", text="are you sure?")
			self.are_you_sure_label.place(x=463, y=45)

			self.yes_button = Button(self.footer_frame, width=8, font=("Century Gothic", 10, "bold"), fg="white", bg="red", text="yes", command=lambda:[self.if_yes()])
			self.yes_button.place(x=431, y=85)

			self.no_button = Button(self.footer_frame, width=8, font=("Century Gothic", 10, "bold"), fg="white", bg="red", text="no", command=lambda:[self.newtk_for_adding_items.destroy()])
			self.no_button.place(x=520, y=85)

	def if_delete_button_pressed(self, apa):
		#menghilangkan di table
		for x in self.dictionary_data_label[apa]:
			self.dictionary_data_label[apa][x].grid_forget()
		del self.dictionary_data_label[apa]	
		del self.data[apa]
		self.settings.save_master_barang()

	def searching_box(self):
		self.berdasarkan_apa = StringVar()
		self.combobox = ttk.Combobox(self.top_right_frame, textvariable=self.berdasarkan_apa, font=("Century Gothic", 11))
		self.combobox["value"] = ("kode barang", "nama barang", "satuan", "stok", "harga satuan")
		self.combobox["state"] = "readonly"
		self.combobox.place(x=954, y=15)
		self.combobox.set("Berdasarkan")

		self.combobox.bind("<<ComboboxSelected>>")

		self.searchingbox = Entry(self.top_right_frame, bg="gray", width=15, font=("Century Gothic", 20, "bold"))
		self.searchingbox.place(x=954, y=40)

	def remove_all_items_from_the_table(self):
		for name, info in self.dictionary_data_label.items():
			for i in info:
				info[i].grid_forget()
		
	def if_search_button_pressed(self, berdasarkan):
		self.answer_searching = self.searchingbox.get()	
		self.remove_all_items_from_the_table()

		o = 0
		if berdasarkan == "nama barang":
			for name, info in self.data.items():
				if self.answer_searching.upper() in name.upper():
					for x in self.data_structure:
						if x == "kode barang":
							self.dictionary_data_label[name][x].grid(row=o, column=0)
						elif x == "satuan":
							self.dictionary_data_label[name][x].grid(row=o, column=2)
						elif x == "stok":
							self.dictionary_data_label[name][x].grid(row=o, column=3)
						elif x == "harga satuan":
							self.dictionary_data_label[name][x].grid(row=o, column=4)
						elif x == "nama barang":
							self.dictionary_data_label[name]["nama barang"].grid(row=o, column=1)
						elif x == "delete":
							self.dictionary_data_label[name]["delete"].grid(row=o, column=5)
						elif x == "edit":
							self.dictionary_data_label[name]["edit"].grid(row=o, column=6)
					o += 1
		else:
			for name, info in self.data.items():
				if berdasarkan.lower() == "berdasarkan":
					pass
				else:
					if self.answer_searching.upper() in info[berdasarkan].upper() or self.main.pages['transaksi_penjualan'].turning_into_three_points(value=self.answer_searching).upper() in info[berdasarkan].upper():
						for p in self.data_structure:
							if p == "kode barang":
								self.dictionary_data_label[name][p].grid(row=o, column=0)
							elif p == "satuan":
								self.dictionary_data_label[name][p].grid(row=o, column=2)
							elif p == "stok":
								self.dictionary_data_label[name][p].grid(row=o, column=3)
							elif p == "harga satuan":
								self.dictionary_data_label[name][p].grid(row=o, column=4)
							elif p == "nama barang":
								self.dictionary_data_label[name]["nama barang"].grid(row=o, column=1)
							elif p == "delete":
								self.dictionary_data_label[name]["delete"].grid(row=o, column=5)
							elif p == "edit":
								self.dictionary_data_label[name]["edit"].grid(row=o, column=6)
						o += 1
	def if_all(self):
		self.combobox.set("Berdasarkan")
		self.searchingbox.delete(0, "end")
		self.remove_all_items_from_the_table()

		counter = 0
		for name, info in self.dictionary_data_label.items():
			for i in info:
				if i == "kode barang":
					self.dictionary_data_label[name][i].grid(row=counter, column=0)
				elif i == "nama barang":
					self.dictionary_data_label[name][i].grid(row=counter, column=1)
				elif i == "satuan":
					self.dictionary_data_label[name][i].grid(row=counter, column=2)
				elif i == "stok":
					self.dictionary_data_label[name][i].grid(row=counter, column=3)
				elif i == "harga satuan":
					self.dictionary_data_label[name][i].grid(row=counter, column=4)
				elif i == "delete":
					self.dictionary_data_label[name][i].grid(row=counter, column=5)
				elif i == "edit":
					self.dictionary_data_label[name][i].grid(row=counter, column=6)
			counter += 1