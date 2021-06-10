from collections import deque


def start(reference_string, frame_size):
    print("LRU")
    print("reference_string", len(reference_string))
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
    print('sum reference_string', page_fault + frame_hits)


def test(reference_string, frame_size):
    capacity = frame_size
    processList = reference_string

    # List of current pages in Main Memory
    s = []
    pageFaults = 0
    page_hits = 0

    for i in processList:

        if i not in s:
            if (len(s) == capacity):
                s.remove(s[0])
                s.append(i)
            else:
                s.append(i)
            pageFaults += 1
        else:
            page_hits += 1
            s.remove(i)
            s.append(i)

    print("================================")
    print('pageFaults', pageFaults)
    print('page_hits', page_hits)
    print('sum reference_string', pageFaults + page_hits)
