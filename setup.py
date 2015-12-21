from distutils.core import setup

files = ['data/*']

setup(
	name = 'SpaceInvaders',
	version = '0.0.0',
	description = 'Its space invaders...',
	author = 'Italo Di Renzo',
	author_email = 'italodirenzo93@gmail.com',
	url = '',
	packages = ['spaceinvaders'],
	package_data = {'package': files},
	long_description = '',
)
