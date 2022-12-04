#!/usr/bin/python3

if __name__ == "__main__":
    """Print all nameas defined by hidden _4 module."""
    import hidden_4

    name = dir(hidden_4)
    for name in name:
        if name[:2] != "__":
            print(name)
