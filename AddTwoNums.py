class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    l1_reversed = ""
    l2_reversed = ""

    current_node_l1 = l1
    current_node_l2 = l2

    while current_node_l1.next:
        l1_reversed += str(current_node_l1.val)
        current_node_l1 = current_node_l1.next
    while current_node_l2.next:
        l2_reversed += str(current_node_l2.val)
        current_node_l2 = current_node_l2.next

    l1_reversed += str(current_node_l1.val)
    l2_reversed += str(current_node_l2.val)

    l1_int = int(l1_reversed[::-1])
    l2_int = int(l2_reversed[::-1])
    result_str = str(l1_int + l2_int)


    dummy_head = ListNode(0)
    current = dummy_head
    for i in reversed(result_str):
        current.next = ListNode(int(i))
        current = current.next

    return dummy_head.next


        




    

    # current nodes are now the last nodes in the linked list
