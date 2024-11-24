from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="anime-generator",
    version="0.1.0",
    author="Abdul Sohail Ahmed",
    author_email="abdulsohail018@gmail.com",
    description="A Python package for generating anime-style stories with web interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AbdulSohail018/anime-story-generator",
    packages=find_packages(),
    include_package_data=True,  # Add this to include static files
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Flask",
    ],
    python_requires=">=3.7",
    install_requires=[
        "flask>=2.0.0",
        "flask-cors>=3.0.0",
        "python-dotenv>=0.19.0",
    ],
    package_data={
        'src': [
            'static/css/*.css',
            'static/js/*.js',
            'templates/*.html'
        ],
    },
)