from django.test import TestCase
from TaskUser.views import home, add
from django.urls import resolve
from django.template.loader import render_to_string
from django.http import HttpRequest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
time.sleep(10)
browser.get('http://localhost:8000/taskuser/')
assert 'utilisateurs' in browser.title
assert 'Tâches' in browser.title
elem = browser.find_elements(By.TAG_NAME, 'div')
assert(elem is not None)

browser.quit()

class StringTest(TestCase):
    '''Test unitaire bidon'''
    def test_concatene(self):
        self.assertEqual("Bon"+"jour", "Bonjour")


class HomePageTest(TestCase):
    '''
    Test unitaire de la page accueil sur la racine du projet
    On vérifie que la méthode home() est bien invoquée sur /taskuser/
    '''
    def test_root_url_resolves_to_home_view(self):
      found = resolve('/taskuser/')
      self.assertEqual(found.func, home)

class HomePageTestContent(TestCase):
    '''Test Unitaire pour vérifier si le contenu de la page d'accueil est bien retourné par home()'''
    def test_contenu_home_return_by_home_view(self):
        request = HttpRequest()
        response = home(request)
        expected_html = render_to_string('list.html')
        self.assertEqual(response.content.decode(), expected_html)

class AddPageTest(TestCase):
    '''
    Test unitaire de la page ajout du projet
    On vérifie que la méthode add() est bien invoquée sur /taskuser/add
    '''
    def test_root_url_resolves_to_add_view(self):
      found = resolve('/taskuser/add')
      self.assertEqual(found.func, add)
