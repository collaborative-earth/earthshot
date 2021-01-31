import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="earthshot", # Replace with your own username
    version="0.0.1",
    author="Earthshot Labs",
    author_email="author@example.com",
    description="A central python package for projects at Eartshot Labs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/earthshot-labs/earthshot",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
