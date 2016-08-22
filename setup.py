from setuptools import setup

setup(name='twitter_streaming',
	version='0.0.1',
	packages=['twitter_streaming']
	entry_point={
		'console_scripts': [
			'twitter_streaming = twitter_streaming.__main__:main'
		]
	},
	)
