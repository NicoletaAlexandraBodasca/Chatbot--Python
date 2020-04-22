from chatbot import Entitate

def testEntitate():
    e1=Entitate("intrebare1",4)
    assert e1.getIntrebare()=="intrebare1"
    assert e1.getRaspuns()==4
    e1.setRaspuns(5)
    e1.setIntrebare("intrebare2")
    assert e1.getIntrebare()=="intrebare2"
    assert e1.getRaspuns()==5
    print("all tests are ok")
testEntitate()

def test_eq():
    e1=Entitate("intrebare",7)
    e2=Entitate("intrebare",7)
    assert(e1==e2)
    e1.setRaspuns(8)
    e2.setRaspuns(9)
    assert(e1!=e2)
    print("all tests are ok")
test_eq()
def test_gt():
    e1=Entitate("int",9)
    e2=Entitate("int",7)
    assert(e1>e2)
    print("all tests are ok")
test_gt()
def test_lt():
    e1=Entitate("int",9)
    e2=Entitate("int",7)
    assert(e1>e2)
    print("all tests are ok")
test_lt()
