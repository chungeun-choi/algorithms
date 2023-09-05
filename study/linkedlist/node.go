package linkedlist

type Node struct {
	prev, next *Node
	value      int
}

func NewNode(value int) *Node {
	return &Node{
		value: value,
	}
}
