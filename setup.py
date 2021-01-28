import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='cli_mailer',  
    version='0.1.1',
    scripts=['cli_mailer'],
    author="Pratyush Saxena",
    author_email="saxena18prats@gmail.com",    description="A command Line mailer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Pratyush-Saxena/CLI_Mailer",
    packages=setuptools.find_packages(),
    install_requires=[
        "click==7.1.2",
        "colorama==0.4.3",
        "constantly==15.1.0",
        "contextlib2==0.6.0.post1",
        "prompt-toolkit==1.0.14",
        "pyfiglet==0.8.post1",
        "pylint==2.5.3",
        "python-http-client==3.2.7",
        "regex==2020.7.14",
        "requests==2.20",
        "sendgrid==6.4.5",
        "urllib3==1.22",
        "virtualenv-clone==0.5.4",
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    python_requires='>=3.6',
 )
