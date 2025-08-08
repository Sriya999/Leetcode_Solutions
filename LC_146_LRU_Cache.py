class LRUCache:
     
    class Node:
        def __init__(self,key,val):
            self.prev=None
            self.key=key
            self.val=val
            self.nxt=None

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}

        #dummy head and tail
        self.head=self.Node(0,0)
        self.tail=self.Node(0,0)
        #connect head and tail
        self.head.nxt=self.tail
        self.tail.prev=self.head

    def insertafter_head(self,node):
        headafter_node=self.head.nxt
        self.head.nxt=node
        node.nxt=headafter_node
        headafter_node.prev=node
        node.prev=self.head
    
    def del_node(self,node):
        prevnode=node.prev
        nextnode=node.nxt
        prevnode.nxt=nextnode
        nextnode.prev=prevnode

    def get(self, key: int) -> int:
        #if present in hashmap just del and insert after head and update the value
        if key in self.cache:
            self.del_node(self.cache[key])#node address
            self.insertafter_head(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:#check in map
            node=self.cache[key]
            node.val=value
            self.del_node(node)
            self.insertafter_head(node)
            return node.val

                #if not in map insert after head and add to map by checking capacity
        else:
            #if capacity exceeds del least used behore tail 
            if self.capacity==len(self.cache):
                deletednode=self.tail.prev
                self.del_node(deletednode)#dll delete
                del self.cache[deletednode.key] #del also in map
            node=self.Node(key,value)
            #if within simply insert
            self.insertafter_head(node)
            self.cache[key]=node
      
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
