# Queue

- 정의
    
    먼저 들어간 요소가 먼저 나오는 형태 ex) 공항 줄 또는 음식점 줄
    
    FIFO (First In First Out)
    
    ![Untitled](./queue.png)
    

- 정의
    
    1) 원소의 추가가 O(1)
    
    2) 원소의 제거가 O(1)
    
    3) 제일 앞/뒤의 원소 확인이 O(1)
    
    4) 제일 앞/뒤가 아닌 나머지 원소들의 확인/변경이 원칙적으로는 불가능


- 개선 사항
    
    기존 구현에서는 Pop 함수가 추가 될 때마다 list를 슬라이싱해서 새롭게 할당하도록 구현하였음 
    Push 함수의 경우 append 함수를 통해 추가해지는 구조 
    
    ```python
    func (q *Queue) Push(value int) {
    	
    	q.list = append(q.list, value)
    	fmt.Printf("Queue size: %d \n",len(q.list))
    }
    
    func (q *Queue) Pop()  int {
    	
    	result := q.list[0]
    	q.list = q.list[1:]
    	fmt.Printf("Queue size: %d \n",len(q.list))
    	return result
    }
    ```
    

Queue의 크기를 고정 시키고 원형 형태의 배열 형태로 변경

```python
func (q *ImproveQueue) Push(value int) {

	if q.tail > len(q.list)-1 {
		q.tail =0 
	}
	
	q.list[q.tail] = value 
	q.tail++
	fmt.Printf("Queue size: %d \n",len(q.list))
}

func (q *ImproveQueue) Pop()  int {
	
	if q.header > len(q.list) -1 {
		q.header = 0 
	}

	result := q.list[q.header]
	q.header++

	return result
}
```