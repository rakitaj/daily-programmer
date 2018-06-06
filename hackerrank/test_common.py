from common import true_for_all

def test_true_for_all_should_be_true():
    items = [2, 4, 6, 8, 12, 16, 24]
    truth_func = lambda x: x % 2 == 0
    assert true_for_all(items, truth_func) is True

def test_true_for_all_with_bad_data_should_be_false():
    items = [2, 4, 6, 8, 13, 16, 24]
    truth_func = lambda x: x % 2 == 0
    assert true_for_all(items, truth_func) is False
