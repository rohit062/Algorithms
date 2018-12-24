class binaryTreeNode {
  constructor(value,left = null ,right = null){
    this.value = value;
    this.left = left;
    this.right = right;
  }

  setRightChild(rightChild){
    this.right = rightChild;
  }

  setLightChild(LeftChild){
    this.left = LeftChild;
  }

  getRightChild(){
    return this.right;
  }

  getLightChild(){
    return this.left;
  }
}

let root = new binaryTreeNode(5);
let left = new binaryTreeNode(6);
let right = new binaryTreeNode(7);

root.setLightChild(left);
root.setRightChild(right);


console.log(root);