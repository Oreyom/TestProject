from selenium import webdriver
from selenium.webdriver.support.select import Select
import numpy as np
sensitiveDetails = open("password.txt", "r")

driver = webdriver.Edge(r"C:\Users\F . O\Desktop\Selenium VS\drivers\msedgedriver.exe")
driver.implicitly_wait(10) 
driver.get("https://first-console-ardova-uat.fbn-devops-uat-asenv.appserviceenvironment.net/login.aspx")
driver.maximize_window()
driver.find_element_by_name("txtUsername").send_keys("TN060365")
driver.find_element_by_name("txtPassword").send_keys(sensitiveDetails.read())
driver.find_element_by_name("btnLogin").click()
driver.implicitly_wait(5)
driver.find_element_by_link_text("Make Payment").click()
driver.find_element_by_link_text("ARDOVA").click()
selCollection = Select(driver.find_element_by_xpath("//select[@name='ctl00$CPHContent$cboSrchProducts']"))
selCollection.select_by_visible_text("NEO FUEL")
driver.implicitly_wait(5)
selRegion = Select(driver.find_element_by_xpath("//select[@name='ctl00$CPHContent$cboSrchRegion']"))
selRegion.select_by_visible_text("Lagos-South")
driver.implicitly_wait(5)
selDealerCode = Select(driver.find_element_by_xpath("//select[@name='ctl00$CPHContent$cboSrchDealer']"))
selDealerCode.select_by_visible_text("870")
driver.implicitly_wait(5)
driver.find_element_by_name("ctl00$CPHContent$txtAmount").send_keys("600")
driver.find_element_by_name("ctl00$CPHContent$txtPaymentPurpose").send_keys("Logistics")
selPaymentType = Select(driver.find_element_by_xpath("//select[@name='ctl00$CPHContent$cboInstrumentType']"))
selPaymentType.select_by_visible_text("FBN Cheque")
driver.implicitly_wait(5)
selBankName = Select(driver.find_element_by_xpath("//select[@name='ctl00$CPHContent$cboBanks']"))
selBankName.select_by_visible_text("First Bank of Nigeria Plc")
#driver.find_element_by_name("ctl00$CPHContent$txtDepositSlipNo").send_keys("08448404")
driver.find_element_by_name("ctl00$CPHContent$txtChequeNo").send_keys(np.random.randint(10000,5983673))
#driver.find_element_by_name("ctl00$CPHContent$txtFBNAccountNumber").send_keys("2011634500")
driver.find_element_by_name("ctl00$CPHContent$btnCaptureEntries").click()
driver.implicitly_wait(5)
driver.find_element_by_name("ctl00$CPHContent$btnPay").click()






