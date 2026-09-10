/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* getIntersectionNode(ListNode* headA, ListNode* headB) {
        int l1 = 0;
        int l2 = 0;
        ListNode* p1 = headA;
        ListNode* p2 = headB;
        while(p1){
            p1 = p1->next;
            l1 ++;
        }
        while(p2){
            p2 = p2->next;
            l2 ++;
        }
        p1 = headA;
        p2 = headB;

        if (l2 > l1){
            int diff = l2 -l1;
            while(diff > 0){
                p2 = p2->next;
                diff--;
            }
        }else if (l2 < l1){
            int diff = l1 -l2;
            while(diff > 0){
                p1 = p1->next;
                diff --;
            } 
        }

        while(p1 and p2){
            if (p1 == p2){
                return p1;
            }
            p1 = p1->next;
            p2 = p2->next;
        }
        return nullptr;
    }
};