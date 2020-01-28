Feature: Searching on the web store
    As a customer,
    I want to search for a product on the home page
    So I can add the listed product to cart

    Scenario: Searching without login
        Given the store home page is displayed
        When the user searches for "dress"
        Then at least one product is listed

