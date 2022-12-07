from collections import deque

class Folder:
    def __init__(self, name, children=None, parent=None):
        self.parent = parent
        self.children = children if children else []
        self.name = name

    @property
    def size(self):
        return sum((child.size for child in self.children))

    @property
    def path(self):
        return "/" if self.parent is None else self.parent.path + self.name + "/"

    @property
    def contents(self):
        return (child.name for child in self.children)


class File:
    def __init__(self, name, parent=None, size=None):
        self.parent = parent
        self.size = size
        self.name = name

    @property
    def path(self):
        return self.parent.path + self.name

    @property
    def children(self):
        return []


with open("input_day7.txt") as file:
    lines = [line.replace("\n", "") for line in file.readlines()]

root = None
curr_folder = None
for line in lines:
    parts = line.split(" ")
    if parts[0] == "$":
        if parts[1] == "cd":
            if parts[2] == "/":
                root = Folder("/")
                curr_folder = root
            elif parts[2] == "..":
                curr_folder = curr_folder.parent
            else:
                curr_folder = next((child for child in curr_folder.children if child.name == parts[2]))
        elif parts[1] == "ls":
            pass  # I do not think we need to do anything here
    elif parts[0] == "dir":
        curr_folder.children.append(Folder(name=parts[1], parent=curr_folder))
    else:
        curr_folder.children.append(File(name=parts[1], size=int(parts[0]), parent=curr_folder))

total_space = 70000000
needed_free_space = 30000000
current_free_space = total_space - root.size
minimum_space_to_delete = needed_free_space - current_free_space

candidate_folders = []

to_visit = deque()
to_visit.append(root)
while len(to_visit) > 0:
    curr_node = to_visit.pop()
    to_visit.extend(curr_node.children)
    if type(curr_node) == type(Folder("dummy")) and curr_node.size >= minimum_space_to_delete:
        candidate_folders.append(curr_node)

# Find the smallest in the list and extract the size
print(sorted(candidate_folders, key=lambda folder: folder.size)[0].size)