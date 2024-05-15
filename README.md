# linkedList

## Class documentaion:  
### How to use it ?  
1- create an instance object of class 
>> my_linked_list = LinkedList()  
>> my_linked_list **.** methodName()  

#### use the following method :
- **append(value)** : append/add the 'value' item to the last position in the list
- **prepend(value)** : prepend/add the 'value' item to the first position in the list
- **len()** : return the length of the list
- **delete(value)** : delete the first occurunce of the 'value' item from the list 
- **my_linked_list[index]** : return the value at 'index' position
- **replacebyindex** : replace the value at 'index' position with the 'substitute' value
- **last()**: return the last item in the list
- **_ _str__** : return string representaion of the list content

## exapmle:

    linked_list = LinkedList()
    # appending:
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    print(linked_list)
    # output: 1 -> 2 -> 3 -> 4 -> 5 -> None

    # prepending:
    linked_list.prepend(0)
    print(linked_list)
    # output: 0 -> 1 -> 2 -> 3 -> 4 -> 5 -> None

    #deleting:
    linked_list.delete(5)
    print(linked_list)
    # output: 0 -> 1 -> 2 -> 3 -> 4 -> None

    # list length:
    print(len(linked_list))
    # output: 5

    # last item list:
    print(linked_list.last())
    # output: 4

    # replacing item using index:
    linked_list.replacebyindex(100,4)
    print(linked_list)
    # output: 0 -> 1 -> 2 -> 3 -> 100 -> None

    # getItem using [index]
    print(linked_list[4])
    # output: 100