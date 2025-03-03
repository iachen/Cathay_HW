import uiautomator2 as u2
import time
import toml
import pytest
import logging
import allure
import operations as op


d = u2.connect_usb()
#logging.basicConfig(level=logging.DEBUG)

# match data
configure = toml.load('data.ini')
cathay_url = configure['url']['url']

xinyi_total = configure['taipeidata']['xinyi_total']
xinyi_downpay = configure['taipeidata']['xinyi_downpay']
xinyi_homeloan = configure['taipeidata']['xinyi_homeloan']

daan_total = configure['taipeidata']['daan_total']
daan_downpay = configure['taipeidata']['daan_downpay']
daan_homeloan = configure['taipeidata']['daan_homeloan']
daan_percent = configure['taipeidata']['daan_percent']

neihu_total = configure['taipeidata']['neihu_total']
neihu_downpay = configure['taipeidata']['neihu_downpay']
neihu_homeloan = configure['taipeidata']['neihu_homeloan']
neihu_percent = configure['taipeidata']['neihu_percent']

shilin_total = configure['taipeidata']['shilin_total']
shilin_downpay = configure['taipeidata']['shilin_downpay']
shilin_homeloan = configure['taipeidata']['shilin_homeloan']
shilin_percent = configure['taipeidata']['shilin_percent']

hsinchu_total = configure['hsinchudata']['total']
hsinchu_downpay = configure['hsinchudata']['downpay']
hsinchu_homeloan = configure['hsinchudata']['homeloan']

# Taichung
taichung_total = configure['taichungdata']['total']
taichung_downpay = configure['taichungdata']['downpay']
taichung_homeloan = configure['taichungdata']['homeloan']





# launch Chorme
d.app_start("com.android.chrome")

# locate search bar and access cathay bank url
if d(resourceId="com.android.chrome:id/search_box", packageName="com.android.chrome").exists(timeout=3.0):
    d(resourceId="com.android.chrome:id/search_box", packageName="com.android.chrome").click()
if d(resourceId="com.android.chrome:id/url_bar", packageName="com.android.chrome").exists(timeout=3.0):
    d(resourceId="com.android.chrome:id/url_bar", packageName="com.android.chrome").set_text(cathay_url)
    #d(resourceId="com.google.android.inputmethod.latin:id/key_pos_ime_action", packageName="com.google.android.inputmethod.latin").click()
    d.press("enter")



