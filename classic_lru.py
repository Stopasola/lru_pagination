from collections import deque


def start(reference_string, frame_size):
    print("====> LRU")
    frame_stack = deque(maxlen=frame_size)
    page_fault = 0
    frame_hits = 0

    for page in reference_string:
        if len(frame_stack) < frame_size:
            frame_stack.appendleft(page)
            page_fault += 1
        else:
            if page not in frame_stack:
                page_fault += 1
                frame_stack.pop()
                frame_stack.appendleft(page)
            else:
                frame_hits += 1
                frame_stack.remove(page)
                frame_stack.appendleft(page)

    print('page_fault', page_fault)
    print('frame_hits', frame_hits)
