def reverse(llist):
    # Write your code here
    prev = None
    cur = llist

    while cur != None:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    head = prev
    return head
