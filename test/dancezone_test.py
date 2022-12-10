
from sourcetest import recommendation

def test_topcase():
    assert recommendation(danceability=float(75), valence=float(50)) == "This song is would be good to play for a party!"

def test_middlecase():
    assert recommendation(danceability=float(75), valence=float(20)) == "This song is would be ok to play at a party, but other options might be better."

def test_bottomcase():
    assert recommendation(danceability=float(20), valence=float(20)) == "This song is not a great choice for a party. A more upbeat, danceable song would be better."