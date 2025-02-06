/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if(head == null) return null;

        ListNode curr = head;

        while(curr != null && curr.next != null){
            if(curr.val == curr.next.val){
                 curr.next = curr.next.next;
            } else {
                curr = curr.next;
            }
        }
    return head;

     }
}


//O algoritmo usa um único ponteiro (curr) para percorrer a lista ligada e remover os nós duplicados.
// Ele começa no primeiro nó (head) e verifica se o próximo nó tem o mesmo valor. Se tiver, ele simplesmente pula esse nó ajustando a referência curr.next para curr.next.next, removendo a duplicata da lista.
// Caso contrário, avança para o próximo nó.
//A complexidade temporal é O(n), pois percorremos a lista uma única vez, e a complexidade espacial é O(1), pois não usamos memória extra além das variáveis já existentes.