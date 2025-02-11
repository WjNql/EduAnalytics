# 定义基础模型
from py2neo import Node, Relationship

class KnowledgeNode:
    def __init__(self, name, subject, difficulty):
        self.node = Node("Concept",
                        name=name,
                        subject=subject,
                        difficulty=float(difficulty))
        
class QuestionNode:
    def __init__(self, q_id, q_type, content):
        self.node = Node("Question",
                        id=str(q_id),
                        type=q_type,
                        content=content)
        
class TeachRelation(Relationship):
    def __init__(self, source, target, rel_type):
        super().__init__(source.node, rel_type, target.node)