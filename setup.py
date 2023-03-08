from setuptools import setup, find_packages

__version__ = '0.2-alpha'
url = 'https://github.com/georgianpartners/Multimodal-Toolkit'

install_requires = [
    'torch>=1.13.1',
    'transformers>=4.26.1',
    'numpy>=1.21.6',
    'tqdm>=4.64.1',
    'scipy>=1.7.3',
    'networkx>=2.6.3',
    'scikit-learn>=1.0.2',
    'pandas>=1.3.5',
    'sacremoses>=0.0.53',
    'pytest>=7.2.2'
]

setup(
    name='multimodal_transformers',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    license='MIT',
    description='Multimodal Extension Library for PyTorch HuggingFace Transformers',
    author='Ken Gu',
    author_email='kgu@georgianpartners.com',
    maintainer='Akash Saravanan, Kyryl Truskovskyi',
    maintainer_email='akash.saravanan@georgian.io, kyryl@georgian.io'
    url=url,
    download_url='{}/archive/v_{}.tar.gz'.format(url, __version__),
    keywords=['pytorch', 'multimodal', 'transformers', 'huggingface'],   # Keywords that define your package best
    install_requires=install_requires,
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',      # Define that your audience are developers
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
  ],
)
