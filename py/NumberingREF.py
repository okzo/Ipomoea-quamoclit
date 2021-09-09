import pcbnew
import json
import os
import re

mods = []
for mod in pcbnew.GetBoard().GetModules():
    mods.append(mod)

ref_max = 0
for mod in mods:
    if re.match("^__Numbering__REF([0-9]+)$",mod.Reference().GetText()):
        ref_num = re.sub("^__Numbering__REF([0-9]+)$","\\1",mod.Reference().GetText())
        if ref_max < ref_num:
            ref_max = ref_num

print "ref_max = " + str(ref_max)

for mod in mods:
    if mod.Reference().GetText() == "REF**":
        ref_max = ref_max + 1
        ref_name = "__Numbering__REF"+str(ref_max)
        print (mod.Reference().GetText() + " -> " + ref_name)
        mod.Reference().SetText(ref_name)

pcbnew.Refresh() #Refreshで画面には反映されるが、編集したことにはならないので、保存するにはひと工夫必要
