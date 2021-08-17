import pytest
import num2words

import num_to_phrase

num = -1


@pytest.mark.repeat(1000)
def test_num_to_phrase():
    global num
    num += 1
    assert num_to_phrase.translate(
        num) == num2words.num2words(num).replace('and ', '')


# def test_sanity():
# 	assert 1 == 1

# def test_sanity_again():
# 	assert 1 != 0
