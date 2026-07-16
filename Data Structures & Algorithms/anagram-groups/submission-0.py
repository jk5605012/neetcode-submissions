class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_list = []
        res = []
        for i in strs:
            char_count = Counter(list(i))
            hash_list.append(dict(char_count))
        while len(strs) > 0:
            cell = []
            cell.append(strs.pop(0))
            hash_item = hash_list.pop(0)
            same_count = []
            print(f'hash_item: {hash_item}')
            for i in range(len(hash_list)):
                if hash_list[i] == hash_item:
                    cell.append(strs[i])
                    same_count.append([hash_list[i], strs[i]])
            for i in same_count:
                hash_list.remove(i[0])
                strs.remove(i[1])

            res.append(cell)
        return res