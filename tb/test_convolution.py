import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer


@cocotb.test()
async def test_convolution(dut):
    #10ns clk
    cocotb.start_soon(Clock(dut.clk, 10, unit="ns").start())

    #cycle 1 init
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
    
    #cycle 4
    C = 9
    dut.din.value = C
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")
    
    #cycle 5
    D = 11
    dut.din.value = D
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")
    
    #cycle 6
    E = 13
    dut.din.value = E
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")

    actual = int(dut.dout.value)
    
    expected = A*2 + B*3 + C*4 + D*5 + E*6 
    
    assert actual == expected, (
        f"A={A}, B={B}, C={C}, D={D}, E={E}: " 
        f"expected {expected}, got {actual}"
    )

    #additional cycle for waveform
    dut.din.value = 0
    await RisingEdge(dut.clk)
    await Timer(1, unit="ps")
