module folding (
    output logic x,
    input logic a, b, c, d
);

    assign x = (c | d) & ((a ^ b) & 1'b0);

endmodule
