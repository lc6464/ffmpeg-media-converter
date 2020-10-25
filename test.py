import ffmpeg_media_converter as C

t = input('0.图片\t1.视频\t2.音频：')
r = input('目录（为空则为当前目录）：')
d = input('是否删除源文件？Y/N：')
r = '.' if (r == None or r.strip(' ') == '') else r
# 处理用户需求

if t == '0':
    c = C.Image(r)
elif t == '1':
    c = C.Video(r)
elif t == '2':
    c = C.Audio(r)
else:
    c = None
    print('数字错误！')
# 实例化转换器对象

if c != None:
    print('转换中……')
    c.convert()
    if d in ['y', 'Y']:
        print('删除中……')
        c.delete()
        print('完成！')
# 转换与删除