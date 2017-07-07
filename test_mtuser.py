# -*- coding: utf-8 -*-
from multiprocessing import Process, Queue, Manager
import os
import time
from requests import Request, Session
import requests
import ujson
import sys

jd_login_url = "http://gg.test.ik3cloud.com/k3cloud/Kingdee.BOS.WebApi.ServicesStub.AuthService.ValidateUser.common.kdsvc"
jd_test_url = "http://gg.test.ik3cloud.com/K3cloud/Kingdee.BOS.WebApi.ServicesStub.DynamicFormService.BatchSave.common.kdsvc"

test_body = {
  "format": 1,
  "useragent": "ApiClient",
  "rid": "1327693546",
  "parameters": "[\"PUR_PurchaseOrder\",\"{\\\"NumberSearch\\\":\\\"True\\\",\\\"ValidateFlag\\\":\\\"True\\\",\\\"IsDeleteEntry\\\":\\\"True\\\",\\\"NeedUpDateFields\\\":[],\\\"NeedReturnFields\\\":[],\\\"SubSystemId\\\":\\\"\\\",\\\"Model\\\": [{\\\"FID\\\": \\\"0\\\",\\\"FBillTypeID\\\": {\\\"FNumber\\\": \\\"CGDD01_SYS\\\"},\\\"FCorrespondOrgId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FConfirmerId\\\": {\\\"FUserID\\\": \\\"\\\"},\\\"FConfirmDate\\\": \\\"1900-01-01\\\",\\\"FBillNo\\\": \\\"\\\",\\\"FDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FSupplierId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FPurchaseOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FPurchaseDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPurchaserGroupId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPurchaserId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FProviderId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FProviderAddress\\\": \\\"\\\",\\\"FSettleId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FChargeId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FProviderContact\\\": \\\"\\\",\\\"FIsModificationOperator\\\": false,\\\"FProviderContactId\\\": {\\\"FCONTACTNUMBER\\\": \\\"\\\"},\\\"FPOOrderFinance\\\": {\\\"FISPRICEEXCLUDETAX\\\": true,\\\"FSEPSETTLE\\\": false,\\\"FSettleCurrId\\\": {\\\"FNumber\\\": \\\"PRE001\\\"},\\\"FPayConditionId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FExchangeTypeId\\\": {\\\"FNumber\\\": \\\"HLTX01_SYS\\\"},\\\"FExchangeRate\\\": 1,\\\"FPriceListId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FDiscountListId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPriceTimePoint\\\": \\\"1\\\",\\\"FSettleModeId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FIsIncludedTax\\\": true,\\\"FLocalCurrId\\\": {\\\"FNumber\\\": \\\"PRE001\\\"},\\\"FPAYADVANCEAMOUNT\\\": 0,\\\"FSupToOderExchangeBusRate\\\": 1,\\\"FFOCUSSETTLEORGID\\\": {\\\"FNumber\\\": \\\"100\\\"}},\\\"FPOOrderEntry\\\": [{\\\"FEntryID\\\": null,\\\"FProductType\\\": \\\"1\\\",\\\"FMaterialId\\\": {\\\"FNumber\\\": \\\"CH4441\\\"},\\\"FRequireDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FMaterialDesc\\\": \\\"平板电脑\\\",\\\"FUnitId\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FQty\\\": 1,\\\"FPriceUnitId\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FPriceUnitQty\\\": 1,\\\"FInventoryQty\\\": 0,\\\"FLocationId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FDeliveryDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FPrice\\\": 2991.452991,\\\"FTaxPrice\\\": 3500,\\\"FEntryDiscountRate\\\": 0,\\\"FLocationAddress\\\": null,\\\"FTaxCombination\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntryTaxRate\\\": 17,\\\"FLocation\\\": null,\\\"FRequireOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FCentSettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryLastDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FDeliveryEarlyDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FDeliveryMaxQty\\\": 1,\\\"FDeliveryControl\\\": false,\\\"FReceiveOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDispSettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryMinQty\\\": 1,\\\"FPriceCoefficient\\\": 1,\\\"FChargeProjectID\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntrySettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryBeforeDays\\\": 0,\\\"FGiveAway\\\": false,\\\"FEntryNote\\\": null,\\\"FDeliveryDelayDays\\\": 0,\\\"FMtoNo\\\": null,\\\"FTimeControl\\\": false,\\\"FGroup\\\": 0,\\\"FLot\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FSupMatId\\\": null,\\\"FSupMatName\\\": null,\\\"FDeliveryStockStatus\\\": {\\\"FNumber\\\": \\\"KCZT02_SYS\\\"},\\\"FProcesser\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntrySettleModeId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntryPayOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FPlanConfirm\\\": true,\\\"FReceiveDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FMaxPrice\\\": 0,\\\"FMinPrice\\\": 0,\\\"FIsStock\\\": false,\\\"FConsumeSumQty\\\": 0,\\\"FBaseConsumeSumQty\\\": 0,\\\"FContractNo\\\": null,\\\"FReqTraceNo\\\": null,\\\"FSupplierLot\\\": null,\\\"FBomId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FBaseSalJoinQty\\\": 0,\\\"FSalJoinQty\\\": 0,\\\"FPriceBaseQty\\\": 1,\\\"FSetPriceUnitID\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FSalUnitID\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FSalQty\\\": 1,\\\"FSalBaseQty\\\": 1,\\\"FStockUnitID\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FStockQty\\\": 1,\\\"FStockBaseQty\\\": 1,\\\"FSubOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FEntryDeliveryPlan\\\": [{\\\"FDetailId\\\": null,\\\"FDeliveryDate_Plan\\\": \\\"2017-07-03 00:00:00\\\",\\\"FPlanQty\\\": 1,\\\"FELocation\\\": \\\"\\\",\\\"FELocationAddress\\\": \\\"\\\",\\\"FSUPPLIERDELIVERYDATE\\\": null,\\\"FTRLT\\\": 0,\\\"FPREARRIVALDATE\\\": \\\"2017-07-03 00:00:00\\\",\\\"FELocationId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FConfirmDeliQty\\\": 0,\\\"FConfirmDeliDate\\\": null,\\\"FConfirmInfo\\\": null}]}]}, {\\\"FID\\\": \\\"0\\\",\\\"FBillTypeID\\\": {\\\"FNumber\\\": \\\"CGDD01_SYS\\\"},\\\"FCorrespondOrgId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FConfirmerId\\\": {\\\"FUserID\\\": \\\"\\\"},\\\"FConfirmDate\\\": \\\"1900-01-01\\\",\\\"FBillNo\\\": \\\"\\\",\\\"FDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FSupplierId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FPurchaseOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FPurchaseDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPurchaserGroupId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPurchaserId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FProviderId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FProviderAddress\\\": \\\"\\\",\\\"FSettleId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FChargeId\\\": {\\\"FNumber\\\": \\\"GYS-DS-0\\\"},\\\"FProviderContact\\\": \\\"\\\",\\\"FIsModificationOperator\\\": false,\\\"FProviderContactId\\\": {\\\"FCONTACTNUMBER\\\": \\\"\\\"},\\\"FPOOrderFinance\\\": {\\\"FISPRICEEXCLUDETAX\\\": true,\\\"FSEPSETTLE\\\": false,\\\"FSettleCurrId\\\": {\\\"FNumber\\\": \\\"PRE001\\\"},\\\"FPayConditionId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FExchangeTypeId\\\": {\\\"FNumber\\\": \\\"HLTX01_SYS\\\"},\\\"FExchangeRate\\\": 1,\\\"FPriceListId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FDiscountListId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FPriceTimePoint\\\": \\\"1\\\",\\\"FSettleModeId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FIsIncludedTax\\\": true,\\\"FLocalCurrId\\\": {\\\"FNumber\\\": \\\"PRE001\\\"},\\\"FPAYADVANCEAMOUNT\\\": 0,\\\"FSupToOderExchangeBusRate\\\": 1,\\\"FFOCUSSETTLEORGID\\\": {\\\"FNumber\\\": \\\"100\\\"}},\\\"FPOOrderEntry\\\": [{\\\"FEntryID\\\": null,\\\"FProductType\\\": \\\"1\\\",\\\"FMaterialId\\\": {\\\"FNumber\\\": \\\"CH4441\\\"},\\\"FRequireDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FMaterialDesc\\\": \\\"平板电脑\\\",\\\"FUnitId\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FQty\\\": 1,\\\"FPriceUnitId\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FPriceUnitQty\\\": 1,\\\"FInventoryQty\\\": 0,\\\"FLocationId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FDeliveryDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FPrice\\\": 2991.452991,\\\"FTaxPrice\\\": 3500,\\\"FEntryDiscountRate\\\": 0,\\\"FLocationAddress\\\": null,\\\"FTaxCombination\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntryTaxRate\\\": 17,\\\"FLocation\\\": null,\\\"FRequireOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FCentSettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryLastDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FDeliveryEarlyDate\\\": \\\"2017-07-03 00:00:00\\\",\\\"FDeliveryMaxQty\\\": 1,\\\"FDeliveryControl\\\": false,\\\"FReceiveOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDispSettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryMinQty\\\": 1,\\\"FPriceCoefficient\\\": 1,\\\"FChargeProjectID\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntrySettleOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FDeliveryBeforeDays\\\": 0,\\\"FGiveAway\\\": false,\\\"FEntryNote\\\": null,\\\"FDeliveryDelayDays\\\": 0,\\\"FMtoNo\\\": null,\\\"FTimeControl\\\": false,\\\"FGroup\\\": 0,\\\"FLot\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FSupMatId\\\": null,\\\"FSupMatName\\\": null,\\\"FDeliveryStockStatus\\\": {\\\"FNumber\\\": \\\"KCZT02_SYS\\\"},\\\"FProcesser\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntrySettleModeId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FEntryPayOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FPlanConfirm\\\": true,\\\"FReceiveDeptId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FMaxPrice\\\": 0,\\\"FMinPrice\\\": 0,\\\"FIsStock\\\": false,\\\"FConsumeSumQty\\\": 0,\\\"FBaseConsumeSumQty\\\": 0,\\\"FContractNo\\\": null,\\\"FReqTraceNo\\\": null,\\\"FSupplierLot\\\": null,\\\"FBomId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FBaseSalJoinQty\\\": 0,\\\"FSalJoinQty\\\": 0,\\\"FPriceBaseQty\\\": 1,\\\"FSetPriceUnitID\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FSalUnitID\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FSalQty\\\": 1,\\\"FSalBaseQty\\\": 1,\\\"FStockUnitID\\\": {\\\"FNumber\\\": \\\"tai\\\"},\\\"FStockQty\\\": 1,\\\"FStockBaseQty\\\": 1,\\\"FSubOrgId\\\": {\\\"FNumber\\\": \\\"100\\\"},\\\"FEntryDeliveryPlan\\\": [{\\\"FDetailId\\\": null,\\\"FDeliveryDate_Plan\\\": \\\"2017-07-03 00:00:00\\\",\\\"FPlanQty\\\": 1,\\\"FELocation\\\": \\\"\\\",\\\"FELocationAddress\\\": \\\"\\\",\\\"FSUPPLIERDELIVERYDATE\\\": null,\\\"FTRLT\\\": 0,\\\"FPREARRIVALDATE\\\": \\\"2017-07-03 00:00:00\\\",\\\"FELocationId\\\": {\\\"FNumber\\\": \\\"\\\"},\\\"FConfirmDeliQty\\\": 0,\\\"FConfirmDeliDate\\\": null,\\\"FConfirmInfo\\\": null}]}]}],\\\"BatchCount\\\":\\\"0\\\"}\"]",
  "timestamp": "/Date(1499066584566+0800)/",
  "v": "1.0"
}

