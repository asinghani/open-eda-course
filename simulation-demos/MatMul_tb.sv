`default_nettype none

`define ASSERT(m_condition) if (!(m_condition)) begin \
    $display("Assertion failed, line %d", `__LINE__); \
    $finish; \
end

module MatMul_tb;
    parameter SIZE = 2;

    logic [7:0] mtx_in[SIZE][SIZE];
    logic [7:0] vec_in[SIZE];
    logic [16:0] vec_out[SIZE];

    logic start, done;
    logic clk, reset;

    MatMul #( .SIZE(SIZE) ) dut ( .* );

    initial begin
        clk = '0;
        forever #5 clk = ~clk;
    end
    
    initial begin
        $dumpfile("_mm_out.vcd");
        $dumpvars;

        start = '0;
        reset = '1;
        repeat(2) @(negedge clk);
        reset = '0;

        // Array literal :>
        mtx_in = '{
            '{8'd1, 8'd2},
            '{8'd3, 8'd4}
        };
        vec_in = '{8'd1, 8'd2};

        start = '1;
        @(negedge clk);
        start = '0;
        `ASSERT(!done);

        // Check output is correct
        while (!done) @(negedge clk);
        $display("Out %d %d", vec_out[0], vec_out[1]);
        `ASSERT(vec_out == '{17'd5, 17'd11});

        // Check that done is persisted
        repeat(5) @(negedge clk);
        `ASSERT(done);

        // Try one more computation
        mtx_in = '{
            '{8'd5, 8'd6},
            '{8'd7, 8'd8}
        };
        vec_in = '{8'd3, 8'd4};

        start = '1;
        @(negedge clk);
        start = '0;
        `ASSERT(!done);

        while (!done) @(negedge clk);
        $display("Out %d %d", vec_out[0], vec_out[1]);
        `ASSERT(vec_out == '{17'd39, 17'd53});

        $finish;
    end

endmodule
