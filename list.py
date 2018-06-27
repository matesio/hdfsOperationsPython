from pywebhdfs.webhdfs import PyWebHdfsClient
import logging
from pprint import pprint

logging.basicConfig(level=logging.DEBUG)
_LOG = logging.getLogger(__name__)


#host= your server address.
hdfs = PyWebHdfsClient(host='',port='50070', user_name='hduser',timeout=4)  # your Namenode IP & username here
my_dir = '/user/hduser/sample'
fileFinal=my_dir+'/file.txt'
pprint(hdfs.list_dir(my_dir))


dir_status = hdfs.get_file_dir_status(my_dir)
print dir_status
print "Reading file from hadoop hdfs"
file_data = hdfs.read_file("user/hduser/sample/file.txt")

print file_data
