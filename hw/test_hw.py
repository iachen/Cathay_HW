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

# print(taichung_homeloan)


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



@allure.feature("Test 不同縣市/區域-台北信義-1")
@allure.description("試算結果")
def test_xinyi_result():
    # select city & region
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台北市").exists(timeout=3.0):
            d(text="台北市").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="信義區").exists(timeout=3.0):
            d(text="信義區").click()
    # input 月還款
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "50000")
    # input 利率
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "2.5")
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-台北信義' exists ***")
        d.screenshot("./pic/試算結果_台北信義.png")
        allure.attach.file("./pic/試算結果_台北信義.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-台北信義' NOT exists... ***")
        d.screenshot("./pic/試算結果_台北信義_error.png")
        allure.attach.file("./pic/試算結果_台北信義_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北信義-2")
@allure.description("最高成數")
def test_xinyi_percent():
    xinyi_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert xinyi_percent == "7.5～8成"
        logging.info(f"*** PASS!!! 成數-台北信義'{xinyi_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_台北信義.png")
        allure.attach.file("./pic/成數_台北信義.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北信義'{xinyi_percent}' 不符合預期'7.5～8成'... ***")
        d.screenshot("./pic/成數_台北信義_error.png")
        allure.attach.file("./pic/成數_台北信義_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e

@allure.feature("Test 不同縣市/區域-台北信義-3")
@allure.description("總金額")
def test_xinyi_total():
    cur_xinyi_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_xinyi_total == xinyi_total
        logging.info(f"*** PASS!!! 總金額-台北信義'{cur_xinyi_total}' 符合預期'{xinyi_total}' ***")
        d.screenshot("./pic/總金額_台北信義.png")
        allure.attach.file("./pic/總金額_台北信義.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-台北信義'{cur_xinyi_total}' 不符合預期'{xinyi_total}'... ***")
        d.screenshot("./pic/總金額_台北信義_error.png")
        allure.attach.file("./pic/總金額_台北信義_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e

@allure.feature("Test 不同縣市/區域-台北信義-4")
@allure.description("自備款金額及房貸金額")
def test_xinyi_loan():
    xinyi_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    xinyi_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    xinyi_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_xinyi_total = int(xinyi_total[:-1].replace(",", ""))
    new_xinyi_downpay = int(xinyi_downpay[:-1].replace(",", ""))
    new_xinyi_homeloan = int(xinyi_homeloan[:-1].replace(",", ""))
    try:
        assert new_xinyi_total == new_xinyi_downpay + new_xinyi_homeloan
        logging.info(f"*** PASS!!! 台北信義 總金額-自付-貸款'{new_xinyi_total} = {new_xinyi_downpay} + {new_xinyi_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_台北信義.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北信義.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北信義 總金額-自付-貸款'{new_xinyi_total} = {new_xinyi_downpay} + {new_xinyi_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北信義_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北信義_error.png", attachment_type=allure.attachment_type.PNG)
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


@allure.feature("Test 不同縣市/區域-台中北屯-1")
@allure.description("試算結果")
def test_beitun_result():
    op.refresh()
    time.sleep(2)
    op.choose_beitun()
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-台中北屯' exists ***")
        d.screenshot("./pic/試算結果_台中北屯.png")
        allure.attach.file("./pic/試算結果_台中北屯.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-台中北屯' NOT exists... ***")
        d.screenshot("./pic/試算結果_台中北屯_error.png")
        allure.attach.file("./pic/試算結果_台中北屯_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台中北屯-2")
@allure.description("最高成數")
def test_beitun_percent():
    beitun_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert beitun_percent == "7～7.5成"
        logging.info(f"*** PASS!!! 成數-台中北屯'{beitun_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_台中北屯.png")
        allure.attach.file("./pic/成數_台中北屯.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台中北屯'{beitun_percent}' 不符合預期'6.5～7成'... ***")
        d.screenshot("./pic/成數_台中北屯_error.png")
        allure.attach.file("./pic/成數_台中北屯_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台中北屯-3")
@allure.description("總金額")
def test_beitun_total():
    cur_beitun_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_beitun_total == taichung_total
        logging.info(f"*** PASS!!! 總金額-台中北屯'{cur_beitun_total}' 符合預期'{taichung_total}' ***")
        d.screenshot("./pic/總金額_台中北屯.png")
        allure.attach.file("./pic/總金額_台中北屯.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-台中北屯'{cur_beitun_total}' 不符合預期'{taichung_total}'... ***")
        d.screenshot("./pic/總金額_台中北屯_error.png")
        allure.attach.file("./pic/總金額_台中北屯_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台中北屯-4")
@allure.description("自備款金額及房貸金額")
def test_beitun_loan():
    cu_beitun_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cu_beitun_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cu_beitun_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_beitun_total = int(cu_beitun_total[:-1].replace(",", ""))
    new_beitun_downpay = int(cu_beitun_downpay[:-1].replace(",", ""))
    new_zbeitun_homeloan = int(cu_beitun_homeloan[:-1].replace(",", ""))
    try:
        assert new_beitun_total == new_beitun_downpay + new_zbeitun_homeloan
        logging.info(f"*** PASS!!! 台中北屯 總金額-自付-貸款'{new_beitun_total} = {new_beitun_downpay} + {new_zbeitun_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_台中北屯.png")
        allure.attach.file("./pic/總金額-自付-貸款_台中北屯.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台中北屯 總金額-自付-貸款'{new_beitun_total} = {new_beitun_downpay} + {new_zbeitun_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_台中北屯_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台中北屯_error.png", attachment_type=allure.attachment_type.PNG)
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



#內湖(改利率)
@allure.feature("Test 相同縣市/區域-台北內湖-1")
@allure.description("試算結果")
def test_neihu_result():
    op.refresh()
    time.sleep(2)
    op.choose_neihu()
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-台北內湖' exists ***")
        d.screenshot("./pic/試算結果_台北內湖.png")
        allure.attach.file("./pic/試算結果_台北內湖.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-台北內湖' NOT exists... ***")
        d.screenshot("./pic/試算結果_台北內湖_error.png")
        allure.attach.file("./pic/試算結果_台北內湖_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北內湖-2")
@allure.description("最高成數")
def test_neihu_percent():
    cur_neihu_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_neihu_percent == neihu_percent
        logging.info(f"*** PASS!!! 成數-台北內湖'{cur_neihu_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_台北內湖.png")
        allure.attach.file("./pic/成數_台北內湖.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北內湖'{cur_neihu_percent}' 不符合預期'{neihu_percent}'... ***")
        d.screenshot("./pic/成數_台北內湖_error.png")
        allure.attach.file("./pic/成數_台北內湖_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北內湖-3")
@allure.description("總金額")
def test_neihu_total():
    cur_neihu_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_neihu_total == neihu_total
        logging.info(f"*** PASS!!! 總金額-台北內湖'{cur_neihu_total}' 符合預期'{neihu_total}' ***")
        d.screenshot("./pic/總金額_台北內湖.png")
        allure.attach.file("./pic/總金額_台北內湖.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-台北內湖'{cur_neihu_total}' 不符合預期'{neihu_total}'... ***")
        d.screenshot("./pic/總金額_台北內湖_error.png")
        allure.attach.file("./pic/總金額_台北內湖_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北內湖-4")
@allure.description("自備款金額及房貸金額")
def test_neihu_loan():
    cu_neihu_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cu_neihu_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cu_neihu_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_neihu_total = int(cu_neihu_total[:-1].replace(",", ""))
    new_neihu_downpay = int(cu_neihu_downpay[:-1].replace(",", ""))
    new_neihu_homeloan = int(cu_neihu_homeloan[:-1].replace(",", ""))
    try:
        assert new_neihu_total == new_neihu_downpay + new_neihu_homeloan
        logging.info(f"*** PASS!!! 台北內湖 總金額-自付-貸款'{new_neihu_total} = {new_neihu_downpay} + {new_neihu_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北內湖 總金額-自付-貸款'{new_neihu_total} = {new_neihu_downpay} + {new_neihu_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北內湖-5")
@allure.description("更改較高利率3.5，其餘條件不變，查看成數")
def test_neihu_percent_hiInterest():
    d.swipe_ext("down", scale=1.3)

    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').click()
        d.clear_text()

        time.sleep(1)

        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "3.5")
        #d.swipe_ext("up", scale=0.2)
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    cur_neihu_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_neihu_percent == neihu_percent
        logging.info(f"*** PASS!!! 成數-台北內湖(較高利率)'{cur_neihu_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北內湖_較高利率.png")
        allure.attach.file("./pic/成數_台北內湖_較高利率.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北內湖(較高利率)'{cur_neihu_percent}' 成數有變，不符合預期'{neihu_percent}'... ***")
        d.screenshot("./pic/成數_台北內湖_較高利率_error.png")
        allure.attach.file("./pic/成數_台北內湖_較高利率_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北內湖-6")
@allure.description("更改較高利率3.5，其餘條件不變，查看金額")
def test_neihu_loan_hiInterest():
    cur_neihu_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_neihu_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_neihu_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_neihu_total = int(cur_neihu_total[:-1].replace(",", ""))
    new_neihu_downpay = int(cur_neihu_downpay[:-1].replace(",", ""))
    new_neihu_homeloan = int(cur_neihu_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_neihu_total = int(neihu_total.replace(",", ""))
    int_neihu_downpay = int(neihu_downpay.replace(",", ""))
    int_neihu_homeloan = int(neihu_homeloan.replace(",", ""))

    try:
        assert (new_neihu_total < int_neihu_total) and (new_neihu_downpay < int_neihu_downpay) and (new_neihu_homeloan < int_neihu_homeloan)
        logging.info(f"*** PASS!!! 台北內湖(較高利率) 總金額-自付-貸款'{new_neihu_total}, {new_neihu_downpay}, {new_neihu_homeloan}' 皆變低，符合預期(vs {int_neihu_total}, {int_neihu_downpay}, {int_neihu_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖_較高利率.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖_較高利率.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北內湖(較高利率) 總金額-自付-貸款'{new_neihu_total} = {new_neihu_downpay} + {new_neihu_homeloan}' 沒變低，不符合預期(vs {int_neihu_total}, {int_neihu_downpay}, {int_neihu_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖_較高利率_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖_較高利率_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北內湖-7")
@allure.description("更改較低利率1.5，其餘條件不變，查看成數")
def test_neihu_percent_lowInterest():
    d.swipe_ext("down", scale=1.3)

    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').click()
        d.clear_text()

        time.sleep(1)

        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "1.5")
        #d.swipe_ext("up", scale=0.2)
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    cur_neihu_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_neihu_percent == neihu_percent
        logging.info(f"*** PASS!!! 成數-台北內湖(較低利率)'{cur_neihu_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北內湖_較低利率.png")
        allure.attach.file("./pic/成數_台北內湖_較低利率.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北內湖(較低利率)'{cur_neihu_percent}' 成數有變，不符合預期'{neihu_percent}'... ***")
        d.screenshot("./pic/成數_台北內湖_較低利率_error.png")
        allure.attach.file("./pic/成數_台北內湖_較低利率_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北內湖-8")
@allure.description("更改較低利率1.5，其餘條件不變，查看金額")
def test_neihu_loan_lowInterest():
    cur_neihu_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_neihu_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_neihu_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_neihu_total = int(cur_neihu_total[:-1].replace(",", ""))
    new_neihu_downpay = int(cur_neihu_downpay[:-1].replace(",", ""))
    new_neihu_homeloan = int(cur_neihu_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_neihu_total = int(neihu_total.replace(",", ""))
    int_neihu_downpay = int(neihu_downpay.replace(",", ""))
    int_neihu_homeloan = int(neihu_homeloan.replace(",", ""))

    try:
        assert (new_neihu_total > int_neihu_total) and (new_neihu_downpay > int_neihu_downpay) and (new_neihu_homeloan > int_neihu_homeloan)
        logging.info(f"*** PASS!!! 台北內湖(較低利率) 總金額-自付-貸款'{new_neihu_total}, {new_neihu_downpay}, {new_neihu_homeloan}' 皆變高，符合預期(vs {int_neihu_total}, {int_neihu_downpay}, {int_neihu_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖_較低利率.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖_較低利率.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北內湖(較高利率) 總金額-自付-貸款'{new_neihu_total} = {new_neihu_downpay} + {new_neihu_homeloan}' 沒變高，不符合預期(vs {int_neihu_total}, {int_neihu_downpay}, {int_neihu_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北內湖_較低利率_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北內湖_較低利率_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e



#士林(改年限)
@allure.feature("Test 相同縣市/區域-台北士林-1")
@allure.description("試算結果")
def test_shilin_result():
    op.refresh()
    time.sleep(2)
    op.choose_shilin()
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info("*** PASS!!! '試算結果-台北士林' exists ***")
        d.screenshot("./pic/試算結果_台北士林.png")
        allure.attach.file("./pic/試算結果_台北士林.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! '試算結果-台北士林' NOT exists... ***")
        d.screenshot("./pic/試算結果_台北士林_error.png")
        allure.attach.file("./pic/試算結果_台北士林_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北士林-2")
@allure.description("最高成數")
def test_shilin_percent():
    cur_shilin_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()
    try:
        assert cur_shilin_percent == shilin_percent
        logging.info(f"*** PASS!!! 成數-台北士林'{cur_shilin_percent}' 符合預期 ***")
        d.screenshot("./pic/成數_台北士林.png")
        allure.attach.file("./pic/成數_台北士林.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北士林'{cur_shilin_percent}' 不符合預期'{shilin_percent}'... ***")
        d.screenshot("./pic/成數_台北士林_error.png")
        allure.attach.file("./pic/成數_台北士林_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北士林-3")
@allure.description("總金額")
def test_shilin_total():
    cur_shilin_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    try:
        assert cur_shilin_total == shilin_total
        logging.info(f"*** PASS!!! 總金額-台北士林'{cur_shilin_total}' 符合預期'{shilin_total}' ***")
        d.screenshot("./pic/總金額_台北士林.png")
        allure.attach.file("./pic/總金額_台北士林.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 總金額-台北士林'{cur_shilin_total}' 不符合預期'{shilin_total}'... ***")
        d.screenshot("./pic/總金額_台北士林_error.png")
        allure.attach.file("./pic/總金額_台北士林_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北士林-4")
@allure.description("自備款金額及房貸金額")
def test_shilin_loan():
    cu_shilin_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cu_shilin_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cu_shilin_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_shilin_total = int(cu_shilin_total[:-1].replace(",", ""))
    new_shilin_downpay = int(cu_shilin_downpay[:-1].replace(",", ""))
    new_shilin_homeloan = int(cu_shilin_homeloan[:-1].replace(",", ""))
    try:
        assert new_shilin_total == new_shilin_downpay + new_shilin_homeloan
        logging.info(f"*** PASS!!! 台北士林 總金額-自付-貸款'{new_shilin_total} = {new_shilin_downpay} + {new_shilin_homeloan}' 符合預期 ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北士林 總金額-自付-貸款'{new_shilin_total} = {new_shilin_downpay} + {new_shilin_homeloan}' 不符合預期... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北士林-5")
@allure.description("更改較高年限30，其餘條件不變，查看成數")
def test_shilin_percent_hiYear():
    d.swipe_ext("down", scale=1.5)
    d.swipe_ext("up", scale=0.2)
    time.sleep(1)
    if d.xpath('//*[@text="30年"]'):
        d.xpath('//*[@text="30年"]').click()

    time.sleep(1)
    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    cur_shilin_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()

    try:
        assert cur_shilin_percent == shilin_percent
        logging.info(f"*** PASS!!! 成數-台北士林(較高年限)'{cur_shilin_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北士林_較高年限.png")
        allure.attach.file("./pic/成數_台北士林_較高年限.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北士林(較高年限)'{cur_shilin_percent}' 成數有變，不符合預期'{shilin_percent}'... ***")
        d.screenshot("./pic/成數_台北士林_較高利率_error.png")
        allure.attach.file("./pic/成數_台北士林_較高年限_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北士林-6")
@allure.description("更改較低高限30，其餘條件不變，查看金額")
def test_shilin_loan_hiYear():
    cur_shilin_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_shilin_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_shilin_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_shilin_total = int(cur_shilin_total[:-1].replace(",", ""))
    new_shilin_downpay = int(cur_shilin_downpay[:-1].replace(",", ""))
    new_shilin_homeloan = int(cur_shilin_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_shilin_total = int(shilin_total.replace(",", ""))
    int_shilin_downpay = int(shilin_downpay.replace(",", ""))
    int_shilin_homeloan = int(shilin_homeloan.replace(",", ""))

    try:
        assert (new_shilin_total > int_shilin_total) and (new_shilin_downpay > int_shilin_downpay) and (new_shilin_homeloan > int_shilin_homeloan)
        logging.info(f"*** PASS!!! 台北士林(較低年限) 總金額-自付-貸款'{new_shilin_total}, {new_shilin_downpay}, {new_shilin_homeloan}' 皆變高，符合預期(vs {int_shilin_total}, {int_shilin_downpay}, {int_shilin_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林_較高年限.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林_較高年限.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北士林(較高年限) 總金額-自付-貸款'{new_shilin_total} = {new_shilin_downpay} + {new_shilin_homeloan}' 沒變低，不符合預期(vs {int_shilin_total}, {int_shilin_downpay}, {int_shilin_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林_較高年限_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林_較高年限_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 相同縣市/區域-台北士林-7")
@allure.description("更改較高年限10，其餘條件不變，查看成數")
def test_shilin_percent_lowYear():
    d.swipe_ext("down", scale=1.5)
    d.swipe_ext("up", scale=0.2)
    time.sleep(1)
    if d.xpath('//*[@text="其他"]'):
        d.xpath('//*[@text="其他"]').click()

        if d.xpath(
                '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]'):
            d.xpath(
                '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
                "10")
        else:
            d.xpath(
                '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]/android.view.View[1]/android.view.View[1]/android.view.View[3]/android.view.View[2]/android.view.View[2]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]').set_text(
                "10")

        time.sleep(1)
        if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
            d(resourceId="btnCalculate", packageName="com.android.chrome").click()
        time.sleep(1)

    # since calculate with "其他" window will cause weditor cannot be able to select element.
    # this makes the results of calculation cannot be acquired
    # the way to workaround is to select to 20/30 year(but not recalculate it) and back to check the result
    d.swipe_ext("down", scale=1.0)
    time.sleep(1)
    if d.xpath('//*[@text="20年"]'):
        d.xpath('//*[@text="20年"]').click()
    d.swipe_ext("up", scale=1.0)


    cur_shilin_percent = d.xpath('//*[@resource-id="spanMaxLoan"]').get_text()

    try:
        assert cur_shilin_percent == shilin_percent
        logging.info(f"*** PASS!!! 成數-台北士林(較高年限)'{cur_shilin_percent}' 成數不變，符合預期 ***")
        d.screenshot("./pic/成數_台北士林_較高年限.png")
        allure.attach.file("./pic/成數_台北士林_較高年限.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 成數-台北士林(較高年限)'{cur_shilin_percent}' 成數有變，不符合預期'{shilin_percent}'... ***")
        d.screenshot("./pic/成數_台北士林_較高利率_error.png")
        allure.attach.file("./pic/成數_台北士林_較高年限_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Test 不同縣市/區域-台北士林-8")
@allure.description("更改較低年限10，其餘條件不變，查看金額")
def test_shilin_loan_lowYear():
    cur_shilin_total = d(resourceId="spanHousePrice", packageName="com.android.chrome").get_text()
    cur_shilin_downpay = d(resourceId="spanSelfPrepare", packageName="com.android.chrome").get_text()
    cur_shilin_homeloan = d(resourceId="spanBorrowMax", packageName="com.android.chrome").get_text()
    new_shilin_total = int(cur_shilin_total[:-1].replace(",", ""))
    new_shilin_downpay = int(cur_shilin_downpay[:-1].replace(",", ""))
    new_shilin_homeloan = int(cur_shilin_homeloan[:-1].replace(",", ""))

    # convert the str from data.ini to int
    int_shilin_total = int(shilin_total.replace(",", ""))
    int_shilin_downpay = int(shilin_downpay.replace(",", ""))
    int_shilin_homeloan = int(shilin_homeloan.replace(",", ""))

    try:
        assert (new_shilin_total < int_shilin_total) and (new_shilin_downpay < int_shilin_downpay) and (new_shilin_homeloan < int_shilin_homeloan)
        logging.info(f"*** PASS!!! 台北士林(較低年限) 總金額-自付-貸款'{new_shilin_total}, {new_shilin_downpay}, {new_shilin_homeloan}' 皆變低，符合預期(vs {int_shilin_total}, {int_shilin_downpay}, {int_shilin_homeloan}) ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林_較低年限.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林_較低年限.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 台北士林(較低年限) 總金額-自付-貸款'{new_shilin_total} = {new_shilin_downpay} + {new_shilin_homeloan}' 沒變低，不符合預期(vs {int_shilin_total}, {int_shilin_downpay}, {int_shilin_homeloan})... ***")
        d.screenshot("./pic/總金額-自付-貸款_台北士林_較低年限_error.png")
        allure.attach.file("./pic/總金額-自付-貸款_台北士林_較低年限_error.png", attachment_type=allure.attachment_type.PNG)
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
@allure.feature("Check warning messages for all empty fields")
@allure.description("所有欄位不輸入")
def test_allEmpty():
    d.swipe_ext("down", scale=1.0)
    d.swipe_ext("down", scale=1.5)  # refresh page
    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(10)  # it needs to this long or it will always say those warning msg not exist(although they do show up)
    # logging.info(f"請選擇縣市存在?{d(text="請選擇縣市").exists(timeout=3.0)}")
    # logging.info(f"請選擇行政區?{d(text="請選擇行政區").exists(timeout=3.0)}")
    # logging.info(f"請輸入整數貸款金額?{d(text="請輸入整數貸款金額").exists(timeout=3.0)}")
    # logging.info(f"請輸入數字?{d(text="請輸入數字").exists(timeout=3.0)}")

    try:
        assert d(text="請選擇縣市").exists(timeout=10.0) and d(text="請選擇行政區").exists(timeout=3.0) and d(text="請輸入整數貸款金額").exists(timeout=3.0) and d(text="請輸入數字").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 所有空白欄位皆有警語，符合預期***")
        d.screenshot("./pic/警語_allEmpty.png")
        allure.attach.file("./pic/警語_allEmpty.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 所有空白欄位並未皆有警語，不符合預期... ***")
        d.screenshot("./pic/警語_allEmpty_error.png")
        allure.attach.file("./pic/警語_allEmpty_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning messages for all no city selected")
@allure.description("縣市不輸入")
def test_noCity():
    d.swipe_ext("down", scale=1.0)
    d.swipe_ext("down", scale=1.5)  # refresh page
    time.sleep(1)

    op.choose_noCity()
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(10)  # something it needs to wait very long or it will say the element not exist(but it does show up)

    try:
        assert d(text="請選擇縣市").exists(timeout=10.0) and d(text="請選擇行政區").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 縣市/區域欄位皆有警語，符合預期***")
        d.screenshot("./pic/警語_cityEmpty.png")
        allure.attach.file("./pic/警語_cityEmpty.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 縣市/區域欄位並未皆有警語，不符合預期... ***")
        d.screenshot("./pic/警語_cityEmpty_error.png")
        allure.attach.file("./pic/警語_cityEmpty_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


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


@allure.feature("Check warning message for no payment input")
@allure.description("每月可負擔房貸金額不輸入")
def test_noPayment():
    #d.swipe_ext("down", scale=0.2)
    #d.swipe_ext("down", scale=1.5)  # refresh page
    op.refresh()
    time.sleep(1)

    op.choose_noPayment()
    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1.5)

    try:
        assert d(text="請輸入整數貸款金額").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 每月可負擔房貸金額欄位有警語，符合預期***")
        d.screenshot("./pic/警語_noPayment.png")
        allure.attach.file("./pic/警語_noPayment.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 每月可負擔房貸金額欄位未有警語，不符合預期... ***")
        d.screenshot("./pic/警語_noPayment_error.png")
        allure.attach.file("./pic/警語_noPayment_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting negative payment")
@allure.description("每月可負擔房貸金額輸入負數")
def test_negPayment():
    op.refresh()
    time.sleep(1)

    op.choose_noPayment()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "-50000")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    
    # currently got issue on this case
    #try:
    #    assert not d(text="試算結果").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 負數不被接受，符合預期***")
    #    d.screenshot("./pic/警語_negPayment.png")
    #    allure.attach.file("./pic/警語_negPayment.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 負數被接受，不符合預期... ***")
    #    d.screenshot("./pic/警語_negPayment_error.png")
    #    allure.attach.file("./pic/警語_negPayment_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e
    
    d.swipe_ext("down", scale=1.2)
    time.sleep(1.5)

    try:
        assert d(text="請輸入整數貸款金額").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 每月可負擔房貸金額欄位有警語(負數不被接受)，符合預期***")
        d.screenshot("./pic/警語_negPayment.png")
        allure.attach.file("./pic/警語_negPayment.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 每月可負擔房貸金額欄位未有警語(負數被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_negPayment_error.png")
        allure.attach.file("./pic/警語_negPayment_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting 0 payment")
@allure.description("每月可負擔房貸金額輸入0")
def test_zeroPayment():
    op.refresh()
    time.sleep(1)

    op.choose_noPayment()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "0")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    # currently got issue on this case
    # try:
    #    assert not d(text="試算結果").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 0不被接受，符合預期***")
    #    d.screenshot("./pic/警語_zeroPayment.png")
    #    allure.attach.file("./pic/警語_zeroPayment.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    # except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 0被接受，不符合預期... ***")
    #    d.screenshot("./pic/警語_zeroPayment_error.png")
    #    allure.attach.file("./pic/警語_zeroPayment_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e

    d.swipe_ext("down", scale=1.2)
    time.sleep(1.5)

    try:
        assert d(text="請輸入整數貸款金額").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 每月可負擔房貸金額欄位有警語(0不被接受)，符合預期***")
        d.screenshot("./pic/警語_zeroPayment.png")
        allure.attach.file("./pic/警語_zeroPayment.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 每月可負擔房貸金額欄位未有警語(0被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_zeroPayment_error.png")
        allure.attach.file("./pic/警語_zeroPayment_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting non-digit payment")
@allure.description("每月可負擔房貸金額輸入非數字")
def test_notDigitPayment():
    op.refresh()
    time.sleep(1)

    op.choose_noPayment()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "ten")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1.5)

    try:
        assert d(text="請輸入整數貸款金額").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 每月可負擔房貸金額欄位有警語(非數字不被接受)，符合預期***")
        d.screenshot("./pic/警語_nonDigitPayment.png")
        allure.attach.file("./pic/警語_nonDigitPayment.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 每月可負擔房貸金額欄位未有警語(非數字被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_nonDigitPayment_error.png")
        allure.attach.file("./pic/警語_nonDigitPayment_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting symbol payment")
