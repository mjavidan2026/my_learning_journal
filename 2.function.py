# pass vs return : 

def test_p (a):
    if a > 3 :
        print("OK")
        pass
    
    if a > 4 :
        print("NO")
        pass

test_p (5)
#OK
#NO

def test_r (a):
    if a > 3 :
        print("OK")
        return
    
    if a > 4 :
        print("NO")
        return

test_r (5)
#OK