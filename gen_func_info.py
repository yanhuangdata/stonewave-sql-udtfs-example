import toml
import os
from stonewave.sql.udtfs.test_utility import check_expected_parameters_list
from stonewave.sql.udtfs.constants import (
    USER_DEFINED_TABLE_FUNCTION_INFO_FILE,
    SIGNATURE_LIST
)
from tests.supported_signature_list import supported_signature_list

def gen_func_info(output_file):
    """
    Generate function information file to output_file path.
    Currently only record the signatures lists, more information in future
    """
    signature_list = supported_signature_list()
    check_expected_parameters_list(signature_list)
    info = {SIGNATURE_LIST: signature_list}

    with open(output_file, 'w') as f:
        toml.dump(info, f)


if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(base_dir)
    gen_func_info(
        # should change the module name
        os.path.join(base_dir, "example_func", USER_DEFINED_TABLE_FUNCTION_INFO_FILE),
    )



