
from sourcetest import dancezone

def test_correct_output():
    assert dancezone(search_song="Bound 2", track_number="1") == "This song is not a great choice for a party. A more upbeat, danceable song would be better."
    assert dancezone(search_song="Happy", track_number="4") == "This song is would be good to play for a party!"