import setuptools
  
with open("README.md", "r") as fh:
    description = fh.read()
  
setuptools.setup(
    name="my-minipack",
    version="1.0.0",
    author="jiglesia",
    author_email="jiglesia@student.42.fr",
    packages=["my_minipack"],
    description="Package to show a loading bar and a logger.",
    long_description=description,
    long_description_content_type="text/markdown",
    url="None",
    license='MIT',
    python_requires='>=3.7',
    install_requires=[],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Students",
        "Topic :: Education",
        "Topic :: HowTo",
        "Topic :: Package",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ]
)