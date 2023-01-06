Feature: Account registry

    Scenario: User is able to create a new account
        Given Account registry is active
        When I create an account using name: "kurt", last name: "cobain", pesel: "01234567890"
        Then Number of accounts in registry equals: "1"
        And Account with pesel "01234567890" exists in registry

    Scenario: User is able to create a second account
        Given Account registry is active
        When I create an account using name: "test", last name: "testt", pesel: "01234567891"
        Then Number of accounts in registry equals: "2"
        And Account with pesel "01234567891" exists in registry

    Scenario: User is able to delete already created account
        Given Account with pesel "01234567891" exists in registry
        When I delete account with pesel: "01234567891"
        Then Account with pesel "01234567891" does not exists in registry

    Scenario: Admin user is able to clear the account registry
        When I clear the account registry
        Then Number of accounts in registry equals: "0"

    Scenario: User is able to update last name saved in account
        Given Account registry is active
        When I create an account using name: "test", last name: "testt", pesel: "01234567891"
        And I update last name to "test2" inside account with pesel: "01234567891"
        Then Last name equals to "test2" inside account with pesel: "01234567891"