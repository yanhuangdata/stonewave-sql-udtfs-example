import os
from stonewave.sql.udtfs.test_utility import (
    check_expected_parameters_list,
    read_arrow_batch_from_csv,
    wrap_apply_function_input_parameter_with_type as type_wrapper,
    check_batch_iterator_results_with_csv_file,
    eval_table_function_test,
    apply_table_function_test,
)
from stonewave.sql.udtfs.constants import ParameterType as pt
from example_func import GenerateTableFunction
from tests.supported_signature_list import supported_signature_list


def _setup():
    func_expected_params = supported_signature_list()
    check_expected_parameters_list(func_expected_params)


def _make_expected_table_csv_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "expected_results", file_name)


def _make_applied_left_table_csv_path(file_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "applied_table", file_name)


def test_eval_table_function():
    _setup()
    func_expected_params = supported_signature_list()
    test_params = []
    test_params.append(3)
    test_params.append("yh")
    test_params.append(821)

    batch_iterator = eval_table_function_test(GenerateTableFunction, test_params, func_expected_params)
    check_batch_iterator_results_with_csv_file(batch_iterator, _make_expected_table_csv_path("data_1.csv"))

    test_params.append(True)
    batch_iterator = eval_table_function_test(GenerateTableFunction, test_params, func_expected_params)
    check_batch_iterator_results_with_csv_file(batch_iterator, _make_expected_table_csv_path("data_2.csv"))

    test_params.append(1.234)
    batch_iterator = eval_table_function_test(GenerateTableFunction, test_params, func_expected_params)
    check_batch_iterator_results_with_csv_file(batch_iterator, _make_expected_table_csv_path("data_3.csv"))


def test_apply_table_function():
    _setup()
    func_expected_params = supported_signature_list()
    applied_table_path = _make_applied_left_table_csv_path("left_table.csv")
    applied_batch = read_arrow_batch_from_csv(applied_table_path)
    # left_table [CROSS] APPLY example_func(num_field, 'abcde', int_field)
    is_outer_apply = False
    params = [
        type_wrapper(pt.COLUMN, "num_field"),
        type_wrapper(pt.LITERAL, "abcde"),
        type_wrapper(pt.COLUMN, "int_field"),
    ]
    batch_iterator = apply_table_function_test(
        GenerateTableFunction, applied_batch, is_outer_apply, params, func_expected_params
    )
    check_batch_iterator_results_with_csv_file(batch_iterator, _make_expected_table_csv_path("data_4.csv"))

    # left_table OUTER APPLY example_func(num_field, str_field, int_field, bool_field, 2.345)
    is_outer_apply = True
    params = [
        type_wrapper(pt.COLUMN, "num_field"),
        type_wrapper(pt.COLUMN, "str_field"),
        type_wrapper(pt.COLUMN, "int_field"),
        type_wrapper(pt.COLUMN, "bool_field"),
        type_wrapper(pt.LITERAL, 2.345),
    ]
    batch_iterator = apply_table_function_test(
        GenerateTableFunction, applied_batch, is_outer_apply, params, func_expected_params
    )
    check_batch_iterator_results_with_csv_file(batch_iterator, _make_expected_table_csv_path("data_5.csv"))
