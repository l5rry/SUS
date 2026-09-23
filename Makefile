SIM = verilator

TOPLEVEL_LANG = verilog
EXTRA_ARGS += -Wno-WIDTHEXPAND
VERILOG_SOURCES = $(PWD)/codegen.sv

export PYTHONPATH := $(PWD)/tb

COMPILE_ARGS += --trace
EXTRA_ARGS += --trace --trace-structs

include $(shell cocotb-config --makefiles)/Makefile.sim


# make hello_hardware
# -> hello_hardware.sus
# -> codegen.sv
# -> Verilator + Cocotb
%: %.sus
	sus_compiler $< --top $@ -o codegen.sv
	$(MAKE) TOPLEVEL=$@ COCOTB_TEST_MODULES=test_$@ sim


wave:
	gtkwave dump.vcd
