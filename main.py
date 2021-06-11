import math
import constant
import time
from datetime import datetime
import classic_lru
import lru_second_chance


def open_trace(folder, trace):
    trace_lst = list()
    file = open(folder + trace + ".txt", "r")
    for t in file:
        t = t.split()
        trace_lst.append((t[0], t[1]))
    return trace_lst


def displacement_bits(ps):
    if not (ps & (ps-1) == 0) and ps != 0:
        print("Must be power of 2")
    else:
        return int(math.log(ps, 2))


def page_number_size(displacement):
    return constant.ARCTCTURE_TRACE - displacement


def hex_to_bin(hex_trace):
    int_value = int(hex_trace, base=16)
    return (bin(int_value))[2:].zfill(32)


def build_reference_string(original_trace_lst, pg_num_size):
    reference_str = list()
    for trace in original_trace_lst:
        bin_trace = hex_to_bin(trace[0])
        page = (bin_trace[:pg_num_size])
        reference_str.append(page)
    return reference_str


def run_lru(reference_string, frame_size):
    lru_start_time = datetime.now()
    classic_lru.start(reference_string, frame_size)
    lru_total_time = datetime.now() - lru_start_time
    print('lru_total_time', lru_total_time.microseconds / 1000)


def run_lru_second_chance(reference_string, frame_size):
    lru_sc_start_time = datetime.now()
    lru_second_chance.start(reference_string, frame_size)
    lru_sc_total_time = datetime.now() - lru_sc_start_time
    print('lru_sc_total_time', lru_sc_total_time.microseconds / 1000)


folder_name = 'trace/'
trace_names = ['bigone.trace', 'bzip.trace', 'gcc.trace', 'sixpack.trace', 'swim.trace']
page_size = 4096  # input
frame_size = 5  # input

displacement = displacement_bits(page_size)
pnz = page_number_size(displacement)


for file in trace_names:
    trace_list = open_trace(folder_name, file)
    reference_string = build_reference_string(trace_list, pnz)
    print('==> ', file)

    run_lru(reference_string, frame_size)
    run_lru_second_chance(reference_string, frame_size)





