import tkinter
from tkinter import ttk
from PIL import Image,ImageTk
import requests
from lxml import etree
import tkinter.messagebox

def go(*args):
	name = comboxlist.get()
	if name == '个性签':
		return 'jfcs.ttf'
	elif name == '连笔签':
		return 'qmt.ttf'
	elif name == '潇洒签':
		return 'bzcs.ttf'
	elif name == "草体签":
		return 'lfc.ttf'
	elif name == "合文签":
		return 'haku.ttf'
	elif name == "商务签":
		return 'zql.ttf'
	elif name == "可爱签":
		return 'yqk.ttf'
		
def download():
	url = 'http://www.uustv.com/'
	name = entry.get()
	if not name:
		tkinter.messagebox.showinfo('提示','请输入名字!')
	else:
		nametype = go()
		data = {
			'word': name,
			'sizes': '60',
			'fonts': nametype,
			'fontcolor': '#000000'
		}
		result = requests.post(url,data=data)
		selector = etree.HTML(result.text)
		r = selector.xpath('//div[@class="tu"]/img/@src')
		imageurl = url + r[0]
		response = requests.get(imageurl).content
		with open('name.jpg','wb') as f:
			f.write(response)
		bm = ImageTk.PhotoImage(Image.open('name.jpg'))
		return bm
def change_photo():
	bm = download()
	second_label.configure(image = bm)
	second_label.image = bm

root = tkinter.Tk()
root.geometry('600x300')
root.title('设计你的签名!')

first_label = ttk.Label(root,text="设计签名").pack(side=tkinter.TOP)

first_frm = ttk.Frame(root)
entry = ttk.Entry(first_frm,width=13)
entry.pack(side=tkinter.LEFT)
comboxlist = ttk.Combobox(first_frm,width=6)
comboxlist['values'] = ('个性签','连笔签','潇洒签','草体签','合文签','商务签','可爱签')
comboxlist.current(0)
comboxlist.bind('<<ComboxonSelected>>',go)
comboxlist.pack(side=tkinter.LEFT)

first_button = ttk.Button(first_frm,text='设计签名',width=10,command=change_photo).pack(side=tkinter.RIGHT)

first_frm.pack()

second_label = ttk.Label(root)
second_label.pack()

root.mainloop()

