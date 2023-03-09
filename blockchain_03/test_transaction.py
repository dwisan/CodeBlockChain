from transaction import Transaction

def test_equality():
    sender = '@sender_addr'
    receiv = '@receiv_addr'
    val = 10

    t1 = Transaction(sender, receiv, val)
    t2 = Transaction(sender, receiv, val)

    transactions = [t1, t2]

    print(t1, t2)
    t3 = Transaction(sender, receiv, 55)

    assert t1 == t2
    assert t1 != t3

    assert t1 in transactions
    assert not t3 in transactions
