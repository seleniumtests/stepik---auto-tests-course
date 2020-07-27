from selenium import webdriver
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x))))) 

link = "http://suninjuly.github.io/redirect_accept.html"
browser=webdriver.Chrome()
browser.get(link)

button = browser.find_element_by_class_name("trollface.btn.btn-primary")
button.click()



#Чтобы узнать имя новой вкладки, нужно использовать метод window_handles,
# который возвращает массив имён всех вкладок. Зная, что в браузере
# теперь открыто две вкладки, выбираем вторую вкладку:

new_window = browser.window_handles[1]

#Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти.
# Это делается с помощью команды switch_to.window:

browser.switch_to.window(new_window)


#После переключения на новую вкладку поиск и взаимодействие с элементами будут происходить уже на новой странице.

# находим и присваиваем
find_x = browser.find_element_by_css_selector("[id='input_value']")
x = int(find_x.text)

y = calc(x)

#находим поле для ввода и вписываем ответ
input_field = browser.find_element_by_id("answer")
input_field.send_keys(y)


button2= browser.find_element_by_class_name("btn.btn-primary")
button2.click()