from setuptools import setup
import os
import codecs
import sys
import re
from country_dialcode import __version__ as version


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


# Compile the list of packages available, because distutils doesn't have
# an easy way to do this.
packages, data_files, temp_data_files, addons_data_files = [], [], [], []
docs_data_files, resources_data_files = [], []

root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('country_dialcode'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'):
            del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        prefix = dirpath[12:]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))


def parse_requirements(file_name):
    requirements = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'(\s*#)|(\s*$)', line):
            continue
        if re.match(r'\s*-e\s+', line):
            requirements.append(re.sub(r'\s*-e\s+.*#egg=(.*)$', r'\1', line))
        elif re.match(r'(\s*git)|(\s*hg)', line):
            pass
        else:
            requirements.append(line)
    return requirements


def parse_dependency_links(file_name, install_flag=False):
    dependency_links = []
    for line in open(file_name, 'r').read().split('\n'):
        if re.match(r'\s*-e\s+', line):
            dependency_links.append(re.sub(r'\s*-e\s+', '', line))
        if re.match(r'(\s*git)|(\s*hg)', line):
            if install_flag:
                line_arr = line.split('/')
                line_arr_length = len(line.split('/'))
                pck_name = line_arr[line_arr_length - 1].split('.git')
                if len(pck_name) == 2:
                    os.system('pip install -f %s %s' % (pck_name[0], line))
                if len(pck_name) == 1:
                    os.system('pip install -f %s %s' % (pck_name, line))
    return dependency_links


install_flag = False
if sys.argv[1] == "install":
    install_flag = True


setup(
    name='django-country-dialcode',
    version=version,
    description='Django Application providing Dialcode and Countries code',
    long_description=read('README.rst'),
    author='Belaid Arezqui',
    author_email='areski@gmail.com',
    url='http://github.com/Star2Billing/django-country-dialcode',
    packages=packages,
    package_data={
        "": [
            "fixtures/*",
        ]
    },
    include_package_data=True,
    download_url='https://github.com/Star2Billing/django-country-dialcode/tarball/master',
    zip_safe=False,
    package_dir={'country_dialcode': 'country_dialcode'},
    entry_points={'django.apps': 'country_dialcode = country_dialcode'},
    install_requires=parse_requirements('requirements.txt'),
    dependency_links=parse_dependency_links('requirements.txt', install_flag),
    license='MIT License',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
