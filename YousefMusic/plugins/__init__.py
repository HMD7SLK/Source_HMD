def __list_all_modules():
    work_dir = dirname(__file__)
    mod_paths = glob.glob(work_dir + "/*/*.py")

    all_modules = []

    for f in mod_paths:
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py"):
            module = f.replace(work_dir, "").replace("/", ".").strip(".")
            module = module[:-3]

            if module:
                all_modules.append(module)

    return all_modules
