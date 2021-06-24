import setuptools

# При обновление поменять version, download_url
# python setup.py sdist
# twine upload dist/*

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bizzare-formatter",
    version="1.0.0",
    author="Peter Ibragimov",
    author_email="peter.ibragimov@gmail.com",
    description="Easy way to create beautiful images from python code",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TeaDove/bizzare_formatter",
    licence='gpl-3.0',
    keywords = ['PIPE', 'UTILITY'],
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: Unix',
        'Topic :: Utilities'
    ],
    python_requires='>=3.7',
    entry_points = {
        'console_scripts': ['bizzare-formatter=bizzare_formatter.main:main']
    },
    install_requires=[
        "Pygments==2.9.0",
        "Pillow==8.2.0",
    ]
)
