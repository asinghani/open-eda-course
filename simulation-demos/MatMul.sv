`default_nettype none

module MatMul #(
    parameter SIZE = 2
) (
    input logic [7:0] mtx_in[SIZE][SIZE],
    input logic [7:0] vec_in[SIZE],
    input logic start,

    output logic [15+$clog2(SIZE):0] vec_out[SIZE],
    output logic done,

    input logic reset,
    input logic clk
);

    enum logic [1:0] {START, COMPUTE, DONE} state;
    logic [$clog2(SIZE):0] index;

    assign done = (state == DONE);

    integer i;
    always_ff @(posedge clk) begin
        if (reset || start) begin
            for (i = 0; i < SIZE; i++) begin
                vec_out[i] <= '0;
            end
        end
        else if (state == COMPUTE) begin
            for (i = 0; i < SIZE; i++) begin
                vec_out[i] <= vec_out[i] + (mtx_in[i][index] * vec_in[index]);
            end
        end
    end

    always_ff @(posedge clk) begin
        if (reset) begin
            state <= START;
        end
        else if (state == START || state == DONE) begin
            if (start) begin
                index <= 0;
                state <= COMPUTE;
            end
        end
            
        else if (state == COMPUTE) begin
            index <= index + 1;

            if (index == SIZE - 1) begin
                state <= DONE;
            end
        end
    end

endmodule
