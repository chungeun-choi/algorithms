package deque

type Deque struct {
	position int
	array    []int
	start    int
	end      int
}

func (d *Deque) PushFront(value int) error {
	pos := d.start - 1
	d.array[pos] = value

	d.start = pos

	return nil
}

func (d *Deque) PushBack(value int) error {
	pos := d.end + 1
	d.array[pos] = value
	d.start = pos

	return nil
}

func (d *Deque) PopFront() int {
	result := d.array[d.start]
	pos := d.start + 1
	d.start = pos
	return result
}

func (d *Deque) PopBack() int {
	result := d.array[d.end]
	pos := d.end - 1
	d.end = pos
	return result
}
