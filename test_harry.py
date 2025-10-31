from harry import Mago

def test_horrocruxes(): 
    mago = Mago("Pizarnik")
    mago.crear_horrocruxes(5)
    assert mago.vivo() == True

def test_muerte_mago_enemigo():
    mago = Mago("Schewblin")
    mago_enemigo = Mago("Hobbes")
    mago.avada_kedavra(mago_enemigo)
    assert not mago_enemigo.vivo()

def test_mago_enemigo_vivo():
    mago = Mago("Enriquez")
    mago_enemigo = Mago("Maquiavelo")
    mago_enemigo.crear_horrocruxes(3)
    mago.avada_kedavra(mago_enemigo)
    assert mago_enemigo.vivo()

def test_multiples_avadas_kedavras_muerto():
    mago = Mago("Tart")
    mago_enemigo = Mago("Rooney")
    mago_enemigo.crear_horrocruxes(2)
    mago.avada_kedavra(mago_enemigo)
    assert mago_enemigo.vivo(), "El mago enemigo deberia seguir vivo despues del primer avada kedavra ya que gasta 1 de los 2 horrocruxes que tenía"
    mago.avada_kedavra(mago_enemigo)
    assert mago_enemigo.vivo(), "El mago enemigo deberia seguir vivo despues del segundo avada kedavra ya que gasta 1 de los 1 horrocruxes que tenía"
    mago.avada_kedavra(mago_enemigo)
    assert not mago_enemigo.vivo()

def test_multiples_avadas_kedavras_vivo():
    mago = Mago("Ruiz Zafón")
    mago_enemigo = Mago("Cortazar")
    mago_enemigo.crear_horrocruxes(4)
    mago.avada_kedavra(mago_enemigo)
    mago.avada_kedavra(mago_enemigo)
    mago.avada_kedavra(mago_enemigo)
    assert mago_enemigo.vivo()