USER_COUNT = 50
TEST_COUNT = 50

def test_func(account_idx, shared_dict):
    p_id = os.getpid()
    # print "pid: %s start working..."%(p_id)

    headers = {
        'content-type': 'application/json'
    }
    login_body = {
        "format": 1,
        "useragent": "ApiClient",
        "rid": "-1913060553",
        "parameters": "[\"591ba7e977faa7\",\"TEST{:03d}\",\"ik3cloud@\",2052]".format(account_idx), 
        "timestamp": "\/Date(1499053088063+0800)\/",
        "v": "1.0"
    }

    success_count = 0
    failed_count = 0
    failed_message_list = []

    for _ in range(TEST_COUNT):
        try:
            # log in
            login_resp = requests.post(jd_login_url, headers=headers, data=ujson.dumps(login_body) ,timeout=20)
            # grab cookie
            headers['ASP.NET_SessionId'] = login_resp.cookies['ASP.NET_SessionId']
            headers['kdservice-sessionid'] = login_resp.cookies['kdservice-sessionid']
            # send test requests
            test_resp = requests.post(jd_test_url, headers=headers, data=ujson.dumps(test_body), timeout=20)
            
            # remote api did not use 400/500 properly (fuck it!), use content-length for fast check to save time
            if test_resp.status_code == 200 and int(test_resp.headers['Content-Length']) in range(260, 280):
                success_count += 1
            else:
                failed_message_list.append(test_resp.text)
                failed_count += 1
        except Exception as e:
            failed_count += 1

    shared_dict[account_idx] = {
        'pid': p_id,
        'done': TEST_COUNT,
        'success': success_count,
        'failed': failed_count,
        'failed_message': failed_message_list
    }
    # print "pid %s done, %d success, %d failed, s_rate: %.2f "%(p_id, success_count, failed_count, success_count/float(TEST_COUNT))

