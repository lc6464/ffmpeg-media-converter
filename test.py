import Converter

converter = None
t = input('0.图片\t1.视频\t2.音频：')
d = input('目录（为空则为当前目录）：')
delete = input('是否删除源文件？输入1则删除：')
d = '.' if (d == None or d == '') else d

if t == '0':
	converter = Converter.Image(d)
elif t == '1':
	converter = Converter.Video(d)
elif t == '2':
	converter = Converter.Audio(d)
else:
	print('数字错误！')

if converter != None:
	print('转换中……')
	converter.convert()
	if delete == '1':
		print('删除中……')
		converter.delete()
		print('完成！')