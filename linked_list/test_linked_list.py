import pytest

from linked_list import LinkedList,Node


def test_append_method():
  my_linked_list = LinkedList()
  befor_appending = len(my_linked_list)
  my_linked_list.append(1)
  after_appending = len(my_linked_list)
  
  assert after_appending == befor_appending + 1
  
def test_delete_method():
  my_linked_list = LinkedList()
  my_linked_list.append(4)
  my_linked_list.append(4)
  befor_deleting = len(my_linked_list)
  
  my_linked_list.delete(4)
  after_deleting = len(my_linked_list)
  
  assert after_deleting == befor_deleting - 1
  
def test_getitem_method():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  
  assert my_linked_list[1] == 2

def test_len_method():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  
  
  assert len(my_linked_list) == 3

def test_replacebyindex_method():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(4)
  my_linked_list.replacebyindex(3,2)
  assert my_linked_list[2] == 3
  
def test_prepend_method():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  my_linked_list.prepend(0)
  assert my_linked_list[0] == 0
  
def test_last_method():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  assert my_linked_list.last() == 3


def test_getitem_out_of_range():
  my_linked_list = LinkedList()
  my_linked_list.append(1)
  my_linked_list.append(2)
  my_linked_list.append(3)
  
  with pytest.raises(IndexError):
    my_linked_list[3]
def test_replace_item_in_empty_list():
  my_linked_list = LinkedList()
  with pytest.raises(IndexError):
    my_linked_list.replacebyindex(100,1)



