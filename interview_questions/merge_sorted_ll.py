class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(lists):
    cur_a = lists[0]
    prev_a = None
    cur_b = lists[1]
    prev_b = None
    if cur_a.val < cur_b.val:
        while cur_a:
            if cur_b.val < cur_a.val:
                prev_b = cur_b
                cur_b = cur_b.next
                prev_b.next = cur_a

            elif cur_a.val < cur_b.val:
                prev_a = cur_a
                cur_a = cur_a.next
                prev_a.next = cur_b

        return lists[0]
    else:
        while cur_b:
            if cur_a.val < cur_b.val:
                prev_a = cur_a
                cur_a = cur_a.next
                prev_a.next = cur_b

            elif cur_b.val < cur_a.val:
                prev_b = cur_b
                cur_b = cur_b.next
                prev_b.next = cur_a

        return lists[1]


a = Node(2, Node(4, Node(6)))
b = Node(1, Node(3, Node(5)))
print(merge([a, b]))
# 123456
