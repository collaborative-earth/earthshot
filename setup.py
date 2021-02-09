from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="earthshot",
    version="0.0.3",
    author="Eartshot Labs Contributors",
    author_email="jlmccreight@gmail.com",
    description="Earthshot Labs Central Python Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/earthshot-labs/earthshot",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "bokeh==2.2.3",
        "earthengine-api==0.1.243",
        "folium>=0.11.0",
        "google-auth==1.24.0",
        "ipython==7.20.0"
        "numpy==1.20.0",
        "pandas==1.2.1",
        "pytest==5.4.3",
        "pytest-html==2.1.1",
        "pytest-datadir-ng==1.1.1",
        "pytest-lazy-fixture==0.6.3",
        "scipy>=1.2.1",
    ],
    packages=find_packages(),
    package_data={"earthshot": ["core/data/*"]},
    python_requires=">=3.6",
)
