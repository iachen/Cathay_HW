import uiautomator2 as u2
import time
import logging
import toml

d = u2.connect_usb()

configure = toml.load('data.ini')
daan_total = configure['taipeidata']['daan_total']
daan_downpay = configure['taipeidata']['daan_downpay']
daan_homeloan = configure['taipeidata']['daan_homeloan']
daan_percent = configure['taipeidata']['daan_percent']

# This file is to do operations for different settings(city, region, payment, profile, year, etc.)

def refresh():
    d.swipe_ext("down", scale=1.5)
    time.sleep(1)
    d.swipe_ext("down", scale=1.5)
    time.sleep(1)


def choose_zhubei():
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="新竹縣").exists(timeout=3.0):
            d(text="新竹縣").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="竹北市").exists(timeout=3.0):
            d(text="竹北市").click()
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


def choose_beitun():
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台中市").exists(timeout=3.0):
            d(text="台中市").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="北屯區").exists(timeout=3.0):
            d(text="北屯區").click()
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


def choose_daan():
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
        if d(text="大安區").exists(timeout=3.0):
            d(text="大安區").click()
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


def choose_neihu():
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
        if d(text="內湖區").exists(timeout=3.0):
            d(text="內湖區").click()
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


def choose_shilin():
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
        if d(text="士林區").exists(timeout=3.0):
            d(text="士林區").click()
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



def choose_noCity():
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


def choose_noRegion():
    # select city
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台中市").exists(timeout=3.0):
            d(text="台中市").click()

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

def choose_noPayment():
    # left payment
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台中市").exists(timeout=3.0):
            d(text="台中市").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="北屯區").exists(timeout=3.0):
            d(text="北屯區").click()

    # input 利率
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[4]/android.view.View[2]').set_text(
            "2.5")

    time.sleep(1)


def choose_noInterest():
    # left interest
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台中市").exists(timeout=3.0):
            d(text="台中市").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="北屯區").exists(timeout=3.0):
            d(text="北屯區").click()
    # input 月還款
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[2]').set_text(
            "50000")

    time.sleep(1)


def choose_noYear():
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="台中市").exists(timeout=3.0):
            d(text="台中市").click()
    if d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]'):
        d.xpath(
            '//*[@resource-id="mainform"]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[4]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]/android.widget.TextView[1]').click()
        if d(text="北屯區").exists(timeout=3.0):
            d(text="北屯區").click()
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

    d.swipe_ext("up", scale=0.25)
    time.sleep(1)
    if d.xpath('//*[@text="其他"]'):
        d.xpath('//*[@text="其他"]').click()

    time.sleep(1)





if __name__ == "__main__":
    #refresh()
    #choose_shilin()
    #print(f"{d(text="請輸入貸款年限").exists(timeout=3.0)}")
    if d(resourceId="com.android.chrome:id/action_button", packageName="com.android.chrome").exists(timeout=3.0):
        d(resourceId="com.android.chrome:id/action_button", packageName="com.android.chrome").click()
        print("Tab closed !")