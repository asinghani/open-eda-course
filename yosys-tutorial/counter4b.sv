`default_nettype none

module counter4b (
    output logic [3:0] value,
    input logic clk
);

    always_ff @(posedge clk) begin
        value <= value + 1;
    end

endmodule
