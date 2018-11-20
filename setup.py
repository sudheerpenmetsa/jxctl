import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="jxctl",
    version="0.0.2",
    author="Deepankumar",
    author_email="deepan0433@gmail.com",
    description="A Command line interface for Jenkins",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deepan10/jxctl",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
          'PyYAML>=3.13',
          'Click>=7.0',
          'requests>=2.20.1',
          'tabulate>=0.8.2',
          'pyfiglet>=0.7.6',
          'python-jenkins>=1.4.0'
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
          'console_scripts': [
              'jxctl = jxctl.jxctl:start'
          ]
    },
)