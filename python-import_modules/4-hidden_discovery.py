#!/usr/bin/python3
import marshal
import types

if __name__ == "__main__":
    pyc_file = "/tmp/hidden_4.pyc"

    with open(pyc_file, "rb") as f:
        f.read(16) 
        code_obj = marshal.load(f)

    def get_names(co):
        names = set(co.co_names)
        for const in co.co_consts:
            if isinstance(const, types.CodeType):
                names.update(get_names(const))
        return names

    all_names = get_names(code_obj)
    filtered = [name for name in all_names if not name.startswith("__")]

    for name in sorted(filtered):
        print(name)
