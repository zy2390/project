# from django.core.management.base import BaseCommand, CommandError
# import urllib.request
# import os



# class Command(BaseCommand):
# 	help = 'Export squirrel_data in csv format'

# 	def add_arguments(self, parser):
# 	    parser.add_argument('url', type=str)

# 	def handle(self, *args, **kwargs):
# 	    url = kwargs['url']
# 	    dir = os.getcwd(); #当前工作目录。
# 	    urllib.request.urlretrieve(url, dir+'//squirrel_data.csv')
