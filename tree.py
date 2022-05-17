# tree.py
# by Alejandro Pascual San Roman
# Student ID: 201255350
#
# Tree data structure
#
# Each node takes the form:
# [parent_node, list_of_child_nodes, [action_path, state, cost, heuristic_value]]

print("Loading tree.py")


# Creates new node with empty initial values
def new_node():
    return [0, [], [[], [], 0, 0]]


# Adds children nodes to current node in node[1] as a list
def node_set_children(node, children):
    for child in children:
        node_add_child(node, child)
    return node


# Adds new child node to node[1]
def node_add_child(node, child):
    node[1].append(child)
    child[0] = node
    return node


# Returns list of children nodes for a given node
def node_get_children(node):
    return node[1]


# Establishes parent node of a given node (adding it to node[0])
def node_set_parent(node, parent):
    node[0] = parent
    parent[1].append(node)
    return node


# Returns parent node of a given node
def node_get_parent(node):
    return node[0]


# Establishes action path to reach a specific node
def node_set_path(node, path):
    node[2][0] = path
    return node


# Returns action path of a given node
def node_get_path(node):
    return node[2][0]


# Establishes state of a given node
def node_set_state(node, state):
    node[2][1] = state
    return node


# Returns state of a given node
def node_get_state(node):
    return node[2][1]


# Establishes cost of reaching a given node
def node_set_cost(node, cost):
    node[2][2] = cost
    return node


# Returns cost of reaching a given node
def node_get_cost(node):
    return node[2][2]


# Establishes heuristic from current node to goal state
def node_set_heuristic(node, heuristic):
    node[2][3] = heuristic
    return node


# Returns result of heuristic for a given node
def node_get_heuristic(node):
    return node[2][3]


# Returns length of action path
def node_get_path_length(node):
    return len(node_get_path(node))


# Prints every item of a given list (for testing and de-bugging)
def showlist(list):
    for item in list:
        print(item)


# Tests if current node contains the goal state
def node_satisfies_goal(node, goal):
    if goal in node_get_state(node):
        return True
    return False


# Checks if state of current node occurs in any ancestors
def node_state_occurs_in_ancestor(node):
    state = node_get_state(node)
    parent = node_get_parent(node)
    return node_state_occurs_in_upward_path(parent, state)


# Compares state of given node and given state. If not equal, compares parent node until node with equal state is found
def node_state_occurs_in_upward_path(node, state):
    while True:
        if node == 0:
            return False
        if node_get_state(node) == state:
            return True
        node = node_get_parent(node)


# Returns depth of current node
def node_get_depth(node):
    depth = 0
    while True:
        if node == 0:
            return depth
        node = node_get_parent(node)
        depth = depth + 1
