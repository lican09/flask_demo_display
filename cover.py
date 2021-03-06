# -*- coding: utf-8 -*-
import os
import coverage
import unittest

omit = ['cover.py', 'tests/*']

env = os.environ.get('VIRTUAL_ENV')
if isinstance(env, str):
    omit.append(env + '/*')
omit.append('')

cov = coverage.coverage(omit=omit)
cov.start()


if __name__ == '__main__':

    loader = unittest.TestLoader()
    tests = loader.discover('tests')
    runner = unittest.runner.TextTestRunner()
    result = runner.run(tests)
    cov.stop()
    cov.save()
    cov.report()
    cov.html_report(directory='coverage_html')
    cov.erase()
    exit(0 if result.wasSuccessful() else 1)
