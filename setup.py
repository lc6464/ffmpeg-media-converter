from setuptools import setup, find_packages


with open("README.md", encoding="utf-8") as f:
	long_description = f.read()


setup(
	name="ffmpeg-media-converter",
	description="Batch media file format converter based on ffmpeg.",
	version="0.2.1",
	packages=find_packages(),
	url="https://github.com/lc6464/ffmpeg-media-converter",
	license="Apache License 2.0",
	long_description=long_description,
	long_description_content_type="text/markdown"
)