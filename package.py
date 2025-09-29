name = "tbb"

version = "2021.9.0.hh.1.0.0"

authors = [
    "Intel",
]

description = """Threading Building Blocks"""

with scope("config") as c:
    import os
    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]

requires = []

private_build_requires = []

variants = []


def commands():
    env.REZ_TBB_ROOT = "{root}"
    env.TBB_ROOT = "{root}"
    env.TBB_LOCATION = "{root}"
    env.TBBROOT = "{root}"
    env.TBB_INSTALL_DIR = "{root}"
    env.TBB_INCLUDE_DIR = "{root}/include"

    env.LD_LIBRARY_PATH.append("{root}/lib")


uuid = "repository.oneTBB"
# build_command = "bash {root}/rez_build.sh {root}"
