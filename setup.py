import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="karafs", 
    version="0.1.1",
    author="Vahid Naeini",
    install_requires=['docutils>=0.3'],
    author_email="naeini.v@gmail.com",
    description="random funny persian name generator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iamvee/karafs",
    packages=setuptools.find_packages(),
    scripts=['bin/karafs'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
