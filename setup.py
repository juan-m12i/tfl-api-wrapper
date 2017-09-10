from setuptools import setup, find_packages

setup (
	name='tfl_api',
	version='0.01',
	description='Wrapper for Transport for London API',
	url='http://github.com/juan-m12i/tfl-api-wrapper/',
	author='Juan Montalvo Bressi',
	author_email='juanm12i@icloud.com',
	license='MIT',
	packages=find_packages(exclude=[]),
	keyword="TfL api REST client",
	zip_safe=False,
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Operating System :: POSIX :: Linux",
		"Operating System :: MacOS :: MacOS X",
		"Operating System :: Unix",
		"Environment :: Console",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python",
		"Programming Language :: Python :: 2.7",
	]
)