def main():
    shared_dict = Manager().dict()
    p_list = [Process(target=test_func, args=(i, shared_dict)) for i in range(1, USER_COUNT+1)]
    s_time = time.time() 
    map(lambda p: p.start(), p_list)
    print "%d processes starting ..."%(USER_COUNT)
    all_processes_done = False
    while not all_processes_done:
        done_count = 0
        for p in p_list:
            if not p.is_alive():
                done_count += 1
        s_used = time.time() - s_time
        if done_count == USER_COUNT:
            all_processes_done = True
        if s_used > 300:
            print "out of time, killing all process.."
            map(lambda p: p.terminate(), p_list)
            all_processes_done = True
        time.sleep(0.001)
    print "all process done"
    total_request_done = 0
    total_request_success = 0
    total_request_failed = 0
    total_success_rate = 0.0    

    for k, ele in dict(shared_dict).iteritems():
        total_request_done += ele['done']
        total_request_success += ele['success']
        total_request_failed += ele['failed']

    total_success_rate = total_request_success/float(total_request_done) if total_request_done > 0 else 0.0
    print "%.3f sec used, total %d requests, %d success, %d failed, %.2f success rate, %.2f req/sec "\
        %(s_used, total_request_done, total_request_success, total_request_failed, total_success_rate, total_request_done/s_used)

if __name__ == '__main__':
    main()
  