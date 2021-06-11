from circular_linked_list import CircularList


def start(reference_string, frame_size):
    print("====> LRU Second Chance")
    frame_list = CircularList(frame_size)
    page_fault = 0
    frame_hits = 0

    for page in reference_string:
        if not frame_list.find(page):
            page_fault += 1
            if frame_list.size() < frame_size:
                frame_list.insert(page)
            else:
                while True:
                    idx_pg_victim = frame_list.page_victim
                    page_victim = frame_list.index(idx_pg_victim)
                    if page_victim.reference_bit == 0:
                        frame_list.shift_page_victim()
                        break
                    page_victim.reference_bit = 0
                    frame_list.shift_page_victim()
                frame_list.remove()
                frame_list.insert(page)
        else:
            frame_hits += 1
            if frame_list.size() == frame_size:
                frame_list.set_page_bit(page)
                frame_list.shift_page_victim()

    print('page_fault', page_fault)
    print('frame_hits', frame_hits)
