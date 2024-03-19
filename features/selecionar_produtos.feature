Feature: Selecionar Produto

    Scenario: Selecionar produto "Sauce Labs Backpack"
        Given que acesso o site Sauce Demo
        When preecho os campos de login com o usuario standard_user e senha secret_sauce
        Then sou direcionado para pagina Home  