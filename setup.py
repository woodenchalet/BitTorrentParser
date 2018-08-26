import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bittorrent Parser",
    version="0.0.1",
    author="Yi Luo",
    author_email="chalet056@gmail.com",
    description="A simple parser for .torrent file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woodenchalet/BitTorrentParser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)