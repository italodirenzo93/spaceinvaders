from setuptools import setup

setup(
	name = 'SpaceInvaders',
	description = 'Its space invaders...',
	author = 'Italo Di Renzo',
	author_email = 'italodirenzo93@gmail.com',
	packages = ['spaceinvaders'],
	package_data = {'spaceinvaders': ['data/*']},
	install_requires = ['pygame'],
	dependency_links = ['https://bitbucket.org/pygame/pygame'],
)
