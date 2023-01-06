from behave import *
from selenium.webdriver.common.keys import Keys
import requests
from unittest_assertions import AssertEqual

assert_equal = AssertEqual()
URL = "http://localhost:5000"


@given('Account registry is active')
def make_sure_that_registry_is_working(context):
    resp = requests.get(URL + f"/konta/ile_kont")  # jezeli zwróci kod 200 zakładamy ze serwer działa
    assert_equal(resp.status_code, 200)


@when('I create an account using name: {name}, last name: {last_name}, pesel: {pesel}')
def utworz_konto(context, name, last_name, pesel):
    json_body = {"imie": name,
                 "nazwisko": last_name,
                 "pesel": pesel.replace('"', "")
                 }
    create_resp = requests.post(URL + "/konta/stworz_konto", json=json_body)
    assert_equal(create_resp.status_code, 201)


@then('Number of accounts in registry equals: "{count}"')
def sprawdz_liczbe_kont_w_rejestrze(context, count):
    ile_kont = requests.get(URL + f"/konta/ile_kont")
    assert_equal(ile_kont.json()["count"], int(count))


@step('Account with pesel "{pesel}" exists in registry')
def sprawdz_czy_konto_z_pesel_istnieje(context, pesel):
    response = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(response.json()["pesel"], pesel)


@step('Account with pesel "{pesel}" does not exists in registry')
def sprawdz_czy_konto_z_pesel_nie_istnieje(context, pesel):
    response = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(response.json()["pesel"], None)


@when('I delete account with pesel: "{pesel}"')
def usun_konto(context, pesel):
    response = requests.delete(URL + f"/konta/konto/delete/{pesel}")
    assert_equal(response.status_code, 200)


@when('I clear the account registry')
def usun_wszystkie_konta(context):
    response = requests.delete(URL + f"/konta/clear")
    assert_equal(response.status_code, 200)


@step('I update last name to "{name}" inside account with pesel: "{pesel}"')
def update_nazwiska(context, name, pesel):
    response = requests.post(URL + f"/konta/update/{pesel}/{name}")
    assert_equal(response.status_code, 200)


@then('Last name equals to "{name}" inside account with pesel: "{pesel}"')
def check_name(context, name, pesel):
    response = requests.get(URL + f"/konta/konto/{pesel}")
    assert_equal(response.json()["nazwisko"], name)
