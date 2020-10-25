import click, sys

@click.command()
@click.option("--root", '-r', default='.', help='查找要转换的文件的根目录，默认为当前目录。', type=click.STRING)
@click.option("--extensions", '-e', default='', help='要转换的文件扩展名。', type=click.STRING)
@click.option("--to_ext", '-t', default='', help='要转换至的扩展名。', type=click.STRING)
@click.option("--delete", '-d', default=False, help='是否删除源文件，默认为不删除。', type=click.BOOL)
def cli(root='.', extensions='', to_ext='', delete=False):
	if not (extensions.strip(' ') == '' or extensions == None or to_ext.strip(' ') == '' or to_ext == None):
		import Converter as C
		c = C.All(extensions, to_ext, root)
		c.convert()
		if delete:
			c.delete()

if __name__ == '__main__':
	cli()