from setuptools import setup, find_packages

with open("README.txt", "r") as fh:
    long_description = fh.read()

setup_args = dict(
                name="engpy",
                version="1.0.1",
                author="Miracle Adebunmi",
                author_email="miraclem2014@gmail.com",
                description="Python for Engineering",
                long_description=long_description,
                license = 'MIT',
                long_description_content_type="text/markdown",
                url="https://github.com/miracle5284/engpy.git",
                packages = find_packages(),
                install_requires = ['matplotlib>=3.3.0'],
                classifiers = [
                                "Programming Language :: Python :: 3",
                                "License :: OSI Approved :: MIT License",
                                "Operating System :: OS Independent",
                              ],
                python_requires ='>=3.6',
                
)

setup(**setup_args)
