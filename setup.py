try:
    from setuptools import setup, find_packages
    packages = find_packages()
except ImportError:
    from distutils import setup
    packages = ['growl']

setup(name='growl',
        version='0.0.1',
        description='Growler for Python',
        author_email='luke.s.campbell@gmail.com',
        author='Luke Campbell',
        packages=packages,
        install_requires=['gntp'],
        entry_points={'console_scripts':['growl = growl.growl:main']},
        )

