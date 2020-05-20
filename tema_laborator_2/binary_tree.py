from BinaryTree import BinaryTree

operations = []
operations_count = 0

with open('abce.in') as f:
    operations_count = int(f.readline())
    for index, line in enumerate(f.readlines()):
        operation_number, *operation_params = [int(number)  for number in line.split()]
        operations.append({'type': operation_number,  'params': operation_params})

tree = BinaryTree()

with open('abce.out', 'w') as g:
    for operation in operations:

        if operation['type'] == 1:
            tree.insert(*operation['params'])

        elif operation['type'] == 2:
            tree.delete(*operation['params'])

        elif operation['type'] == 3:
            current = tree.find(tree.root, *operation['params'])
            g.write('{}\n'.format('1' if current else '0'))

        elif operation['type'] == 4:
            g.write('{}\n'.format(tree.predecessor(*operation['params'])))

        elif operation['type'] == 5:
            g.write('{}\n'.format(tree.successor(*operation['params'])))

        elif operation['type'] == 6:
            response= tree.sorted(tree.root, *operation['params'])
            if response:
                g.write('{}\n'.format(' '.join(str(res) for res in response)))
        else:
            g.write('Operation not found\n')