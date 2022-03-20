import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colbychristian",
    version="0.0.1",
    author="Colby Jamieson",
    author_email="colbyjamieson@outlook.com",
    description="Grove DHT20 temp hum sensor",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colbychristian/pitent",
    project_urls={
        "DHT20": "https://github.com/colbychristian/pitent/tree/main/dht20",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
