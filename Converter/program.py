from Converter.Converter import Converter
from Converter.extensions import extensions

class Image(Converter):
	def __init__(self, root='.', extensions=extensions['Image'], toExt='.webp'):
		self.root = root
		self.extensions = extensions
		self.toExt = toExt

class Video(Converter):
	def __init__(self, root='.', extensions=extensions['Video'], toExt='.webm'):
		self.root = root
		self.extensions = extensions
		self.toExt = toExt

class Audio(Converter):
	def __init__(self, root='.', extensions=extensions['Audio'], toExt='.webm'):
		self.root = root
		self.extensions = extensions
		self.toExt = toExt