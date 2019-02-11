from rockyridge import read_string_from_file

############################################################

def test_rockyridge():

    print("testing rockyridge")

    assert read_string_from_file(None, "default") == "default"

############################################################
