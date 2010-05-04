from setuptools import setup, find_packages
 
setup(
    name='form_helpers',
    version=__import__('form_helpers').__version__,
    description='Helpers for working with Django forms',
    author='Luke Hutscal',
    author_email='luke@creaturecreative.com',
    url='http://github.com/girasquid/django-form-helpers/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)