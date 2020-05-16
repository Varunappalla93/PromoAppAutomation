import unittest
from TestCases.TC1_LoginTest import Logintest
from TestCases.TC2_SignUpTest import SignUptest
from TestCases.TC3_ManageEvent import ManageEventtest
tc1=unittest.TestLoader().loadTestsFromTestCase(Logintest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUptest)
tc3=unittest.TestLoader().loadTestsFromTestCase(ManageEventtest)

#Sanity test Suite
sanitytestsuite=unittest.TestSuite([tc1,tc2])

#Functional test Suite
functionaltestsuite=unittest.TestSuite([tc3])

#Run Suites
unittest.TextTestRunner().run(sanitytestsuite)
unittest.TextTestRunner().run(functionaltestsuite)
