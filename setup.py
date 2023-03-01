from setuptools import setup, find_packages

setup(
    name='Explained Recommendations',
    version='0.1.0',
    author='Fer Aguirre',
    description='A repository for building a system recommendation explained using generative AI for prompt engineering, text embeddings and vector search. This model will be deployed with Steamship packages and applied to Writing Atlas content.',
    python_requires='>=3',
    license='MIT License',
    packages=find_packages(),
)