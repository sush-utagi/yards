def addTwoNumbers(l1, l2):

    l1_reversed = str(l1.val)
    l2_reversed = str(l2.val)

    current_node_l1 = l1
    current_node_l2 = l2

    while current_node_l1.next:
        l1_reversed += str(current_node_l1.val)
        current_node_l1 = current_node_l1.next
    while current_node_l2.next:
        l2_reversed += str(current_node_l2.val)
        current_node_l2 = current_node_l2.next

    

    # current nodes are now the last nodes in the linked list
