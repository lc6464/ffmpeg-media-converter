"""
用途：
	将一个文件夹下的所有指定扩展名（可指定多个）的媒体文件转换为指定的格式。
原理：
	使用 FFmpeg 进行转换。
缺陷：
	- FFmpeg 不支持的文件格式无法转换（被转换和转换至的文件格式任意一个不支持都将无法成功）
	- delete 方法删除文件时无法判断是否转换成功，所有指定扩展名（可指定多个）的文件均会被删除
使用：
	- Image  Audio  Video 三个 class 根据需要自行选择，默认：
		- From：
			- "Image": [".png", ".jpg", ".bmp", ".jpeg", ".jpe", ".gif", ".tif", ".tiff"]
			- "Audio": [".mp3", ".flac", ".m4a", ".ogg", ".oga", ".wma", ".wav"]
			- "Video": [".mp4", ".mov", ".avi", ".flv", ".3gp", ".h264", ".mpeg", ".ogv", ".wmv"]
		- To：
			- Image：.webp
			- Audio: .webm
			- Video: .webm
	- 三个类功能其实一致，只是初始化时的默认参数不同，可随意使用
	- 实例方法：
		- convert 转换
			- 将遍历文件夹，转换所有指定扩展名的文件到指定格式
			- 调用 FFmpeg，请确保 FFmpeg 加入了环境变量
		- delete 删除
			- 将遍历文件夹，删除所有指定扩展名的文件
			- 此方法无需 FFmpeg
			- 无法单独保留某个扩展名在指定扩展名列表内的文件，将会全部删除
"""
from Converter.program import *