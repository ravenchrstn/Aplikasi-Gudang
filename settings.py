from json import load, dump

class Settings:

	def __init__(self, main):
		self.main = main
		self.title = "Aplikasi Gudang"

		self.logo_path = "img/xiaomi.png"
		self.background_path = "img/mario.png"
		self.delete_path = "img/delete.png"
		self.edit_path = "img/edit.png"
		self.master_barang_file_path = "data_master_barang.json"

		self.data = self.load_master_barang()
		
	def load_master_barang(self):
		with open(self.master_barang_file_path, "r") as file:
			self.thedata = load(file)
		return self.thedata

	def save_master_barang(self):
		with open(self.master_barang_file_path, "w") as save:
			dump(self.thedata, save)

	def update_dic_price_to_data(self):
		for name, info in self.data.items():
			self.data[name]["stok"]	
		
		