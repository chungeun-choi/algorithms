package queue

type QueueInterface interface {
	Push(value int)
	Pop()int
	GetAllObject()
}