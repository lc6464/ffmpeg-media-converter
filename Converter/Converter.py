import os, json, os.path

class Converter:
	def convert(self, root=None, extensions=None, toExt=None):
		self.root = root if root != None else self.root
		self.extensions = extensions if extensions != None else self.extensions
		self.toExt = toExt if toExt != None else self.toExt
		for Dir, _, files in os.walk(self.root):
			Dir += '\\'
			for file in files:
				fn = os.path.splitext(file)
				if fn[1] in self.extensions:
					print(os.system('ffmpeg -i "%s" "%s"' % (Dir + file, Dir + fn[0] + self.toExt)))

	def delete(self, root=None, extensions=None):
		self.root = root if root != None else self.root
		self.extensions = extensions if extensions != None else self.extensions
		for Dir, _, files in os.walk(self.root):
			Dir += '\\'
			for file in files:
				fn = os.path.splitext(file)
				if fn[1] in self.extensions:
					os.remove(Dir + file)