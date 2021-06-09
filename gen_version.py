import toml
import os

base_dir = os.path.dirname(os.path.abspath(__file__))

def get_project_version():
    poetry_toml = toml.load(os.path.join(base_dir, "pyproject.toml"))
    return poetry_toml["tool"]["poetry"]["version"]

def gen_version_py(project_ver, output_file):
    content = f"""
# Do not change the content of this file
# this file is generated with gen_version.sh
# when building the function


def example_func_version():
    return "{project_ver}"

"""
    with open(output_file, "w") as f:
        f.write(content)


if __name__ == "__main__":
    os.chdir(base_dir)
    gen_version_py(
        get_project_version(),
        os.path.join(base_dir, "example_func", "version.py"),
    )
