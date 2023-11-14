def read_material_properties(Path_file):
    
    materials=[]
    with open (Path_file,"r") as f:
        lines=f.readlines()
        for i in range(0,len(lines),5):
            material_name=lines[i].strip().split(':')[1].lower()
            if material_name=='steel':
                density=float(lines[i+1].strip().split(':')[1])
                Young_modulus=float(lines[i+2].strip().split(':')[1])
                Poisson_ratio=float(lines[i+3].strip().split(':')[1])
        
                material_properties={
            'material':material_name,
            'density':density,
            'Young_modulus':Young_modulus,
            'Poisson_ratio':Poisson_ratio,
            }
        materials.append(material_properties)
        return materials
    
Path_file="D:/python/text/test.txt"
steel_materials = read_material_properties(Path_file)

print(steel_materials)

