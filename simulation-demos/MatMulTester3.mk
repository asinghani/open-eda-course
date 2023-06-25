TOPLEVEL_LANG = verilog
VERILOG_SOURCES = $(shell pwd)/MatMul.sv
TOPLEVEL = MatMul
MODULE = MatMulTester3
include $(shell cocotb-config --makefiles)/Makefile.sim
