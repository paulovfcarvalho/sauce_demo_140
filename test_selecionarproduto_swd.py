# 1 - Bibliotecas
from selenium import webdriver
from selenium.webdriver.common.by import By

# 2 - Classe (Opcional no Python)
class Teste_Produto():

    # 2.1 Atributos
    url = "https://www.saucedemo.com"
   

    # 2.2 Funções e Métodos
    def setup_method(self, method):                         # método de inicialização dos testes
        self.driver = webdriver.Chrome()                    # instancia o objeto do selenium WebDriver como Chrome
        self.driver.implicitly_wait(1)                      # define o tempo de espera padrão por elementos em 1seg

    def teardown_method(self, method):                      # método de finalização dos testes
        self.driver.quit                                    # encerra / destrói o objeto do Selenium WebDriver da memória

    def test_selecionar_produto(self):                      # método de teste  
        self.driver.get(self.url)                           # abre o navegador
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")     # escreve no campo user-name
        self.driver.find_element(By.NAME,"password").send_keys("secret_sauce")     # escreve a senha
        self.driver.find_element(By.CSS_SELECTOR, "input.submit-button.btn_action").click() # clica no botão

        # transição de página
        assert self.driver.find_element(By.CSS_SELECTOR, "span.title").text == "Products"      # confirma se está escrito Products no elemento
        assert self.driver.find_element(By.ID, "item_4_title_link"). text == "Sauce Labs Backpack"  # confirma se é a mochila
        assert self.driver.find_element(By.CSS_SELECTOR, ".inventory_item:nth-child(1) .inventory_item_price").text == "$29.99" # confi. preço


        
    # 3 - 