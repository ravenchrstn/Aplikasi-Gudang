from tkinter import *
from settings import Settings
from lobby import Lobby
from master_barang import Master
from transaksi_penjualan import Transaksi_Penjualan

class Main(Tk):

	def __init__(self, app):
		self.settings = Settings(self)
		self.app = app
		self.data = self.settings.thedata

		super().__init__()

		#data
		self.pages = {}
		self.dic_price_int = {}

		#commands
		self.getting_your_resolution()
		self.container()
		self.transaksi_penjualan_page()
		self.master_barang_page()
		self.lobby_page()
		self.convert_to_int()

		#configuration
		self.geometry("%dx%d+0+0" % (self.width, self.height))
		self.title(self.settings.title)
		#self.attributes("-fullscreen", True)	

	def getting_your_resolution(self):
		self.width = self.winfo_screenwidth()
		self.height = self.winfo_screenheight()

	def change_page(self, which):
		change_page = self.pages[which]
		change_page.tkraise()

	def container(self):
		self.container = Frame(self)
		self.container.pack(expand=True, fill="both")

	def lobby_page(self):
		self.pages["lobby_page"] = Lobby(self)

	def master_barang_page(self):
		self.pages["master_barang"] = Master(self)

	def transaksi_penjualan_page(self):
		self.pages["transaksi_penjualan"] = Transaksi_Penjualan(self)

	def if_stock_is_zero(self, yangmana):
		if self.data[yangmana]["stok"] == 0:
			self.data.pop(yangmana)
		self.pages["master_barang"].dictionary_data_label.pop(yangmana)
		self.pages["transaksi_penjualan"].dictionary_label_data.pop(yangmana)

	def convert_to_int(self):
		for name, info in self.settings.data.items():
			self.dic_price_int[name] = int(self.settings.data[name]["harga satuan"].replace(".", ""))

class App:

	def __init__(self):
		self.main = Main(self)

	def starting_app(self):
		self.main.mainloop()

if __name__ == "__main__":
	app = App()
	app.starting_app()

#fokus ke int dan str only di pembuatan yang baru