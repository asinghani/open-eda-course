import math
import os
import random
from typing import Any, Dict, List

import cocotb
from cocotb.binary import BinaryValue
from cocotb.clock import Clock
from cocotb.handle import SimHandleBase
from cocotb.queue import Queue
from cocotb.triggers import RisingEdge, ReadOnly

import numpy as np

random.seed(42) # reproducability

NUM_ITERS = 300
SIZE = int(cocotb.top.SIZE)

class DataMonitor:
    # Instead of taking the whole DUT as input, it only takes the relevant ports
    # from the DUT and works with those, that way it is modular and easily
    # extendable to different things
    def __init__(self, clk, fields, valid):
        self.values = Queue()
        self._clk = clk
        self._fields = fields
        self._valid = valid
        self._coro = None

    def start(self):
        self._coro = cocotb.start_soon(self._run())

    def stop(self):
        self._coro.kill()
        self._coro = None

    async def _run(self) -> None:
        while True:
            await RisingEdge(self._valid)
            await ReadOnly()
            self.values.put_nowait(self._sample())

    def _sample(self):
        return {name: handle.value for name, handle in self._fields.items()}


class MatMulTester:
    def __init__(self, dut):
        self.dut = dut

        self.input_monitor = DataMonitor(
            clk=self.dut.clk,
            valid=self.dut.start,
            fields={"mtx_in": self.dut.mtx_in, "vec_in": self.dut.vec_in}
        )

        self.output_monitor = DataMonitor(
            clk=self.dut.clk,
            valid=self.dut.done,
            fields={"vec_out": self.dut.vec_out}
        )

        self._checker = None

    def start(self):
        self.input_monitor.start()
        self.output_monitor.start()
        self._checker = cocotb.start_soon(self._check())

    def stop(self):
        self.input_monitor.stop()
        self.output_monitor.stop()
        self._checker.kill()
        self._checker = None

    async def _check(self) -> None:
        while True:
            actual = await self.output_monitor.values.get()
            inputs = await self.input_monitor.values.get()
            vec_out_actual = [x.integer for x in actual["vec_out"]]

            # Evaluate golden model to figure out expected output
            vec_out_expected = matmul_golden(inputs["mtx_in"], inputs["vec_in"])

            assert vec_out_expected == vec_out_actual

def matmul_golden(mtx, vec):
    mtx = np.array([x.integer for x in mtx]).reshape((2, 2))
    vec = np.array([x.integer for x in vec]).reshape((2, 1))

    vec_out_exp = list(mtx.dot(vec).flatten())
    return vec_out_exp

@cocotb.test()
async def test_matmul(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    tester = MatMulTester(dut)

    # Reset DUT
    dut.start.value = 0
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.reset.value = 0

    tester.start()

    for _ in range(NUM_ITERS):
        dut.mtx_in.value = [random.randint(0, 255) for _ in range(SIZE*SIZE)]
        dut.vec_in.value = [random.randint(0, 255) for _ in range(SIZE)]

        dut.start.value = 1
        await RisingEdge(dut.clk)
        dut.start.value = 0
        await RisingEdge(dut.clk)

        while dut.done.value != 1:
            await RisingEdge(dut.clk)

    for _ in range(20):
        await RisingEdge(dut.clk)

# Can have more than one test!
@cocotb.test()
async def test_trivial(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset DUT
    dut.start.value = 0
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    dut.reset.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)

    assert dut.done.value == 0
