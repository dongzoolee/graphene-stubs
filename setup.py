from setuptools import setup
import os

name = "graphene-stubs"
description = "Graphene stubs and mypy plugin"

install_instructions = """
# View installation instructions on github
"""


def find_stub_files():
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith(".pyi"):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    print(result)
    return result


setup(
    name="types-graphene",
    version="0.22",
    description=description,
    long_description=install_instructions,
    long_description_content_type="text/markdown",
    author="dongzoolee",
    author_email="me@leed.at",
    license="MIT License",
    url="https://github.com/dongzoolee/types-graphene",
    py_modules=["graphene_plugin", "graphene_typing"],
    install_requires=["mypy>=0.750", "typing-extensions>=3.6.5"],
    packages=["graphene-stubs"],
    package_data={"graphene-stubs": find_stub_files()},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
