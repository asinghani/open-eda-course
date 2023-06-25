#include <stdlib.h>
#include <iostream>
#include <verilated.h>
#include <verilated_vcd_c.h>
#include "VMatMul.h"

// These "eval" calls are unique to pure-software simulators
// and aren't needed with SystemVerilog simulators because
// they can intelligently propagate signals (but trying to
// do the same propagation with this kind of simulation would
// be far less efficient)
void step(VMatMul *dut) {
    dut->eval();
    dut->clk = 1;
    dut->eval();
    dut->clk = 0;
    dut->eval();
}

void load_mtx(VMatMul *dut, int mtx[2][2]) {
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 2; j++) {
            dut->mtx_in[i][j] = mtx[i][j];
        }
    }
}

void load_vec(VMatMul *dut, int vec[2]) {
    for (int i = 0; i < 2; i++) {
        dut->vec_in[i] = vec[i];
    }
}

void run_matmul(VMatMul *dut) {
    dut->start = 1;
    step(dut);
    dut->start = 0;
    while (!dut->done) step(dut);
}

void print_result(VMatMul *dut) {
    printf("{ ");
    for (int i = 0; i < 2; i++) {
        printf("%d ", dut->vec_out[i]);
    }
    printf("}\n");
}

void assert_result(VMatMul *dut, int vec[2]) {
    for (int i = 0; i < 2; i++) {
        assert(dut->vec_out[i] == vec[i]);
    }
}

int main() {
    printf("hello\n");

    VMatMul *dut = new VMatMul();

    dut->start = 0;
    dut->reset = 1;
    step(dut);
    step(dut);
    dut->reset = 0;

    // Everything abstracted away into utility functions, really easy
    // to do in C++
    int mtx[2][2] = {
        {1, 2},
        {3, 4}
    };
    load_mtx(dut, mtx);

    int vec[2] = {1, 2};
    load_vec(dut, vec);

    run_matmul(dut);
    printf("result = ");
    print_result(dut);

    int expected[2] = {5, 11};
    assert_result(dut, expected);

    // Do everything one more time :>
    int mtx1[2][2] = {
        {5, 6},
        {7, 8}
    };
    load_mtx(dut, mtx1);

    int vec1[2] = {3, 4};
    load_vec(dut, vec1);

    run_matmul(dut);
    printf("result = ");
    print_result(dut);

    int expected1[2] = {39, 53};
    assert_result(dut, expected1);


    return 0;
}
