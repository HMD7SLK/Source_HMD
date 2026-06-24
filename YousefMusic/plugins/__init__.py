import glob
from os.path import dirname, isfile

def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = []

    for f in mod_paths:
        if not isfile(f):
            continue

        if f.endswith("__init__.py"):
            continue

        if not f.endswith(".py"):
            continue

        module = f.replace(work_dir, "").replace("/", ".").strip(".")

        if module.endswith(".py"):
            module = module[:-3]

        if module:
            all_modules.append(module)

    return all_modules


ALL_MODULES = sorted(__list_all_modules())

__all__ = ALL_MODULES + ["ALL_MODULES"]
