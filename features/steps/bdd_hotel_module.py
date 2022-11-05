import datetime
import re
import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


@given(u'Open the browser and enter the valid url')
def launch_browser(context):
    context.driver = webdriver.Chrome()
    context.action_obj = ActionChains(context.driver)
    context.driver.get("https://www.goibibo.com/")
    context.driver.maximize_window()


@when(u'Click on hotel button')
def click_hotel_btn(context):
    context.driver.find_element("xpath", '//a[@class="nav-link ."]').click()


@when(u'Click on india radio button')
def click_on_india_button(context):
    context.driver.find_element("xpath", '//h4[text()="India"]/..//input[@name="CountryType"]').click()


@when(u'Click on international radio button')
def click_on_international_button(context):
    context.driver.find_element("xpath", '//h4[text()="International"]/..//input[@name="CountryType"]').click()


@when(u'Enter the city name"{city_name}"')
def enter_city_name(context,city_name):
    context.driver.find_element("id", "downshift-1-input").send_keys(city_name)
    context.action_obj.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    time.sleep(2)
    context.action_obj.key_down(Keys.ENTER).key_up(Keys.ENTER).perform()


@when(u'Select check in  and check out dates')
def select_dates(context):
    context.driver.find_element("xpath", '//div[text() = "Check-in"]').click()
    context.driver.implicitly_wait(10)
    context.driver.find_element("xpath", '//span[@data-testid="date_8_10_2022"]').click()
    context.driver.implicitly_wait(10)
    context.driver.find_element("xpath", '//span[@data-testid="date_10_10_2022"]').click()


@when(u'Select number of guests and rooms')
def select_no_of_guestsAndRooms(context):
    context.driver.find_element("xpath", '//input[@value="2 Adults | 0 Child | 1 Room "]').click()
    context.driver.find_element("xpath", '//span[text()="Adults"]/../div//span[text()="-"]').click()
    context.driver.find_element("class name", "dwebCommonstyles__ButtonBase-sc-112ty3f-12.PaxWidgetstyles__ButtonWrapper-sc-gv3w6r-11.QWIoF.jxqLbm").click()


@when(u'Click on search button')
def click_on_search(context):
    context.driver.find_element("xpath", '//button[text()="Search"]').click()


@when(u'Click on search location and enter hotel name "{Hotel_name}"')
def select_hotel_name(context,Hotel_name):
    context.driver.find_element("xpath", '//input[@placeholder="Search Location or Property Name"]').send_keys(Hotel_name)
    time.sleep(2)
    context.action_obj.key_down(Keys.ARROW_DOWN).key_up(Keys.ARROW_DOWN).perform()
    time.sleep(2)
    context.driver.find_element("xpath", '(//h4[@class="dwebCommonstyles__SmallSectionHeader-sc-112ty3f-9 bjZxoj"])[1]').click()


@when(u'Click on view room options and select room')
def select_room(context):
    handles = context.driver.window_handles
    context.driver.switch_to.window(handles[1])
    context.driver.find_element("class name", "TextFieldExpt__Tag-sc-7a7pro-0.bxWEDo").click()
    time.sleep(2)
    # driver.find_element("class name","TextFieldExpt__Tag-sc-7a7pro-0 ftxkiq").click()
    context.driver.find_element("xpath", '(//button[@data-testid="selectRoomBtn"])[1]').click()


@when(u'Enter guest First name "{first_name}"')
def enter_first_name(context,first_name):
    list_box1 = context.driver.find_element("class name", "PersonalProfile__NameEnterSelect-sc-1r9ak8b-7.hkMeMW")
    s_obj = Select(list_box1)
    s_obj.select_by_visible_text("Mr")
    time.sleep(1)
    try:
        result = re.findall('[a-zA-Z]',first_name)
        assert result, "invalid first_name"
        context.driver.find_element("xpath", '//input[@placeholder="Enter First Name"]').send_keys(first_name)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg




@when(u'Enter guest Last name "{last_name}"')
def enter_last_name(context,last_name):
    try:
        result = re.findall('[a-zA-Z]',last_name)
        assert result, "invalid last_name"
        context.driver.find_element("xpath", '//input[@placeholder="Enter Last Name"]').send_keys(last_name)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@when(u'Enter guest Email ID "{email_id}"')
def email_id(context,email_id):
    try:
        pattern = r"\w+@gmail\.com"
        result = re.findall(pattern, email_id)
        assert result,"invalid email_id"
        context.driver.find_element("xpath", '//input[@placeholder="Enter Email Address"]').send_keys(email_id)

    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg



@when(u'Enter guest Mobile number "{mb_num}"')
def enter_mb_num(context,mb_num):
    list_box2 = context.driver.find_element("class name", "PersonalProfile__CountryCodeWrap-sc-1r9ak8b-10.ca-dHee")
    s_obj = Select(list_box2)
    # s_obj.select_by_visible_text("+247 Ascension Island")
    s_obj.select_by_visible_text("+91 India")
    time.sleep(1)
    try:
        assert len(str(mb_num)) == 10
        context.driver.find_element("xpath", '//input[@placeholder="Enter Phone Number"]').send_keys(mb_num)
        time.sleep(2)
    except BaseException as error_msg:
        td = datetime.datetime.now()
        name = f"screenshot_{td.hour}_{td.minute}_{td.second}.png"
        ss_path = r"../../screenshots/"
        context.driver.save_screenshot(ss_path + name)
        raise error_msg


@when(u'Proceed to payment option')
def proceed_to_payment(context):
    context.driver.find_element("class name", "GuestDetailsBlockstyles__ButtonSpan-sc-1rzm4ar-8.pjMOb").click()
    time.sleep(5)


@when(u'Enter pan number "{pan_num}"')
def enter_pan_number(context,pan_num):
    context.driver.find_element("id", "panInput").click()
    context.driver.implicitly_wait(3)
    context.driver.find_element("id", "panInput").send_keys(pan_num)
    time.sleep(3)
    context.driver.find_element("xpath", '//button[text()="Proceed to Payments"]').click()


@when(u'Enter Card number "{card_number}"')
def enter_card_number(context,card_number):
    context.driver.find_element("xpath", '//span[text()="Debit/Credit Card"]').click()
    context.driver.find_element("class name", "form-control.inputMedium.cr_crd_no").send_keys(card_number)


@when(u'Enter Name on card "{name_on_card}"')
def name_on_card(context,name_on_card):
    context.driver.find_element("class name", "form-control.inputMedium.cr_crd_name").send_keys(name_on_card)


@when(u'Enter Expiry date "{exp_date}"')
def enter_exp_date(context,exp_date):
    context.driver.find_element("class name", "form-control.inputMedium.cr_crd_exp").send_keys(exp_date)


@when(u'Enter CVV "{cvv}"')
def enter_cvv(context,cvv):
    context.driver.find_element("xpath", '(//input[@class="gpayformFeildWrap inputMedium marginT5 cr_cvv_no"])[1]').send_keys(cvv)


@when(u'Click on Pay')
def click_on_pay(context):
    context.driver.find_element("xpath",'(//button[@class="button green large citipatBtn btn payNowBtn"])[3]').click()


@then(u'Verify hotelpage should be displayed')
def close_method(context):
    context.driver.quit()
