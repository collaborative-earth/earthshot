from setuptools import find_packages, setup

setup(
    name="earthshot",
    version="0.0.1",
    packages=find_packages(),
    package_data={"earthshot": ["data/*"]},
    url="https://github.com/earthshot-labs/earthshot",
    license="MIT",
    install_requires=[
        "bokeh==2.2.3",
        "earthengine-api==0.1.243",
        "folium>=0.11.0",
        "numpy==1.18.5",
        "pandas==1.0.5",
        "pytest==5.4.3",
        "pytest-html==2.1.1",
        "pytest-datadir-ng==1.1.1",
        "pytest-lazy-fixture==0.6.3",
        "scipy>=1.2.1",
    ],
    author="Eartshot Labs Contributors",
    author_email="jlmccreight@gmail.com",
    description="Earthshot Labs Central Python Package",
)
