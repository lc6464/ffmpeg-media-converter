import os, json, os.path

class Converter:
	def convert(self, root=None, extensions=None, toExt=None):
		self.root = str(root) if root != None else self.root
		self.extensions = list(extensions) if extensions != None else self.extensions
		self.toExt = str(toExt).lower() if toExt != None else self.toExt
		for Dir, _, files in os.walk(self.root):
			Dir += '\\'
			for file in files:
				fn, ext = os.path.splitext(file)
				if ext in self.extensions:
					print(os.system('ffmpeg -i "%s" "%s"' % (Dir + file, Dir + fn + self.toExt)))

	def delete(self, root=None, extensions=None, toExt=None):
		self.root = str(root) if root != None else self.root
		self.extensions = list(extensions) if extensions != None else self.extensions
		self.toExt = str(toExt).lower() if toExt != None else self.toExt
		for Dir, _, files in os.walk(self.root):
			Dir += '\\'
			for file in files:
				fn, ext = os.path.splitext(file)
				if ext in self.extensions:
					if os.path.exists(Dir + fn + self.toExt):
						os.remove(Dir + file)