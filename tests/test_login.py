def test_login():
    userName = 'Yaashick Sriram'
    passWord = 'admin_123'

    assert userName == 'Yaashick Sriram'
    assert passWord == 'admin_123'

def test_userName_is_notEmpty():
    userName = 'Yaashick Sriram'

    assert userName != ''