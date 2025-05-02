from binary_search_tree import BST

def main():
    bst = BST()
    values = [15, 10, 20, 8, 12, 17, 25, 6, 11, 16, 27]
    
    for val in values:
        bst.insert(val)
    
    print("Tree (ordered traversal):", bst.inorder_traversal())
    
    # Task execution
    print("\nTask 1: The largest value in the tree:", bst.find_max())
    print("Task 2: Smallest value in the tree:", bst.find_min())
    print("Task 3: Sum of all values ​​in the tree:", bst.sum_values())

if __name__ == "__main__":
    main()
