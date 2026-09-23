import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_convolution(dut):
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    #cycle 1
    dut.din.value = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")

    #cycle 2
    A = 5
    dut.din.value = A
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")

    #cycle 3
    B = 7
    dut.din.value = B
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")

    expected = A * 2 + B * 3
    actual = int(dut.dout.value)

    assert actual == expected, (
        f"A={A}, B={B}: erwartet {expected}, bekommen {actual}"
    )

    #additional cycle
    dut.din.value = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")
