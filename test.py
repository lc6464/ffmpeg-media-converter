import Converter

converter = None
t = input('0.图片\t1.视频\t2.音频：')
d = input('目录（为空则为当前目录）：')
delete = input('是否删除源文件？Y/N：')
d = '.' if (d == None or d == '') else d
# 处理用户需求

if t == '0':
    converter = Converter.Image(d)
elif t == '1':
    converter = Converter.Video(d)
elif t == '2':
    converter = Converter.Audio(d)
else:
    print('数字错误！')
# 实例化转换器对象

if converter != None:
    print('转换中……')
    converter.convert()
    if delete in ['y', 'Y', 'yes', 'Yes', 'YES']:
        print('删除中……')
        converter.delete()
        print('完成！')
# 转换与删除