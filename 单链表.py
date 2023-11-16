class Node():
    """创建结点类"""
    def __init__(self,data):
        self.data = data
        self.next = None

class Single_Link_List():
    """创建链表类"""
    def __init__(self,node=None):
        """头指针指向第一个结点"""
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        if self.__head == None:
            return True
        else:
            return False

    def len(self):
        """计算链表长度"""
        cur = self.__head # cur是游标，记录当前指向哪个结点
        count = 0
        while cur != None:
            count += 1
            cur = cur.next # cur也是node对象
        return count

    def travel(self):
        """遍历链表中的元素"""
        if self.is_empty():
            return '空链表，没有元素'
        cur = self.__head
        while cur != None:
            print(cur.data,end=' ')
            cur = cur.next
        print() # 遍历完后换行

    def append(self,data):
        """向链表末尾加入结点"""
        if self.is_empty(): # 如果为空结点的处理办法
            self.__head = Node(data)
        else:
            cur = self.__head
            # 该循环用来找到最后一个结点
            while cur.next != None:
                cur = cur.next
            cur.next = Node(data) # 把最后一个结点的next指向添加的结点

    def insert(self,pos,data):
        """向链表指定位置添加结点"""
        if pos > self.len() - 1:
            raise '越界，此位置无法插入结点'
        cur = self.__head
        prior = self.__head # 和C语言链表添加结点操作一样，想先找到前一个结点，这里prior用来指向前一个结点
        count = 0
        while cur != None:
            if pos == 0:
                cur = Node(data)
                cur.next = prior
                self.__head = cur
                break
            if count == pos- 1: # 如果要插入的结点位置已经找到，就按C语言的操作顺序来。
                cur = Node(data)
                cur.next = prior.next # 先连
                prior.next = cur # 后断
                break # 插入完成后，退出循环
            cur = cur.next
            prior = prior.next
            count += 1

    def pop(self):
        cur = self.__head
        # 该循环用来寻找倒数第二个结点
        while cur.next.next != None:
            cur = cur.next
        cur.next = None

    def modify(self,pos,new_data): # 为了与常规一样，链表的结点个数也从0下标开始数
        if pos > self.len() - 1:
            raise '越界，该位置没有结点'
        cur = self.__head
        count = 0
        while cur != None:
            if count == pos:
                cur.data = new_data
                break # 找到要修改的结点的数据后，退出循环
            cur = cur.next
            count += 1
    def search(self,data):
        cur = self.__head
        count = 0 # 表示要找的数据放在第几个结点（下标从0开始）
        while cur != None:
            if cur.data == data:
                return count
            cur = cur.next
            count += 1
        return count

if __name__ == '__main__':
    sll = Single_Link_List()
    print(sll.is_empty())
    print(sll.len())
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.append(40)
    sll.append(50)
    print(sll.is_empty())
    print(sll.len())
    sll.travel()
    print('-'*20)
    sll.pop()
    print(sll.len())
    print('-'*20)
    print(sll.search(10))
    print('-' * 20)
    sll.modify(0,10000)
    sll.travel()
    print('-' * 20)
    sll.insert(2,25)
    sll.travel()
