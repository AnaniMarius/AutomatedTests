from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.get("http://collaborative.ase.ro/Pasul1.0.aspx")
driver.implicitly_wait(2)
driver.maximize_window()

radio_button_2 = driver.find_element(By.ID, "RadioButton2")
radio_button_2.click()
time.sleep(2)

next_button_1 = driver.find_element(By.ID, "Button1")
next_button_1.click()

checkbox_1 = driver.find_element(By.ID, "CheckBoxList1_0")
checkbox_1.click()

checkbox_5 = driver.find_element(By.ID, "CheckBoxList1_4")
checkbox_5.click()

checkbox_10 = driver.find_element(By.ID, "CheckBoxList1_9")
checkbox_10.click()
time.sleep(2)

listbox = Select(driver.find_element(By.ID, "ListBox1"))
listbox.select_by_visible_text("1.1. Aparate frigorifice de mari dimensiuni")
listbox.select_by_visible_text("1.3. Aparate frigorifice / Congelatoare")
listbox.select_by_visible_text("1.10. Plite electrice")
time.sleep(2)

next_button_2 = driver.find_element(By.ID, "Button1")
next_button_2.click()

checkbox_ecologic = driver.find_element(By.ID, "CheckBoxList1_1")
checkbox_ecologic.click()
time.sleep(2)

listbox = Select(driver.find_element(By.ID, "ListBox1"))
listbox.select_by_visible_text("2.2. Volumul (cantitatea) de DEEE tratate")
listbox.select_by_visible_text("2.7. Consumul de energie pe unitatea de DEEE reciclat")
time.sleep(2)

next_button_3 = driver.find_element(By.ID, "Button1")
next_button_3.click()
time.sleep(2)

textboxes = [
    "TextBox00", "TextBox01",
    "TextBox10", "TextBox11",
    "TextBox20", "TextBox21"
]

values = [1, 2, 3, 4, 5, 6]

for textbox_id, value in zip(textboxes, values):
    textbox = driver.find_element(By.ID, textbox_id)
    textbox.clear()
    textbox.send_keys(str(value))
time.sleep(2)

next_button_4 = driver.find_element(By.ID, "Button1")
next_button_4.click()
time.sleep(2)

next_button_x = driver.find_element(By.ID, "Button1")
next_button_x.click()
time.sleep(2)


editable_textbox = driver.find_element(By.NAME, "ctl21")
editable_textbox.send_keys("9")
next_button_5 = driver.find_element(By.ID, "Button1")
next_button_5.click()
time.sleep(2)

export = driver.find_element(By.ID, "Button1")
export.click()
time.sleep(2)

driver.quit()
