import xml.dom.minidom as minidom
import pandas as pd

# Parse the XML file
dom = minidom.parse("C:/Users/DELL/OneDrive/桌面/progaming/go_obo.xml")
root = dom.documentElement
terms = root.getElementsByTagName('term')

nodeparents = {}
result = {}
#we should write the relation between two nodes in a dic (key is the child and value are parents) because dic is suitable for checking
for term in terms:
    node_id = term.getElementsByTagName("id")[0].childNodes[0].data
    ancestor_ids = []
    for is_a in term.getElementsByTagName("is_a"):
        ancestor_ids.append(is_a.childNodes[0].data)
    nodeparents[node_id] = ancestor_ids
    result[node_id] = 0
    # Initialize the "reult" which is used to store the answer

def findparentsnodes(node_id, parent_ids):
    ancestor_ids = nodeparents[node_id]
    #take parent_ids as a set to store all parents relationship 
    for ancestor_id in ancestor_ids:
        parent_ids.add(ancestor_id) 
        findparentsnodes(ancestor_id, parent_ids)
        #parents_ids means all ancestor node (including parent's parents...etc)

#here is to get the final result part
for key in nodeparents.keys():
    parent_ids = set()
    # reset the parent_ids
    findparentsnodes(key, parent_ids)
    for parent_id in parent_ids:
        result[parent_id] += 1
        #if a node is included in another node's ancestor it surely should take it into the childnodes
        
# Initialize Excel dataframe
go_id=[]
term_name=[]
defstr=[]
child_count=[]
# Find 'autophagosome' related gene ontology terms and their child nodes
row_num = 2  # Start from row 2        
for term in terms:
    new_defstr = term.getElementsByTagName('defstr')[0].childNodes[0].data
    if 'autophagosome' in new_defstr.lower():
        go_id_new=term.getElementsByTagName('id')[0].childNodes[0].data
        go_id.append(go_id_new)
        term_name.append(term.getElementsByTagName('name')[0].childNodes[0].data)
        defstr.append(new_defstr)
    # Check if 'autophagosome' is present in the definition string
        child_count.append(result[go_id_new])
        # Write the information to the dataframe
df=pd.DataFrame({'GO_ID':go_id, 'Term_Name':term_name, 'Definition':defstr, 'Child_Nodes':child_count})
# Save the dataframe
df.to_excel('C:/Users/DELL/OneDrive/桌面/progaming/go_terms.xlsx')

# I suppose there is many same counting process during the code running, especially in the findparentsnodes part. However, I didn't come up with a better one and maybe I can use something to store the things have already counted
#The result is shown in a another file
