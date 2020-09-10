from td1 import somme_depenses
from td1 import somme_personne
from td1 import somme_par_personne
from td1 import avoir_par_personne


def test_somme_depenses():
    """
    Test de somme_depenses
    """
    mesdepenses = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5)]
    assert somme_depenses(mesdepenses) == 57

def test_somme_personne():
    """
    Test de somme_personne
    """
    mesdepenses = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5)]
    assert somme_personne(mesdepenses, "ophelie") == 29
    assert somme_personne(mesdepenses, "fab") == 0

def test_somme_par_personne():
    """
    test de somme_par_personne
    """
    mesdepenses = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5)]
    mesdepensesbis = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5), ('paul', 26)]
    assert somme_par_personne(mesdepenses) == {'joe' : 23, 'ophelie' : 29, 'paul' : 5}
    assert somme_par_personne(mesdepensesbis) == {'joe' : 23, 'ophelie' : 29, 'paul' : 31}
    assert somme_par_personne([]) == {}

def test_avoir_par_personne():
    """
    test de avoir_par_personne
    """
    mesdepenses = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5)]
    mesdepensesbis = [('joe', 23), ('ophelie', 17), ('ophelie', 12), ('paul', 5), ('paul', 27)]
    assert avoir_par_personne(mesdepenses) == {'joe' : -4, 'ophelie' : -10, 'paul' : 14}
    assert avoir_par_personne(mesdepensesbis) == {'joe' : 5 , 'ophelie' : -1, 'paul' : -4}
