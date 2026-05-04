#!/usr/bin/env python3

def division(a: float, b: float) -> float:
    return a/b

if __name__ == "__main__":
    try:
        division(23, 0)
    except ZeroDivisionError as e:
        print(f"Error: {e}")
