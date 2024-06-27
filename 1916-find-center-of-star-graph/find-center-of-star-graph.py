class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        frequency = {}
        # Traverse each edge and update the frequency of nodes
        for edge in edges:
            u, v = edge
            if u in frequency:
                frequency[u] += 1
            else:
                frequency[u] = 1
            
            if v in frequency:
                frequency[v] += 1
            else:
                frequency[v] = 1

        # Find the node with the maximum frequency (center of the tree)
        max_freq_node = None
        max_freq = -1

        for node, freq in frequency.items():
            if freq > max_freq:
                max_freq = freq
                max_freq_node = node

        return max_freq_node

        