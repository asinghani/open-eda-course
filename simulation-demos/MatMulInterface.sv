`default_nettype none

// Matrix-multiply with a memory-mapped interface
//
// Memory-map (using decimal for simplicity):
// 0-15  = input matrix (row-major order)
// 16-19 = input vector
// 20    = start (control)
// 21-31 = UNUSED
// 32-35 = output vector
// 36    = done (status)

module MatMulInterface (
    input logic [31:0] addr,
    input logic wr_en, rd_en,
    input logic [31:0] data_in,
    output logic [31:0] data_out,

    input logic reset,
    input logic clk
);
    
    logic [7:0] mtx_in[4][4];
    logic [7:0] vec_in[4];
    logic start;

    logic [17:0] vec_out[4];
    logic done;

    MatMul #( .SIZE(4) ) matmul ( .* );

    // Read side
    always_ff @(posedge clk) begin
        if (rd_en) begin
            // Read from output vector
            if ((addr >= 32) && (addr < 36)) begin
                data_out <= vec_out[addr - 32];
            end

            // Read from "done" status register
            if (addr == 36) begin
                data_out <= done;
            end
        end
    end

    // Write side
    always_ff @(posedge clk) begin
        start <= '0;

        if (wr_en) begin
            // Write to matrix
            if ((addr >= 0) && (addr < 16)) begin
                // Fortunately, synthesis is smart and will turn div and mod
                // by a power of 2 into bit-shift / bit-selection (which is
                // free in hardware because it's just wires)
                mtx_in[addr / 4][addr % 4] <= data_in[7:0];
            end

            // Write to vector
            if ((addr >= 16) && (addr < 20)) begin
                vec_in[addr - 16] <= data_in[7:0];
            end

            // Start command
            if ((addr == 20) && (data_in[0] == 1)) begin
                start <= '1;
            end
        end
    end

endmodule