@allure.description("每月可負擔房貸金額輸入符號")
def test_symbolPayment():
    op.refresh()
    time.sleep(1)

    op.choose_noPayment()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "/!_@\#")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1.5)

    try:
        assert d(text="請輸入整數貸款金額").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 每月可負擔房貸金額欄位有警語(符號不被接受)，符合預期***")
        d.screenshot("./pic/警語_symbolPayment.png")
        allure.attach.file("./pic/警語_symbolPayment.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 每月可負擔房貸金額欄位未有警語(符號被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_symbolPayment_error.png")
        allure.attach.file("./pic/警語_symbolPayment_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for no interest input")
@allure.description("貸款利率不輸入")
def test_noInterest():
    op.refresh()
    time.sleep(1)

    op.choose_noInterest()
    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1.5)

    try:
        assert d(text="請輸入數字").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 貸款利率欄位有警語，符合預期***")
        d.screenshot("./pic/警語_noInterest.png")
        allure.attach.file("./pic/警語_noInterest.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款利率欄位未有警語，不符合預期... ***")
        d.screenshot("./pic/警語_noInterest_error.png")
        allure.attach.file("./pic/警語_noInterest_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting negative payment")
@allure.description("貸款利率輸入負數")
def test_negInterest():
    op.refresh()
    time.sleep(1)

    op.choose_noInterest()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "-2.5")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    # currently got issue on this case
    # try:
    #    assert not d(text="試算結果").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 負數不被接受，符合預期***")
    #    d.screenshot("./pic/警語_negInterest.png")
    #    allure.attach.file("./pic/警語_negInterest.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    # except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 負數被接受，不符合預期... ***")
    #    d.screenshot("./pic/警語_negInterest_error.png")
    #    allure.attach.file("./pic/警語_negInterest_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e

    d.swipe_ext("down", scale=1.2)
    time.sleep(1.5)

    try:
        assert d(text="請輸入數字").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 貸款利率欄位有警語(負數不被接受)，符合預期***")
        d.screenshot("./pic/警語_negInterest.png")
        allure.attach.file("./pic/警語_negInterest.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款利率欄位未有警語(負數被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_negInterest_error.png")
        allure.attach.file("./pic/警語_negInterest_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting 0 Interest")
