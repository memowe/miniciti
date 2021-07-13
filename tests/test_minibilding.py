import pytest

from miniciti.minibilding import MiniBilding

def testBildingHeight():
    assert MiniBilding.floor_height == 2
    assert MiniBilding(stories=17).height() == 17 * 2
