# 98-154 / 18-224 / 18-624 Intro to Open-Source Chip Design

![](banner.png)

## Contents

- [Background](#background)
- [The Course](#the-course)
- [Student Projects](#student-projects)
- [Course Lectures](#course-lectures)
- [Next Steps](#next-steps)
- [Contact](#contact)

## Background

There has been a substantial growth in the use of open-source technologies for hardware design over the past few years. The 2020 release of the open-source, manufacturable Skywater 130nm process node made it possible to design and manufacture a chip using entirely open-source tools. Since then, there have been over 400 chips designed and manufactured on these open-source process nodes.

This provides an interesting educational opportunity for introducing students to chip design in a low-stakes environment, without the overhead of NDAs and complex software stacks. A student only needs a baseline level of digital logic design knowledge to hit the ground running and start exploring how to prepare a simple design for fabrication. They can use [interactive Jupyter notebooks](https://github.com/chipsalliance/silicon-notebooks/blob/main/xls-workshop-openlane.ipynb) to configure and understand each step of the design flow, resulting in a GDS file which they can then submit to be manufactured.

## The Course

In Spring 2023, [we started a new course](https://www.ece.cmu.edu/news-and-events/story/2023/08/introducing-students-to-open-source-chip-design.html) in the CMU Electrical & Computer Engineering department: "18-224 Intro to Open Source Chip Design". The course was developed and taught by Anish Singhani, advised by Prof. Bill Nace. This course is intended to be accessible to students from a wide variety of backgrounds, and get them interested in chip design, to help them decide whether they intend to pursue further study in the space (such as by taking graduate-level coursework in the space, and/or by getting involved in research projects).

Additionally, by culminating the course in a project where students actually tape out a design and get it manufactured, students get the excitement and satisfaction of having something they can hold in their hand and say "I made this". 

The first iteration of the course was a resounding success. Students were given a designated amount of area (roughly equivalent to 4000 standard cells) on the chip and had the option of using Verilog or a schematic editor. They then used the OpenLane flow to complete physical layout. We then took the submitted student designs and multiplexed them onto a single die, which we sent to Skywater for manufacturing through the ChipIgnite shuttle program. 

## Student Projects

Students developed a wide variety of projects ranging from games to CPUs to accelerators. Following are the projects designed by students (this includes both the Spring 2023 18-224 course as well as the experimental workshop version of this course taught in Fall 2022).

| **Index** | **Project**                          | **Student**             | **Link**                                                                                                              |
|-----------|--------------------------------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------|
| 1         | 6-Bit Combinational Adder            | (demo)                  | [d01_example_adder](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d01_example_adder)               |
| 2         | 12-Bit Counter                       | (demo)                  | [d02_example_counter](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d02_example_counter)           |
| 3         | "Beep Boop" Traffic Light Controller | (demo)                  | [d03_example_beepboop](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d03_example_beepboop)         |
| 4         | AES-128 Side-Channel Model           | (demo)                  | [d04_example_aes128sca](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d04_example_aes128sca)       |
| 5         | Tapeout Meta-Info                    | (demo)                  | [d05_meta_info](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d05_meta_info)                       |
| 6         | Pong Game with VGA                   | (demo)                  | [d06_demo_vgapong](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d06_demo_vgapong)                 |
| 7         | Endless Runner Game with VGA         | (demo)                  | [d07_demo_vgarunner](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d07_demo_vgarunner)             |
|           |                                      |                         |                                                                                                                       |
| 10        | Tic-Tac-Toe Game                     | Wahib Abib              | [d10_wabib_tictactoe](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d10_wabib_tictactoe)           |
| 11        | Brainfuck CPU                        | Gary Bailey             | [d11_gbailey_bfchip](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d11_gbailey_bfchip)             |
| 12        | I2C Peripheral                       | Owen Ball               | [d12_oball_i2c](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d12_oball_i2c)                       |
| 13        | S444 FPGA Logic Cell                 | Jack Duvall             | [d13_jrduvall_s444](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d13_jrduvall_s444)               |
| 14        | Traffic Light Controller             | Jessie Fan              | [d14_jessief_trafficlight](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d14_jessief_trafficlight) |
| 15        | Pseudo Random Number Generator       | Jerry Feng              | [d15_jerryfen_prng](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d15_jerryfen_prng)               |
| 16        | Digital Phase Locked Loop            | Joel Gonzalez           | [d16_bgonzale_pll](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d16_bgonzale_pll)                 |
| 17        | Tetris Game                          | Navod Jayawardhane      | [d17_njayawar_tetris](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d17_njayawar_tetris)           |
| 18        | Multiply-Accumulate Unit             | Nikhil Dinkar Joshi     | [d18_nikhildj_mac](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d18_nikhildj_mac)                 |
| 19        | Encryption Unit (custom cipher)      | Roman Kapur             | [d19_rdkapur_encryptor](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d19_rdkapur_encryptor)       |
| 20        | Simplified Tetris Game               | Rashi Kejriwal          | [d20_rashik_tetris](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d20_rashik_tetris)               |
| 21        | Motor Controller                     | Varun Kumar             | [d21_varunk2_motorctrl](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d21_varunk2_motorctrl)       |
| 22        | Convolution Accelerator              | Yushuang Liu            | [d22_yushuanl_convolution](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d22_yushuanl_convolution) |
| 23        | Turing Machine                       | Ying Meng               | [d23_zhiyingm_turing](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d23_zhiyingm_turing)           |
| 24        | Tensor Processing Unit               | M Nguyen                | [d24_mnguyen2_tpu](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d24_mnguyen2_tpu)                 |
| 25        | Huffman Encoder                      | Anusha Raghavendra      | [d25_araghave_huffman](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d25_araghave_huffman)         |
| 26        | Trainable Perceptron                 | Christopher Stange      | [d26_cjstange_perceptron](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d26_cjstange_perceptron)   |
| 27        | Floating Point Unit                  | Sri Lakshmi Vemulapalli | [d27_svemulap_fpu](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d27_svemulap_fpu)                 |
| 28        | Microcoded CPU                       | Ganesh Venkatachalam    | [d28_gvenkata_ucpu](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d28_gvenkata_ucpu)               |
| 29        | Intel 8008-based CPU                 | Brendan Wilhelm         | [d29_bwilhelm_i8008](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d29_bwilhelm_i8008)             |
| 30        | Tiny FPGA                            | Yu-Ching Wu             | [d30_yuchingw_fpga](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d30_yuchingw_fpga)               |
|           |                                      |                         |                                                                                                                       |
| 31        | Linear Feedback Shift Register       | Mihir Dhamankar         | [d31_mdhamank_lfsr](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d31_mdhamank_lfsr)               |
| 32        | 4-bit CPU                            | Noah Gaertner           | [d32_ngaertne_cpu](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d32_ngaertne_cpu)                 |
| 33        | Adder Architecture in Wokwi          | Michael Gee             | [d33_mgee3_adder](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d33_mgee3_adder)                   |
| 34        | Collatz Sequence Computer            | Harrison Grodin         | [d34_hgrodin_collatz](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d34_hgrodin_collatz)           |
| 35        | Magnitude Comparator                 | Caroline Kasuba         | [d35_ckasuba_comparator](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d35_ckasuba_comparator)     |
| 36        | Floating Point Multiplier            | Joseph Li               | [d36_jxli_fpmul](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d36_jxli_fpmul)                     |
| 37        | Calculator Chip                      | Sophia Li               | [d37_sophiali_calculator](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d37_sophiali_calculator)   |
| 38        | PWM Signal Generator                 | Jason Lu                | [d38_jxlu_pwm](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d38_jxlu_pwm)                         |
| 39        | Hex to Seven-Segment                 | Kachi Onyeador          | [d39_oonyeado_sevenseg](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d39_oonyeado_sevenseg)       |
| 40        | Clock Domain Crossing FIFO           | Jon Recta               | [d40_jrecta_asyncfifo](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d40_jrecta_asyncfifo)         |
| 41        | "Corral" Game                        | Michael Stroucken       | [d41_stroucki_corralgame](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d41_stroucki_corralgame)   |
| 42        | Hex to Seven-Segment                 | Samuel Sun              | [d42_qilins_sevenseg](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d42_qilins_sevenseg)           |
| 43        | Counter                              | Mason Xiao              | [d43_mmx_counter](https://github.com/asinghani/18224-s23-tapeout/tree/main/designs/d43_mmx_counter)                   |

The tools used to merge and verify the designs with the multiplexer, as well as the resultant GDS files, can be found on GitHub: [Tools/Designs Repo](https://github.com/asinghani/18224-s23-tapeout) / [Integration/GDS Repo](https://github.com/asinghani/18224-tapeout-s23-caravel)


## Course Lectures

_Author's Note: Most of these lectures were given in a highly-interactive fashion (with lots of whiteboarding and live demos) so some of these slides are fairly sparse (with the notable exception of lecture 8). However, we hope that the slides will be useful as an outline and a starting point for further study. Definitely be sure to check out the demos and resources as well!_


### Lecture 1: Background & Overview of Chip Design

**Lecture Slides:** [lec01.pdf](slides/lec01.pdf)

**Summary:**
- Introduction to the course structure
- Why is chip design and computer architecture still growing and innovating?
- What are FPGAs and ASICs, and what are they used for?
- What are the different software tools needed to design chips?

**Resources:**
- [NandGame (digital logic from first principles)](https://nandgame.com/)
- [NandLand Verilog Tutorials](https://nandland.com/learn-verilog/)
- [NandLand FPGA 101](https://nandland.com/fpga-101/)
- [HDLBits (good review if your Verilog is rusty)](https://hdlbits.01xz.net/wiki/Main_Page)
- [_Digital Design and Computer Architecture_ by Harris & Harris](https://www.amazon.com/Digital-Design-Computer-Architecture-Harris/dp/0123944244)


### Lecture 2: Digital Logic Synthesis & Yosys

**Lecture Slides:** [lec02.pdf](slides/lec02.pdf)

**Summary:**
- Necessity of logic synthesis
- FPGA vs ASIC design flows
- Levels of abstraction in digital logic design
- Yosys synthesis and optimization passes (see "Synthesis Demos")

**Demo:** [yosys-tutorial.md](yosys-tutorial/yosys-tutorial.md)

**Resources:**
- [Yosys manual](https://yosyshq.readthedocs.io/projects/yosys/en/latest/)
- [Interactive design investigation](https://yosyshq.readthedocs.io/projects/yosys/en/latest/appendix/APPNOTE_011_Design_Investigation.html)
- [SKY130 standard cell library](https://diychip.org/sky130/sky130_fd_sc_hd/cells/)
- [Quine-McCluskey logic-optimization algorithm](https://en.wikipedia.org/wiki/Quine%E2%80%93McCluskey_algorithm)


### Lecture 3: Intro to ASIC Tapeout

**Lecture Slides:** [lec03.pdf](slides/lec03.pdf)

**Summary:**
- Why open source chips are important?
- Security implications of a fully-auditable chip
- History of open source tapeouts
- What is TinyTapeout and how does it work?
- TinyTapeout project ideas

**Resources:**
- [SkyWater PDK Release Talk (webinar)](https://www.youtube.com/watch?v=EczW2IWdnOM)
- ["45 Chips in 30 Days" (webinar)](https://www.youtube.com/watch?v=qlBzE27at6M)
- [Sam Zeloof's Garage Fab](http://sam.zeloof.xyz/)
- [TinyTapeout (bringing tapeouts to the masses)](https://tinytapeout.com/)
- [April 2023 TinyTapeout Submissions](https://tinytapeout.com/runs/tt03/#all-projects)


### Lecture 4: FPGAs & PnR Flows

**Lecture Slides:** [lec04.pdf](slides/lec04.pdf)

**Summary:**
- FPGA Internals (CLBs/PLBs, Routing)
- How to design for FPGAs
- FPGA memory hierarchy and DSP blocks
- How to use hard IP in synthesis
- FPGA place-and-route algorithms

Resources:
- [iCEBreaker FPGA Workshop](https://github.com/icebreaker-fpga/icebreaker-workshop)
- [NandLand FPGA 101](https://nandland.com/fpga-101/)
- [NextPNR Paper](https://arxiv.org/pdf/1903.10407.pdf)
- [ACM FPGA Conference Proceedings](https://www.isfpga.org/past/fpga2020/program.html)
- [ULX3S FPGA Board](https://www.crowdsupply.com/radiona/ulx3s)


### Lecture 5: Simulation & Testbenching

**Lecture Slides:** [lec05.pdf](slides/lec05.pdf)

**Summary:**
- Verilog vs SystemVerilog vs VHDL
- Why simulation is important
- Software-hardware cosimulation using Verilator and CocoTB
- How to structure a testbench

**Demo:** [simulation-demos](simulation-demos/)

**Resources:**
- [SV2V SystemVerilog Transpiler](https://github.com/zachjs/sv2v)
- [Verilator C++ Testbench Tutorial](https://itsembedded.com/dhd/verilator_1/)
- [SystemVerilog / UVM in Verilator](https://antmicro.com/blog/2023/01/open-source-systemverilog-uvm-support-in-verilator/)
- [CocoTB Quickstart](https://docs.cocotb.org/en/stable/quickstart.html)
- [GTKWave Waveform Viewer](https://gtkwave.sourceforge.net/)
- [PyVCD Python Waveform Parser](https://pyvcd.readthedocs.io/en/latest/)


### Lecture 6: ASIC Layout Flows

**Lecture Slides:** [lec06.pdf](slides/lec06.pdf)

**Summary:**
- SKY130 process node
- How ASICs are designed from standard cells
- Design representation formats
- Steps in the RTL-to-GDS ASIC design flow (+ interactive exercise) 

**Resources:**
- [OpenLane Talk (webinar)](https://www.youtube.com/watch?v=Vhyv0eq_mLU)
- [OpenRAM Talk (webinar)](https://www.youtube.com/watch?v=9Lw83kFtnc4)
- ["45 Chips in 30 Days" (webinar)](https://www.youtube.com/watch?v=qlBzE27at6M)
- [Intro to Timing Analysis](https://www.youtube.com/watch?v=2V41i4xVTZ8)
- [SiliWiz (online analog design tool)](https://tinytapeout.com/siliwiz/)
- [OpenLane Jupyter Demo](https://github.com/chipsalliance/silicon-notebooks/blob/main/xls-workshop-openlane.ipynb)


### Lecture 7: Altenative HDLs

**Lecture Slides:** [lec07.pdf](slides/lec07.pdf)

**Summary:**
- Taxonomy of hardware description languages
- Alternative HDL languages
- Demos of Amaranth and Chisel3 (+ interactive exercise) 
- Automated system-on-chip generation tools

**Resources:**
- [Chisel (Scala-based HDL) Interactive Tutorial](https://mybinder.org/v2/gh/freechipsproject/chisel-bootcamp/master)
- [Amaranth (Python-based HDL) Tutorial](https://github.com/RobertBaruch/amaranth-tutorial/blob/main/3_modules.md)
- [Amaranth (Python-based HDL) Advanced Tutorial](https://vivonomicon.com/2020/04/14/learning-fpga-design-with-nmigen/)
- [HardCaml (OCaml-based HDL)](https://github.com/janestreet/hardcaml)
- [PipelineC (auto-pipelined HDL)](https://github.com/JulianKemmerer/PipelineC)
- [Google XLS (HLS toolchain)](https://google.github.io/xls/)
- [Merlin Compiler (HLS toolchain)](https://github.com/falconcomputing/merlin-compiler)
- [MATLAB HDL Coder (Matlab-based hardware generator)](https://www.mathworks.com/products/hdl-coder.html)
- [LiteX SoC Generator](https://github.com/enjoy-digital/litex/wiki/Tutorials-Resources)


### Lecture 8: Hardware Security

**Lecture Slides:** [lec08.pdf](slides/lec08.pdf)

**Summary:**
- Unique challenges associated with hardware security
- Why are systems insecure?
- Side channel attacks and power-analysis
- Hidden hardware trojans in chips
- Shared tenancy attacks on cloud FPGAs

**Resources:**
- [_Reflections on Trusting Trust_](https://www.cs.cmu.edu/~rdriley/487/papers/Thompson_1984_ReflectionsonTrustingTrust.pdf)
- [Joe Grand's Hardware Exploitation Series](https://www.youtube.com/playlist?list=PLsyTdiI7kVn8brLk9n4D7CDazCuYnGucQ)
- [NewAE ChipWhisperer](https://www.newae.com/chipwhisperer)
- [_Hardware Hacking Handbook_](https://www.oreilly.com/library/view/the-hardware-hacking/9781098129835/)
- [Undetectable Hardware Trojans Paper](https://www.iacr.org/archive/ches2013/80860203/80860203.pdf)
- [Trustworthy Self-Replicating RISC-V on FPGA](http://www.contrib.andrew.cmu.edu/~somlo/BTCP/)


### Lecture 9: Misc Topics and Next Steps (short lecture)

**Lecture Slides:** [lec09.pdf](slides/lec09.pdf)

**Summary:**
- Mutation Cover for testbench coverage (+ interactive exercise) 
- FPGA board recommendations for future projects
- More project ideas using FPGAs
- Getting involved with the online community

**Resources**
- [Mutation Cover with Yosys](https://yosyshq.readthedocs.io/projects/mcy/en/latest/)
- [ULX3S FPGA Board](https://www.crowdsupply.com/radiona/ulx3s)
- [iCEBreaker FPGA Board](https://1bitsquared.com/collections/embedded-hardware/products/icebreaker)
- [Open Source Silicon Slack](https://open-source-silicon.dev/)
- [TinyTapeout Community](https://discord.gg/qZHPrPsmt6)


### Lecture 10: Post-Tapeout Bringup & Research Landscape

**Lecture Slides:** [lec10.pdf](slides/lec10.pdf)

**Summary:**
- Chip packaging after manufacturing
- Package assembly and inspection
- JTAG + I/O boundary scan
- Scan chain insertion of internal registers
- Research literature and future directions of this space

**Resources**
- [Open Circuits Book](https://opencircuitsbook.com/)
- [Intro to JTAG and Boundry Scan](https://www.youtube.com/watch?v=TlWlLeC5BUs)
- [_Fault, an Open Source DFT Toolchain_](https://woset-workshop.github.io/PDFs/2019/a13.pdf)
- [WOSET Workshop Proceedings](https://woset-workshop.github.io/)


## Next Steps

If you found this content interesting, check out the linked resources above, get your hands on an FPGA development board, and submit your own project to the next [Tiny Tapeout](https://tinytapeout.com/)!

## Contact

If you have any questions or suggestions, please reach out at: anish [-at-] anishsinghani [-dot-] com

Copyright 2023 Anish Singhani All Rights Reserved
