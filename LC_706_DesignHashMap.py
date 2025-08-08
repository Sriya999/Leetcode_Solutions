class MyHashMap:
    class Node:
        def __init__(self,key,val):
            self.key=key
            self.val=val
            
    def __init__(self,size=16):
        self.size=size
        #creating buckets
        self.buckets=[[] for _ in range(size)]

    def put(self, key: int, value: int) -> None:
        idx=hash(key)%self.size
        bucket=self.buckets[idx]
        for node in bucket:
            if node.key==key:
                node.val=value
                return
        bucket.append(self.Node(key,value))
    
    def get(self, key: int) -> int:
        idx=hash(key)%self.size
        bucket=self.buckets[idx]
        for node in bucket:
            if node.key==key:
                return node.val
        return -1
     
    def remove(self, key: int) -> None:
        idx=hash(key)%self.size
        bucket=self.buckets[idx]
        for i,node in enumerate(bucket):
            if node.key==key:
                bucket.pop(i)
                return
        return -1
       
        

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
