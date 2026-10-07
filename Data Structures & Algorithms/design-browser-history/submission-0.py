class BrowserHistory:

    class Node:
        def __init__(self, url):
            self.prev = None
            self.next = None
            self.url = url




    def __init__(self, homepage: str):
        self.curr = self.Node(homepage)
        

    def visit(self, url: str) -> None:
        new_node = self.Node(url)
       
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node
        

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.prev is None:
                break
            self.curr = self.curr.prev

        return self.curr.url        
        


    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.curr.next is None:
                break

            self.curr = self.curr.next
        return self.curr.url        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)