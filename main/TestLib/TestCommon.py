import time
import numpy as np

import django
from django.test.client import RequestFactory
from django.core.wsgi import get_wsgi_application
from django.test import Client

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RankingMockup.settings")

django.setup()
application = get_wsgi_application()
c = Client()
rf = RequestFactory()

def runAllTests(local_functions):
    start_time = time.time()
    tests_passed = 0
    total_tests = 0
    for f_name, testFunction in local_functions.items():
        if f_name[-5:] == '_test':
            total_tests += 1
            try:
                assert(testFunction() == None)
                tests_passed += 1
            except:
                print('Test Failed! ' + f_name)
    time_taken = time.time() - start_time
    print('Total time taken:', np.round(time_taken, 2))
    print('Tests passed :',tests_passed,'/',total_tests)
