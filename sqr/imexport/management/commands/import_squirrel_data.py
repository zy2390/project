from django.core.management.base import BaseCommand, CommandError
import urllib.request
import os



class Command(BaseCommand):
	help = 'Import squirrel_data in csv format'

	def add_arguments(self, parser):
	    parser.add_argument('url', type=str)

	def handle(self, *args, **kwargs):
	    url = kwargs['url']
	    # url = 'https://data.cityofnewyork.us/api/views/vfnx-vebw/rows.csv'
	    dir = os.getcwd(); #当前工作目录。
	    urllib.request.urlretrieve(url, dir+'//squirrel_data.csv')
	# https://blog.csdn.net/zhangphil/article/details/87704179
	# https://blog.csdn.net/qq_34971175/article/details/79430274
	# https://simpleisbetterthancomplex.com/tutorial/2018/08/27/how-to-create-custom-django-management-commands.html
