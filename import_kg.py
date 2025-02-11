from model import KnowledgeNode, QuestionNode, TeachRelation
from py2neo import Graph
import pandas as pd

class KGImporter:
    def __init__(self, uri="bolt://localhost:7687", 
                auth=("neo4j", "Wjjd16zd~")):
        self.g = Graph(uri, auth=auth)
        
    def create_constraints(self):
        self.g.run("CREATE CONSTRAINT concept_name IF NOT EXISTS FOR (c:Concept) REQUIRE c.name IS UNIQUE")
        self.g.run("CREATE CONSTRAINT question_id IF NOT EXISTS FOR (q:Question) REQUIRE q.id IS UNIQUE")
    
    def import_concepts(self, csv_path):
        df = pd.read_csv(csv_path)
        tx = self.g.begin()
        
        for _, row in df.iterrows():
            node = KnowledgeNode(row['name'], 'math', row['difficulty'])
            tx.create(node.node)
            
            if pd.notna(row['parent_id']):
                parent = self.g.nodes.match("Concept", name=row['parent_id']).first()
                rel = TeachRelation(parent, node, "HAS_SUBCONCEPT")
                tx.create(rel)
        
        tx.commit()
    
    def link_questions(self, csv_path):
        df = pd.read_csv(csv_path)
        tx = self.g.begin()
        
        for _, row in df.iterrows():
            question = QuestionNode(row['question_id'], '例题', '内容示例')
            tx.merge(question.node, "Question", "id")
            
            concept = self.g.nodes.match("Concept", name=row['concept_id']).first()
            rel = Relationship(question.node, "TESTS", concept, weight=float(row['weight']))
            tx.create(rel)
        
        tx.commit()

# 执行导入
if __name__ == "__main__":
    importer = KGImporter()
    importer.create_constraints()
    importer.import_concepts("data/raw/math_concepts.csv")
    importer.link_questions("data/raw/question_relations.csv")