TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/MatMul.sv
TOPLEVEL = MatMul
MODULE = MatMulTester2
include $(shell cocotb-config --makefiles)/Makefile.sim
