from pywebhdfs.webhdfs import PyWebHdfsClient
import logging

logging.basicConfig(level=logging.DEBUG)
_LOG = logging.getLogger(__name__)

example_dir='/user/hive/warehouse/sample'
example_file='{dir}/file.txt'.format(dir=example_dir)

hdfs = PyWebHdfsClient(host='', port='50070',
                       user_name='hduser')


print('reading data from file at: {0}\n'.format(example_file))
file_data = hdfs.read_file(example_file)
print(file_data)

