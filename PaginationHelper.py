# The constructor takes in an array of items and a integer indicating
  # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
      
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
      
  
  # returns the number of pages
    def page_count(self):
        if len(self.collection) % self.items_per_page == 0:
            return len(self.collection) // self.items_per_page
        else:
            return len(self.collection) // self.items_per_page + 1

  # returns the number of items on the current page. page_index is zero based
  # this method should return -1 for page_index values that are out of range
    def page_item_count(self,page_index):
        print(self.collection, self.items_per_page, page_index)
        if page_index * self.items_per_page > len(self.collection):
            return -1
        elif page_index == 1:
            return self.items_per_page
        return (len(self.collection) % (page_index * self.items_per_page))
        
      
    # determines what page an item is    on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self,item_index):
        if (item_index >= len(self.collection)) or (item_index < 0) or(len(self.collection) == 0):
            return -1
        elif item_index < self.items_per_page:
            return 0
        elif item_index > self.items_per_page:
            return item_index // self.items_per_page
