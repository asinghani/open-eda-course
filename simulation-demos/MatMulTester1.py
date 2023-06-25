import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

SIZE = int(cocotb.top.SIZE)

def read_testcases():
    testcases = []
    with open("MatMulTestVectors.txt") as f:
        for line in f:
            mtx, vec, vec_out = [eval(x) for x in line.strip().split(";")]
            assert len(mtx) == SIZE*SIZE
            assert len(vec) == SIZE
            assert len(vec_out) == SIZE
            testcases.append((mtx, vec, vec_out))

    return testcases

async def reset(dut):
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.reset.value = 0

@cocotb.test()
async def test_matmul(dut):
    testcases = read_testcases()

    # Automatic clock (timescale is for VCD files)
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset DUT
    dut.start.value = 0
    await reset(dut)

    for mtx, vec, vec_out in testcases:
        dut.mtx_in.value = mtx
        dut.vec_in.value = vec

        dut.start.value = 1
        await RisingEdge(dut.clk)
        dut.start.value = 0
        await RisingEdge(dut.clk)

        while dut.done.value != 1:
            await RisingEdge(dut.clk)

        await RisingEdge(dut.clk)

        print(dut.vec_out.value, vec_out)
        assert dut.vec_out.value == vec_out
