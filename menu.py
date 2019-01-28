city_arch = {
    'head':{
        '灯光效果':['背景灯颜色', '背景灯强度', '计时灯强度'],
        'LCD效果':['对比度', '背景灯'],
        '时间调整':['时区调整', '时分秒调整']
    }
}

counter = 0
node_list = []
pointer = 1
cursor = 1
class Node():

    def __init__(self, description):
        global counter
        counter += 1
        self.node_id = counter
        self.next_nodes = []
        self.description = description
        self.previous_node = 0
        if self.description == 'head':
            self.previous_node = 0

    def __str__(self):
        return self.description

    def __repr__(self):
        return self.description

def operation_list_parser(city_arch, previous_node=None):
    for obj_name, obj_content in city_arch.items():
        if isinstance(obj_content, list):
            parent_node = Node(obj_name)
            previous_node.next_nodes.append(parent_node)
            parent_node.previous_node = previous_node
            node_list.append(parent_node)
            for end_point in obj_content:
                next_node = Node(end_point)
                next_node.previous_node = parent_node
                parent_node.next_nodes.append(next_node)
                node_list.append(next_node)
        else:
            parent_node = Node(obj_name)
            node_list.append(parent_node)
            operation_list_parser(obj_content, parent_node)


operation_list_parser(city_arch)

node_list = node_list[1:]

def list_render(content_list, cursor):
    buffer_list = []
    # location = len(content_list) % cursor
    for line_num in range(len(content_list)):
        if line_num == cursor - 1:
            buffer_list.append('>')
        else:
            buffer_list.append(' ')

    return zip(buffer_list, content_list)


while True:
    display_list = [node for node in node_list if node.previous_node.node_id == pointer]
    for line in list_render(display_list, cursor):
        print(line[0] + str(line[1]))

    selection = input('')
    if selection == '1':
        if cursor > 1:
            cursor -= 1
    elif selection == '2':
        if cursor < len(display_list):
            cursor += 1
    elif selection == '3':
        if pointer != 1:
            pointer = display_list[0].previous_node.previous_node.node_id
        print(pointer)
    elif selection == '4':
        if display_list[cursor-1].next_nodes:
            pointer = display_list[cursor-1].node_id
            cursor = 1
        print(pointer)
    else:
        pass