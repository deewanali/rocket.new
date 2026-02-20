from setuptools import setup, find_packages

setup(
    name='rocket.new',
    version='0.1',
    packages=find_packages(),
    install_requires=[],  # Add your dependencies here
    entry_points={
        'console_scripts': [
            'rocket=rocket.new:main',  # Adjust this based on your package structure
        ],
    },
    author='Your Name',  # Replace with your name
    author_email='youremail@example.com',  # Replace with your email
    description='A short description of your package',
    url='https://github.com/deewanali/rocket.new',  # Replace with your repository URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)