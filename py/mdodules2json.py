import pcbnew
import json
import os

mods = []
for mod in pcbnew.GetBoard().GetModules():
    mods.append(mod)

dic_mods = []
for mod in mods:
    pos = pcbnew.ToMM(mod.GetPosition())
    dic = {
        "ref" : mod.Reference().GetText(),
        "pos.x" : pos[0],
        "pos.y" : pos[1],
        "deg" : mod.GetOrientationDegrees(),
        "flip" : mod.IsFlipped(),
    }
    dic_mods.append(dic)

dic_mods.sort(key=lambda x:x["ref"])
mods_ary = []
for mod in dic_mods:
    mods_ary.append(json.dumps(mod))

dir_name = os.path.dirname(pcbnew.GetBoard().GetFileName())
file_name = '__' + os.path.splitext(os.path.basename(pcbnew.GetBoard().GetFileName()))[0] + '.json'
file_path = os.path.join(dir_name,file_name)

s = '[\n'+',\n'.join(mods_ary)+'\n]'

with open(file_path, mode='w') as f:
    f.write(s)
