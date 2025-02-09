from py2neo import Graph

try:
    g = Graph("bolt://localhost:7687", 
             auth=("neo4j", "Wjjd16zd~"))
    print("连接成功！Neo4j版本:", g.run("CALL dbms.components() YIELD versions RETURN versions").data()[0]['versions'][0])
except Exception as e:
    print("连接失败:", str(e))