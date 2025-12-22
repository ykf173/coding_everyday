# 合并两个有序链表

class LinkList:
    def __init__(self, val):
        self.data = val
        self.next = None

def merge_list(head1, head2):
    pro_h1, pro_h2 = head1, head2
    if head1.next and head2.next:
        cur_h1 = head1.next
        cur_h2 = head2.next
    elif head2:
        return head1
    else:
        return head2

    while head1.next or head2.next:
        if cur_h1.data > cur_h2.data:
            cur_h2 = pro_h1.next
            
            cur_h2 = cur_h2.next
            pro_h2 = pro_h2.next

            pro_h2.next = pro_h1.next

            pro_h2 = cur_h2

        else:
            cur_h1 = cur_h1.next
            pro_h1 = pro_h1.next

    if not head2.next:
        cur_h1 = head2.next

    return head1

