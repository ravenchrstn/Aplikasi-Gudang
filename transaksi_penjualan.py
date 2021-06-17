from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class Transaksi_Penjualan(Frame):

	def __init__(self, main):
		self.main = main
		self.data = self.main.data
		self.dictionary_label_data = self.data.copy()

		super().__init__(self.main.container)
		self.configure(bg="aqua")
		self.grid(row=0, column=0, sticky="nsew")
		self.main.container.grid_rowconfigure(0, weight=1)
		self.main.container.grid_columnconfigure(0, weight=1)

		#dictionary or list
		self.counter_frame_buying = []
		self.counter_frame_selling = []
		self.frame_right_counter = []
		self.data_structure = ["kode barang", "nama barang", "satuan", "stok", "harga satuan", "sell"]

		#commands
		self.title()
		self.left_frame()
		#self.selling_right_frame()

	def title(self):
		self.title = Frame(self, bg="black", width=self.main.width)
		self.title.pack(fill="both")

		self.title_text()
		self.lobby_button()

	def title_text(self):
		self.text = Label(self.title, fg="white", text="Transaksi Penjualan", font=("Century Gothic", 30, "bold"), bg="black")
		self.text.grid()

	def lobby_button(self):
		self.lobby_button = Button(self.title, fg="white", text="Lobby", font=("Century Gothic", 19, "bold"), bg="black", command=lambda:[self.main.change_page("lobby_page")])
		self.lobby_button.place(x=1430, y=2)

	def left_frame(self):
		self.left_frame = Frame(self, bg="white", width=self.main.width/5, height=self.main.height)
		self.left_frame.pack(side="left")

		self.left_content()

	def left_content(self):
		self.counter_for_change_right_frame = {}
		self.counter_right_side_buying = []
		self.counter_right_side_selling = []

		self.list_box = Listbox(self.left_frame, bg="dark blue", font=("Century Gothic", 16), height=self.main.height)
		self.list_box.pack(side="left", expand=True, fill="both")
		feature = ["Penjualan", "Pembelian"]
		self.list_box.bind("<<ListboxSelect>>", self.pressed_left_content)

		for i in feature:
			self.list_box.insert("end", i)

	def pressed_left_content(self, event):
		selection = event.widget.curselection()
		try:
			self.index = selection[0]
			self.last_index = self.index
		except IndexError:
			self.index = self.last_index

		if self.index == 0:
			if "buying" in self.counter_for_change_right_frame:
				self.counter_for_change_right_frame.pop("buying")
				self.buying_right_frame.destroy()
				self.frame_top.destroy()
				self.frame_bottom.destroy()

			if len(self.counter_right_side_selling) == 0:
				self.frame_selling_right_side()

			self.counter_right_side_selling.append("aku")
			self.counter_right_side_buying = []

		elif self.index == 1:
			if "selling" in self.counter_for_change_right_frame:
				self.counter_for_change_right_frame.pop("selling")
				self.selling_right_frame.destroy()
				self.frame_top.destroy()
				self.frame_bottom.destroy()

			if len(self.counter_right_side_buying) == 0:
				self.frame_buying_right_side()

			self.counter_right_side_buying.append("aku")
			self.counter_right_side_selling = []

	def frame_selling_right_side(self):
		self.selling_right_frame = Frame(self, width=6*self.main.width/7, height=self.main.height, bg="gray")
		self.selling_right_frame.pack(side="left", expand=True, fill="both")

		self.counter_for_change_right_frame["selling"] = "ada"

		self.top_and_bottom(frame_siapa=self.selling_right_frame, background_color_top="dark red", background_color_bottom="dark blue", ganti="self.selling_right_frame")

	def frame_buying_right_side(self):
		self.buying_right_frame = Frame(self, width=6*self.main.width/7, height=self.main.height, bg="red")
		self.buying_right_frame.pack(side="left", expand=True, fill="both")

		self.counter_for_change_right_frame["buying"] = "ada"

		self.top_and_bottom(frame_siapa=self.buying_right_frame, background_color_top = "blue", background_color_bottom="yellow", ganti="self.buying_right_frame")

	def top_and_bottom(self, frame_siapa, background_color_top, background_color_bottom, ganti):
		self.which_frame = frame_siapa

		self.frame_top = Frame(frame_siapa, bg=background_color_top, width=6*self.main.width/7, height=100)
		self.frame_top.pack(side="top", fill="both")

		self.frame_bottom = Frame(frame_siapa, bg=background_color_bottom, width=6*self.main.width/7, height=700)
		self.frame_bottom.pack(side="top", fill="both", expand=True)

		if ganti == "self.selling_right_frame":
			self.frame_selling_right_side_content(background_color_bottom=background_color_bottom)
			self.searching_box()

			self.search = Button(self.frame_top, bg="black", width=4, font=("Century Gothic", 13), text="enter", fg="white", command=lambda:[self.if_search_button_pressed(berdasarkan=self.combobox.get())])
			self.search.place(x=1184, y=40)
		
			self.show_all = Button(self.frame_top, bg="black", width=4, font=("Century Gothic", 13), text="all", fg="white", command=lambda:[self.if_all()])
			self.show_all.place(x=1235, y=40)
		elif ganti == "self.buying_right_frame":
			pass

	def if_all(self):
		self.combobox.set("Berdasarkan")
		self.remove_all_items_from_the_table()

		counter = 0
		for name, info in self.dictionary_label_data.items():
			for i in self.data_structure:
				if i == "kode barang":
					self.dictionary_label_data[name][i].grid(row=counter, column=0)
				elif i == "nama barang":
					self.dictionary_label_data[name][i].grid(row=counter, column=1)
				elif i == "satuan":
					self.dictionary_label_data[name][i].grid(row=counter, column=2)
				elif i == "stok":
					self.dictionary_label_data[name][i].grid(row=counter, column=3)
				elif i == "harga satuan":
					self.dictionary_label_data[name][i].grid(row=counter, column=4)
				elif i == "sell":
					self.dictionary_label_data[name][i].grid(row=counter, column=5)
			counter += 1

	def if_search_button_pressed(self, berdasarkan):
		self.answer_searching = self.searchingbox.get()	
		self.remove_all_items_from_the_table()

		o = 0
		if berdasarkan == "nama barang":
			for name, info in self.data.items():
				if self.answer_searching.upper() in name.upper():
					for x in self.data_structure:
						if x == "kode barang":
							self.dictionary_label_data[name][x].grid(row=o, column=0)
						elif x == "satuan":
							self.dictionary_label_data[name][x].grid(row=o, column=2)
						elif x == "stok":
							self.dictionary_label_data[name][x].grid(row=o, column=3)
						elif x == "harga satuan":
							self.dictionary_label_data[name][x].grid(row=o, column=4)
						elif x == "sell":
							self.dictionary_label_data[name][x].grid(row=o, column=5)
						elif x == "nama barang":
							self.dictionary_label_data[name]["nama barang"].grid(row=o, column=1)
				o += 1
		else:
			for name, info in self.data.items():
				if self.answer_searching.upper() in info[berdasarkan].upper() or self.turning_into_three_points(value=self.answer_searching).upper() in info[berdasarkan].upper():
					for p in self.data_structure:
						if p == "kode barang":
							self.dictionary_label_data[name][p].grid(row=o, column=0)
						elif p == "satuan":
							self.dictionary_label_data[name][p].grid(row=o, column=2)
						elif p == "stok":
							self.dictionary_label_data[name][p].grid(row=o, column=3)
						elif p == "harga satuan":
							self.dictionary_label_data[name][p].grid(row=o, column=4)
						elif p == "sell":
							self.dictionary_label_data[name][p].grid(row=o, column=5)
						elif p == "nama barang":
							self.dictionary_label_data[name]["nama barang"].grid(row=o, column=1)
				o += 1

	def remove_all_items_from_the_table(self):
		for name, info in self.dictionary_label_data.items():
			for i in info:
				info[i].grid_forget()

	def searching_box(self):
		self.berdasarkan_apa = StringVar()
		self.combobox = ttk.Combobox(self.frame_top, textvariable=self.berdasarkan_apa, font=("Century Gothic", 11))
		self.combobox["value"] = ("kode barang", "nama barang", "satuan", "stok", "harga satuan")
		self.combobox["state"] = "readonly"
		self.combobox.place(x=954, y=15)
		self.combobox.set("Berdasarkan")

		self.combobox.bind("<<ComboboxSelected>>")

		self.searchingbox = Entry(self.frame_top, bg="gray", width=15, font=("Century Gothic", 20, "bold"))
		self.searchingbox.place(x=954, y=40)

	def frame_selling_right_side_content(self, background_color_bottom):
		self.right_side_frame_title = Frame(self.frame_bottom, bg="pink", width=2*self.main.width/10, height=self.main.height/7)
		self.right_side_frame_title.pack(side="top", fill="both")

		self.right_side_frame_content = Frame(self.frame_bottom, bg="aqua", width=2*self.main.width/10, height=self.main.height)
		self.right_side_frame_content.pack(side="top", fill="both")

		self.making_bottom_title()
		self.making_bottom_content()

	def making_bottom_title(self):
		self.label_code_items = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Kode Barang", width=12, height=2, relief="raised", borderwidth=1)
		self.label_code_items.pack(side="left", fill="x", expand=True)

		self.label_items_name = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Nama Barang", width=12, height=2, relief="raised", borderwidth=1)
		self.label_items_name.pack(side="left", fill="x", expand=True)

		self.label_unit = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Satuan", width=12, height=2, relief="raised", borderwidth=1)
		self.label_unit.pack(side="left", fill="x", expand=True)

		self.label_stock = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Stok", width=6, height=2, relief="raised", borderwidth=1)
		self.label_stock.pack(side="left", fill="x", expand=True)

		self.label_each_price = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Harga Satuan", width=12, height=2, relief="raised", borderwidth=1)
		self.label_each_price.pack(side="left", fill="x", expand=True)

		self.label_action = Label(self.right_side_frame_title, bg="gray25", font=("Century Gothic", 18, "bold"), fg="white", text="Aksi", width=6, height=2, relief="raised", borderwidth=1)
		self.label_action.pack(side="left", fill="x", expand=True)

	def making_bottom_content(self):
		self.canvas = Canvas(self.right_side_frame_content, width=500, height=700, bg="gray45")
		self.scrollbar = ttk.Scrollbar(self.right_side_frame_content, orient="vertical", command=self.canvas.yview)
		self.frame_scrollable = ttk.Frame(self.canvas)

		self.frame_scrollable.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
		self.canvas.create_window((0,0), window=self.frame_scrollable, anchor="nw")
		self.canvas.configure(yscrollcommand=self.scrollbar.set)

		self.canvas.pack(side="left", expand=True, fill="both")
		self.scrollbar.pack(side="right", fill="y")

		#put all items
		self.put_items_code()
		self.put_items_name()
		self.put_unit()
		self.put_stock()
		self.put_each_price()
		self.put_action()

	def put_items_code(self):
		i = 0
		for x in self.data:
			self.dictionary_label_data[x] = {}
			self.kode_barang = Label(self.frame_scrollable, text=self.data[x]["kode barang"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.kode_barang.grid(row=i, column=0)
			i += 1
			self.dictionary_label_data[x][self.data_structure[0]] = self.kode_barang

	def put_items_name(self):
		i = 0
		for x in self.data:
			self.nama_barang = Label(self.frame_scrollable, text=x, width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.nama_barang.grid(row=i, column=1)
			i += 1
			self.dictionary_label_data[x][self.data_structure[1]] = self.nama_barang

	def put_unit(self):
		i = 0
		for x in self.data:
			self.satuan = Label(self.frame_scrollable, text=self.data[x]["satuan"], width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.satuan.grid(row=i, column=2)
			i += 1
			self.dictionary_label_data[x][self.data_structure[2]] = self.satuan

	def put_stock(self):
		i = 0
		for x in self.data:
			self.stok = Label(self.frame_scrollable, text=self.data[x]["stok"], width=15, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.stok.grid(row=i, column=3)
			i += 1
			self.dictionary_label_data[x][self.data_structure[3]] = self.stok

	def put_each_price(self):
		i = 0
		for x in self.data:
			self.harga_satuan = Label(self.frame_scrollable, text=f"Rp.{self.data[x]['harga satuan']},00", width=24, height=6, relief="raised", borderwidth=1, bg="gray65", font=("Century Gothic", 13, "bold"))
			self.harga_satuan.grid(row=i, column=4)
			i += 1
			self.dictionary_label_data[x][self.data_structure[4]] = self.harga_satuan

	def put_action(self):
		i = 0
		for x in self.data:
			self.sell = Button(self.frame_scrollable, width=14, text="sell", relief="raised", borderwidth=3, font=("Century Gothic", 12), bg="red", command=lambda y=x:[self.if_sell(yangmana=y)])
			self.sell.grid(row=i, column=5)
			i += 1
			self.dictionary_label_data[x][self.data_structure[5]] = self.sell

	def if_sell(self, yangmana):
		self.right_side_frame_title.destroy()
		self.frame_bottom.destroy()

		self.canvas.destroy()
		self.scrollbar.destroy()
		self.frame_scrollable.destroy()

		self.frame_for_sell = Frame(self.which_frame, bg="dark blue", width=6*self.main.width/7, height=700)
		self.frame_for_sell.pack(side="top", fill="both", expand=True)

		#title for the items
		self.kode_barang = Label(self.frame_for_sell, text="Kode Barang", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.kode_barang.place(x=150, y=50)

		self.nama_barang = Label(self.frame_for_sell, text="Nama Barang", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.nama_barang.place(x=150, y=120)

		self.satuan = Label(self.frame_for_sell, text="Satuan", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.satuan.place(x=150, y=190)

		self.stock = Label(self.frame_for_sell, text="Stok", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.stock.place(x=150, y=260)

		self.hargasatuan = Label(self.frame_for_sell, text="Harga Satuan", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.hargasatuan.place(x=150, y=330)

		self.berapaunit = Label(self.frame_for_sell, text="Berapa Unit", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.berapaunit.place(x=150, y=400)

		self.grandtotal = Label(self.frame_for_sell, text="Grandtotal", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.grandtotal.place(x=150, y=470)

		cntr = 50
		for x in range(7):
			self.samadengan = Label(self.frame_for_sell, text="=", bg="dark blue", width=4, font=("Century Gothic", 16, "bold"), fg="white")
			self.samadengan.place(x=400, y=cntr)
			cntr += 70

		self.answer_kode_barang = Label(self.frame_for_sell, text=self.data[yangmana]["kode barang"], bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.answer_kode_barang.place(x=600, y=50)

		self.answer_nama_barang = Label(self.frame_for_sell, text=yangmana, bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.answer_nama_barang.place(x=600, y=120)

		self.answer_satuan = Label(self.frame_for_sell, text=self.data[yangmana]["satuan"], bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.answer_satuan.place(x=600, y=190)

		self.answer_stock = Label(self.frame_for_sell, text=self.data[yangmana]["stok"], bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.answer_stock.place(x=600, y=260)

		self.answer_harga_satuan = Label(self.frame_for_sell, text=f"Rp.{self.data[yangmana]['harga satuan']},00", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.answer_harga_satuan.place(x=600, y=330)

		self.grandtotal_answer = Label(self.frame_for_sell, text="", bg="dark blue", width=18, font=("Century Gothic", 16, "bold"), fg="white")
		self.grandtotal_answer.place(x=600, y=470)

		self.answer_berapa_unit = Entry(self.frame_for_sell, text=5, width=18, font=("Century Gothic", 16))
		self.answer_berapa_unit.place(x=600, y=400)

		self.enter_berapa_unit = Button(self.frame_for_sell, width=3, text="enter", bg="red", command=lambda:[self.making_answer_grand_total(mana=yangmana)])
		self.enter_berapa_unit.place(x=830, y=403)

		self.oke = Button(self.frame_for_sell, text="OK!", width=7, bg="dark blue", font=("Century Gothic", 16, "bold"), fg="white", command=lambda x=yangmana:[self.if_ok(mana=x)], state="disable")
		self.oke.place(x=350, y=550)

	def making_answer_grand_total(self, mana):
		if len(self.answer_berapa_unit.get()) == 0:
			self.answer_berapa_unit.place(x=600, y=400)
		elif int(self.answer_berapa_unit.get()) > int(self.data[mana]["stok"]):
			if self.data[mana]["stok"] == "1":
				messagebox.showerror("error", f"the stock of items is 1 only")
			else:
				messagebox.showerror('error', f'The range of stock items is 1 to {self.data[mana]["stok"]} only!')
			self.answer_berapa_unit.place(x=600, y=400)
		else:
			self.jual_berapa_unit = int(self.answer_berapa_unit.get())
			grandtotal = int(self.answer_berapa_unit.get())*int(self.main.dic_price_int[mana])
			self.grandtotal_answer.configure(text=f"Rp.{self.turning_into_three_points(value=grandtotal)},00")
			self.oke.configure(state=NORMAL)

	def turning_into_three_points(self, value):
		final_value = ""
		counter = 0
		depan = len(str(value))-((len(str(value))//3)*3)
		for x in range(depan):
			final_value += str(value)[x]
			if x+1 == depan:
				final_value += "."
		counter = 0

		for x in str(value)[depan:]:
			if counter == 3:
				final_value += "."
				counter = 0
			final_value += x
			counter += 1
		return final_value

	def if_ok(self, mana):
		#self.frame_for_sell.destroy()
		self.enter_berapa_unit.configure(text=None)
		self.selling_right_frame.destroy()

		value = int(self.data[mana]["stok"])-self.jual_berapa_unit
		self.data[mana]["stok"] = value

		self.main.if_stock_is_zero(yangmana=mana)
		self.frame_selling_right_side()
		self.main.settings.save_master_barang()
	#lanjutke yang if stok is zero!!			