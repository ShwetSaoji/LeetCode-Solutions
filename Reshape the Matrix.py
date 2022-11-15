class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = [item for sublist in mat for item in sublist]
        if r * c != len(flat): return mat    
        output = [flat[(row *c) :c * (row +1)] for row in range(r)]
        return output  
