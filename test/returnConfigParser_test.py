CURRENT_DIR=path.dirname(os.path.abspath(__file__))
sys.path.append(CURRENT_DIR + '/' + "../")

from ConfigParser.returnConfigParser import returnConfigParser


class TestReturnConfigParser(unittest.TestCase):
	def setUp(self):
		self.conf = ConfigParser.SafeConfigParser()
		conf_file = os.path.join(os.path.dirname(__file__), "server.conf")
		(self.conf).read(conf_file)

	def test_GetObject(self):



if __name__ == '__main__':
	unittest.main()