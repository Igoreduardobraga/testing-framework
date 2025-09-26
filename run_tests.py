from test_loader import TestLoader, TestLoaderTest
from test_runner import TestRunner

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)