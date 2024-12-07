import pytest
from appium import webdriver
from appium.options.common.base import AppiumOptions

@pytest.fixture(scope="module")
def driver():
	options = AppiumOptions()
	options.load_capabilities({
		"platformName": "Android",
		"appium:platformVersion": "<android_version>",
		"appium:deviceName": "<device_name>",
		"appium:automationName": "UIAutomator2",
		"appium:ensureWebviewsHavePages": True,
		"appium:nativeWebScreenshot": True,
		"appium:newCommandTimeout": 3600,
		"appium:connectHardwareKeyboard": True,
		"appium:noReset": True,
		"appium:appPackage": "br.com.paguemenos.anjodaguarda",
		"appium:appActivity": ".MainActivity",
		"appium:autoGrantPermissions": True,
	})

	driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

	yield driver
	try:
		driver.terminate_app("br.com.paguemenos.anjodaguarda")
	finally:
		driver.quit()
