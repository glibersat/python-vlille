from distutils.core import setup

setup(
    name = "vlille",
    author = "Guillaume Libersat",
    author_email = "glibersat@sigill.org",
    description = "Get information from the Vlille bike system",
    long_description = open("README.rst").read(),
    license = "GPL v3",
    url = "http://github.com/glibersat/python-vlille",
    packages = [
        "vlille",
    ],
    zip_safe=False,
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GPL License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ]
)
