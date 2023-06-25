import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, ReadOnly

from cocotb_bus.monitors import Monitor
from cocotb_bus.scoreboard import Scoreboard

SIZE = int(cocotb.top.SIZE)

def read_testcases():
    testcases = []
    with open("MatMulTestVectors.txt") as f:
        for line in f:
            mtx, vec, vec_out = [eval(x) for x in line.strip().split(";")]
            testcases.append((mtx, vec, vec_out))

    return testcases

class VecOutMonitor(Monitor):
    def __init__(self, name, valid_signal, vec_signal, callback=None, event=None):
        self.name = name
        self.valid_signal = valid_signal
        self.vec_signal = vec_signal
        Monitor.__init__(self, callback, event)

    async def _monitor_recv(self):
        while True:
            await RisingEdge(self.valid_signal)
            await ReadOnly()
            self._recv(self.vec_signal.value)

async def reset(dut):
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.reset.value = 0

@cocotb.test()
async def test_matmul(dut):
    testcases = read_testcases()

    vec_out_mon = VecOutMonitor("vec_out", dut.done, dut.vec_out)
    scoreboard = Scoreboard(dut)
    vec_out_queue = []
    scoreboard.add_interface(vec_out_mon, vec_out_queue)

    # Automatic clock (timescale is for VCD files)
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset DUT
    dut.start.value = 0
    await reset(dut)

    for mtx, vec, vec_out in testcases:
        dut.mtx_in.value = mtx
        dut.vec_in.value = vec
        vec_out_queue.append(vec_out)

        dut.start.value = 1
        await RisingEdge(dut.clk)
        dut.start.value = 0
        await RisingEdge(dut.clk)

        while dut.done.value != 1:
            await RisingEdge(dut.clk)

    raise scoreboard.result