@allure.feature("Test 首頁")
@allure.description("Check if the URL is accessible")
def test_url():
    try:
        assert d(text="房貸試算-建議購屋預算", packageName="com.android.chrome").exists(timeout=3.0)
        logging.info("*** PASS!!! URL '房貸試算-建議購屋預算' is accessible ***")
        d.screenshot("./pic/建議購屋預算首頁.png")
        allure.attach.file("./pic/建議購屋預算首頁.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! URL '房貸試算-建議購屋預算' is NOT accessible... ***")
        d.screenshot("./pic/建議購屋預算首頁.png")
        allure.attach.file("./pic/建議購屋預算首頁.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e



@allure.feature("Test 不同縣市/區域-新竹竹北-1")
@allure.description("試算結果")
def test_zhubei_result():
    op.refresh()
    time.sleep(2)
    op.choose_zhubei()
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-新竹竹北' exists ***")
        d.screenshot("./pic/試算結果_新竹竹北.png")
        allure.attach.file("./pic/試算結果_新竹竹北.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-新竹竹北' NOT exists... ***")
        d.screenshot("./pic/試算結果_新竹竹北_error.png")
        allure.attach.file("./pic/試算結果_新竹竹北_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-新竹竹北-2")
@allure.description("最高成數")
def test_zhubei_percent():
    zhubei_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert zhubei_percent == "6.5～7成"
        logging.info(f"*** PASS!!! 成數-新竹竹北'{zhubei_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_新竹竹北.png")
        allure.attach.file("./pic/成數_新竹竹北.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-新竹竹北'{zhubei_percent}' 不符合預期'6.5～7成'... ***")
        d.screenshot("./pic/成數_新竹竹北_error.png")
        allure.attach.file("./pic/成數_新竹竹北_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-新竹竹北-3")
@allure.description("總金額")
def test_zhubei_total():
    cur_zhubei_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_zhubei_total == hsinchu_total
        logging.info(f"*** PASS!!! 總金額-新竹竹北'{cur_zhubei_total}' 符合預期'{hsinchu_total}' ***")
        d.screenshot("./pic/總金額_新竹竹北.png")
        allure.attach.file("./pic/總金額_新竹竹北.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-新竹竹北'{cur_zhubei_total}' 不符合預期'{hsinchu_total}'... ***")
        d.screenshot("./pic/總金額_新竹竹北_error.png")
        allure.attach.file("./pic/總金額_新竹竹北_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


# 新竹竹北
@allure.feature("Test 不同縣市/區域-新竹竹北-4")
@allure.description("自備款金額及房貸金額")
def test_zhubei_loan():
    cu_zhubei_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cu_zhubei_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cu_zhubei_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_zhubei_total = int(cu_zhubei_total[:-1].replace(",", ""))
    new_zhubei_downpay = int(cu_zhubei_downpay[:-1].replace(",", ""))
    new_zhubei_homeloan = int(cu_zhubei_homeloan[:-1].replace(",", ""))
    try:
        assert new_zhubei_total == new_zhubei_downpay + new_zhubei_homeloan
        logging.info(f"*** PASS!!! 新竹竹北 總金額-自付-貸款'{new_zhubei_total} = {new_zhubei_downpay} + {new_zhubei_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_新竹竹北.png")
        allure.attach.file("./pic/總金額-自付-貸款_新竹竹北.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 新竹竹北 總金額-自付-貸款'{new_zhubei_total} = {new_zhubei_downpay} + {new_zhubei_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_新竹竹北_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_新竹竹北_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e



@allure.feature("Test 相同縣市/區域-台北大安-1")
@allure.description("試算結果")
def test_daan_result():
    op.refresh()
    time.sleep(2)
    op.choose_daan()
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-台北大安' exists ***")
        d.screenshot("./pic/試算結果_台北大安.png")
        allure.attach.file("./pic/試算結果_台北大安.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-台北大安' NOT exists... ***")
        d.screenshot("./pic/試算結果_台北大安_error.png")
        allure.attach.file("./pic/試算結果_台北大安_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北大安-2")
@allure.description("最高成數")
def test_daan_percent():
    cur_daan_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_daan_percent == daan_percent
        logging.info(f"*** PASS!!! 成數-台北大安'{cur_daan_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_台北大安.png")
        allure.attach.file("./pic/成數_台北大安.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北大安'{cur_daan_percent}' 不符合預期'{daan_percent}'... ***")
        d.screenshot("./pic/成數_台北大安_error.png")
        allure.attach.file("./pic/成數_台北大安_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北大安-3")
@allure.description("總金額")
def test_daan_total():
    cur_daan_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_daan_total == daan_total
        logging.info(f"*** PASS!!! 總金額-台北大安'{cur_daan_total}' 符合預期'{daan_total}' ***")
        d.screenshot("./pic/總金額_台北大安.png")
        allure.attach.file("./pic/總金額_台北大安.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-台北大安'{cur_daan_total}' 不符合預期'{daan_total}'... ***")
        d.screenshot("./pic/總金額_台北大安_error.png")
        allure.attach.file("./pic/總金額_台北大安_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北大安-4")
@allure.description("自備款金額及房貸金額")
def test_daan_loan():
    cu_daan_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cu_daan_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cu_daan_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_daan_total = int(cu_daan_total[:-1].replace(",", ""))
    new_daan_downpay = int(cu_daan_downpay[:-1].replace(",", ""))
    new_daan_homeloan = int(cu_daan_homeloan[:-1].replace(",", ""))
    try:
        assert new_daan_total == new_daan_downpay + new_daan_homeloan
        logging.info(f"*** PASS!!! 台北大安 總金額-自付-貸款'{new_daan_total} = {new_daan_downpay} + {new_daan_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北大安 總金額-自付-貸款'{new_daan_total} = {new_daan_downpay} + {new_daan_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北大安-5")
@allure.description("更改較高月還款60000，其餘條件不變，查看成數")
def test_daan_percent_hipay():
    d.swipe_ext("down", scale=1.3)
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').click()
        d.clear_text()
        time.sleep(1)
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "60000")
        #d.swipe_ext("up", scale=0.2)
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    cur_daan_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_daan_percent == daan_percent
        logging.info(f"*** PASS!!! 成數-台北大安(較高月還款)'{cur_daan_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北大安_較高月還款.png")
        allure.attach.file("./pic/成數_台北大安_較高月還款.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北大安(較高月還款)'{cur_daan_percent}' 成數有變，不符合預期'{daan_percent}'... ***")
        d.screenshot("./pic/成數_台北大安_較高月還款_error.png")
        allure.attach.file("./pic/成數_台北大安_較高月還款_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北大安-6")
@allure.description("更改較高月還款60000，其餘條件不變，查看金額")
def test_daan_loan_hipay():
    cur_daan_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_daan_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_daan_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_daan_total = int(cur_daan_total[:-1].replace(",", ""))
    new_daan_downpay = int(cur_daan_downpay[:-1].replace(",", ""))
    new_daan_homeloan = int(cur_daan_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_daan_total = int(daan_total.replace(",", ""))
    int_daan_downpay = int(daan_downpay.replace(",", ""))
    int_daan_homeloan = int(daan_homeloan.replace(",", ""))

    try:
        assert (new_daan_total > int_daan_total) and (new_daan_downpay > int_daan_downpay) and (new_daan_homeloan > int_daan_homeloan)
        logging.info(f"*** PASS!!! 台北大安(較高月還款) 總金額-自付-貸款'{new_daan_total}, {new_daan_downpay}, {new_daan_homeloan}' 皆變高，符合預期(vs {int_daan_total}, {int_daan_downpay}, {int_daan_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安_較高月還款.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安_較高月還款.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北大安(較高月還款) 總金額-自付-貸款'{new_daan_total} = {new_daan_downpay} + {new_daan_homeloan}' 沒變高，不符合預期(vs {int_daan_total}, {int_daan_downpay}, {int_daan_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安_較高月還款_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安_較高月還款_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北大安-7")
@allure.description("更改較低月還款40000，其餘條件不變，查看成數")
def test_daan_percent_lowpay():
    d.swipe_ext("down", scale=1.3)
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').click()
        d.clear_text()
        time.sleep(1)
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "40000")
        #d.swipe_ext("up", scale=0.2)
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    cur_daan_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_daan_percent == daan_percent
        logging.info(f"*** PASS!!! 成數-台北大安(較低月還款)'{cur_daan_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北大安_較低月還款.png")
        allure.attach.file("./pic/成數_台北大安_較低月還款.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北大安(較低月還款)'{cur_daan_percent}' 成數有變，不符合預期'{daan_percent}'... ***")
        d.screenshot("./pic/成數_台北大安_較低月還款_error.png")
        allure.attach.file("./pic/成數_台北大安_較低月還款_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


# 台北大安-不同月還款
@allure.feature("Test 不同縣市/區域-台北大安-8")
@allure.description("更改較高月還款40000，其餘條件不變，查看金額")
def test_daan_loan_lowpay():
    cur_daan_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_daan_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_daan_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_daan_total = int(cur_daan_total[:-1].replace(",", ""))
    new_daan_downpay = int(cur_daan_downpay[:-1].replace(",", ""))
    new_daan_homeloan = int(cur_daan_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_daan_total = int(daan_total.replace(",", ""))
    int_daan_downpay = int(daan_downpay.replace(",", ""))
    int_daan_homeloan = int(daan_homeloan.replace(",", ""))

    try:
        assert (new_daan_total < int_daan_total) and (new_daan_downpay < int_daan_downpay) and (new_daan_homeloan < int_daan_homeloan)
        logging.info(f"*** PASS!!! 台北大安(較低月還款) 總金額-自付-貸款'{new_daan_total}, {new_daan_downpay}, {new_daan_homeloan}' 皆變低，符合預期(vs {int_daan_total}, {int_daan_downpay}, {int_daan_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安_較低月還款.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安_較低月還款.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北大安(較低月還款) 總金額-自付-貸款'{new_daan_total}, {new_daan_downpay}, {new_daan_homeloan}' 沒變低，不符合預期(vs {int_daan_total}, {int_daan_downpay}, {int_daan_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北大安_較低月還款_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北大安_較低月還款_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e



# Reset button
@allure.feature("Test Reset Button")
@allure.description("重新試算 button")
def test_resetButton():
    op.refresh()
    time.sleep(2)
    op.choose_beitun()

    time.sleep(1)
    d.swipe_ext("down", scale=0.5)
    calcu_result = d(resourceId="spanHousePrice", packageName="com.android.chrome").exists(timeout=3.0)
    logging.info(f"Does 試算結果 exist: {calcu_result}")
    d.screenshot("./pic/試算結果_rest前.png")
    allure.attach.file("./pic/試算結果_rest前.png", attachment_type=allure.attachment_type.PNG)

    if d(resourceId="btnReset", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnReset", packageName="com.android.chrome").click()

    time.sleep(5)

    calcu_result = d(resourceId="spanHousePrice", packageName="com.android.chrome").exists(timeout=5.0)
    logging.info(f"Does 試算結果 exist: {calcu_result}")

    try:
        assert not calcu_result
        logging.info(f"*** PASS!!! Does 試算結果 exist: '{calcu_result}' 試算結果不存在，符合預期***")
        d.screenshot("./pic/試算結果_rest後.png")
        allure.attach.file("./pic/試算結果_rest後.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! Does 試算結果 exist: '{calcu_result}' 試算結果存在，不符合預期... ***")
        d.screenshot("./pic/試算結果_rest後_error.png")
        allure.attach.file("./pic/試算結果_rest後_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e

    d.swipe_ext("down", scale=0.65)



# error handling
@allure.feature("Check warning message for no region selected")
@allure.description("區域不輸入")
def test_noRegion():
    d.swipe_ext("down", scale=1.0)
    d.swipe_ext("down", scale=1.5)  # refresh page
    time.sleep(1)

    op.choose_noRegion()
    time.sleep(1)
    d.swipe_ext("up", scale=0.3)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(10)  # something it needs to wait very long or it will say the element not exist(but it does show up)

    try:
        assert d(text="請選擇行政區").exists(timeout=10.0)
        logging.info(f"*** PASS!!! 區域欄位皆有警語，符合預期***")
        d.screenshot("./pic/警語_區域Empty.png")
        allure.attach.file("./pic/警語_區域Empty.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 區域欄位並未皆有警語，不符合預期... ***")
        d.screenshot("./pic/警語_區域Empty_error.png")
        allure.attach.file("./pic/警語_區域Empty_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for no year input")
@allure.description("貸款年限不輸入")
def test_noYear():
    op.refresh()
    time.sleep(1)

    op.choose_noYear()
    time.sleep(1)
    #d.swipe_ext("up", scale=0.1)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(15)  # not sure why it needs to wait this long or it will say "請輸入貸款年限" not exist(although it does show up)
    #time.sleep(5)
    #year_msg = d(text="請輸入貸款年限").get_text()  # use this can short the sleep time above

    try:
        assert d(text="請輸入貸款年限").exists(timeout=7.0)
        # assert year_msg == "請輸入貸款年限"
        logging.info(f"*** PASS!!! 貸款年限欄位有警語，符合預期***")
        d.screenshot("./pic/警語_noYear.png")
        allure.attach.file("./pic/警語_noYear.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款年限欄位未有警語，不符合預期... ***")
        d.screenshot("./pic/警語_noYear_error.png")
        allure.attach.file("./pic/警語_noYear_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting negative year")
@allure.description("貸款年限輸入負數")
def test_negYear():
    op.refresh()
    time.sleep(1)

    op.choose_noYear()
    time.sleep(1)
    #d.swipe_ext("up", scale=0.1)

    if d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'):
        d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
        "-25")
    else:
        d.xpath('//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text("-25")


    d.swipe_ext("up", scale=0.1)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1)

    # currently got issue on this case
    # try:
    #    assert not d(text="試算結果").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 負數不被接受，符合預期***")
    #    d.screenshot("./pic/警語_negYear.png")
    #    allure.attach.file("./pic/警語_negYear.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    # except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 負數被接受，不符合預期... ***")
    #    d.screenshot("./pic/警語_negYear_error.png")
    #    allure.attach.file("./pic/警語_negYear_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e

    d.swipe_ext("down", scale=1.2)
    time.sleep(1.5)

    try:
        assert d(text="請輸入貸款年限").exists(timeout=7.0)
        logging.info(f"*** PASS!!! 貸款年限欄位有警語(負數不被接受)，符合預期***")
        d.screenshot("./pic/警語_negYear.png")
        allure.attach.file("./pic/警語_negYear.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款年限欄位未有警語(負數被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_negYear_error.png")
        allure.attach.file("./pic/警語_negYear_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting 0 year")
@allure.description("貸款年限輸入0")
def test_zeroYear():
    op.refresh()
    time.sleep(1)

    op.choose_noYear()
    time.sleep(1)
    #d.swipe_ext("up", scale=0.1)

    if d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'):
        d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
        "0")
    else:
        d.xpath('//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text("0")


    time.sleep(1)
    d.swipe_ext("up", scale=0.1)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1)

    # currently got issue on this case
    # try:
    #    assert not d(text="試算結果").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 0不被接受，符合預期***")
    #    d.screenshot("./pic/警語_zeroYear.png")
    #    allure.attach.file("./pic/警語_zeroYear.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    # except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 0被接受，不符合預期... ***")
    #    d.screenshot("./pic/警語_zeroYear_error.png")
    #    allure.attach.file("./pic/警語_zeroYear_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e

    d.swipe_ext("down", scale=1.2)
    time.sleep(5)

    try:
        assert d(text="請輸入貸款年限").exists(timeout=7.0)
        logging.info(f"*** PASS!!! 貸款年限欄位有警語(0不被接受)，符合預期***")
        d.screenshot("./pic/警語_zeroYear.png")
        allure.attach.file("./pic/警語_zeroYear.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款年限欄位未有警語(0被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_zeroYear_error.png")
        allure.attach.file("./pic/警語_zeroYear_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


# error handling for 貸款年限
@allure.feature("Check warning message for inputting non-digit year")
@allure.description("貸款年限輸入非數字")
def test_notDigitYear():
    op.refresh()
    time.sleep(1)

    op.choose_noYear()
    time.sleep(1)
    #d.swipe_ext("up", scale=0.1)

    if d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'):
        d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
        "ten")
    else:
        d.xpath('//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text("ten")

    time.sleep(1)
    d.swipe_ext("up", scale=0.1)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(5)

    try:
        assert d(text="請輸入貸款年限").exists(timeout=7.0)
        logging.info(f"*** PASS!!! 貸款年限欄位有警語(非數字不被接受)，符合預期***")
        d.screenshot("./pic/警語_notDigitYear.png")
        allure.attach.file("./pic/警語_notDigitYear.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款年限欄位未有警語(非數字被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_notDigitYear_error.png")
        allure.attach.file("./pic/警語_notDigitYear_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting symbol year")
@allure.description("貸款年限輸入符號")
def test_symbolYear():
    op.refresh()
    time.sleep(1)

    op.choose_noYear()
    time.sleep(1)
    #d.swipe_ext("up", scale=0.1)

    if d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'):
        d.xpath(
        '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
        "/!_@\#")
    else:
        d.xpath('//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text("/!_@\#")

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    time.sleep(5)

    try:
        assert d(text="請輸入貸款年限").exists(timeout=7.0)
        logging.info(f"*** PASS!!! 貸款年限欄位有警語(符號不被接受)，符合預期***")
        d.screenshot("./pic/警語_symbolYear.png")
        allure.attach.file("./pic/警語_symbolYear.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款年限欄位未有警語(符號被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_symbolYear_error.png")
        allure.attach.file("./pic/警語_symbolYear_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


# teardown
@pytest.fixture(scope="module", autouse=True)
def close_chrome():
    yield
    if d(resourceId="com.android.chrome:id/tab_switcher_button", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="com.android.chrome:id/tab_switcher_button", packageName="com.android.chrome").click()

    if d(resourceId="com.android.chrome:id/action_button", packageName="com.android.chrome").exists(timeout=3.0):
        logging.info(f"{d(resourceId="com.android.chrome:id/action_button", packageName="com.android.chrome").exists(timeout=3.0)}")
        d(resourceId="com.android.chrome:id/action_button", packageName="com.android.chrome").click()
    logging.info("Tab closed!")
    time.sleep(2)
    d(resourceId="com.android.systemui:id/recent_apps", packageName="com.android.systemui").click()
    d(resourceId="com.vivo.recents:id/snapshot", packageName="com.android.launcher3").swipe("up", steps=10)
    #d.app_stop("com.android.chrome")
    logging.info("close Chrome!")
    logging.info("!!!Test Complete!!!")
    allure.attach.file("./pytest_log.txt", attachment_type=allure.attachment_type.TEXT)
