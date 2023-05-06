from unittest.mock import patch
import pytest

import lab8_9.subtask_1
import lab8_9.subtask_2
import lab8_9.subtask_3
import lab8_9.subtask_4
import lab8_9.subtask_5_6
import lab8_9.subtask_7
import lab8_9.subtask_8
import lab8_9.subtask_9
import lab8_9.subtask_10
import lab8_9.subtask_11
import lab8_9.subtask_12


@pytest.mark.parametrize('input_param, expected',
                         [(['Sophia', 'Madison', 'Admin'],
                           ['Sophia, thank you for logging in again..',
                            'Madison, thank you for logging in again..',
                            'Admin, I hope you\'re well']),
                          ([], ['We need to find some users!'])])
def test_subtask_1(input_param, expected):
    result = lab8_9.subtask_1.get_greetings(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(1, None),
                                                   (4, 'quadrilateral'),
                                                   (3, 'triangle')])
def test_subtask_2(input_param, expected):
    result = lab8_9.subtask_2.get_figure_name(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(list(range(1, 5)),
                                                    ['1st', '2nd', '3rd', '4th', ])])
def test_subtask_3(input_param, expected):
    result = lab8_9.subtask_3.get_number_names(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(4, 'The number is even'),
                                                   (11, 'The number is odd')])
def test_subtask_4(input_param, expected):
    result = lab8_9.subtask_4.get_parity(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(2024, True), (2003, False)])
def test_subtask_5_6_is_leap_year(input_param, expected):
    result = lab8_9.subtask_5_6.is_leap_year(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected, mock_value', [(('mAy', 1984), 31, True),
                                                               (('February', 2024), 29, True),
                                                               (('augustember', 2005), None, False),
                                                               (('february', 2003), 28, False)])
@patch('lab8_9.subtask_5_6.is_leap_year')
def test_subtask_5_6_get_days_or_default_not_leap_years(mock, input_param, expected, mock_value):
    mock.return_value = mock_value
    result = lab8_9.subtask_5_6.get_days_or_default(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((123, 423), 546)])
def test_subtask_8_add(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.add(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((123, 423), -300)])
def test_subtask_8_diff(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.diff(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((20, 4), 5),
                                                   ((20, 0), None),
                                                   ((20, -4), -5)])
def test_subtask_8_divide(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.divide(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((12, 5), 60)])
def test_subtask_8_multiply(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.multiply(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((15, 2), 1),
                                                   ((22, 0), None)])
def test_subtask_8_mod(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.mod(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((2, 3), 8)])
def test_subtask_8_power(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.power(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [((12, 2), 6),
                                                   ((66, 0), None),
                                                   ((44, 690), 0)])
def test_subtask_8_div(input_param, expected):
    result = lab8_9.subtask_8.BasicMathOperations.div(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(100, 'Taras Shevchenko'),
                                                   (200, 'Lesya Ukrainka'),
                                                   (123, None)])
def test_subtask_9(input_param, expected):
    result = lab8_9.subtask_9.get_banknote_person(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(('a', 4), 'white'),
                                                   (('h', 5), 'white'),
                                                   (('a', 7), 'black'),
                                                   (('j', 22), None),
                                                   (('23', 22), None)])
def test_subtask_10(input_param, expected):
    result = lab8_9.subtask_10.get_square_color(input_param[0], input_param[1])
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(16, '10000')])
def test_subtask_11_to_binary(input_param, expected):
    result = lab8_9.subtask_11.to_binary(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [('100110', 38)])
def test_subtask_11_to_decimal(input_param, expected):
    result = lab8_9.subtask_11.to_decimal(input_param)
    assert result == expected


@pytest.mark.parametrize('input_param, expected', [(('🪨', '🪨'), 'Draw!'),
                                                   (('✂️', '📃'), 'You Win!'),
                                                   (('🤨', '📃'), None)])
def test_subtask_12(input_param, expected):
    result = lab8_9.subtask_12.check_winner(input_param[0], input_param[1])
    assert result == expected
