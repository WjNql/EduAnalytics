from py2neo import Node, Relationship

class KnowledgeGraph:
    def __init__(self):
        self.nodes = {}
        
    def add_concept(self, name, subject, difficulty):
        node = Node("Concept", 
                   name=name,
                   subject=subject,
                   difficulty=difficulty)
        self.nodes[name] = node
        return node
    
    def add_relation(self, source, target, relation_type):
        return Relationship(self.nodes[source], 
                          relation_type, 
                          self.nodes[target])

# # 示例用法（数学知识点）
# kg = KnowledgeGraph()
# kg.add_concept("二次函数", "math", 0.7)
# kg.add_concept("一元二次方程", "math", 0.6)
# kg.add_relation("二次函数", "一元二次方程", "PREREQUISITE")