/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
    if (list1 == nullptr) return list2;
    if (list2 == nullptr) return list1;

    ListNode *tracker1 = list1;
    ListNode *tracker2 = list2;

    ListNode dummy(0);       // Dummy node to mark strting point of merged linklist
    ListNode *mergeTrail = &dummy; // Tracker merged node [privouse nodes are merged]

    while (tracker1 != nullptr && tracker2 != nullptr) {
        if (tracker1->val <= tracker2->val) {
            mergeTrail->next = tracker1;
            tracker1 = tracker1->next;
        } else {
            mergeTrail->next = tracker2;
            tracker2 = tracker2->next;
        }
        mergeTrail = mergeTrail->next;
    }

    // Append the remaining nodes of tracker1 or tracker2.
    mergeTrail->next = (tracker1 != nullptr) ? tracker1 : tracker2;

    return dummy.next;
    }
};