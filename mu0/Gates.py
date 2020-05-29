HIGH  = 1
LOW   = 0


def and_gate(in_1, in_2):
    if in_1 == HIGH and in_2 == HIGH:
        return HIGH
    return LOW

def or_gate(in_1, in_2):
    if in_1 == HIGH or in_2 == HIGH:
        return HIGH
    return LOW

def not_gate(in_1):
    if in_1 == HIGH:
        return LOW
    return HIGH

def xor_gate(in_1, in_2):
    if in_1 == in_2:
        return LOW
    return HIGH

def or_not_gate(in_1, in_2):
    return not_gate(or_gate(in_1, in_2))

def and_not_gate(in_1, in_2):
    return not_gate(and_gate(in_1, in_2))


if __name__ == '__main__':
    print("and_gate")
    print("input: HIGH, LOW")
    print("  output: ", and_gate(HIGH, LOW))

    print("input: HIGH, HIGH")
    print("  output: ", and_gate(HIGH, HIGH))

    print("input: LOW, HIGH")
    print("  output: ", and_gate(LOW, HIGH))

    print("input: LOW, LOW")
    print("  output: ", and_gate(LOW, LOW))
    print("")

    print("or_gate")
    print("input: HIGH, LOW")
    print("  output: ", or_gate(HIGH, LOW))

    print("input: HIGH, HIGH")
    print("  output: ", or_gate(HIGH, HIGH))

    print("input: LOW, HIGH")
    print("  output: ", or_gate(LOW, HIGH))

    print("input: LOW, LOW")
    print("  output: ", or_gate(LOW, LOW))
    print("")

    print("xor_gate")
    print("input: HIGH, LOW")
    print("  output: ", xor_gate(HIGH, LOW))

    print("input: HIGH, HIGH")
    print("  output: ", xor_gate(HIGH, HIGH))

    print("input: LOW, HIGH")
    print("  output: ", xor_gate(LOW, HIGH))

    print("input: LOW, LOW")
    print("  output: ", xor_gate(LOW, LOW))
    print("")

    print("not_gate")
    print("input: HIGH")
    print("  output: ", not_gate(HIGH))

    print("input: LOW")
    print("  output: ", not_gate(LOW))
    print("")

    print("or_not_gate")
    print("input: HIGH, LOW")
    print("  output: ", or_not_gate(HIGH, LOW))

    print("input: HIGH, HIGH")
    print("  output: ", or_not_gate(HIGH, HIGH))

    print("input: LOW, HIGH")
    print("  output: ", or_not_gate(LOW, HIGH))

    print("input: LOW, LOW")
    print("  output: ", or_not_gate(LOW, LOW))
    print("")

    print("and_not_gate")
    print("input: HIGH, LOW")
    print("  output: ", and_not_gate(HIGH, LOW))

    print("input: HIGH, HIGH")
    print("  output: ", and_not_gate(HIGH, HIGH))

    print("input: LOW, HIGH")
    print("  output: ", and_not_gate(LOW, HIGH))

    print("input: LOW, LOW")
    print("  output: ", and_not_gate(LOW, LOW))
    print("")







