import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_or_gate(dut):

    # Waveform-Aufzeichnung aktivieren
    dut._log.info("Starting waveform capture")

    test_vectors = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
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

