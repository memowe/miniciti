import pytest

from miniciti.bilding import Bilding
from anglr import Angle

def testBildingHeight():
    assert Bilding.floor_height == 3
    assert Bilding(stories=17).height() == 17 * 3

def testAngle():
    assert Bilding().is_upright()
    assert not Bilding(angle=Angle(42, "degrees")).is_upright()
