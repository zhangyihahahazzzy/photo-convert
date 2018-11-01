import tkinter.messagebox
import requests
from lxml import etree
from PIL import Image,ImageTk
import tkinter
from tkinter import ttk

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
		im = Image.open('name.jpg')
		bm = ImageTk.PhotoImage(im)
		
		label2 = ttk.Label(root,image=bm)
		label2.bm = bm
		label2.grid(row=2,column=3,columnspan=3)
		
root = tkinter.Tk()
root.title('interesting program')
root.geometry('900x400')


l = ttk.Label(root,text='设计签名').grid(row=0,column=0)

entry = ttk.Entry(root,width=13)
entry.grid(row=1,column=0)
comboxlist = ttk.Combobox(root,width=5)
comboxlist['values'] = ('个性签','连笔签','潇洒签','草体签','合文签','商务签','可爱签')
comboxlist.current(0)
comboxlist.bind("<<ComboxonSelected>>",go)
comboxlist.grid(row=1,column=1)
ttk.Button(root,text='获取签名',command = download).grid(row=1,column=2)

root.mainloop()
