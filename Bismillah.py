"""
Annisa Erlambang_J0303201024
#Line 11 hingga 135
#====================================

#Muhammad Fazri Nahar_J0303202170
#Line  138 hinga 207
#===================================="""


def menu():
	import os
	os.system("CLS")
	print(".:Selamat datang:.")
	print("==================\n")
	print("Pilih Menu Berikut: ")
	print("1. Update Konektivitas")
	print("2. Mencari Jarak Terdekat")
	print("3. Daftar Nama Kota")
	print("0. SELESAI")
	print("==================")
	pilih = input("PILIH NOMOR:  ")
	
	if pilih == "1":
		print("==================")
		print("\n.:Daftar Nama Kota Saat Ini:.")
		print("====================")
		x = g.getVertex()
		y = 0
		for i in x:
			y+=1
			print("%2s"%str(y) + ".", i)
		frm = input("\nAsal Kota: ")
		to = input("Kota yang di Tuju: ")
		wght = int(input("Masukkan Jarak: "))
		g.UpdtConnection(frm,to,wght)
		print("tekan [enter] untuk melanjutkan")
		input()
		menu()
	if pilih == "2":
		print("==================")
		print("\n.:Daftar Nama Kota:.")
		print("====================")
		x = g.getVertex()
		y = 0
		for i in x:
			y+=1
			print("%2s"%str(y) + ".", i)
		g.tester()
		print("tekan [enter] untuk melanjutkan")
		input()
		menu()
	if pilih == "3":
		print("==================")
		print("\n.:Daftar Nama Kota:.")
		print("====================")
		x = g.getVertex()
		y = 0
		for i in x:
			y+=1
			print("%2s"%str(y) + ".", i)
		print("tekan [enter] untuk melanjutkan")
		input()
		menu()
	if pilih == "0":
		print("==================")
		print("\nTERIMA KASIH TELAH MENGGUNAKAN PROGRAM INI")


class Graph:
	def __init__(self, gdict=None):
		if gdict is None:
			gdict=[]
		self.gdict=gdict
		
	def getVertex(self):
		vertex = []
		for i in self.gdict.keys():
			for c in i:
				vertex.append(c)
		return list(dict.fromkeys(vertex))


	def UpdtConnection(self,frm,to, wght):
		f = open("data/file.txt")
		isi = f.readlines()
		idx = 0
		frm = frm.upper()
		to = to.upper()
		y = 0
		for x in in_graph:
			i = 0
			if x == (frm,to) and (int(in_graph[(frm,to)]) > int(wght)) :
				for x in isi:
					xp = x.split(" ")
					if xp[0] == frm and xp[1] == to:
						xp[0] = frm
						xp[1] = to
						xp[2] = str(wght) + "\n"
						xg = " ".join(xp)
						isi[idx] = xg
					idx+=1
				print("Berhasil di UPDATE")
				i = 1
				y = 1
			elif x == (to,frm) and (int(in_graph[(to,frm)]) > int(wght)) :
				for x in isi:
					xp = x.split(" ")
					if xp[1] == frm and xp[0] == to:
						xp[0] = to
						xp[1] = frm
						xp[2] = str(wght) + "\n"
						xg = " ".join(xp)
						isi[idx] = xg
					idx+=1
				print("Berhasil di UPDATE")
				i = 1
				y = 1
			elif x == (frm,to) and (int(in_graph[(frm,to)]) < int(wght)) :
				print("Sudah ada jalur Tercepat")
				y = 1
			elif x == (to,frm) and (int(in_graph[(to,frm)]) < int(wght)) :
				print("Sudah ada jalur Tercepat")
				y = 1
		if frm in g.getVertex() and to not in g.getVertex():
			berkas = open("data/file.txt", 'a')
			berkas.write(frm+" "+to+" "+str(wght)+"\n")
			print("Berhasil di UPDATE")
			y = 1
		elif to in g.getVertex() and frm not in g.getVertex():
			berkas = open("data/file.txt", 'a')
			berkas.write(frm+" "+to+" "+str(wght)+"\n")
			print("Berhasil di UPDATE")
			y = 1
		
		if y == 0:
			print("\nMaaf,antara Asal dan Tujuan Kota tidak ada pada daftar")
			
		f.close()
		f = open("data/file.txt","w")
		isi = f.writelines(isi)


	def tester(self):
		start_node = input('\nMasukkan Asal Kota: ') 
		end_node  = input('Masukkan Tujuan: ')
		print("==================\n")
		
		if start_node.upper() in g.getVertex() and end_node.upper() in g.getVertex():
			si = dijkstra(in_graph, start_node.upper())
			spath = shortest(si, end_node.upper())
			s = _output.format(in_graph, start_node.upper(), end_node.upper(),  spath)
			print(s)
		else:
			print("Maaf, Sepertinya ada salah penulisan atau salah satu nama kota yang anda masukkan tidak ada pada daftar")

def duplicate_path(in_graph):
	"""Update graph with reverse path costs"""
	out_graph = {(i[1],i[0]):in_graph[i] for i in in_graph.keys()}
	out_graph.update(in_graph)
	return out_graph


def dijkstra(graph, start_node, makefull = True):
	"""Implementation of Dijkstra's algorithm"""
	if makefull: graph = duplicate_path(graph) 
	# uvnodes : unvisited nodes
	uvnodes = {i[0] for i in graph.keys()}
	# dictionary in the form node : (nearest_node, min_dist)
	searchinfo = {i:(None, float('inf')) for i in uvnodes}
	searchinfo[start_node] = (None, 0)

	while True:
		minm, current = float('inf'), None
		for node in uvnodes:
			cand = searchinfo[node][1]
			if cand < minm:
				current, minm = node, cand
		if minm == float('inf'): break
		uvnodes.remove(current)
		for node in uvnodes:
			path = (current, node)
			if path in graph:
				tentv = searchinfo[current][1] + graph[path]
				if tentv < searchinfo[node][1]:
					searchinfo[node] = (current, tentv)

	return searchinfo
      

def shortest(searchinfo, end_node):
	"""Find the shortest path from search result of dijkstra fn"""
	path, current = [end_node], end_node
	while searchinfo[current][0] != None:
		current = searchinfo[current][0]
		path.append(current)
	path.reverse()
	return path

_output = """\
Input graph is         : {0}\n
Asal Kota: {1}\n   
Kota Tujuan  : {2}\n
Jalur Terdekat       : {3}\n
"""


in_graph = {}
in_file = open("data/file.txt")
for line in in_file:
	key1,key2,value = line.split()
	in_graph[key1,key2] = int(value)
g = Graph(in_graph)

menu()

