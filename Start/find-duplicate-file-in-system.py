class Solution:
    def findDuplicate(self, path):
        hash_content = {}
        to_return = []
        for pa in path:
            f_path, *files = pa.split()
            for f in files:
                file_name, content = f.split("(")
                if content[:-1] in hash_content:
                    hash_content[content[:-1]].append(f_path + "/"+file_name)
                else:
                    hash_content[content[:-1]] = [f_path + "/"+file_name]        
        for content, paths in hash_content.items(): 
            if len(paths) > 1:
                to_return.append(paths)
        return to_return