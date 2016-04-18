#coding=utf-8
"Combine tests for gnosis.xml.objectify package (req 2.3+)"
import unittest, doctest,time
import login,R08_NewRequest_1Row,PMIBM_DispatchRequest,AA_EstimateAPP,PMIBM_EstimateRequest_1App,R08_SendForApprovalRequest,R02_ApproveRequest,R04_ApproveRequest,R05_ApproveRequest,R08_CompleteRequest,R08_CloseRequest
import HTMLTestRunner,function

# Wo workflow with 1 approval approve 1 row financial
suite = doctest.DocTestSuite()
suite.addTest(unittest.makeSuite(R08_NewRequest_1Row.R08NewRequest1Row))
suite.addTest(unittest.makeSuite(PMIBM_DispatchRequest.PMIBMDispatchRequest))
suite.addTest(unittest.makeSuite(AA_EstimateAPP.AAEstimateReq))
suite.addTest(unittest.makeSuite(PMIBM_EstimateRequest_1App.PMIBMEstimateRequest))
suite.addTest(unittest.makeSuite(R08_SendForApprovalRequest.R08SendForApprovalRequest))
suite.addTest(unittest.makeSuite(R02_ApproveRequest.R02ApproveRequest))
suite.addTest(unittest.makeSuite(R08_CompleteRequest.R08CompleteRequest))
suite.addTest(unittest.makeSuite(R08_CloseRequest.R08CloseRequest))

runner = function.generateTestReport()
runner.run(suite)