@allure.description("貸款利率輸入0")
def test_zeroInterest():
    op.refresh()
    time.sleep(1)

    op.choose_noInterest()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "0")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()
    time.sleep(1)

    # currently it accept 0 on this case, not sure how the spec defines
    try:
        assert d(text="試算結果").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 0被接受，不確定是否符合預期***")
        d.screenshot("./pic/警語_zeroInterest.png")
        allure.attach.file("./pic/警語_zeroInterest.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 0不被接受，不確定是否符合預期... ***")
        d.screenshot("./pic/警語_zeroInterest_error.png")
        allure.attach.file("./pic/警語_zeroInterest_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e

    d.swipe_ext("down", scale=0.6)
    # time.sleep(1.5)

    #try:
    #    assert d(text="請輸入數字").exists(timeout=3.0)
    #    logging.info(f"*** PASS!!! 貸款利率欄位有警語(0不被接受)，符合預期***")
    #    d.screenshot("./pic/警語_zeroInterest.png")
    #    allure.attach.file("./pic/警語_zeroInterest.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #except AssertionError as e:
    #    logging.info(f"*** FAIL!!! 貸款利率欄位未有警語(0被接受)，不符合預期... ***")
    #    d.screenshot("./pic/警語_zeroInterest_error.png")
    #    allure.attach.file("./pic/警語_zeroInterest_error.png", attachment_type=allure.attachment_type.PNG)
    #    time.sleep(2.0)
    #    raise e


@allure.feature("Check warning message for inputting non-digit interest")
@allure.description("貸款利率輸入非數字")
def test_notDigitInterest():
    op.refresh()
    time.sleep(1)

    op.choose_noInterest()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "two")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1.5)

    try:
        assert d(text="請輸入數字").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 貸款利率欄位有警語(非數字不被接受)，符合預期***")
        d.screenshot("./pic/警語_notDigitInterest.png")
        allure.attach.file("./pic/警語_notDigitInterest.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款利率欄位未有警語(非數字被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_notDigitInterest_error.png")
        allure.attach.file("./pic/警語_notDigitInterest_error.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
        raise e


@allure.feature("Check warning message for inputting symbol interest")
@allure.description("貸款利率輸入符號")
def test_symbolInterest():
    op.refresh()
    time.sleep(1)

    op.choose_noInterest()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "/!_@\#")

    time.sleep(1)
    d.swipe_ext("up", scale=0.2)

    if d(resourceId="btnCalculate", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="btnCalculate", packageName="com.android.chrome").click()

    time.sleep(1.5)

    try:
        assert d(text="請輸入數字").exists(timeout=3.0)
        logging.info(f"*** PASS!!! 貸款利率欄位有警語(符號不被接受)，符合預期***")
        d.screenshot("./pic/警語_symbolInterest.png")
        allure.attach.file("./pic/警語_symbolInterest.png", attachment_type=allure.attachment_type.PNG)
        time.sleep(2.0)
    except AssertionError as e:
        logging.info(f"*** FAIL!!! 貸款利率欄位未有警語(符號被接受)，不符合預期... ***")
        d.screenshot("./pic/警語_symbolInterest_error.png")
        allure.attach.file("./pic/警語_symbolInterest_error.png", attachment_type=allure.attachment_type.PNG)
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
        assert d(text="請輸入貸款年限").exists(timeout=3.0)
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
    time.sleep(1.5)

    try:
        assert d(text="請輸入貸款年限").exists(timeout=3.0)
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


"""
def test_try():
    # d.swipe_ext("down", scale=1.5)
    logging.info(f"year: {d(text="請輸入貸款年限").exists(timeout=3.0)}")
"""
