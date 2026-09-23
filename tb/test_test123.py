import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_and_gate(dut):

    test_vectors = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
    ]

    for a, b, expected in test_vectors:
        dut.a.value = a
        dut.b.value = b

        await Timer(1, unit="ns")

        actual = int(dut.c.value)

        assert actual == expected, (
            f"a={a}, b={b}: erwartet {expected}, "
            f"bekommen {actual}"
        )
        
        await Timer(10, unit="ns")
