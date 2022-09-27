#include <stdio.h>

//Max-heapify: Exchange the parent with the largest (if exists) of its children
void max_heapify(int* A, int i, int heap_size){
	int l = 2 * i;
	int r = (2 * i) + 1;
	int largest = i;
	int aux;
	
	if(l <= heap_size && A[l] > A[i])
		largest = l;
	else
		largest = i;
	
	if (r <= heap_size && A[r] > A[largest])
		largest = r;
	
	if (largest != i){
		aux = A[i];
		A[i] = A[largest];
		A[largest] = aux;
		max_heapify(A, largest, heap_size);	
	}
}

//Build Max-Heap: Applies Max-Heapify on every parent-node, getting the largest one at the tree root
void build_max_heap(int* A, int size){
	int i;
	
	int upper = (int) (size)/2;
	
	for (i = upper; i >= 1; i--)
		max_heapify(A, i, size);
	
}


//Heapsort: Every time you get the largest node at the root, it's exchanged with the last leaf
//then the Max-Heapify is applied to get the second largets, which one is exchanged with the leaf before the last one
//until the smaller node is the tree root and the largest are in the leafs
void heapsort(int* A, int size){
	int i;
	int aux;
	int heap_size = size;
	
	build_max_heap(A, size);
	
	for(i = size; i >= 2; i--){
		aux = A[1];
		A[1] = A[i];
		A[i] = aux;
		heap_size = heap_size - 1;
		
		max_heapify(A, 1, heap_size);
	}
}

//Function to reverse the array
void reverse(int * A, int size){
	int B[size + 1];
	int i = 1;
	for (i = size; i>0; i--){
		B[i] = A[size - i + 1];
	}
	for (i = 1; i<=size; i++){
		A[i] = B[i];
	}
	
}


//Insert a new value at the tree and apply Build Max-Heap to hold the rule of Max-Heap-Tree
void insert(int* A, int e, int size){
	A[size] = e;
	
	if(size > 1)
		build_max_heap(A, size);
		
}

//Delete the root node which one is exchanged by the last leaf, then Build Max-Heap is applied
void delete_first(int* A, int* size){
	A[1] = A[*size];
	A[*size] = 0;
	*size = *size-1;
	build_max_heap(A, *size);	
}


///////*************THIS IS ONLY FOR TESTING***********/////////////
void main(){
	int A []= {0, 5, 12, 9, 2, 12, 11};
		
	int size = 6;
	reverse(A, size);
	int i;
	
	for (i = 1; i <= size; i++){
		printf("%d\n", A[i]);
	}
	
	
}



