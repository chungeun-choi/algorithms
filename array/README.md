# 배열 (Array)

## **바킹독 - 알고리즘 - 배열**

### 배열이란?

메모리 상에 원소를 *연속* 하게 배치한 자료구조

- > 자료구조의 배열은 길이가 자유롭다라고 설정

### 성질?

- O(1) K번째 원소를 확인/ 값 변경 가능
- 추가적으로 소모되는 메모리의 양이 거의 없다 (No overhead)
- Cache hit rate가 높음 (지역 참조성의 원리에 의해)
- 메모리 상에 연속한 구간을 잡아야해서 할당에 제약이 걸림 -> 단점….

### 배열을 사용하는 때?

- 입력을 담아두고 싶을때
- 연속되는 데이터를 빠르게 접근하고 싶을 때

### 배열에서의 데이터 활용 예제 시의 시간 복잡도

- 특정 순서의 데이터를 조회(수정) -> O(1)
- 원소를 끝에 추가 -> O(1)
- 마지막 원소 제거 -> O(1)
- **임의의 위치에 원소를 추가 -> O(n)**
    
    특정 주소를 기준으로 뒤의 시간을 밀어야하기 때문에
    
    ![Untitled](array/Untitled.png)
    
- **임의의 위치에 원소를 제거 -> O(n)**
    
    특정 주소를 기준으로 뒤의 시간을 당겨야하기 때문에
    
    ![Untitled](array/Untitled1.png)
    

### TIP

- 삽입하고자하는 데이터의 인덱스를 처음부터 체크하기보다는 배열의 뒤에서부터 시작해서 데이터를 당기도록 하자(삭제하고자 할때는 입력받은 인덱스 기준부터 옮기면 효율적임)

### 구현

- 최초 구현 [[link]](./array.go)
- TIP을 활용한 개선 구현 [[link]](./improvementArray.go)

### GO 구현시 slicing 기법을 통해 구현하는 법

- 삭제
    
    ```go
    slice = append(slice[:idx], slice[idx+1:]...)
    ```


### 코딩테스트 문제

백준 10808

- 기존 해결
    
    기존 문제 풀이 시 아스키 코드까지는 생각을 하여 반복을 하게 끔 하였으나  count 함수를 씀으로 인해서 큰 의미가 없는 풀이가 되어버렸음 
    

```go
const startAlpha = 97

func Solution(s string) string {
	//returnArray := make([]int, 26)
	var result string 
	for cnt := startAlpha ; cnt <= startAlpha + 26 ;cnt ++ {
		result += fmt.Sprintf("%d",strings.Count(s,string(cnt)))
	}
	result = strings.TrimSpace(result)
	return result
} 
```

- 개선 해결
    
    알파벳 소문자는 97부터 26개로 연속적으로 이루어져있음 이에 따라 0~25 까지로 표현이 가능함 
    
    1) 크기 26의 배열을 선언
    
    2) 입력되는 string 값을 ‘a’ 아스키 코드인 97을 뺌으로서 해당 배열에 1을 추가하는 식의 연산 
    
    → 알파벳의 갯수만큼 연산하는 것이 아닌 입력되는 string의 크기만큼만 연산함에 따라 효율적인 연산
    

```go
func ImporoveSolution(s string) (result string) {
	count := make([]int,26)

	for _,c := range(s){
		char := rune(c) - rune('a')
		count[char]++
	}

	for _, i := range count {
		result += fmt.Sprintf("%d",i)
	}

	result = strings.TrimSpace(result)

	return
}
```