from setuptools import setup, find_packages

setup(
    name='KubeflowProject',
    version='0.1.0',
    description='Machine Learning project utilizing Kubeflow for managing ML workflows',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://yourprojectrepository.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'flask',
        'kubeflow-kale',  # If using Kale for Kubeflow Pipelines
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    keywords='machine learning, kubeflow, data science, ML pipelines',
    python_requires='>=3.6, <4',
    project_urls={
        'Bug Reports': 'https://yourprojectrepository.com/issues',
        'Source': 'https://yourprojectrepository.com/',
    },
)
