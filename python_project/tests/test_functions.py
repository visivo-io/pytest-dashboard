from python_project.functions import add_one, remove_all_u

def test_add_one_valid():
    assert 2 == add_one(1)

def test_add_one_invalid():
    assert 3 == add_one(1)

def test_remove_all_u_invalid():
    assert "Mst Think of Wrds wth 's" == remove_all_u("Must Think of Wurds wuth U's")