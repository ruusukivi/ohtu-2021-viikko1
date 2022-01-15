import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_tilavuus_nollataan(self):
        self.varasto2 = Varasto(-1.0)
        self.assertAlmostEqual(self.varasto2.tilavuus, 0)
           
    def test_negatiivinen_alkusaldo_nollataan(self):
        self.varasto2 = Varasto(0.0, -1)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_negatiivinen_lisays_ohitetaan(self):
        saldo = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, saldo)

    def test_varastoon_ei_lisata_enempaa_kuin_mahtuu(self):
        self.varasto.lisaa_varastoon(1000)
        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_varastosta_ei_oteta_negatiivista_maaraa(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1.0), 0.0)

    def test_varastosta_ei_oteta_enempaa_kuin_siella_on(self):
        otettavissa = self.varasto.saldo
        self.assertAlmostEqual(self.varasto.ota_varastosta(1000.0), otettavissa)

    def test_str_toimii(self):
	        self.assertEqual(str(self.varasto),"saldo = 0, vielä tilaa 10")
