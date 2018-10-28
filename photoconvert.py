import numpy as np
from PIL import Image
from PIL import ImageDraw  
from PIL import ImageFont

def convert_image(image_name,char_table):
	img = Image.open(image_name)
	pix = img.load()
	width = img.size[0]
	height = img.size[1]

	canvas = np.ndarray((height*2, width*2, 3), np.uint8)
	canvas[:, :, :] = 255
	new_image = Image.fromarray(canvas)
	draw = ImageDraw.Draw(new_image)

	font = ImageFont.truetype("consola.ttf", 10, encoding="unic")
	char_table = list(char_table)

	pix_count = 0
	table_len = len(char_table)
	for y in range(height):
		for x in range(width):
			if x%3 == 0 and y%3 == 0:
				draw.text((x*2, y*2), char_table[pix_count % table_len], pix[x, y], font)
				pix_count += 1
	new_image.save('output.jpg')
	new_image.show()
if __name__ == '__main__':
	while True:
		print("============================================")
		image_name = input("请输入图片的名字,如image.jpg(输入q/quit退出程序): ")
		if image_name == 'q' or image_name == 'quit':
			break
		try:
			a = Image.open(image_name)
			char_table = input("请输入想要转换成的英文字母(转换的效果因图片和字母而异,可以有空格): ")
			if char_table == 'q' or char_table == 'quit':
				break
			print("============================================")
			print("图片越大,时间越久,请耐心等待....")
			print("正在转换中,请稍后............")
			convert_image(image_name,char_table)
			print('转换的图片在当前文件夹下,out.jpg')
		except FileNotFoundError:
			print("图片不存在,请重新输入: ")
		
